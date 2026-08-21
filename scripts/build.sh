#!/bin/sh
# Regenerate the MyST edition from the source PDF.
set -e
cd "$(dirname "$0")"
python3 extract.py          # PDF -> build/document.json
python3 render_figures.py   # figures -> images/, annotates document.json
python3 build_book.py       # document.json -> Markdown
