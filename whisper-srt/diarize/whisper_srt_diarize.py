#!/usr/bin/env python3
"""
Merge whisper-server transcription with pyannote speaker diarization.
Output: SRT with speaker labels, e.g. "[Speaker 1] 你好"
Requires: running whisper-server, HF_TOKEN for pyannote, and audio as 16kHz mono WAV.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys


def parse_srt(srt_text: str) -> list[tuple[float, float, str]]:
    """Parse SRT content to list of (start_sec, end_sec, text)."""
    blocks = re.split(r"\n\s*\n", srt_text.strip())
    result = []
    for block in blocks:
        lines = block.strip().split("\n")
        if len(lines) < 3:
            continue
        # lines[0] = index, lines[1] = "0.00 --> 1.23", lines[2:] = text
        match = re.match(r"(\d+:\d+:\d+[,.]\d+)\s*-->\s*(\d+:\d+:\d+[,.]\d+)", lines[1])
        if not match:
            continue
        start = _srt_time_to_sec(match.group(1))
        end = _srt_time_to_sec(match.group(2))
        text = " ".join(lines[2:]).strip()
        if text:
            result.append((start, end, text))
    return result


def _srt_time_to_sec(t: str) -> float:
    """Convert SRT timestamp (00:00:00,000 or 00:00:00.000) to seconds."""
    t = t.replace(",", ".")
    parts = t.split(":")
    h, m = int(parts[0]), int(parts[1])
    s = float(parts[2])
    return h * 3600 + m * 60 + s


def _sec_to_srt_time(sec: float) -> str:
    """Convert seconds to SRT timestamp 00:00:00,000."""
    h = int(sec // 3600)
    sec -= h * 3600
    m = int(sec // 60)
    sec -= m * 60
    s = int(sec)
    ms = int((sec - s) * 1000)
    return f"{h:02d}:{m:02d}:{s:02d},{ms:03d}"


def overlap(a_start: float, a_end: float, b_start: float, b_end: float) -> float:
    return max(0.0, min(a_end, b_end) - max(a_start, b_start))


def assign_speakers(
    segments: list[tuple[float, float, str]],
    diar: list[tuple[float, float, str]],
) -> list[tuple[float, float, str, str]]:
    """For each (start, end, text) assign speaker with max overlap. Return (start, end, text, speaker)."""
    out = []
    for s_start, s_end, text in segments:
        best_speaker = "Speaker 0"
        best_overlap = 0.0
        for d_start, d_end, sp in diar:
            o = overlap(s_start, s_end, d_start, d_end)
            if o > best_overlap:
                best_overlap = o
                best_speaker = sp
        out.append((s_start, s_end, text, best_speaker))
    return out


def run_diarization(wav_path: str, hf_token: str) -> list[tuple[float, float, str]]:
    """Run pyannote pipeline; return list of (start, end, speaker_label)."""
    from pyannote.audio import Pipeline

    pipeline = Pipeline.from_pretrained(
        "pyannote/speaker-diarization-3.1",
        use_auth_token=hf_token,
    )
    diarization = pipeline(wav_path)
    result = []
    for segment, _, speaker in diarization.itertracks(yield_label=True):
        result.append((segment.start, segment.end, str(speaker)))
    return result


def fetch_whisper_srt(
    wav_path: str,
    server_url: str,
    language: str | None,
) -> str:
    """POST WAV to whisper-server with response_format=srt; return SRT string."""
    import requests

    with open(wav_path, "rb") as f:
        files = {"file": (os.path.basename(wav_path), f, "audio/wav")}
        data = {"temperature": "0.0", "response_format": "srt"}
        if language:
            data["language"] = language
        r = requests.post(server_url, files=files, data=data, timeout=600)
    r.raise_for_status()
    return r.text


def fetch_whisper_json(
    wav_path: str,
    server_url: str,
    language: str | None,
) -> list[tuple[float, float, str]]:
    """POST WAV to whisper-server with response_format=verbose_json; return segments."""
    import requests

    with open(wav_path, "rb") as f:
        files = {"file": (os.path.basename(wav_path), f, "audio/wav")}
        data = {"temperature": "0.0", "response_format": "verbose_json"}
        if language:
            data["language"] = language
        r = requests.post(server_url, files=files, data=data, timeout=600)
    r.raise_for_status()
    j = r.json()
    segments = j.get("segments", [])
    return [(s["start"], s["end"], s.get("text", "").strip()) for s in segments if s.get("text")]


def write_srt(segments: list[tuple[float, float, str, str]], path: str, prefix_format: str = "[%s] ") -> None:
    """Write (start, end, text, speaker) to SRT with speaker prefix."""
    with open(path, "w", encoding="utf-8") as f:
        for i, (start, end, text, speaker) in enumerate(segments, 1):
            prefix = prefix_format % speaker
            line = f"{prefix}{text}".strip()
            f.write(f"{i}\n")
            f.write(f"{_sec_to_srt_time(start)} --> {_sec_to_srt_time(end)}\n")
            f.write(f"{line}\n\n")


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Transcribe with whisper-server and mark speakers via pyannote diarization."
    )
    parser.add_argument("input", help="Input WAV file (16kHz mono recommended)")
    parser.add_argument("output", nargs="?", help="Output SRT path (default: <input>.srt)")
    parser.add_argument("-l", "--language", default=None, help="Language code (e.g. zh, en)")
    parser.add_argument("--server", default=None, help="Whisper server URL (default: env WHISPER_SRT_SERVER_URL)")
    parser.add_argument("--no-diarize", action="store_true", help="Skip diarization; only transcribe (no speaker labels)")
    parser.add_argument("--prefix", default="[%s] ", help="Speaker prefix format (default: '[%%s] ')")
    args = parser.parse_args()

    server_url = args.server or os.environ.get("WHISPER_SRT_SERVER_URL", "http://127.0.0.1:8080/inference")
    hf_token = os.environ.get("HF_TOKEN") or os.environ.get("HUGGING_FACE_HUB_TOKEN")

    out_path = args.output or (os.path.splitext(args.input)[0] + ".srt")

    if not os.path.isfile(args.input):
        print(f"Error: input file not found: {args.input}", file=sys.stderr)
        return 1

    # 1) Transcribe
    try:
        segments = fetch_whisper_json(args.input, server_url, args.language)
    except Exception as e:
        print(f"Whisper request failed: {e}", file=sys.stderr)
        return 1
    if not segments:
        print("No segments from whisper-server.", file=sys.stderr)
        return 1

    if args.no_diarize:
        write_srt(
            [(s, e, t, "Speaker 1") for s, e, t in segments],
            out_path,
            prefix_format="",
        )
        print(f"Saved (no diarization): {out_path}")
        return 0

    if not hf_token:
        print("Set HF_TOKEN or HUGGING_FACE_HUB_TOKEN for pyannote diarization.", file=sys.stderr)
        return 1

    # 2) Diarize
    try:
        diar = run_diarization(args.input, hf_token)
    except Exception as e:
        print(f"Diarization failed: {e}", file=sys.stderr)
        return 1
    if not diar:
        print("No speaker segments from pyannote; writing transcript without labels.", file=sys.stderr)
        labeled = [(s, e, t, "Speaker 1") for s, e, t in segments]
    else:
        labeled = assign_speakers(segments, diar)

    write_srt(labeled, out_path, prefix_format=args.prefix)
    print(f"Saved: {out_path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
