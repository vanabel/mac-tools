# mac-tools

Personal toolkit for macOS. Shell scripts, functions, and utilities.

<p align="center">
  <a href="#english">🇬🇧 English</a>
  ·
  <a href="#chinese">🇨🇳 中文</a>
</p>

---

### English <span id="english"></span>

<details open>
<summary><b>🇬🇧 English</b></summary>

#### Tools

| Tool | Description |
|------|-------------|
| [**pdfmerge**](./pdfmerge/) | Merge PDFs with bookmarks (书签) and natural sort order |
| [**video-downloader**](./video-downloader/) | Download videos from YouTube, Rutube, etc. via yt-dlp |
| [**whisper-srt**](./whisper-srt/) | Generate SRT subtitles from MP4/video via whisper-server |
| [**mp4towav**](./mp4towav/) | Extract 16 kHz mono WAV from video for speech recognition |
| [**media-tools**](./media-tools/) | mp4tomp3, ffcompress (extract MP3, compress video) |
| [**pdf-tools**](./pdf-tools/) | pdfextract, pdf_crop, pdfcompress |

#### Setup

Add to your `~/.zshrc` (loads all tools and adds `mac-tools-help` / `mthelp`):

```bash
source ~/development/mac-tools/load
```

Then run **`mthelp`** or **`mac-tools-help`** to see all functions in a table.

</details>

### 中文 <span id="chinese"></span>

<details>
<summary><b>🇨🇳 中文</b></summary>

#### 工具列表

| 工具 | 说明 |
|------|------|
| [**pdfmerge**](./pdfmerge/) | 合并 PDF，支持书签与自然排序 |
| [**video-downloader**](./video-downloader/) | 通过 yt-dlp 从 YouTube、Rutube 等下载视频 |
| [**whisper-srt**](./whisper-srt/) | 通过 whisper-server 从 MP4/视频生成 SRT 字幕 |
| [**mp4towav**](./mp4towav/) | 从视频提取 16 kHz 单声道 WAV，用于语音识别 |
| [**media-tools**](./media-tools/) | mp4tomp3、ffcompress（提 MP3、压视频） |
| [**pdf-tools**](./pdf-tools/) | pdfextract、pdf_crop、pdfcompress |

#### 配置

在 `~/.zshrc` 中添加（会加载全部工具并提供 `mac-tools-help` / `mthelp`）：

```bash
source ~/development/mac-tools/load
```

运行 **`mthelp`** 或 **`mac-tools-help`** 可查看所有函数表格。

</details>
