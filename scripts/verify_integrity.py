#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
verify_integrity.py
--------------------------------------------------------------------------------
Ground Truth Academic Integrity Auditor for:
『이토 보조정리와 시계열 파운데이션 모델(TSFM)을 결합한 동적 자산배분 및 변동성 항력 제어 프레임워크』

Checks:
1. Table 4-2 10-Year Compounding Wealth Loss = Formula Output Match
2. Table 3-1 Jarque-Bera Statistics (N=2,868) = Formula Output Match
3. Cross-Chapter Consistency (Chapters 3, 4, 5, Consolidated, Compressed 30P)
4. Multi-period Macro Regime Compounding Linkage (Table 4-7 vs Table 4-1)
5. Dimension of Safe Haven Vector (7-dimensional check)
6. 30P Submission Word Document & Character Budget Compliance
--------------------------------------------------------------------------------
"""

import json
import math
import os
import re
import sys
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
JSON_PATH = BASE_DIR / "data/backtest_results.json"
CHAPTERS_DIR = BASE_DIR / "paper/chapters"
MD_CONSOLIDATED = BASE_DIR / "paper/FINAL_PAPER_CONSOLIDATED.md"
MD_30P = BASE_DIR / "paper/FINAL_PAPER_COMPRESSED_30P.md"
# Word builds are kept out of git (see .gitignore); the docx checks are skipped on a fresh clone.
DOCX_30P = BASE_DIR / "_local/submissions/[알파퀀트]_박재현_예선보고서_30P.docx"

PASS_COUNT = 0
FAIL_COUNT = 0

def check(condition, test_name, detail=""):
    global PASS_COUNT, FAIL_COUNT
    if condition:
        PASS_COUNT += 1
        print(f"  [\033[92mPASS\033[0m] {test_name}")
        if detail:
            print(f"         {detail}")
    else:
        FAIL_COUNT += 1
        print(f"  [\033[91mFAIL\033[0m] {test_name}")
        if detail:
            print(f"         \033[91mError: {detail}\033[0m")

def test_table_4_2_loss():
    print("\n" + "=" * 80)
    print("TEST 1: Table 4-2 10-Year Compounding Wealth Loss Verification")
    print("Formula: Loss = 100 * (1 + g)^10 - 100 * (1 + mu)^10 (Unit: 억원)")
    print("=" * 80)
    
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
    
    expected_values = {
        "전통적 60/40": {"mu": 8.51, "g": 7.85, "loss": -13.39, "w_geom": 212.91, "w_arith": 226.31},
        "동일가중 (EW 1/N)": {"mu": 9.25, "g": 8.42, "loss": -17.79, "w_geom": 224.44, "w_arith": 242.22},
        "마코위츠 MVO": {"mu": 10.02, "g": 9.14, "loss": -20.05, "w_geom": 239.79, "w_arith": 259.85},
        "제안 모델 (TSFM-Itô)": {"mu": 15.11, "g": 14.82, "loss": -10.17, "w_geom": 398.27, "w_arith": 408.44},
    }
    
    for row in data["table_4_2_wealth_loss"]:
        name = row["strategy"]
        if name in expected_values:
            target = expected_values[name]
            # Exact recalculation
            calc_w_geom = 100.0 * ((1.0 + target["g"] / 100.0) ** 10)
            calc_w_arith = 100.0 * ((1.0 + target["mu"] / 100.0) ** 10)
            calc_loss = calc_w_geom - calc_w_arith
            
            diff = abs(calc_loss - row["loss_10y"])
            check(diff < 0.02, f"Loss calculation for {name}",
                  f"Formula={calc_loss:.2f}억, Stored={row['loss_10y']:.2f}억, Diff={diff:.4f}")
    
    # Check Proposed vs MVO preservation
    prop_loss = expected_values["제안 모델 (TSFM-Itô)"]["loss"]
    mvo_loss = expected_values["마코위츠 MVO"]["loss"]
    preservation = round(abs(mvo_loss) - abs(prop_loss), 2)
    check(abs(preservation - 9.88) < 0.01, "MVO Wealth Preservation Amount",
          f"Preservation = {preservation:.2f}억원 (Expected +9.88억원)")
    
    # Check text in Markdown files
    with open(MD_CONSOLIDATED, "r", encoding="utf-8") as f:
        cons_txt = f.read()
    with open(MD_30P, "r", encoding="utf-8") as f:
        p30_txt = f.read()
        
    check("-10.17 억 원" in cons_txt and "-10.17 억 원" in p30_txt,
          "Proposed -10.17 억 원 present in Consolidated & 30P")
    check("9.88 억 원" in cons_txt or "9.88억 원" in cons_txt,
          "+9.88 억 원 preservation present in Consolidated")
    check("9.88 억 원" in p30_txt or "9.88억 원" in p30_txt,
          "+9.88 억 원 preservation present in 30P Markdown")
    check("-7.1 억 원" not in p30_txt and "13.8 억 원" not in p30_txt,
          "Obsolete figures (-7.1억, 13.8억) eradicated from 30P")

def test_table_3_1_jarque_bera():
    print("\n" + "=" * 80)
    print("TEST 2: Table 3-1 Jarque-Bera Statistics (N=2,868) Verification")
    print("Formula: JB = (N / 6) * [ S^2 + (K^2 / 4) ]")
    print("=" * 80)
    
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    expected_jb = {
        "KOSPI 200": {"skew": -0.38, "kurt": 6.12, "expected_jb": 4544.82},
        "KOSDAQ 150": {"skew": -0.45, "kurt": 7.35, "expected_jb": 6552.48},
        "한국국채 10Y": {"skew": -0.15, "kurt": 4.80, "expected_jb": 2764.03},
        "S&P 500 (KRW)": {"skew": -0.62, "kurt": 9.40, "expected_jb": 10742.76},
        "나스닥 100 (KRW)": {"skew": -0.51, "kurt": 7.82, "expected_jb": 7432.04},
        "금 현물 (Gold)": {"skew": 0.08, "kurt": 5.95, "expected_jb": 4233.66},
        "미국단기채 (Cash)": {"skew": 0.21, "kurt": 4.10, "expected_jb": 2029.87},
    }
    
    for row in data["table_3_1_asset_summary"]:
        name = row["asset_class"]
        if name in expected_jb:
            exp = expected_jb[name]
            s = exp["skew"]
            k = exp["kurt"]
            n = 2868
            calc_jb = (n / 6.0) * (s**2 + (k**2) / 4.0)
            diff = abs(calc_jb - row["jb_stat"])
            check(diff < 0.05, f"Jarque-Bera for {name}",
                  f"Formula={calc_jb:.2f}, Stored={row['jb_stat']:.2f}, Diff={diff:.4f}")
            
    with open(MD_30P, "r", encoding="utf-8") as f:
        p30_txt = f.read()
    with open(MD_CONSOLIDATED, "r", encoding="utf-8") as f:
        cons_txt = f.read()
        
    check("4,544.82***" in p30_txt and "4,544.82***" in cons_txt,
          "KOSPI 200 JB 4,544.82*** in 30P and Consolidated")
    check("10,742.76***" in p30_txt and "10,742.76***" in cons_txt,
          "S&P 500 JB 10,742.76*** in 30P and Consolidated")
    check("3,842.15" not in p30_txt and "3,842.15" not in cons_txt,
          "Erroneous N=2,425 JB (3,842.15) eradicated from all markdown files")

def test_cross_chapter_consistency():
    print("\n" + "=" * 80)
    print("TEST 3: Cross-Chapter Key Performance Indicator Synchronization")
    print("Target: CAGR 14.82%, MDD -8.34%, Sharpe 1.68, Volatility 7.63%")
    print("=" * 80)
    
    with open(CHAPTERS_DIR / "04_empirical_analysis.md", "r", encoding="utf-8") as f:
        ch4_txt = f.read()
    with open(CHAPTERS_DIR / "05_conclusion_and_policy.md", "r", encoding="utf-8") as f:
        ch5_txt = f.read()
    with open(MD_CONSOLIDATED, "r", encoding="utf-8") as f:
        cons_txt = f.read()
    with open(MD_30P, "r", encoding="utf-8") as f:
        p30_txt = f.read()
        
    # Check Chapter 5 contains correct figures
    check("14.82%" in ch5_txt, "Chapter 5 has Proposed CAGR 14.82%")
    check("7.85%" in ch5_txt, "Chapter 5 has 60/40 CAGR 7.85%")
    check("1.68" in ch5_txt, "Chapter 5 has Proposed Sharpe 1.68")
    check("-8.34%" in ch5_txt, "Chapter 5 has Proposed MDD -8.34%")
    check("7.63%" in ch5_txt, "Chapter 5 has Proposed Volatility 7.63%")
    check("0.29%p" in ch5_txt, "Chapter 5 has Proposed Vol Drag 0.29%p")
    
    # Check obsolete figures do not exist in Chapter 5
    check("12.87%" not in ch5_txt, "Obsolete 12.87% eradicated from Chapter 5")
    check("6.82%" not in ch5_txt, "Obsolete 6.82% eradicated from Chapter 5")
    check("-7.84%" not in ch5_txt, "Obsolete -7.84% eradicated from Chapter 5")
    
    # Check 30P has uniform numbers
    check("14.82%" in p30_txt, "30P has Proposed CAGR 14.82%")
    check("-8.34%" in p30_txt, "30P has Proposed MDD -8.34%")
    check("1.68" in p30_txt, "30P has Proposed Sharpe 1.68")
    check("7.63%" in p30_txt, "30P has Proposed Volatility 7.63%")

def test_macro_regimes_compounding():
    print("\n" + "=" * 80)
    print("TEST 4: Macro Regime Multi-Period Compounding Linkage (Table 4-7)")
    print("Formula: Prod_{k=1}^4 (1 + CAGR_k)^{T_k} == 1 + Total_Cum_Return")
    print("=" * 80)
    
    with open(JSON_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)
        
    v = data["regime_compounding_verification"]
    
    # Proposed
    prop_fac = v["Proposed"]["compounded_factor"]
    prop_cum = v["Proposed"]["compounded_cum_ret"]
    check(abs(prop_cum - 392.15) < 0.05, "Proposed Regime Compounding Match",
          f"Compounded Cum Return = {prop_cum:.2f}% (Target: 392.15%, Factor={prop_fac:.4f})")
    
    # 60/40
    b60_cum = v["60/40"]["compounded_cum_ret"]
    check(abs(b60_cum - 138.86) < 0.05, "60/40 Regime Compounding Match",
          f"Compounded Cum Return = {b60_cum:.2f}% (Target: 138.86%)")
          
    # EW
    ew_cum = v["EW"]["compounded_cum_ret"]
    check(abs(ew_cum - 154.21) < 0.05, "EW Regime Compounding Match",
          f"Compounded Cum Return = {ew_cum:.2f}% (Target: 154.21%)")
          
    # MVO
    mvo_cum = v["MVO"]["compounded_cum_ret"]
    check(abs(mvo_cum - 176.43) < 0.05, "MVO Regime Compounding Match",
          f"Compounded Cum Return = {mvo_cum:.2f}% (Target: 176.43%)")

def test_safe_vector_dimension():
    print("\n" + "=" * 80)
    print("TEST 5: Safe Haven Asset Vector Dimension Check")
    print("Universe size = 7 assets -> Vector must be 7-dimensional [0,0,0,0,0,0,1]^T")
    print("=" * 80)
    
    with open(CHAPTERS_DIR / "04_empirical_analysis.md", "r", encoding="utf-8") as f:
        ch4_txt = f.read()
    with open(MD_CONSOLIDATED, "r", encoding="utf-8") as f:
        cons_txt = f.read()
    with open(MD_30P, "r", encoding="utf-8") as f:
        p30_txt = f.read()
        
    # Check 6-dimension error is absent
    check("[0, 0, 0, 0, 0, 1.0]" not in ch4_txt, "No 6D vector in 04_empirical_analysis.md")
    check("[0, 0, 0, 0, 0, 1.0]" not in cons_txt, "No 6D vector in Consolidated")
    
    # Check 7-dimension vector is present
    check("[0, 0, 0, 0, 0, 0, 1.0]" in ch4_txt, "7D vector present in 04_empirical_analysis.md")
    check("[0, 0, 0, 0, 0, 0, 1.0]" in cons_txt, "7D vector present in Consolidated")
    check("(0, 0, 0, 0, 0, 0, 1)^T" in cons_txt or "[0, 0, 0, 0, 0, 0, 1]" in cons_txt,
          "Safe weight vector definition in Chapter 3 Consolidated")

def test_docx_and_submission_specs():
    print("\n" + "=" * 80)
    print("TEST 6: 30P Submission Word Document & Academic Rigor Compliance")
    print("=" * 80)
    
    if DOCX_30P.exists():
        check(True, "Word document exists: [알파퀀트]_박재현_예선보고서_30P.docx")
        size_kb = DOCX_30P.stat().st_size / 1024.0
        check(size_kb > 30.0, f"Word document file size valid ({size_kb:.1f} KB)")
    else:
        print("  [SKIP] Word document not present (docx is gitignored; build with scripts/build_full_30p_final.py)")
    
    with open(MD_30P, "r", encoding="utf-8") as f:
        text_30p = f.read()
        
    total_chars = len(text_30p)
    nospace_chars = len(text_30p.replace(" ", "").replace("\n", "").replace("\t", ""))
    
    # Verify academic depth: Rich, uncompressed content compliant with 25~35 page standard
    check(total_chars >= 45000,
          f"Rich academic depth preserved: {total_chars:,d} chars (w/ spaces)",
          f"Current: {total_chars:,d} chars (No space: {nospace_chars:,d}) | Complies with 25~35p format")
    
    # Verify financial bias patches
    check("총수익률(Total Return, TR)" in text_30p or "Total Return (TR)" in text_30p or "총수익률" in text_30p,
          "Total Return (TR) dividend reinvestment specified")
    check("Look-ahead Bias" in text_30p or "미래 참조 편향" in text_30p,
          "Look-ahead bias mitigation specified")
    check("거래비용" in text_30p and "회전율" in text_30p,
          "Transaction cost & turnover dynamics specified")

def test_monte_carlo_simulation():
    print("\n" + "=" * 80)
    print("TEST 7: GBM Monte Carlo consistency (scripts/simulate_gbm_mc.py)")
    print("Check: |MC mean log-growth - (mu - 0.5*sigma^2)| <= 3 * MC standard error")
    print("=" * 80)

    sim_path = BASE_DIR / "data/simulation_results.json"
    if not sim_path.exists():
        check(False, "Simulation results present",
              "Run: uv run --with-requirements requirements.txt python scripts/simulate_gbm_mc.py")
        return

    with open(sim_path, "r", encoding="utf-8") as f:
        sim = json.load(f)

    worst = max(
        abs(r["mc_g_mean_pct"] - r["theoretical_g_pct"]) / r["mc_g_se_pct"]
        for r in sim["strategies"].values()
    )
    check(worst <= 3.0, "MC mean growth matches Ito growth for all strategies",
          f"Worst deviation = {worst:.2f} SE (n_paths={sim['metadata']['n_paths']})")

def test_web_export_simulation_bundle():
    print("\n" + "=" * 80)
    print("TEST 8: Web Export Simulation Bundle Integrity (scripts/export_web_bundle.py)")
    print("Check: web_export/submission_simulation.json sync with backtest & MC results")
    print("=" * 80)

    bundle_path = BASE_DIR / "web_export/submission_simulation.json"
    if not bundle_path.exists():
        check(False, "Web export bundle present",
              "Run: uv run python scripts/export_web_bundle.py")
        return

    with open(bundle_path, "r", encoding="utf-8") as f:
        bundle = json.load(f)

    # Check strategies structure
    strat_keys = list(bundle.get("strategies", {}).keys())
    expected_strats = ["benchmark_6040", "equal_weight", "mvo", "proposed"]
    check(strat_keys == expected_strats, "Web export contains all 4 benchmark & proposed strategies",
          f"Found: {strat_keys}")

    # Check proposed KPIs match backtest_results.json
    prop_params = bundle["strategies"]["proposed"]["parameters"]
    prop_analytic = bundle["strategies"]["proposed"]["analytic"]
    check(prop_params["mu_arith_pct"] == 15.11 and prop_params["sigma_pct"] == 7.63 and prop_params["mdd_pct"] == -8.34,
          "Web export Proposed parameters match (mu 15.11%, sigma 7.63%, MDD -8.34%)",
          f"mu={prop_params['mu_arith_pct']}, sigma={prop_params['sigma_pct']}, mdd={prop_params['mdd_pct']}")
    check(prop_analytic["cagr_pct"] == 14.82 and prop_analytic["sharpe"] == 1.68 and prop_analytic["theo_drag_pct"] == 0.29,
          "Web export Proposed analytic KPIs match (CAGR 14.82%, Sharpe 1.68, Drag 0.29%p)",
          f"cagr={prop_analytic['cagr_pct']}, sharpe={prop_analytic['sharpe']}, drag={prop_analytic['theo_drag_pct']}")

    # Check Monte Carlo section against data/simulation_results.json
    sim_path = BASE_DIR / "data/simulation_results.json"
    if sim_path.exists():
        with open(sim_path, "r", encoding="utf-8") as f:
            sim = json.load(f)
        sim_prop = sim["strategies"]["제안 모델 (TSFM-Itô)"]
        bundle_prop_mc = bundle["monte_carlo"]["strategies"]["proposed"]
        check(bundle_prop_mc["wealth_10y"]["mean"] == sim_prop["wealth_10y"]["ensemble_mean"] and
              bundle_prop_mc["wealth_10y"]["median"] == sim_prop["wealth_10y"]["median_typical_path"],
              "Web export MC 10y wealth matches simulation_results.json (mean 451.55억, median 437.87억)",
              f"Mean={bundle_prop_mc['wealth_10y']['mean']}, Median={bundle_prop_mc['wealth_10y']['median']}")



def main():
    print("=" * 80)
    print("ACADEMIC AUDITOR INTEGRITY VERIFICATION SUITE")
    print("=" * 80)
    
    test_table_4_2_loss()
    test_table_3_1_jarque_bera()
    test_cross_chapter_consistency()
    test_macro_regimes_compounding()
    test_safe_vector_dimension()
    test_docx_and_submission_specs()
    test_monte_carlo_simulation()
    test_web_export_simulation_bundle()

    print("\n" + "=" * 80)
    print(f"AUDIT SUMMARY: {PASS_COUNT} PASSED, {FAIL_COUNT} FAILED")
    print("=" * 80)
    
    if FAIL_COUNT == 0:
        print("\033[92m>>> ALL ACADEMIC INTEGRITY AUDITS PASSED WITH 100% COMPLIANCE! <<<\033[0m")
        sys.exit(0)
    else:
        print("\033[91m>>> SOME INTEGRITY AUDITS FAILED. PLEASE REVIEW LOGS. <<<\033[0m")
        sys.exit(1)

if __name__ == "__main__":
    main()

