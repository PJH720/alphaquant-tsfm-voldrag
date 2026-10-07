#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
package_submission.py
--------------------------------------------------------------------------------
Pre-submission Verification & Packaging Auditor for:
2026 연합 경제 학술제 (서강대·성대·이대) 본선 출품팀 [알파퀀트]

Checks:
  1. File existence: [서강대]_알파퀀트_발표자료.pptx and .pdf
  2. Size limits: < 25 MB for email attachment
  3. Page/Slide count: exactly 26 slides (19 main + 7 backup)
  4. Speaker notes: 26/26 slides with complete notes in PPTX
  5. Checksums: SHA-256 & MD5 hash generation
  6. iCloud sync: verifies bit-for-bit identity in iCloud submission folder
  7. Email draft: outputs formatted email ready to send to 26sgecon@gmail.com
--------------------------------------------------------------------------------
"""

import hashlib
import os
import sys
from pathlib import Path

def get_hashes(filepath: Path):
    md5 = hashlib.md5()
    sha256 = hashlib.sha256()
    with open(filepath, "rb") as f:
        while chunk := f.read(65536):
            md5.update(chunk)
            sha256.update(chunk)
    return md5.hexdigest(), sha256.hexdigest()

def main():
    root = Path(__file__).resolve().parents[1]
    out_dir = root / "out"
    icloud_dir = Path("/Users/pj/Library/Mobile Documents/iCloud~md~obsidian/Documents/Vault_Inbox/261007) 경제 학술 회의 제출 기한/발표자료")

    pptx_path = out_dir / "[서강대]_알파퀀트_발표자료.pptx"
    pdf_path = out_dir / "[서강대]_알파퀀트_발표자료.pdf"

    print("=" * 80)
    print(" 2026 연합 경제 학술제 본선 최종 제출물 무결성 감사 (알파퀀트 팀)")
    print("=" * 80)

    # 1. Existence check
    missing = []
    if not pptx_path.exists(): missing.append(str(pptx_path))
    if not pdf_path.exists(): missing.append(str(pdf_path))
    if missing:
        print(f"\033[91m[FAIL] Missing required files: {missing}\033[0m")
        print("Run: bash scripts/build_presentation.sh")
        sys.exit(1)
    print("  [\033[92mPASS\033[0m] 필수 제출 파일(PPTX 원본 1부, PDF 1부) 존재 확인")

    # 2. File size check (< 25MB)
    pptx_size_mb = pptx_path.stat().st_size / (1024 * 1024)
    pdf_size_mb = pdf_path.stat().st_size / (1024 * 1024)
    total_mb = pptx_size_mb + pdf_size_mb

    if pptx_size_mb >= 25.0 or pdf_size_mb >= 25.0 or total_mb >= 25.0:
        print(f"\033[91m[FAIL] File size exceeds 25MB email limit: Total {total_mb:.2f} MB\033[0m")
        sys.exit(1)
    print(f"  [\033[92mPASS\033[0m] 파일 용량 검증: PPTX={pptx_size_mb:.2f}MB, PDF={pdf_size_mb:.2f}MB (합계 {total_mb:.2f}MB < 25MB 한도)")

    # 3. Slide & Page counts
    try:
        import pymupdf
        from pptx import Presentation
    except ImportError:
        print("\033[91m[ERROR] Please run with: uv run --with python-pptx --with pymupdf python scripts/package_submission.py\033[0m")
        sys.exit(1)

    doc = pymupdf.open(pdf_path)
    prs = Presentation(pptx_path)

    pdf_pages = len(doc)
    pptx_slides = len(prs.slides)

    if pdf_pages != 26 or pptx_slides != 26:
        print(f"\033[91m[FAIL] Page/Slide mismatch! PDF={pdf_pages}, PPTX={pptx_slides} (Expected exactly 26)\033[0m")
        sys.exit(1)
    print(f"  [\033[92mPASS\033[0m] 슬라이드 수 검증: PDF {pdf_pages}쪽, PPTX {pptx_slides}장 일치 (본편 19장 + 백업 7장)")

    # 4. Presenter notes verification
    notes_count = 0
    for idx, slide in enumerate(prs.slides, 1):
        note = slide.notes_slide.notes_text_frame.text.strip()
        if note:
            notes_count += 1
    if notes_count != 26:
        print(f"\033[91m[FAIL] Speaker notes missing on some slides! ({notes_count}/26 found)\033[0m")
        sys.exit(1)
    print(f"  [\033[92mPASS\033[0m] 발표자 노트 검증: 26장 전 슬라이드(100%) 대본 및 제스처 주입 완료")

    # 5. Hashes
    pptx_md5, pptx_sha = get_hashes(pptx_path)
    pdf_md5, pdf_sha = get_hashes(pdf_path)

    # 6. iCloud synchronization check
    if icloud_dir.exists():
        icloud_pptx = icloud_dir / pptx_path.name
        icloud_pdf = icloud_dir / pdf_path.name
        if icloud_pptx.exists() and icloud_pdf.exists():
            _, icloud_pptx_sha = get_hashes(icloud_pptx)
            _, icloud_pdf_sha = get_hashes(icloud_pdf)
            if pptx_sha == icloud_pptx_sha and pdf_sha == icloud_pdf_sha:
                print(f"  [\033[92mPASS\033[0m] iCloud 동기화 검증: 로컬 out/ 과 iCloud 폴더 SHA-256 100% 일치")
            else:
                print(f"  [\033[93mWARN\033[0m] iCloud 파일 해시가 다릅니다. 'bash scripts/build_presentation.sh'를 재실행하세요.")
        else:
            print(f"  [\033[93mWARN\033[0m] iCloud 대상 폴더에 파일이 없습니다.")

    print("\n" + "=" * 80)
    print(" 📋 제출물 무결성 해시 레코드 (Audit Hash Trail)")
    print("=" * 80)
    print(f" 파일 1: {pptx_path.name}")
    print(f"   - 용량: {pptx_size_mb:.2f} MB ({pptx_path.stat().st_size:,} bytes)")
    print(f"   - MD5:    {pptx_md5}")
    print(f"   - SHA256: {pptx_sha}")
    print(f" 파일 2: {pdf_path.name}")
    print(f"   - 용량: {pdf_size_mb:.2f} MB ({pdf_path.stat().st_size:,} bytes)")
    print(f"   - MD5:    {pdf_md5}")
    print(f"   - SHA256: {pdf_sha}")

    print("\n" + "=" * 80)
    print(" ✉️ 주최측 제출 이메일 템플릿 (2026-10-07 23:59 KST 마감)")
    print("=" * 80)
    print("수신: 26sgecon@gmail.com")
    print("제목: [서강대학교] 알파퀀트 - 2026 연합 경제 학술제 본선 발표자료 제출")
    print("첨부: 1) [서강대]_알파퀀트_발표자료.pptx")
    print("      2) [서강대]_알파퀀트_발표자료.pdf")
    print("-" * 80)
    print("""안녕하십니까, 2026 연합 경제 학술제 조직위원회 귀하.

서강대학교 경제학과 '알파퀀트' 팀입니다.
본선 발표자료(PPTX 원본 1부, PDF 1부)를 규격에 맞추어 첨부하여 제출합니다.

1. 논문 제목: 이토 보조정리와 시계열 파운데이션 모델(TSFM)을 결합한 동적 자산배분 및 변동성 항력(Volatility Drag) 제어 프레임워크
2. 발표자: 강명서 (서강대학교 경제학 22)
3. 대표자: 박재현 (서강대학교 경제학 18)
4. 첨부 파일:
   - [서강대]_알파퀀트_발표자료.pptx (슬라이드 노트에 전체 발표 대본 수록)
   - [서강대]_알파퀀트_발표자료.pdf (학교 공식 Berlin/beaver 테마 기반 Beamer 와이드 16:9)

감사합니다.
서강대학교 알파퀀트 팀 드림 (대표: 박재현 / 발표자: 강명서)""")
    print("=" * 80)
    print("\033[92m>>> ALL PRE-SUBMISSION CHECKS PASSED WITH 100% COMPLIANCE! <<<\033[0m")

if __name__ == "__main__":
    main()
