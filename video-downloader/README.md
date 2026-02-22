# video-downloader

> Download videos from YouTube, Rutube, and other sites via yt-dlp.

<p align="center">
  <a href="#english">🇬🇧 English</a>
  ·
  <a href="#chinese">🇨🇳 中文</a>
</p>

### English <span id="english"></span>
<details open>
<summary><b>🇬🇧 English</b></summary>

#### Prerequisites

macOS discourages installing into system Python. Use [pipx](https://pipx.pypa.io/) to run yt-dlp in an isolated environment:

```bash
# 1. Install pipx
brew install pipx

# 2. Ensure PATH is configured
pipx ensurepath

# 3. Install yt-dlp
pipx install yt-dlp
```

**Optional** – [aria2c](https://aria2.github.io/) for faster parallel downloads:

```bash
brew install aria2
```

#### Usage

```bash
source ~/development/mac-tools/video-downloader/download   # or add to your .zshrc

video-download <url>           # Download as MP4
video-download-list <url>      # List available formats

# Example (Rutube)
video-download "https://rutube.ru/play/embed/05b4bbef471cbeb2fe35c705ed58857d"
```

#### Supported sites

Works with any site [yt-dlp](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md) supports, including:

- YouTube
- Rutube
- Bilibili
- Vimeo
- Many more

#### Output format

Downloads as MP4, preferring:

1. `bestvideo[ext=mp4][vcodec=mpeg4] + bestaudio[ext=mp4][acodec=ac3]`
2. Fallback: `best[ext=mp4]`

Output filename: `%(title)s.%(ext)s`

If aria2c is installed, it is used automatically with 16 connections and 1M split size for faster downloads.

</details>

### 中文 <span id="chinese"></span>

<details>
<summary><b>🇨🇳 中文</b></summary>

#### 依赖

macOS 禁止安装到系统 Python 环境。使用 [pipx](https://pipx.pypa.io/) 在隔离环境中运行 yt-dlp：

```bash
# 1. 安装 pipx
brew install pipx

# 2. 确保路径配置
pipx ensurepath

# 3. 安装 yt-dlp
pipx install yt-dlp
```

**可选** – 安装 [aria2c](https://aria2.github.io/) 以启用多连接加速下载：

```bash
brew install aria2
```

#### 使用方法

```bash
source ~/development/mac-tools/video-downloader/download   # 或加入 .zshrc

video-download <url>           # 下载为 MP4
video-download-list <url>      # 查看可用格式列表

# 示例（Rutube）
video-download "https://rutube.ru/play/embed/05b4bbef471cbeb2fe35c705ed58857d"
```

#### 支持的网站

支持 [yt-dlp](https://github.com/yt-dlp/yt-dlp/blob/master/supportedsites.md) 支持的所有站点，包括：

- YouTube
- Rutube
- Bilibili
- Vimeo
- 更多

#### 输出格式

下载为 MP4，优先级：

1. `bestvideo[ext=mp4][vcodec=mpeg4] + bestaudio[ext=mp4][acodec=ac3]`
2. 回退：`best[ext=mp4]`

输出文件名：`%(title)s.%(ext)s`

若已安装 aria2c，将自动使用 16 连接和 1M 分片大小以加速下载。

</details>
