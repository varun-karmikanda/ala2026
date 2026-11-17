# ALA 2026 LaTeX Notes

This repository contains the course notes, lecture documents, and assignments.
The LaTeX build is configured to use project-local fonts so documents can be
compiled consistently on different devices without installing those fonts
system-wide.

## What changed

- Added bundled OpenType fonts under `fonts/`:
  - Libertinus Serif and Sans
  - STIX Two Math
- Updated the LaTeX documents to load fonts from the repository with
  `fontspec` and `unicode-math`.
- Added the root `Makefile` for:
  - downloading/verifying fonts
  - compiling one document or all documents
  - opening generated PDFs
  - cleaning auxiliary files
- Added `lectures/Makefile` shortcuts such as `make intro` and
  `make affine`.

The fonts are not LaTeX packages. Packages such as `nicematrix` still need to
be provided by the TeX installation on each device.

## Requirements

Install the following tools:

- GNU Make
- TeX Live or MiKTeX
- `latexmk`
- XeLaTeX
- `curl`
- `unzip`

On Debian or Ubuntu, the common dependencies can be installed with:

```bash
sudo apt update
sudo apt install make latexmk texlive-xetex texlive-latex-extra curl unzip
```

`texlive-latex-extra` provides many additional LaTeX packages, including
packages commonly used by the documents. If a package is still missing, install
the corresponding TeX Live package with `apt`.

## Build one PDF

Run commands from the repository root:

```bash
make pdf FILE=lectures/intro.tex
make pdf FILE=lectures/affine.tex
make pdf FILE=course/assignments/assignment2.tex
```

The generated PDF is placed beside its source `.tex` file.

To open a generated PDF on Linux:

```bash
xdg-open lectures/intro.pdf
```

The Makefile's default opener is `open`. On Linux, override it with:

```bash
make open FILE=lectures/intro.pdf OPEN=xdg-open
```

## Build using shortcuts

From the `lectures/` directory:

```bash
make intro
make affine
make vec-angle-proof
```

The lecture shortcuts delegate to the root Makefile. From the repository root,
the equivalent command is:

```bash
make -C lectures intro
```

## Build every document

```bash
make all
```

## Fonts

The first build runs the `fonts` target. It downloads the required fonts only
when they are missing and stores them in the repository's `fonts/` directory.
The font files can then be committed and shared with the project.

To download or verify them explicitly:

```bash
make fonts
```

Documents use XeLaTeX through `latexmk`, which is required for
`fontspec` and `unicode-math`:

```bash
latexmk -xelatex --shell-escape -cd lectures/intro.tex
```

## Cleaning generated files

Remove auxiliary files:

```bash
make clean
```

Remove auxiliary files while leaving generated PDFs untouched:

```bash
make clean-all
```

## List available documents

```bash
make list
```
