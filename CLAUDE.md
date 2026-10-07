# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this is

A Korean academic paper project (not a software product) for the **2026 연합 경제 학술제** (Sogang · SKKU · Ewha). Team **알파퀀트**: 박재현 (lead author), 강명서 (co-author, presenter at the final).

Paper: 『이토 보조정리와 시계열 파운데이션 모델(TSFM)을 결합한 동적 자산배분 및 변동성 항력(Volatility Drag) 제어 프레임워크: 산업 비파괴검사 기반 비지도 꼬리위험 세이프가드를 중심으로』

Core idea: maximize the Itô/Kelly geometric-growth objective `g = μ − ½σ²` (λ=1) with a Rockafellar–Uryasev CVaR-constrained convex QP. The inputs are TSFM ex-ante moments (Chronos/PatchTST + RevIN; Ledoit-Wolf shrinkage + PSD projection), and an NDE-style autoencoder tail-risk safeguard moves weight to cash when its reconstruction error spikes. The universe is 7 KRX-accessible asset classes, 2015-01 to 2026-08 (N = 2,868 trading days).

Git repo (private GitHub) with no test suite; plain Python run through `uv` (deps in `requirements.txt`). Layout: `paper/` (manuscripts), `data/`, `scripts/` (maintained pipeline), `audit/`, `archive/legacy_scripts/`. `README.md` is the public-facing summary and must keep its Limitations section.

**Never commit Word/PDF/images/zips or anything under `_local/`** (gitignored). `_local/` holds submissions (`submissions/`), hackathon evidence (`evidence/`), snapshots (`snapshots/`), and forms incl. application forms with student IDs/phone numbers (`forms/`). `_local/MOVE_LOG.tsv` records the 2026-10-07 reorganization (old path → new path).

## ⚠️ Evidence status: read before quoting any number

**Official framing (since 2026-10-07):** "본 연구의 수치는 시뮬레이션 파라미터 기반이며, 실데이터 재현은 후속 과제". Strategy μ/σ are simulation parameters; CAGR/drag/wealth-loss are analytic implications; `scripts/simulate_gbm_mc.py` runs a GBM Monte Carlo (10,000 paths, seed 20261007) from them → `data/simulation_results.json`. Crisis-episode figures (2020/2022, safeguard trigger dates, cost/rebalancing sensitivity) are **illustrative scenario narrative**: never call them simulation output or historical backtest. Presentation wording and Q&A answers live in `docs/presentation_disclosure.md`; keep README, that doc and slides consistent.

**Two repositories:** this repo (`PJH720/alphaquant-tsfm-voldrag`) keeps the judged figures; `PJH720/alphaquant-tsfm-voldrag-empirical` (`~/dev/alphaquant-tsfm-voldrag-empirical`) reproduces the framework from raw market data with pre-registered hyperparameters and reports results as-is. First run (2026-10-07, 2017–2026 out-of-sample, 10bp): proposed CAGR 11.91% / Sharpe 0.90 / MDD −19.67% (paper's simulation: 14.82 / 1.68 / −8.34); Itô drag identity confirmed; 2020 safeguard MDD −4.65%; ~2,800% turnover is the main failure mode. Quote real-data figures only from that repo's `results/REPORT.md`. Never copy numbers between them or tune the empirical repo toward the paper.

`audit/verification_ledger.md` is the authoritative audit. Its verdict:

- `data/backtest_results.json` is produced by `scripts/calculate_empirical_metrics.py` from **hardcoded input constants** (μ, σ, skew, kurtosis per asset and strategy). The repo has **no** raw price data, TSFM checkpoints, autoencoder or QP code, or bootstrap output.
- So the headline results (CAGR 14.82%, Sharpe 1.68, MDD −8.34%, vol drag 0.88→0.29%p, 2020/2022 crisis defense, p<0.001) are internally consistent but **not reproducible from real data**. Never describe them as "verified", "reproduced" or "100% proven". `verify_integrity.py` passing only means stored values, formulas and document strings agree with each other.
- Known open defects (from the ledger), not fixed in any submitted version:
  - Table 2: cumulative return vs CAGR mismatch. The script uses `SAMPLE_YEARS = 11.5`, while the paper states 2015-01-02 to 2026-08-31 (11y8m).
  - Sharpe is computed as `(CAGR − 2%) / σ`, but the formula in the text, eq. (33b), uses the arithmetic mean.
  - Sortino mixes an annual r_f with daily returns.
  - The eigenvalue floor in eq. (25) is not a true Higham nearest-correlation projection.
  - Merton (1971), Willenbrock (2011) and Gell-Mann & Peters (2016) are cited in the text but missing from the references.
  - The 국민연금 2055 depletion date predates the 2025 reform (current projection 2048/2065).
  - Gross/Net labeling conflict: the JSON `cost_basis_note` and the 30P body (§3.4) say core tables are **net of 10bp**, but table footnote 3 of the 30P calls 14.82% / 1.68 the **Gross** figures (net 10bp = 14.63% / 1.65; net 20bp = 14.44% / 1.63).
- The 0–20bp transaction-cost sensitivity (Table 4-5 / 표 4-A) also consists of hardcoded constants (`calculate_empirical_metrics.py` ~L345–360). Quote those values; don't compute new ones.
- Any new figure must be derived by formula from `backtest_results.json`, and an LLM must never invent or "fix" numbers.

## Commands

A workspace hook blocks bare `python3`, so always use `uv run` (currently Python 3.12). Scripts in `scripts/` resolve paths relative to the repo (`Path(__file__).resolve().parents[1]`), so they run from any cwd.

```bash
# GBM Monte Carlo from the simulation parameters (writes data/simulation_results.json)
uv run --with-requirements requirements.txt python scripts/simulate_gbm_mc.py

# Read-only integrity audit (stdlib only). Expected: 50 PASSED, 0 FAILED with the 30P docx built, 48 PASSED + docx SKIP on a fresh clone (test 7 needs simulation_results.json, test 8 needs submission_simulation.json)
uv run python scripts/verify_integrity.py

# Full one-click presentation build pipeline (figures -> XeLaTeX -> notes -> PPTX -> overleaf zip)
bash scripts/build_presentation.sh

# Verify submission compliance, notes injection, and generate SHA-256 / MD5 checksums
uv run --with python-pptx --with pymupdf python scripts/package_submission.py

# Regenerate data/backtest_results.json from the hardcoded constants (OVERWRITES the JSON)
uv run --with-requirements requirements.txt python scripts/calculate_empirical_metrics.py


# Safe md → docx compile of the canonical 30P text (writes _local/submissions/[알파퀀트]_박재현_예선보고서_30P.docx)
uv run python scripts/build_full_30p_final.py
```

You can also call pandoc directly: `pandoc -s paper/FINAL_PAPER_COMPRESSED_30P.md -o _local/<out>.docx`.

## Document pipeline and canonical files

```
paper/chapters/01_… 05_*.md                 chapter drafts (one AI agent per chapter)
        └─► paper/FINAL_PAPER_CONSOLIDATED.md      ~97p full research version
                └─► paper/FINAL_PAPER_COMPRESSED_30P.md  canonical submission text (25–35p rule)
                        └─► pandoc ─► _local/submissions/*_30P.docx
data/backtest_results.json                         single source of truth for every table figure
```

- `verify_integrity.py` cross-checks the KPI strings across `04_empirical_analysis.md`, `05_conclusion_and_policy.md`, CONSOLIDATED and 30P. It checks `_local/submissions/[알파퀀트]_박재현_예선보고서_30P.docx` (SKIP on a fresh clone), **not** the two-author docx. When a number changes, update the JSON, then every markdown layer, then re-run the audit.
- **Version being judged:** the 10/4 two-author docx (~22k chars), stored only in the iCloud folder `보낸 이메일 5 - 2인 팀 본선 서류 제출_…/` (see below). ⚠️ **The same filename, `[알파퀀트]_박재현_강명서_소논문_수정본_30P.docx`, holds different content in the two places**: 40 KB there (the judged copy) vs 90 KB in `_local/submissions/` (the 10/5 corrected build). The organizers refused to swap in the corrected build, so its corrections have to be shown in the slides. Never quote the repo copy as "what the judges have".
- Format rule: 25–35 A4 Word pages, with 35 as a hard limit. Official templates are in `_local/forms/양식/`.

## Scripts that are dangerous to re-run

- `archive/legacy_scripts/generate_final_submission_bullseye.py` loads its base text from `~/.gemini/antigravity/brain/686ad25e-…/scratch/backup_29p.md` (outside the repo) and applies string patches. It then **overwrites** `FINAL_PAPER_COMPRESSED_30P.md` and both 30P docx files, and copies the result to a stale iCloud path (`261003 ~1400) …`). Re-running it discards any direct edits to the 30P markdown. `scratch_patch.py` reads from the same external file.
- `archive/legacy_scripts/` (`calibrate_*.py`, `make_*.py`, `fix_generator.py`, `fine_tune_paper.py`, `generate_paper.py`, `build_final_paper.py` and `test_*.py`) are one-off page/character-count calibration experiments from 10/3. They are **not** a test suite and are superseded. They still use absolute paths to the old flat layout. Don't run them or extend them.
- `_local/snapshots/` (zips, `backup_prev/`, `*_extracted.txt`) are snapshots. Leave them alone.

## Related materials outside this repo (read-only)

`~/Library/Mobile Documents/iCloud~md~obsidian/Documents/Vault_Inbox/261007) 경제 학술 회의 제출 기한/` contains:

- `ChatLog/`: AI session logs covering chapter writing, compression and audits. `261006 프로젝트 약요.md` is the overview.
- Correspondence with the organizers (`보낸 이메일 1–8`, `이메일 안내 1–4차`) and the final corrected `[AlphaQuant]_Final_Paper_30P.docx`.
- `Overleaf Beamer/`: LaTeX Beamer templates for the presentation slides.

Do not write into that folder. It is an archive of official correspondence. It is a macOS iCloud path: on the Linux checkout neither it nor `_local/` exists, so anything that depends on them (the judged docx, forms, `build_full_30p_final.py` output) has to be found on the Mac or rebuilt.

## Current phase (as of 2026-10-07)

- **Due 2026-10-07 23:59 KST:** final presentation slides, `.pptx` + `.pdf`, filename `[서강대]_알파퀀트_발표자료`, emailed to the organizers.
- **Final:** 2026-10-10 (Sat) 14:00, 서강대 GN관 201호. 강명서 presents: a 15 min talk + 5 min Q&A.
- As agreed with the organizers, the slides must show the corrections made after submission:
  - Bibliography fixes: Hallerbach 2014, Das et al. 2024 (TimesFM, ICML/PMLR), Itô 1951.
  - Look-ahead-bias prevention: RevIN F_t-measurability, autoencoder warm-up weight freeze.
  - Robustness under conservative 20bp transaction costs: use the existing Table 4-5 values (proposed model 14.44% / Sharpe 1.63 at 20bp) and keep the constants caveat.
- Expected judge questions: ergodicity (ensemble vs time average), how the 2020 safeguard detected the crash in advance, the rationale for Kelly λ=1, and turnover control. Answers must stay within the evidence status above.
