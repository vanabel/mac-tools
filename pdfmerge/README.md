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
pdfmerge --sort <out.pdf> <in1.pdf> ...   # natural sort (for globs)
```

#### Features

| Feature | Description |
|---------|-------------|
| **Bookmarks** | Each PDF gets a bookmark (filename without `.pdf`) → its first page |
| **Argument order** | Merges in the order you list files |
| **Natural sort** | Optional `--sort` / `-s`: `Lecture-1.pdf` → `Lecture-2.pdf` → `Lecture-10.pdf` |

#### Examples

```bash
# Merge specific files
pdfmerge merged.pdf chapter1.pdf chapter2.pdf appendix.pdf

# Merge with glob (use --sort for Lecture-1, Lecture-2, ..., Lecture-10)
pdfmerge --sort all_lectures.pdf Lecture-*.pdf

# Merge all PDFs in current directory (natural order)
pdfmerge --sort combined.pdf *.pdf
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
pdfmerge --sort <输出.pdf> <输入1.pdf> ...   # 自然排序（通配符场景）
```

#### 功能

| 功能 | 说明 |
|------|------|
| **书签** | 每个 PDF 生成一个书签（文件名去掉 `.pdf`）指向其第一页 |
| **参数顺序** | 按你列出的文件顺序合并 |
| **自然排序** | 可选 `--sort` / `-s`：`Lecture-1.pdf` → `Lecture-2.pdf` → `Lecture-10.pdf` |

#### 示例

```bash
# 合并指定文件
pdfmerge merged.pdf chapter1.pdf chapter2.pdf appendix.pdf

# 使用通配符合并（加 --sort 得到 Lecture-1, Lecture-2, ..., Lecture-10）
pdfmerge --sort all_lectures.pdf Lecture-*.pdf

# 合并当前目录所有 PDF（自然排序）
pdfmerge --sort combined.pdf *.pdf
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
