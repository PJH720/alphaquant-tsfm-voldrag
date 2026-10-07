#!/usr/bin/env bash
# ==============================================================================
# build_presentation.sh
# ------------------------------------------------------------------------------
# One-click build script for 2026 연합 경제 학술제 본선 발표자료
# Pipeline:
#   1. Generate vector charts (slides/make_figures.py)
#   2. Compile Beamer XeLaTeX (main.tex -> main.pdf)
#   3. Update speaker scripts & slide notes (generate_scripts_and_notes.py)
#   4. Render high-res slides & inject notes to PPTX (pdf_to_pptx.py)
#   5. Package Overleaf upload zip
#   6. Sync to iCloud presentation folder if available
# ==============================================================================
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

echo "========================================================================"
echo " [1/5] Generating slide figures (slides/make_figures.py)..."
echo "========================================================================"
uv run --with matplotlib --with pandas --with numpy --with segno python slides/make_figures.py


echo "========================================================================"
echo " [2/5] Compiling Beamer XeLaTeX (slides/main.tex)..."
echo "========================================================================"
cd slides
xelatex -interaction=nonstopmode main.tex > /dev/null
bibtex main > /dev/null || true
xelatex -interaction=nonstopmode main.tex > /dev/null
xelatex -interaction=nonstopmode main.tex
cd "$REPO_ROOT"

echo "========================================================================"
echo " [3/5] Updating speaker script and presenter notes..."
echo "========================================================================"
python3 slides/generate_scripts_and_notes.py
cp out/"[서강대]_알파퀀트_발표스크립트_큐시트.md" docs/presentation_script_cuesheet.md


echo "========================================================================"
echo " [4/5] Converting PDF to PPTX with presenter notes (pdf_to_pptx.py)..."
echo "========================================================================"
uv run --with pymupdf --with python-pptx python pdf_to_pptx.py

echo "========================================================================"
echo " [5/5] Packaging Overleaf project (out/overleaf_upload.zip)..."
echo "========================================================================"
python3 -c "
import os, zipfile
from pathlib import Path
slides_dir = Path('slides')
zip_path = Path('out/overleaf_upload.zip')
exts = {'.tex', '.bib', '.pdf', '.png', '.jpg', '.jpeg'}
with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zf:
    for root, dirs, files in os.walk(slides_dir):
        for f in files:
            p = Path(root) / f
            rel = p.relative_to(slides_dir)
            if p.suffix in exts and rel != Path('main.pdf'):
                zf.write(p, arcname=str(rel))
print(f'Overleaf zip created: {zip_path.stat().st_size / 1024:.1f} KB')
"

ICLOUD_DIR="/Users/pj/Library/Mobile Documents/iCloud~md~obsidian/Documents/Vault_Inbox/261007) 경제 학술 회의 제출 기한/발표자료"
if [ -d "$ICLOUD_DIR" ]; then
    echo "Syncing deliverables to iCloud folder..."
    cp out/"[서강대]_알파퀀트_발표자료.pptx" "$ICLOUD_DIR/"
    cp out/"[서강대]_알파퀀트_발표자료.pdf" "$ICLOUD_DIR/"
    cp out/"[서강대]_알파퀀트_발표스크립트_큐시트.md" "$ICLOUD_DIR/"
    cp docs/presentation_script_cuesheet.md "$ICLOUD_DIR/"
    cp out/overleaf_upload.zip "$ICLOUD_DIR/"
    echo "iCloud sync complete."
fi

echo "========================================================================"
echo " Presentation build completed successfully!"
echo " Outputs:"
echo "   - out/[서강대]_알파퀀트_발표자료.pptx"
echo "   - out/[서강대]_알파퀀트_발표자료.pdf"
echo "   - docs/presentation_script_cuesheet.md"
echo "   - out/overleaf_upload.zip"
echo "========================================================================"
