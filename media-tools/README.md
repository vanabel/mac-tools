# media-tools

音视频小工具：提取 MP3、转 MP4、压缩 MOV/MP4。

## 依赖

- **ffmpeg**（含 ffprobe）：`brew install ffmpeg`
- 压缩使用 VideoToolbox（macOS 自带）

## 用法

通过统一加载使用（推荐）：

```bash
source ~/development/mac-tools/load
mthelp   # 查看所有工具
```

或仅加载本模块：

```bash
source ~/development/mac-tools/media-tools/media-tools
```

| 函数 | 说明 |
|------|------|
| **mp4tomp3** | 从 MP4 提取 MP3（已是 MP3 则直接 copy，否则重编码） |
| **videotomp4** | 转 MP4（默认 H.264 硬编，兼容优先；可显式切 H.265 或 copy） |
| **ffcompress** | 用 VideoToolbox 将 MOV/MP4 压成更小的 MP4（默认 1280 宽、约 2500k） |

### 示例

```bash
mp4tomp3 video.mp4              # 输出 video.mp3
mp4tomp3 video.mp4 out.mp3      # 指定输出

videotomp4 screen.mov                    # 默认 H.264 硬编，输出 screen_h264.mp4
videotomp4 --h265 screen.mov             # 显式 HEVC，输出 screen_h265.mp4
videotomp4 --copy screen.mov             # 仅换封装（不重编码）
videotomp4 --h264 -b 3500 *.mov          # 批量处理（注意不要给 *.mov 加引号）

ffcompress record.mov                    # 输出 record_compressed.mp4
ffcompress record.mov out.mp4 2000      # 指定输出与视频码率(kbps)
```
