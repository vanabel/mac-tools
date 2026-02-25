# pdf-tools

PDF 小工具：按页提取、裁边、压缩。

## 依赖

- **qpdf**（仅 pdfextract）：`brew install qpdf`
- **Ghostscript**（pdf_crop、pdfcompress）：`brew install ghostscript`

## 用法

通过统一加载使用（推荐）：

```bash
source ~/development/mac-tools/load
mthelp   # 查看所有工具
```

或仅加载本模块：

```bash
source ~/development/mac-tools/pdf-tools/pdf-tools
```

| 函数 | 说明 |
|------|------|
| **pdfextract** | 用 qpdf 按页提取到新 PDF |
| **pdf_crop** | 按厘米数裁掉四边白边 |
| **pdfcompress** | 用 gs 压成屏幕质量，减小体积 |

### 示例

```bash
pdfextract input.pdf "1,3-5,28" output.pdf
pdf_crop 1 slides.pdf              # 四边各裁 1cm → slides-cropped.pdf
pdfcompress large.pdf              # → large.compressed.pdf
```
