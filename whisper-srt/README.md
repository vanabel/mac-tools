# whisper-srt

> Generate SRT subtitles from MP4/video files via whisper-server (whisper.cpp).

<p align="center">
  <a href="#english">🇬🇧 English</a>
  ·
  <a href="#chinese">🇨🇳 中文</a>
</p>

### English <span id="english"></span>

<details open>
<summary><b>🇬🇧 English</b></summary>

#### Prerequisites

1. **whisper-server** (from [whisper.cpp](https://github.com/ggml-org/whisper.cpp)) – build and have `whisper-server` on your PATH.

2. **ffmpeg** – for MP4 → WAV conversion:

   ```bash
   brew install ffmpeg
   ```

3. **GGML model** – e.g. `ggml-medium.en.bin` in `~/.33ZiMu/models/`.

#### Usage

```bash
source ~/development/mac-tools/whisper-srt/whisper-srt   # or add to your .zshrc

# Start server (in a separate terminal, or background)
whisper-srt-server

# Generate SRT from MP4
whisper-srt video.mp4
# Output: video.srt

# Specify output path
whisper-srt video.mp4 subtitles.srt

# WAV files are sent directly (no conversion)
whisper-srt audio.wav
```

#### Workflow

1. MP4 (or other video/audio) → converted to 16 kHz mono WAV via ffmpeg.
2. WAV → sent to whisper-server `/inference` with `response_format=srt`.
3. SRT → written to `<basename>.srt` or the given output path.

#### Environment

| Variable | Default | Description |
|----------|---------|-------------|
| `WHISPER_SRT_MODEL` | `~/.33ZiMu/models/ggml-medium.en.bin` | GGML model path |
| `WHISPER_SRT_HOST` | `127.0.0.1` | Server host |
| `WHISPER_SRT_PORT` | `8080` | Server port |
| `WHISPER_SRT_SERVER_PATH` | `whisper-server` | whisper-server binary |
| `WHISPER_SRT_KEEP_WAV` | `0` | Set to `1` to keep temp WAV after conversion |
| `WHISPER_SRT_THREADS` | `8` | Server CPU threads (M4: use 8–10) |

#### Acceleration (Apple Silicon M1–M4)

**Quick win – more threads** (default: 8):
```bash
WHISPER_SRT_THREADS=10 whisper-srt-server
```

**Core ML (~3× faster)** – uses Neural Engine for encoding. Model name (e.g. `medium` or `large-v3`) must match your existing `.bin` filename.

```bash
# 1. Clone whisper.cpp
git clone https://github.com/ggml-org/whisper.cpp
cd whisper.cpp

# 2. Create venv and install Python deps (keeps system Python clean)
python3 -m venv .venv
source .venv/bin/activate
pip install torch openai-whisper coremltools ane_transformers

# 3. Convert: downloads PyTorch model, outputs ggml-<name>-encoder.mlmodelc
#    Use "medium" for ggml-medium.bin, "large-v3" for ggml-large-v3.bin
./models/generate-coreml-model.sh medium
deactivate

# 4. Copy your .bin into models/ (same dir as .mlmodelc)
cp /opt/homebrew/share/whisper/ggml-medium.bin models/

# 5. Build with Core ML
WHISPER_COREML=1 make -j

# 6. Run whisper-srt with the new server and model
WHISPER_SRT_SERVER_PATH="$(pwd)/build/bin/whisper-server" \
WHISPER_SRT_MODEL="$(pwd)/models/ggml-medium.bin" \
whisper-srt-server
```

</details>

### 中文 <span id="chinese"></span>

<details>
<summary><b>🇨🇳 中文</b></summary>

#### 依赖

1. **whisper-server**（来自 [whisper.cpp](https://github.com/ggml-org/whisper.cpp)）— 需要自行编译并将 `whisper-server` 加入 PATH。

2. **ffmpeg** — 用于 MP4 → WAV 转换：

   ```bash
   brew install ffmpeg
   ```

3. **GGML 模型** — 如 `ggml-medium.en.bin`，放在 `~/.33ZiMu/models/` 等路径。

#### 使用方法

```bash
source ~/development/mac-tools/whisper-srt/whisper-srt   # 或加入 .zshrc

# 启动服务器（单独终端或后台）
whisper-srt-server

# 从 MP4 生成 SRT 字幕
whisper-srt video.mp4
# 输出：video.srt

# 指定输出路径
whisper-srt video.mp4 subtitles.srt

# WAV 文件直接发送，无需转换
whisper-srt audio.wav
```

#### 流程

1. MP4（或其他音视频）→ 通过 ffmpeg 转为 16 kHz 单声道 WAV。
2. WAV → 发送到 whisper-server `/inference`，`response_format=srt`。
3. SRT → 写入 `<basename>.srt` 或指定输出路径。

#### 环境变量

| 变量 | 默认值 | 说明 |
|------|--------|------|
| `WHISPER_SRT_MODEL` | `~/.33ZiMu/models/ggml-medium.en.bin` | GGML 模型路径 |
| `WHISPER_SRT_HOST` | `127.0.0.1` | 服务器主机 |
| `WHISPER_SRT_PORT` | `8080` | 服务器端口 |
| `WHISPER_SRT_SERVER_PATH` | `whisper-server` | whisper-server 可执行文件 |
| `WHISPER_SRT_KEEP_WAV` | `0` | 设为 `1` 可在转换后保留临时 WAV |
| `WHISPER_SRT_THREADS` | `8` | 服务器 CPU 线程数（M4 建议 8–10） |

#### 加速（Apple Silicon M1–M4）

**快速提升 – 增加线程**（默认 8）：
```bash
WHISPER_SRT_THREADS=10 whisper-srt-server
```

**Core ML（约 3× 加速）** – 使用 Neural Engine 进行编码。模型名（如 `medium`、`large-v3`）需与你的 `.bin` 文件名对应。

```bash
# 1. 克隆 whisper.cpp
git clone https://github.com/ggml-org/whisper.cpp
cd whisper.cpp

# 2. 创建 venv 并安装 Python 依赖（不污染系统 Python）
python3 -m venv .venv
source .venv/bin/activate
pip install torch openai-whisper coremltools ane_transformers

# 3. 转换：会下载 PyTorch 模型，生成 ggml-<name>-encoder.mlmodelc
#    ggml-medium.bin 用 medium，ggml-large-v3.bin 用 large-v3
./models/generate-coreml-model.sh medium
deactivate

# 4. 把你的 .bin 复制到 models/（与 .mlmodelc 同目录）
cp /opt/homebrew/share/whisper/ggml-medium.bin models/

# 5. 启用 Core ML 后编译
WHISPER_COREML=1 make -j

# 6. 用新编译的 server 和模型运行 whisper-srt
WHISPER_SRT_SERVER_PATH="$(pwd)/build/bin/whisper-server" \
WHISPER_SRT_MODEL="$(pwd)/models/ggml-medium.bin" \
whisper-srt-server
```

</details>
