#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
simulate_gbm_mc.py
--------------------------------------------------------------------------------
Monte Carlo simulation of the paper's strategy parameters under geometric
Brownian motion (GBM).

The strategy figures in this repository are SIMULATION PARAMETERS (annualized
arithmetic mean mu and volatility sigma per strategy), not a historical
backtest. This script simulates many GBM paths from those parameters to show
what they imply:

  * time-average (typical path) growth  -> g = mu - 0.5 * sigma^2   (Ito)
  * ensemble-average (mean) wealth       -> grows at mu
  * the gap between the two is the volatility drag the paper is about.

Daily log-return:  r_t = (mu - 0.5*sigma^2)/252 + sigma/sqrt(252) * eps_t,
eps_t ~ iid N(0, 1). Strategies are simulated with independent shocks (no
cross-strategy correlation is specified by the parameters).

Input : data/backtest_results.json (table_4_1_strategy_performance)
Output: data/simulation_results.json
--------------------------------------------------------------------------------
"""

import json
import math
from pathlib import Path

import numpy as np

BASE_DIR = Path(__file__).resolve().parents[1]
JSON_IN = BASE_DIR / "data" / "backtest_results.json"
JSON_OUT = BASE_DIR / "data" / "simulation_results.json"

SEED = 20261007
N_PATHS = 10_000
CHUNK = 1_000
TRADING_DAYS_PER_YEAR = 252
HORIZON_10Y_DAYS = 10 * TRADING_DAYS_PER_YEAR
RISK_FREE_PCT = 2.0  # same r_f the paper uses for Sharpe
PRINCIPAL = 100.0    # 100억원, as in Table 4-2


def load_parameters():
    with open(JSON_IN, "r", encoding="utf-8") as f:
        data = json.load(f)
    n_days = int(data["metadata"]["total_trading_days"])
    params = {
        row["strategy"]: {
            "mu_arith_pct": float(row["mu_arith"]),
            "sigma_pct": float(row["sigma"]),
            "paper_cagr_pct": float(row["cagr"]),
        }
        for row in data["table_4_1_strategy_performance"]
    }
    return params, n_days


def simulate_strategy(rng, mu_pct, sigma_pct, n_days):
    """Simulate N_PATHS GBM paths in chunks; return per-path summary arrays."""
    mu, sigma = mu_pct / 100.0, sigma_pct / 100.0
    drift = (mu - 0.5 * sigma ** 2) / TRADING_DAYS_PER_YEAR
    vol = sigma / math.sqrt(TRADING_DAYS_PER_YEAR)
    years = n_days / TRADING_DAYS_PER_YEAR

    growth, wealth10, mdd, sharpe = [], [], [], []
    for _ in range(N_PATHS // CHUNK):
        r = drift + vol * rng.standard_normal((CHUNK, n_days))
        log_wealth = np.cumsum(r, axis=1)

        # Annualized continuously-compounded growth of each path (time average)
        growth.append(log_wealth[:, -1] / years)
        # Terminal wealth after 10 years, starting from PRINCIPAL
        wealth10.append(PRINCIPAL * np.exp(log_wealth[:, HORIZON_10Y_DAYS - 1]))
        # Maximum drawdown over the full horizon
        running_peak = np.maximum.accumulate(np.maximum(log_wealth, 0.0), axis=1)
        mdd.append(np.min(np.exp(log_wealth - running_peak) - 1.0, axis=1))
        # Sharpe on simple returns, eq. (33b) definition: (mu_hat - r_f) / sigma_hat
        simple = np.expm1(r)
        mu_hat = simple.mean(axis=1) * TRADING_DAYS_PER_YEAR
        sigma_hat = simple.std(axis=1, ddof=1) * math.sqrt(TRADING_DAYS_PER_YEAR)
        sharpe.append((mu_hat - RISK_FREE_PCT / 100.0) / sigma_hat)

    return (np.concatenate(growth), np.concatenate(wealth10),
            np.concatenate(mdd), np.concatenate(sharpe))


def pct(x):
    return round(float(x) * 100.0, 4)


def summarize(p, growth, wealth10, mdd, sharpe):
    mu, sigma = p["mu_arith_pct"] / 100.0, p["sigma_pct"] / 100.0
    theo_g = mu - 0.5 * sigma ** 2
    return {
        "mu_arith_pct": p["mu_arith_pct"],
        "sigma_pct": p["sigma_pct"],
        "paper_cagr_pct": p["paper_cagr_pct"],
        "theoretical_g_pct": pct(theo_g),
        "theoretical_drag_pct": pct(0.5 * sigma ** 2),
        "mc_g_mean_pct": pct(growth.mean()),
        "mc_g_se_pct": pct(growth.std(ddof=1) / math.sqrt(len(growth))),
        "mc_g_p05_pct": pct(np.percentile(growth, 5)),
        "mc_g_p50_pct": pct(np.percentile(growth, 50)),
        "mc_g_p95_pct": pct(np.percentile(growth, 95)),
        "wealth_10y": {
            "unit": "억원 (principal 100)",
            "ensemble_mean": round(float(wealth10.mean()), 2),
            "median_typical_path": round(float(np.median(wealth10)), 2),
            "p05": round(float(np.percentile(wealth10, 5)), 2),
            "p95": round(float(np.percentile(wealth10, 95)), 2),
            "analytic_ensemble_mean": round(PRINCIPAL * math.exp(10 * mu), 2),
            "analytic_median": round(PRINCIPAL * math.exp(10 * theo_g), 2),
        },
        "mdd_p50_pct": pct(np.median(mdd)),
        "mdd_p05_pct": pct(np.percentile(mdd, 5)),
        "sharpe_p50": round(float(np.median(sharpe)), 3),
        "sharpe_p05": round(float(np.percentile(sharpe, 5)), 3),
        "sharpe_p95": round(float(np.percentile(sharpe, 95)), 3),
    }


def main():
    params, n_days = load_parameters()
    rng = np.random.default_rng(SEED)

    results, growth_by_name = {}, {}
    for name, p in params.items():
        growth, wealth10, mdd, sharpe = simulate_strategy(
            rng, p["mu_arith_pct"], p["sigma_pct"], n_days)
        results[name] = summarize(p, growth, wealth10, mdd, sharpe)
        growth_by_name[name] = growth

    proposed = next(n for n in params if "제안" in n)
    mvo = next(n for n in params if "MVO" in n)
    beats = float(np.mean(growth_by_name[proposed] > growth_by_name[mvo]))

    output = {
        "metadata": {
            "nature": "GBM Monte Carlo from simulation parameters; NOT a historical backtest",
            "source_parameters": "data/backtest_results.json:table_4_1_strategy_performance",
            "seed": SEED,
            "n_paths": N_PATHS,
            "n_days": n_days,
            "years": round(n_days / TRADING_DAYS_PER_YEAR, 4),
            "risk_free_pct": RISK_FREE_PCT,
            "shocks": "iid N(0,1), independent across strategies",
            "growth_definition": "annualized log growth = ln(W_T/W_0)/T, compare to mu - 0.5*sigma^2",
        },
        "strategies": results,
        "proposed_vs_mvo": {
            "proposed": proposed,
            "mvo": mvo,
            "share_paths_proposed_growth_higher": round(beats, 4),
        },
    }
    with open(JSON_OUT, "w", encoding="utf-8") as f:
        json.dump(output, f, ensure_ascii=False, indent=2)

    print(f"{'strategy':<24}{'theo g%':>9}{'MC g%':>9}{'±SE':>8}{'10y mean':>10}{'10y med':>9}{'MDD p50':>9}{'SR p50':>8}")
    for name, r in results.items():
        w = r["wealth_10y"]
        print(f"{name:<24}{r['theoretical_g_pct']:>9.3f}{r['mc_g_mean_pct']:>9.3f}{r['mc_g_se_pct']:>8.3f}"
              f"{w['ensemble_mean']:>10.2f}{w['median_typical_path']:>9.2f}{r['mdd_p50_pct']:>9.2f}{r['sharpe_p50']:>8.3f}")
    print(f"Proposed growth > MVO growth on {beats:.1%} of paths (independent shocks)")
    print(f"Saved: {JSON_OUT}")


if __name__ == "__main__":
    main()
