# pdfmerge

> Merge PDFs with bookmarks and natural sort. Shell function for zsh/bash.

<p align="center">
  <a href="#english">🇬🇧 English</a>
  ·
  <a href="#chinese">🇨🇳 中文</a>
</p>

### English <span id="english"></span>
<details open>
<summary><b>🇬🇧 English</b></summary>

#### Usage

```bash
source ~/development/mac-tools/pdfmerge/pdfmerge   # or add to your .zshrc

pdfmerge <out.pdf> <in1.pdf> <in2.pdf> ... <inn.pdf>
```

#### Features

| Feature | Description |
|---------|-------------|
| **Bookmarks** | Each PDF gets a bookmark (filename without `.pdf`) → its first page |
| **Natural sort** | `Lecture-1.pdf` → `Lecture-2.pdf` → `Lecture-10.pdf` (not lexicographic) |

#### Examples

```bash
# Merge specific files
pdfmerge merged.pdf chapter1.pdf chapter2.pdf appendix.pdf

# Merge with glob (natural sort)
pdfmerge all_lectures.pdf Lecture-*.pdf

# Merge all PDFs in current directory
pdfmerge combined.pdf *.pdf
```

#### Setup

Uses project venv with `pypdf`. Lookup order:

1. `$PDFMERGE_VENV/bin/python3`
2. `$HOME/development/mac-tools/pdfmerge/.venv/bin/python3`
3. `./.venv/bin/python3`
4. System `python3`

Recreate venv:

```bash
cd ~/development/mac-tools/pdfmerge
python3 -m venv .venv
.venv/bin/pip install pypdf
```

Falls back to Ghostscript if no pypdf (merge only, no bookmarks).

</details>

### 中文 <span id="chinese"></span>

<details>
<summary><b>🇨🇳 中文</b></summary>

#### 使用方法

```bash
source ~/development/mac-tools/pdfmerge/pdfmerge   # 或加入 .zshrc

pdfmerge <输出.pdf> <输入1.pdf> <输入2.pdf> ... <输入n.pdf>
```

#### 功能

| 功能 | 说明 |
|------|------|
| **书签** | 每个 PDF 生成一个书签（文件名去掉 `.pdf`）指向其第一页 |
| **自然排序** | 按数字顺序：`Lecture-1.pdf` → `Lecture-2.pdf` → `Lecture-10.pdf`（非字典序） |

#### 示例

```bash
# 合并指定文件
pdfmerge merged.pdf chapter1.pdf chapter2.pdf appendix.pdf

# 使用通配符合并（自动自然排序）
pdfmerge all_lectures.pdf Lecture-*.pdf

# 合并当前目录所有 PDF
pdfmerge combined.pdf *.pdf
```

#### 环境配置

使用项目 venv 中的 `pypdf`。查找顺序：

1. `$PDFMERGE_VENV/bin/python3`
2. `$HOME/development/mac-tools/pdfmerge/.venv/bin/python3`
3. `./.venv/bin/python3`
4. 系统 `python3`

重新创建 venv：

```bash
cd ~/development/mac-tools/pdfmerge
python3 -m venv .venv
.venv/bin/pip install pypdf
```

若未找到 pypdf，则回退到 Ghostscript（仅合并，无书签）。

</details>
