# mp4towav

> Extract audio from video as 16 kHz mono WAV for speech recognition (语音识别).

<p align="center">
  <a href="#english">🇬🇧 English</a>
  ·
  <a href="#chinese">🇨🇳 中文</a>
</p>

### English <span id="english"></span>

<details open>
<summary><b>🇬🇧 English</b></summary>

#### Prerequisites

```bash
brew install ffmpeg
```

#### Usage

```bash
source ~/development/mac-tools/mp4towav/mp4towav   # or add to .zshrc

mp4towav video.mp4
# Output: video.wav (16 kHz, mono, PCM s16le)

mp4towav video.mp4 audio.wav
# Custom output path
```

#### Format

- **Codec**: PCM 16-bit little-endian
- **Channels**: 1 (mono)
- **Sample rate**: 16000 Hz

Suitable for Whisper, other ASR engines, and 语音识别 pipelines.

</details>

### 中文 <span id="chinese"></span>

<details>
<summary><b>🇨🇳 中文</b></summary>

#### 依赖

```bash
brew install ffmpeg
```

#### 使用方法

```bash
source ~/development/mac-tools/mp4towav/mp4towav   # 或加入 .zshrc

mp4towav video.mp4
# 输出：video.wav（16 kHz，单声道，PCM s16le）

mp4towav video.mp4 audio.wav
# 指定输出路径
```

#### 输出格式

- **编码**: PCM 16-bit 小端
- **声道**: 1（单声道）
- **采样率**: 16000 Hz

适用于 Whisper、其他语音识别引擎及语音识别流程。

</details>
