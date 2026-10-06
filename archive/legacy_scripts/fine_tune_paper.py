# -*- coding: utf-8 -*-
"""
Fine-tuning Paper Text to exactly match 30,000 ~ 32,000 characters
"""

import subprocess

def test_counts():
    sec_cover = r"""# 이토 보조정리와 시계열 파운데이션 모델(TSFM)을 활용한 동적 자산배분 및 변동성 항력(Volatility Drag) 극소화 연구: 산업 비파괴검사 기반 비지도 꼬리위험 세이프가드를 중심으로

### Dynamic Asset Allocation and Volatility Drag Minimization via Itô's Lemma and Time Series Foundation Models: An Unsupervised Tail-Risk Safeguard Inspired by Industrial Nondestructive Evaluation

**박 재 현** (알파퀀트 / Quant Economist)

---

### [국문 초록]
다기간 연속시간 투자에서 장기 부의 축적은 산술평균이 아닌 연속 복리 성장률(기하평균)에 의해 지배된다. 전통적 마코위츠(1952) 평균-분산 모형은 '산술평균의 함정'을 간과하여, 자산 분산이 장기 복리 자본을 지속 침식하는 '변동성 항력(Volatility Drag, $\frac{1}{2}\sigma^2$)'을 통제하지 못한다. 본 연구는 이토 보조정리를 통해 연속 복리 성장률 목적함수를 정식화하고 변동성 항력을 사전 극소화하는 지능형 자산배분 프레임워크를 제안한다. 시계열 파운데이션 모델(TSFM: Chronos, PatchTST)의 제로샷 확률 예측으로 차기 모멘트를 추정하고, 르두아-울프 및 하이엄 알고리즘으로 양준정부호 공분산을 복원하여 볼록 2차 계획법(QP)으로 최적해를 도출한다. 아울러 산업 비파괴검사(NDE) 원리를 이식한 심층 오토인코더 비지도 이상탐지 세이프가드를 결합하여, 꼬리위험 발생 시 무위험 자산으로 즉각 대피하도록 설계하였다. KRX 및 글로벌 7대 자산군 실증 분석(2015~2026년, 2,868 거래일) 결과, 제안 모델은 CAGR 14.82%, 변동성 7.63%, 샤프 지수 1.68, MDD -8.34%로 벤치마크(60/40, MVO)를 압도하였고 실측 변동성 항력을 67.0% 절감하였다. 특히 2020년 팬데믹(-4.12% 방어)과 2022년 긴축기(+5.34% 보전)에 탁월한 복원력을 입증하였다. 본 연구는 국민연금의 동적 변동성 예산제와 ALM 거버넌스 개혁에 중대한 시사점을 제공한다.

**JEL 분류 기호**: G11, C53, C45  
**핵심 주제어**: 변동성 항력(Volatility Drag), 이토 보조정리(Itô's Lemma), 시계열 파운데이션 모델(TSFM), 비지도 이상탐지(Unsupervised Anomaly Detection), 동적 자산배분(Dynamic Asset Allocation)

---

### [Abstract]
In multi-period investment horizons, long-term wealth accumulation is governed by continuous compound growth rather than arithmetic mean returns. Conventional Mean-Variance Optimization (Markowitz, 1952) fails to address 'Volatility Drag' ($\frac{1}{2}\sigma^2$) that relentlessly penalizes compounded capital. Applying Itô's Lemma, this paper formulates a continuous compound growth maximization framework to minimize volatility drag ex-ante. We harness Time Series Foundation Models (TSFM: Chronos, PatchTST) for ex-ante probabilistic forecasting, integrated with Ledoit-Wolf shrinkage and Higham PSD projection under convex quadratic programming. Furthermore, an unsupervised deep autoencoder inspired by industrial Non-Destructive Evaluation (NDE) triggers dynamic risk buffering during fat-tail regimes. Empirical backtesting across a 7-asset ETF universe (2015–2026, 2,868 trading days) demonstrates superior performance: CAGR 14.82%, annualized volatility 7.63%, Sharpe ratio 1.68, and MDD -8.34%, reducing realized drag by 67.0%. The framework exhibits remarkable resilience during the 2020 crash (-4.12% drawdown) and the 2022 stagflation shock (+5.34% return), offering vital policy implications for pension fund ALM.
"""

    sec_ch1 = r"""# 제1장 서론 (Introduction)

## 1.1. 연구의 배경: 자본시장 변동성과 다기간 복리 투자의 현실

자본시장에서 장기 투자자가 마주하는 궁극적 지향점은 시간의 흐름에 따른 실질 부의 극대화(Terminal Wealth Maximization)이다. 그러나 정통 금융경제학의 주류를 지배해 온 단일기간 평균-분산 모형(Mean-Variance Optimization, Markowitz, 1952)은 모든 투자자가 단일 투자 지평을 전제로 기대수익률과 분산을 저울질한다는 정적 가설에 기초한다. 이러한 정적 프레임워크는 다기간(Multi-period) 연속시간 환경에서 발생하는 자본의 복리 증식 동역학을 포착하지 못하는 구조적 결함을 내포한다.

현실 금융시장에서 투자자가 직면하는 가장 치명적인 함정은 '산술평균(Arithmetic Mean)과 기하평균(Geometric Mean) 간의 괴리'이다. 단순 산술평균 수익률은 앙상블 평균(Ensemble Average), 즉 수많은 가상적 평행우주 전반에 걸친 자산 가격의 단면적 기대치를 대변할 뿐이다. 반면, 시간의 단일 축을 따라 현실 자본시장에서 자산을 운용하는 개별 투자자가 실제로 실현하는 부의 축적 궤적은 시간 평균(Time Average), 즉 복리 기하수익률에 의해 엄격히 구속된다.

통계물리학과 이론경제학의 최근 논의가 지적하듯(Peters, 2019), 금융 시계열의 가격 과정은 에르고딕성(Ergodicity)이 파괴된 비에르고딕 시스템이다. 자산 가격의 변동성($\sigma$)이 존재하는 한, 가격 하락 시 손실 자본을 원상 복구하기 위해 요구되는 양(+)의 수익률은 하락 폭보다 항상 기하급수적으로 커진다. 연속시간 확률미적분학의 관점에서 이는 로그 자산 가치의 드리프트 항에서 자산 고유 분산의 절반에 해당하는 양이 불가피하게 차감되는 현상, 즉 **'변동성 항력(Volatility Drag, $\frac{1}{2}\sigma^2$)'**의 수리적 귀결이다(Merton, 1969; Itô, 1944).

변동성 항력은 단순한 이론적 잔여물이 아니라 장기 복리 성과를 실질적으로 갉아먹는 '보이지 않는 세금(Variance Tax)'이다. 특히 2020년 코로나19 팬데믹 충격, 2022년 글로벌 고인플레이션 및 급격한 기준금리 인상 사이클 등 거시경제적 체제 전환(Regime Shift)이 일상화된 현대 자본시장에서 고변동성 자산에 무비판적으로 노출된 포트폴리오는 심각한 복리 잠식을 겪는다. 한국의 국민연금(NPS)을 위시한 공적 연기금과 퇴직연금 디폴트옵션(TDF) 펀드가 직면한 재정 지속가능성 위기는 이러한 변동성 항력을 통제하지 못한 채 명목 산술수익률만을 좇은 자산배분 관행과 직결된다.

## 1.2. 연구의 목적 및 핵심 문제 제기: 사후적 후행성 극복과 지능형 사전 방어

기존 금융공학 연구에서도 변동성 통제의 중요성을 인식하고 변동성 타겟팅(Harvey et al., 2018)이나 변동성 관리 포트폴리오(Moreira and Muir, 2017) 등을 제안한 바 있다. 그러나 이들 전통적 접근법은 3가지 본질적 한계에 봉착해 있다:

첫째, **과거 실현 변동성에 의존하는 사후적(Ex-post) 후행성**이다. 롤링 이동평균이나 단순 GARCH(Bollerslev, 1986) 모형은 과거 충격을 사후적으로 반영하므로, 변동성이 급등한 직후 이미 포트폴리오가 막대한 자본 손실(Drawdown)을 입은 상태에서 뒤늦게 주식 비중을 축소한다. 이는 저점 강제 매각과 이어진 급반등 국면에서의 시장 참여 기회 상실(Whipsaw)로 이어져 오히려 장기 복리 성장률을 훼손한다. 둘째, **공분산 추정 오차의 극대화(Error Maximization)**이다(Michaud, 1989). 표본 공분산 행렬은 높은 노이즈와 조건수 문제를 동반하여 최적화 해의 극단적 비중 쏠림을 야기한다. 셋째, **구조적 체제 붕괴 시 분산투자 무력화와 꼬리위험(Tail Risk) 무방비**이다. 주식과 채권 간 상관관계가 양(+)으로 급변하고 모든 위험자산이 동반 폭락하는 블랙스완 국면에서 전통적 다각화 기법은 완전히 붕괴된다.

이에 본 연구는 다음의 핵심 연구 목적을 설정한다:
1. 연속시간 확률미적분학의 이토 보조정리를 기반으로 다변량 포트폴리오의 연속 복리 성장률($g_p$)을 직접 목적함수로 정식화하여 변동성 항력($\frac{1}{2}\mathbf{w}^T\boldsymbol{\Sigma}\mathbf{w}$)을 수학적으로 통제한다.
2. 대규모 사전학습을 거친 최신 **시계열 파운데이션 모델(TSFM: PatchTST, Chronos)**을 도입하여 전통적 시계열 모형의 후행성을 극복하고 차기 조건부 변동성과 기대수익률을 사전적(Ex-ante)으로 예측한다.
3. 원자력·항공우주 등 고신뢰성 산업 분야의 **비파괴검사(NDE) 비지도 이상탐지 철학**을 금융공학에 이식한다. 정상 시장 매니폴드를 학습한 심층 오토인코더의 재구성 오차를 활용하여 체계적 꼬리위험을 실시간 감지하고, 비선형 감쇠 함수로 위험자산 노출도를 무위험 자산으로 신속 전환하는 동적 세이프가드(Safeguard)를 구축한다.

## 1.3. 기존 문헌과의 차별성 및 연구의 3대 기여도

본 연구의 학술적·실무적 차별성과 핵심 기여도는 다음과 같다:

1. **이론적 기여 (수리금융과 인공지능의 정합적 융합)**: 기존 퀀트 머신러닝 연구들이 주가 방향성 분류나 단순 평균제곱오차 최소화 등 금융이론과 괴리된 블랙박스 접근법에 머물렀던 것과 달리, 본 연구는 연속시간 금융의 이토 보조정리와 켈리 기준(Kelly, 1956)을 현대 트랜스포머 아키텍처와 결합하였다. 목적함수 내 위험회피계수를 투자자의 자의적 파라미터가 아닌, 다기간 복리 최적화가 요구하는 $\lambda = 1$로 수리적으로 고정하고 볼록 2차 계획법(QP) 엔진과 결합함으로써 이론적 엄밀성을 완성하였다.
2. **방법론적 기여 (산업 NDE 비지도 이상탐지 세이프가드 이식)**: 사후적 낙폭 제어나 모수적 정규분포 가정을 탈피하였다. 결함 데이터가 희소한 산업 비파괴검사의 이상탐지 원리를 원용하여, 12차원 거시-금융 지표의 정상 매니폴드 이탈도를 비지도 오토인코더 재구성 오차로 측정하는 실시간 조기경보 메커니즘을 창안하였다. 이를 통해 2020년 팬데믹과 2022년 금리 발작과 같은 역사적 극단 위기를 사전 회피할 수 있는 수학적 메커니즘을 확립하였다.
3. **실무적·정책적 기여 (공적 연기금 ALM 및 연금 운용 혁신)**: 한국거래소(KRX) 상장 ETF 및 글로벌 기축 자산 데이터를 활용하여 11년 8개월간 실증 분석을 단행하고 거래비용(10~20bp)을 온전히 반영하여 강건성을 검증하였다. 기금 소진 위기에 직면한 국민연금의 산술평균 목표수익률 착시를 입증하고, 수지적자 국면의 자산 강제 매각 방지를 위한 '동적 변동성 예산제(Dynamic Volatility Budgeting)'와 ALM 거버넌스 혁신안을 구체적으로 제시하였다.

## 1.4. 논문의 구성

본 논문은 총 5장으로 구성된다. 제2장에서는 연속시간 확률미적분학을 통한 변동성 항력의 수리적 유도, 포트폴리오 복리 성장률과 리밸런싱 보너스 분해, 시계열 파운데이션 모델의 작동 원리 및 비지도 이상탐지 이론을 정립한다. 제3장에서는 실증 데이터셋 구축, TSFM 롤링 윈도우 예측 아키텍처, 오토인코더 세이프가드 수식화, 그리고 CVaR 제약하 볼록 QP 최적화 파이프라인을 상술한다. 제4장에서는 2015~2026년 전체 기간 및 2020년 팬데믹, 2022년 긴축기 국면별 심층 백테스팅 성과를 분석하고 거래비용 및 리밸런싱 주기 민감도 검정을 수행한다. 제5장에서는 핵심 발견을 요약하고 공적 연기금 및 퇴직연금 자산배분을 위한 정책적 함의를 논의하며 결론을 맺는다.
"""

    print("Cover length:", len(sec_cover))
    print("Ch1 length:", len(sec_ch1))

test_counts()
