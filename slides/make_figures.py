#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
make_figures.py
Generates presentation figures in PDF format and QR code in PNG format.
"""

from pathlib import Path
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np
import pandas as pd
import segno

plt.rcParams['font.family'] = 'Apple SD Gothic Neo'
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 10

OUT_DIR = Path("/Users/pj/dev/alphaquant-tsfm-voldrag/slides/MyFigure")
EMP_DIR = Path("/Users/pj/dev/alphaquant-tsfm-voldrag-empirical")
OUT_DIR.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------------------------
# 1. Figure 1: Arithmetic Mean Illusion (+50% / -50%)
# ---------------------------------------------------------------------------
def make_fig1():
    fig, ax = plt.subplots(figsize=(6.5, 3.2), dpi=300)
    
    periods = np.arange(7)
    returns = [0.50, -0.50, 0.50, -0.50, 0.50, -0.50]
    
    wealth_actual = [100.0]
    for r in returns:
        wealth_actual.append(wealth_actual[-1] * (1.0 + r))
        
    wealth_arith = [100.0 * (1.0 + 0.0)**t for t in periods]
    
    ax.plot(periods, wealth_actual, 'o-', color='#B22222', linewidth=2.5, markersize=6, label=r'실제 복리 자산 궤적 ($W_t$)')
    ax.plot(periods, wealth_arith, '--', color='#4682B4', linewidth=2, label=r'산술평균 기대 궤적 ($\mu = 0\%$)')
    
    for t, w in zip(periods, wealth_actual):
        ax.annotate(f"{w:.1f}", (t, w), textcoords="offset points", xytext=(0, 8 if t%2!=0 else -15),
                    ha='center', fontsize=9, fontweight='bold', color='#B22222')
        
    ax.axhline(100.0, color='gray', linestyle=':', alpha=0.6)
    ax.set_title(r"산술평균의 착시: +50%와 -50%의 반복과 복리 자본 잠식", fontsize=11, fontweight='bold', pad=10)
    ax.set_xlabel("투자 기간 (t)", fontsize=10)
    ax.set_ylabel("자산 가치 (초기 100 기준)", fontsize=10)
    ax.set_xticks(periods)
    ax.set_xticklabels([f"t={t}" for t in periods])
    ax.set_ylim(30, 160)
    ax.grid(True, linestyle='--', alpha=0.4)
    ax.legend(loc='upper right', framealpha=0.9)
    
    ax.text(0.03, 0.12, r"산술평균: $\mu = (+50\% - 50\%)/2 = 0\%$" + "\n" +
                        r"기하평균: $g = \sqrt{1.5 \times 0.5} - 1 = -13.4\%$" + "\n" +
                        r"변동성 항력: $\Delta = \mu - g = 13.4\%p$",
            transform=ax.transAxes, fontsize=8.5, bbox=dict(boxstyle="round,pad=0.4", fc="#FFF8DC", ec="#D2B48C", alpha=0.9))
    
    plt.tight_layout()
    fig.savefig(OUT_DIR / "arith_vs_geom.pdf")
    plt.close(fig)
    print("Saved arith_vs_geom.pdf")

# ---------------------------------------------------------------------------
# 2. Figure 2: Volatility Drag vs Sigma and Leverage L^2 Scaling
# ---------------------------------------------------------------------------
def make_fig2():
    fig, ax = plt.subplots(figsize=(6.5, 3.2), dpi=300)
    
    sigma = np.linspace(0.0, 0.40, 100)
    drag_1x = 0.5 * sigma**2 * 100.0
    drag_2x = 0.5 * (2 * sigma)**2 * 100.0
    drag_3x = 0.5 * (3 * sigma)**2 * 100.0
    
    ax.plot(sigma * 100, drag_1x, color='#2E8B57', linewidth=2.2, label=r'기본 자산 (L = 1x): $\frac{1}{2}\sigma^2$')
    ax.plot(sigma * 100, drag_2x, color='#DAA520', linewidth=2.2, label=r'2배 레버리지 (L = 2x): $2\sigma^2$ ($4\times$)')
    ax.plot(sigma * 100, drag_3x, color='#B22222', linewidth=2.2, label=r'3배 레버리지 (L = 3x): $\frac{9}{2}\sigma^2$ ($9\times$)')
    
    ax.axvline(24.53, color='#B22222', linestyle=':', alpha=0.5)
    ax.text(24.8, 12.0, r"KOSDAQ 150" + "\n" + r"($\sigma=24.5\%$, 항력 3.0%p)", fontsize=8, color='#8B0000')
    
    ax.set_title(r"변동성 항력의 비선형성: $\sigma$ 증가 및 레버리지($L^2$)에 따른 급증", fontsize=11, fontweight='bold', pad=10)
    ax.set_xlabel(r"기초 자산 연율화 변동성 ($\sigma$, %)", fontsize=10)
    ax.set_ylabel("연간 변동성 항력 손실률 (%p)", fontsize=10)
    ax.set_xlim(0, 40)
    ax.set_ylim(0, 35)
    ax.grid(True, linestyle='--', alpha=0.4)
    ax.legend(loc='upper left', framealpha=0.9, fontsize=9)
    
    plt.tight_layout()
    fig.savefig(OUT_DIR / "drag_vs_sigma.pdf")
    plt.close(fig)
    print("Saved drag_vs_sigma.pdf")

# ---------------------------------------------------------------------------
# 3. Figure 3: Real 2020 Pandemic Safeguard Defense (Real Market Data)
# ---------------------------------------------------------------------------
def make_fig3():
    ret_file = EMP_DIR / "results" / "daily_returns_primary_10bp.csv"
    sig_file = EMP_DIR / "results" / "safeguard_signals.csv"
    
    if not (ret_file.exists() and sig_file.exists()):
        print("Real data CSV not found, skipping fig3")
        return
        
    df_ret = pd.read_csv(ret_file, parse_dates=['date']).set_index('date')
    df_sig = pd.read_csv(sig_file, parse_dates=['date']).set_index('date')
    
    mask_ret = (df_ret.index >= '2020-01-02') & (df_ret.index <= '2020-06-30')
    sub_ret = df_ret.loc[mask_ret].copy()
    
    cum_prop = (1.0 + sub_ret['proposed']).cumprod()
    cum_6040 = (1.0 + sub_ret['6040']).cumprod()
    cum_mvo  = (1.0 + sub_ret['mvo']).cumprod()
    
    sub_sig = df_sig.reindex(sub_ret.index).fillna(0.0)
    
    fig, ax1 = plt.subplots(figsize=(7.2, 3.4), dpi=300)
    
    ax1.plot(sub_ret.index, cum_prop, color='#B22222', linewidth=2.4, label='제안 모델 (TSFM-Ito, 실데이터 MDD -4.65%)')
    ax1.plot(sub_ret.index, cum_mvo, color='#4682B4', linewidth=1.8, linestyle='--', label='마코위츠 MVO (MDD -10.64%)')
    ax1.plot(sub_ret.index, cum_6040, color='#708090', linewidth=1.8, linestyle=':', label='전통적 60/40 (MDD -19.18%)')
    
    ax1.set_ylabel("누적 자산 가치 (2020-01-02=1.0)", fontsize=9.5)
    ax1.set_ylim(0.75, 1.15)
    ax1.grid(True, linestyle='--', alpha=0.35)
    
    ax2 = ax1.twinx()
    ax2.fill_between(sub_ret.index, sub_sig['beta'], color='#FFA500', alpha=0.25, label=r'세이프가드 현금 비중 ($\beta_t$, 평균 69%)')
    ax2.plot(sub_ret.index, sub_sig['beta'], color='#FF8C00', linewidth=1.2)
    ax2.set_ylabel(r"현금 대피 비중 ($\beta$)", fontsize=9.5, color='#B8860B')
    ax2.set_ylim(0.0, 1.05)
    ax2.tick_params(axis='y', labelcolor='#B8860B')
    
    trigger_dt = pd.to_datetime('2020-02-03')
    ax1.axvline(trigger_dt, color='#8B0000', linestyle='--', linewidth=1.5, alpha=0.8)
    ax1.text(trigger_dt, 0.80, " 2020-02-03\n 첫 세이프가드 발동", color='#8B0000', fontsize=8.5, fontweight='bold')
    
    ax1.set_title("실데이터 검증: 2020 팬데믹 세이프가드의 선제적 현금 대피 및 방어", fontsize=10.5, fontweight='bold', pad=10)
    
    lines1, labels1 = ax1.get_legend_handles_labels()
    lines2, labels2 = ax2.get_legend_handles_labels()
    ax1.legend(lines1 + lines2, labels1 + labels2, loc='upper left', fontsize=8, framealpha=0.9)
    
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%m월'))
    ax1.xaxis.set_major_locator(mdates.MonthLocator())
    
    plt.tight_layout()
    fig.savefig(OUT_DIR / "real_2020_safeguard.pdf")
    plt.close(fig)
    print("Saved real_2020_safeguard.pdf")

# ---------------------------------------------------------------------------
# 4. Figure 4: Transaction Cost Sensitivity (Simulation vs Real-Data)
# ---------------------------------------------------------------------------
def make_fig4():
    fig, ax = plt.subplots(figsize=(6.5, 3.2), dpi=300)
    
    costs = [0, 5, 10, 15, 20]
    paper_cagr = [14.82, 14.73, 14.63, 14.54, 14.44]
    
    real_costs = [0, 10, 20]
    real_cagr = [15.11, 11.91, 8.81]
    
    ax.plot(costs, paper_cagr, 's-', color='#2E8B57', linewidth=2.2, label='제출본 시뮬레이션 (회전율 46.8% 가정)')
    ax.plot(real_costs, real_cagr, 'o-', color='#B22222', linewidth=2.4, label='실데이터 사전등록 재현 (회전율 2,804% 실측)')
    
    ax.axhline(10.37, color='#708090', linestyle='--', linewidth=1.5, label='실데이터 60/40 벤치마크 (10.37%)')
    
    ax.set_title("거래비용 민감도: 주간 회전율 마찰과 초과수익 감쇠", fontsize=11, fontweight='bold', pad=10)
    ax.set_xlabel("편도 거래비용 (bp)", fontsize=10)
    ax.set_ylabel("연평균 복리수익률 (CAGR, %)", fontsize=10)
    ax.set_xticks(costs)
    ax.set_ylim(6, 17)
    ax.grid(True, linestyle='--', alpha=0.4)
    ax.legend(loc='lower left', framealpha=0.9, fontsize=8.5)
    
    ax.annotate("0bp: 15.11%\n(수수료 없을 때 초과수익)", (0, 15.11), xytext=(2.5, 15.4),
                ha='left', fontsize=8, color='#B22222')
    ax.annotate("20bp: 8.81%\n(잦은 재최적화로 침식)", (20, 8.81), xytext=(15, 9.8),
                ha='right', fontsize=8, color='#B22222')
    
    plt.tight_layout()
    fig.savefig(OUT_DIR / "cost_sensitivity.pdf")
    plt.close(fig)
    print("Saved cost_sensitivity.pdf")

# ---------------------------------------------------------------------------
# 5. QR Code for GitHub
# ---------------------------------------------------------------------------
def make_qr():
    qr = segno.make('https://github.com/PJH720/alphaquant-tsfm-voldrag-empirical')
    qr.save(OUT_DIR / "qr_github.png", scale=8, border=2)
    print("Saved qr_github.png")

if __name__ == '__main__':
    make_fig1()
    make_fig2()
    make_fig3()
    make_fig4()
    make_qr()
    print("All presentation figures successfully generated!")
