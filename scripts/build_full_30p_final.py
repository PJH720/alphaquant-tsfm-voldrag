# -*- coding: utf-8 -*-
"""
Build script for official 30-page compliant paper.
Compiles paper/FINAL_PAPER_COMPRESSED_30P.md to _local/submissions/[알파퀀트]_박재현_예선보고서_30P.docx.
The output folder is gitignored: Word builds are never committed.
"""
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]

def build():
    md_path = str(BASE_DIR / "paper" / "FINAL_PAPER_COMPRESSED_30P.md")
    out_dir = BASE_DIR / "_local" / "submissions"
    out_dir.mkdir(parents=True, exist_ok=True)
    docx_path = str(out_dir / "[알파퀀트]_박재현_예선보고서_30P.docx")

    with open(md_path, "r", encoding="utf-8") as f:
        text = f.read()
    
    print("=" * 70)
    print("OFFICIAL 30-PAGE MASTERPIECE AUDIT")
    print("=" * 70)
    print(f"Total characters with spaces   : {len(text):,d}")
    print(f"Total characters without spaces: {len(text.replace(' ', '').replace('\n', '').replace('\t', '')):,d}")
    
    cmd = ["pandoc", "-s", md_path, "-o", docx_path]
    res = subprocess.run(cmd, capture_output=True, text=True)
    if res.returncode == 0:
        print(f"Pandoc compilation succeeded! Output: {docx_path}")
    else:
        print("Pandoc compilation failed:", res.stderr)

if __name__ == "__main__":
    build()
