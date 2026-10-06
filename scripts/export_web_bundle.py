#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
export_web_bundle.py
--------------------------------------------------------------------------------
Export the submitted (judged) simulation figures as one JSON bundle for the
final-round demo site, which lives in the separate empirical repository
(alphaquant-tsfm-voldrag-empirical/web/). The site is not built here.

Every figure is copied from the two data files below; nothing is recomputed,
and no real-data result from the empirical repository is included.

Each figure carries one of the four natures from the README table:
  parameter            simulation input parameter (hardcoded constant)
  analytic             analytic implication of the parameters
  monte_carlo          GBM Monte Carlo result (scripts/simulate_gbm_mc.py)
  illustrative_scenario  illustrative scenario narrative; neither simulation
                       output nor historical backtest. Crisis-regime, cost and
                       rebalancing figures live only under this key.

Input : data/backtest_results.json, data/simulation_results.json
Output: web_export/submission_simulation.json
Stdlib only.
--------------------------------------------------------------------------------
"""

import json
import subprocess
from datetime import datetime, timezone
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[1]
BACKTEST_JSON = BASE_DIR / "data" / "backtest_results.json"
SIM_JSON = BASE_DIR / "data" / "simulation_results.json"
OUT_JSON = BASE_DIR / "web_export" / "submission_simulation.json"

# Strategy key used on the web side -> name in both data files, and key in
# the cost-sensitivity / regime tables.
STRATEGIES = [
    ("benchmark_6040", "전통적 60/40", "6040", "60/40"),
    ("equal_weight", "동일가중 (EW 1/N)", "ew", "EW"),
    ("mvo", "마코위츠 MVO", "mvo", "MVO"),
    ("proposed", "제안 모델 (TSFM-Itô)", "proposed", "Proposed"),
]

LABELS = {
    "parameter": {
        "ko": "시뮬레이션 입력 파라미터 (실측 추정치 아님)",
        "en": "Simulation input parameter (hardcoded constant, not estimated from market data)",
        "examples": "전략별 μ, σ, 자산별 왜도·첨도",
    },
    "analytic": {
        "ko": "파라미터로부터의 해석적 계산",
        "en": "Analytic implication of the parameters",
        "examples": "CAGR (= μ − ½σ²), 변동성 항력, 10년 복리 손실액, JB 통계량",
    },
    "monte_carlo": {
        "ko": "파라미터 기반 GBM 시뮬레이션 결과 (10,000 경로, seed 고정)",
        "en": "GBM Monte Carlo result from the parameters (10,000 paths, fixed seed)",
        "examples": "성장률·10년 자산·MDD·샤프의 분포, 제안 모델 우위 경로 비율",
    },
    "illustrative_scenario": {
        "ko": "예시적 시나리오 서술 (시뮬레이션도, 역사적 백테스트도 아님)",
        "en": "Illustrative scenario narrative (neither simulation output nor historical backtest)",
        "examples": "2020년 팬데믹·2022년 긴축기 방어, 세이프가드 발동일, 거래비용·리밸런싱 민감도",
    },
}


def git_head():
    try:
        sha = subprocess.run(
            ["git", "rev-parse", "HEAD"], cwd=BASE_DIR,
            capture_output=True, text=True, check=True,
        ).stdout.strip()
        # Last commit that touched the inputs; unlike HEAD, this does not
        # change when the export itself is committed.
        data_sha = subprocess.run(
            ["git", "log", "-1", "--format=%H", "--", "data/"], cwd=BASE_DIR,
            capture_output=True, text=True, check=True,
        ).stdout.strip()
        dirty = subprocess.run(
            ["git", "status", "--porcelain", "--", "data/"], cwd=BASE_DIR,
            capture_output=True, text=True, check=True,
        ).stdout.strip()
    except (OSError, subprocess.CalledProcessError):
        return None, None, None
    return sha, data_sha, bool(dirty)


def main():
    with open(BACKTEST_JSON, "r", encoding="utf-8") as f:
        bt = json.load(f)
    with open(SIM_JSON, "r", encoding="utf-8") as f:
        sim = json.load(f)

    perf = {row["strategy"]: row for row in bt["table_4_1_strategy_performance"]}
    commit, data_commit, data_dirty = git_head()

    strategies = {}
    monte_carlo = {}
    for key, name, _, _ in STRATEGIES:
        p = perf[name]
        s = sim["strategies"][name]
        strategies[key] = {
            "name": name,
            "parameters": {
                "nature": "parameter",
                "mu_arith_pct": p["mu_arith"],
                "sigma_pct": p["sigma"],
                # MDD is a hardcoded input constant, not derivable from mu/sigma.
                "mdd_pct": p["mdd"],
            },
            "analytic": {
                "nature": "analytic",
                "cagr_pct": p["cagr"],
                "sharpe": p["sharpe"],
                "theo_drag_pct": p["theo_drag_pct"],
                "loss_10y_eok": p["loss_10y"],
            },
        }
        w = s["wealth_10y"]
        monte_carlo[key] = {
            "name": name,
            "theoretical_g_pct": s["theoretical_g_pct"],
            "mc_g_mean_pct": s["mc_g_mean_pct"],
            "mc_g_se_pct": s["mc_g_se_pct"],
            "wealth_10y": {
                "unit": w["unit"],
                "mean": w["ensemble_mean"],
                "median": w["median_typical_path"],
                "p05": w["p05"],
                "p95": w["p95"],
            },
            "mdd_p50_pct": s["mdd_p50_pct"],
            "sharpe_p50": s["sharpe_p50"],
        }

    cost_sensitivity = [
        {
            "cost_bp": row["cost_bp"],
            "label": row["label"],
            **{
                key: {"cagr_pct": row[f"{cost_key}_cagr"], "sharpe": row[f"{cost_key}_sr"]}
                for key, _, cost_key, _ in STRATEGIES
            },
        }
        for row in bt["cost_sensitivity"]
    ]

    regimes = [
        {
            "name": r["name"],
            "period": r["period"],
            "years": r["years"],
            **{key: r["weights"][regime_key] for key, _, _, regime_key in STRATEGIES},
        }
        for r in bt["table_4_7_regimes"]
    ]

    vs = sim["proposed_vs_mvo"]
    bundle = {
        "metadata": {
            "nature": "simulation parameters (NOT a historical backtest)",
            "disclosure_ko": "본 연구의 수치는 시뮬레이션 파라미터 기반이며, 실데이터 재현은 후속 과제",
            "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "source_repo": "PJH720/alphaquant-tsfm-voldrag",
            "source_commit": commit,
            "source_data_commit": data_commit,
            "source_data_dirty": data_dirty,
            "source_files": [
                "data/backtest_results.json",
                "data/simulation_results.json",
            ],
            "sample": {
                "start": bt["metadata"]["sample_start"],
                "end": bt["metadata"]["sample_end"],
                "trading_days": bt["metadata"]["total_trading_days"],
            },
            "cost_basis_note": bt["metadata"]["cost_basis_note"],
            "known_caveats": [
                "Sharpe is computed as (CAGR - 2%) / sigma, while eq. (33b) in the text uses the arithmetic mean.",
                "Gross/Net labeling conflict: cost_basis_note says core tables are net of 10bp, "
                "but the 30P table footnote calls 14.82% / 1.68 the Gross figures (= the 0bp row here).",
                "See audit/verification_ledger.md for the full list of open defects.",
            ],
        },
        "labels": LABELS,
        "strategies": strategies,
        "monte_carlo": {
            "nature": "monte_carlo",
            "seed": sim["metadata"]["seed"],
            "n_paths": sim["metadata"]["n_paths"],
            "years": sim["metadata"]["years"],
            "shocks": sim["metadata"]["shocks"],
            "strategies": monte_carlo,
            "proposed_vs_mvo": {
                "share_paths_proposed_growth_higher": vs["share_paths_proposed_growth_higher"],
            },
        },
        "illustrative_scenario": {
            "nature": "illustrative_scenario",
            "note": "Hardcoded constants in scripts/calculate_empirical_metrics.py. "
                    "Do not present as simulation output or historical backtest.",
            "regimes": regimes,
            "cost_sensitivity": cost_sensitivity,
        },
    }

    OUT_JSON.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT_JSON, "w", encoding="utf-8") as f:
        json.dump(bundle, f, ensure_ascii=False, indent=2)
        f.write("\n")
    print(f"Saved: {OUT_JSON.relative_to(BASE_DIR)}")


if __name__ == "__main__":
    main()
