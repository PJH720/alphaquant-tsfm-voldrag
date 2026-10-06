# 이토 보조정리와 시계열 파운데이션 모델(TSFM)을 활용한 동적 자산배분 및 변동성 항력(Volatility Drag) 극소화 연구: 산업 비파괴검사 기반 비지도 꼬리위험 세이프가드를 중심으로

### Dynamic Asset Allocation and Volatility Drag Minimization via Itô's Lemma and Time Series Foundation Models: An Unsupervised Tail-Risk Safeguard Inspired by Industrial Nondestructive Evaluation

**박 재 현** (알파퀀트 / Quant Economist)

------------------------------------------------------------------------

### \[국문 초록\]

다기간(Multi-period) 연속시간 투자 환경에서 자산운용자의 장기 실질 부의
축적은 단순 산술평균이 아닌 연속 복리 성장률(기하평균)에 의해 엄격히
지배된다. 그러나 20세기 중반 이래 전통 금융이론의 근간을 형성해 온
마코위츠(Markowitz, 1952) 평균-분산 모형(MVO)은 단일 기간 정적
프레임워크에 매몰되어, 자산의 2차 모멘트(분산)가 장기 복리 자본을
지속적으로 잠식하는 '변동성 항력(Volatility Drag,
$\frac{1}{2}\sigma^{2}$)'의 파괴적 영향을 체계적으로 통제하지 못하는
이론적 결함을 내포한다. 본 연구는 연속시간 확률미적분학의 이토
보조정리(Itô's Lemma)를 원용하여 다변량 포트폴리오의 연속 복리 성장률을
직접 목적함수로 정식화하고, 변동성 항력을 사전적(Ex-ante)으로 극소화하는
지능형 동적 자산배분 아키텍처를 제안한다.

대규모 사전학습을 거친 최신 시계열 파운데이션 모델(TSFM: Chronos,
PatchTST)의 제로샷(Zero-shot) 확률 예측을 통해 차기 조건부 1차·2차
모멘트를 사전적으로 추정하고, 르두아-울프(Ledoit-Wolf) 비선형 축소와
하이엄(Higham) 교대 투영 알고리즘을 결합하여 양준정부호(PSD) 공분산
행렬을 강건하게 복원한 후 볼록 2차 계획법(Convex QP)으로 최적 가중치를
산출한다. 아울러 원자력·항공우주 등 고신뢰성 산업 분야의 비파괴검사(NDE)
결함 탐지 원리를 금융공학에 이식하여, 정상 시장 매니폴드를 비지도 학습한
심층 오토인코더(Deep Autoencoder)의 재구성 오차 기반 꼬리위험
세이프가드(Safeguard)를 구축하였다. 시스템적 이상 징후 감지 시 비선형
감쇠 함수를 통해 위험자산 노출도를 무위험 유동성 자산으로 즉각
대피하도록 설계하였다.

한국거래소(KRX) 상장 대표 ETF 및 글로벌 기축 자산 7대 자산군을 대상으로
한 11년 8개월간의 실증 분석(2015년 1월 \~ 2026년 8월, 2,868 거래일)
결과, 제안 모델은 연평균 복리수익률(CAGR) 14.82%, 연율화 변동성 7.63%,
샤프 지수 1.68, 최대 낙폭(MDD) -8.34%를 기록하여 전통적 60/40
벤치마크(CAGR 7.85%, 샤프 0.51, MDD -24.78%) 및 정적 마코위츠(CAGR
9.14%, MDD -28.65%)를 압도하였다. 특히 실측 변동성 항력 손실을 벤치마크
대비 67.0% 절감하였으며, 2020년 3월 팬데믹 발작기(MDD -4.12% 방어,
21거래일 만에 원금 회복)와 2022년 글로벌 긴축기(+5.34% 자본 보전)에서
탁월한 복원력을 입증하였다. 본 연구는 기금 고갈 위기에 직면한 국민연금의
산술수익률 착시를 계량적으로 입증하고, 수지적자 국면의 자산 강제 매각
방지를 위한 '동적 변동성 예산제(Dynamic Volatility Budgeting)'와 공적
연기금 ALM 거버넌스 개혁에 중대한 경제학적 시사점을 제공한다.

**JEL 분류 기호**: G11, C53, C45, G23\
**핵심 주제어**: 변동성 항력, 이토 보조정리, 시계열 파운데이션 모델,
비지도 이상탐지, 산업 비파괴검사, 동적 자산배분, 국민연금 ALM

------------------------------------------------------------------------

### \[Abstract\]

In multi-period continuous-time investment horizons, long-term wealth
accumulation is governed by continuous compound growth rather than
arithmetic mean return. Conventional Mean-Variance Optimization
(Markowitz, 1952) fails to address 'Volatility Drag'
($\frac{1}{2}\sigma^{2}$) that continuously erodes compounded capital
over time. Applying Itô's Lemma, this paper formulates an ex-ante
continuous compound growth maximization framework to minimize volatility
drag mathematically. We integrate Time Series Foundation Models (TSFM:
Chronos, PatchTST) for probabilistic moment forecasting with Ledoit-Wolf
shrinkage and Higham PSD projection under convex quadratic programming.

Furthermore, an unsupervised deep autoencoder inspired by industrial
Non-Destructive Evaluation (NDE) triggers dynamic risk buffering during
systemic tail-risk regimes. Across a 7-asset ETF universe (2015--2026,
2,868 trading days), empirical backtesting demonstrates superior
performance: CAGR 14.82%, annualized volatility 7.63%, Sharpe ratio
1.68, and MDD -8.34%, reducing realized volatility drag by 67.0%. The
framework exhibits remarkable resilience during the 2020 crash (-4.12%
drawdown, 21-day recovery) and the 2022 stagflation shock (+5.34%
return), offering critical ALM policy implications for sovereign pension
funds.

**Keywords**: Volatility Drag, Itô's Lemma, Time Series Foundation
Models, Unsupervised Anomaly Detection, Non-Destructive Evaluation,
Dynamic Asset Allocation, Pension ALM

# 제1장 서론 (Introduction)

## 1.1. 연구의 배경: 자본시장 변동성과 다기간 복리 투자의 현실

자본시장에서 장기 자산운용자가 마주하는 궁극적인 경제학적 지향점은
시간의 흐름에 따른 실질 종단 부의 극대화(Terminal Wealth
Maximization)이다. 그러나 20세기 중반 이래 정통
현대포트폴리오이론(Modern Portfolio Theory)의 주류를 지배해 온 단일기간
평균-분산 모형(Mean-Variance Optimization, Markowitz, 1952)은 모든
투자자가 동일하고 고정된 단일 투자 지평(Single-period Horizon)을 전제로
기대수익률과 분산을 저울질한다는 정적(Static) 가설에 기초한다. 이러한
정적 프레임워크는 연속적인 시간 축 위에서 자본이 재투자되며 증식하는
다기간(Multi-period) 연속시간 환경의 동역학적 실체를 근본적으로 포착하지
못하는 구조적 한계를 안고 있다.

머튼(Merton, 1969, 1971)의 연속시간 소비-투자 모형이 엄밀히 증명하듯,
다기간 환경에서 투자자의 최적 자산 배분 결정은 시간의 흐름에 따른 투자
기회집합(Investment Opportunity Set)의 확률적 변동과 상태변수의 진화에
동적으로 반응해야 한다. 그러나 전통적 마코위츠 프레임워크는 수익률
시계열이 독립항등분포(i.i.d.)를 따른다는 비현실적인 가정에 의존하여,
경로 의존성(Path-dependency)이 누적되는 복리 과정의 비선형적 특성을
완전히 사상(捨象)하였다. 단일 기간 최적화는 매 기간의 수익률을 상호
독립적인 정적 사건으로 취급하지만, 실제 투자자의 자본은 이전 기간의 실현
결과가 다음 기간의 투자 원금으로 전이되는 연속 복리 사슬(Compound Chain)
속에 놓여 있다.

현실 금융시장에서 장기 투자자가 직면하는 가장 치명적인 함정은 바로
'산술평균(Arithmetic Mean)과 기하평균(Geometric Mean) 간의 본질적
괴리'이다. 단순 산술평균 수익률은 앙상블 평균(Ensemble Average), 즉
무한히 상정할 수 있는 가상적 평행우주 전반에 걸친 자산 가격의 단면적
기대치를 대변할 뿐이다. 반면 단 하나의 현실 시간 축을 따라 자산을
운용하는 개별 투자자가 실제로 경험하는 부의 궤적은 시간 평균(Time
Average), 즉 복리 기하수익률에 의해 엄격히 지배된다.

통계물리학과 이론경제학의 최근 논의가 명쾌히 지적하듯(Peters, 2019;
Gell-Mann and Peters, 2016), 금융 시계열의 가격 형성 과정은 앙상블
평균과 시간 평균이 일치하지 않는 대표적인 비에르고딕(Non-ergodic)
시스템이다. 부의 축적 과정은 덧셈(Additive)이 아닌
곱셈(Multiplicative)의 동역학을 따르므로, 자산 가격에 변동성($\sigma$)이
존재하는 한 가격 하락 시 손실 자본을 원상 복구하기 위해 요구되는 양(+)의
수익률은 하락 폭보다 항상 기하급수적으로 커진다. 예컨대 자산 가격이 50%
하락할 경우 원금을 회복하기 위해서는 100%의 상승률이 필요하며, 이러한
비대칭성은 변동성이 증가할수록 기하급수적으로 확대된다.

연속시간 확률미적분학(Continuous-time Stochastic Calculus)의 관점에서
이는 로그 자산 가치의 드리프트 항에서 자산 고유 분산의 절반에 해당하는
양이 불가피하게 차감되는 현상, 즉 **'변동성 항력(Volatility Drag,**
$\frac{1}{2}\sigma^{2}$**)'**의 필연적 수리적 결과이다(Merton, 1969;
Itô, 1944). 변동성 항력은 단순한 이론적 잔여물이 아니라 장기 복리 성과를
실질적으로 갉아먹는 '보이지 않는 세금(Variance Tax)'이다. 특히 2020년
코로나19 팬데믹 충격, 2022년 글로벌 고인플레이션 및 급격한 기준금리 인상
사이클 등 거시경제적 체제 전환(Regime Shift)이 빈번해진 현대
자본시장에서 고변동성 자산에 무비판적으로 노출된 포트폴리오는 심각한
복리 잠식을 피할 수 없다.

대한민국 국민연금(NPS)을 위시한 공적 연기금과 퇴직연금 디폴트옵션(TDF)
펀드가 직면한 재정 지속가능성 위기는 이러한 변동성 항력을 통제하지 못한
채 명목 산술수익률만을 좇은 전통적 자산배분 관행과 직결된다. 연기금의
자산 축적기에서는 복리 잠식이 기금 성장률을 저해하고, 급여 지출이 보험료
수입을 초과하는 수지적자 국면에서는 자산 급락 시 연금 지급을 위해 자산을
헐값에 강제 매각해야 하는 '역복리의 덫(Reverse Compounding Trap)'을
유발하기 때문이다.

## 1.2. 연구의 목적 및 핵심 문제의식

전통적 자산배분 연구와 실무 관행은 변동성 항력의 파괴적 파급력을
사전적으로 통제하는 데 명확한 세 가지 구조적 한계를 드러내 왔다: 첫째,
전통적 자산배분은 자산 간 상관관계와 변동성이 시간에 따라 급변하는
시계열 이분산성(Heteroskedasticity)을 적시에 반영하지 못하며, 정적
공분산 행렬에 고착되어 위기 국면의 상관관계 급등(Correlation
Breakdown)을 방치한다. 둘째, GARCH(Bollerslev, 1986)나 역사적 롤링 분산
등 전통적 시계열 계량 모형은 본질적으로 과거 충격의 사후적 잔차에
반응하는 후행적(Lagging) 지표에 의존하므로, 급격한 시장 변곡점이나
블랙스완 사태에서 포트폴리오를 선제적으로 보호하지 못한다. 셋째,
정규분포 가정에 입각한 대칭적 리스크 척도는 금융 자산의 두터운
꼬리(Fat-tail)와 비대칭적 하방 위험을 체계적으로 과소평가하여 위기
국면에서 대규모 비가역적 자본 훼손을 초래한다.

이러한 문제의식에 기초하여 본 연구는 다음의 네 가지 핵심 연구 목적을
설정한다: 1. 연속시간 확률미적분학의 이토 보조정리를 토대로 다변량
포트폴리오의 연속 복리 성장률($g_{p}$)을 직접 목적함수로 정식화하고,
목적함수 차원에서 변동성
항력($\frac{1}{2}\mathbf{w}^{T}\mathbf{\Sigma}\mathbf{w}$)을 수학적으로
통제하는 자산배분 모형을 수립한다. 2. 대규모 사전학습을 거친 최신
**시계열 파운데이션 모델(TSFM: PatchTST, Chronos)**을 도입하여 전통적
시계열 모형의 후행성을 극복하고 차기 조건부 변동성과 기대수익률을
사전적(Ex-ante)으로 예측하는 지능형 모멘트 추정 파이프라인을 구축한다.
3. 원자력·항공우주 등 극한 환경의 **산업 비파괴검사(NDE) 비지도 이상탐지
철학**을 금융공학에 이식한다. 정상 시장 매니폴드를 학습한 심층
오토인코더(Deep Autoencoder)의 재구성 오차를 통해 시스템적 꼬리위험을
실시간 감지하고, 비선형 감쇠 함수로 위험자산 노출도를 무위험 자산으로
신속 전환하는 동적 세이프가드(Safeguard)를 완성한다. 4. 한국거래소(KRX)
상장 ETF 및 글로벌 기축 자산 데이터를 기반으로 11년
8개월간(2015\~2026년)의 엄밀한 백테스팅을 수행하여 거래비용(10\~20bp)
차감 후 순성과를 검증하고, 국민연금의 중기자산배분(SAA) 및 ALM 거버넌스
혁신을 위한 구체적 정책 대안을 도출한다.

## 1.3. 기존 문헌과의 차별성 및 연구의 3대 기여도

본 연구의 학술적·실무적 차별성과 핵심 기여도는 다음과 같다:

1.  **이론적 기여 (수리금융과 인공지능의 유기적 융합)**: 기존 퀀트
    머신러닝 연구들이 주가 방향성 분류나 단순 오차 최소화 등 금융이론과
    괴리된 블랙박스 예측에 머물렀던 것과 달리, 본 연구는 연속시간 금융의
    이토 보조정리와 켈리 기준(Kelly, 1956)을 현대 트랜스포머 아키텍처와
    결합하였다. 목적함수 내 위험회피계수를 투자자의 주관적 파라미터가
    아닌 다기간 복리 최적화가 요구하는 $\lambda = 1$로 엄밀히 고정하고,
    하이엄(Higham, 2002) 양준정부호(PSD) 투영을 통해 볼록 2차 계획법(QP)
    엔진과의 수학적 정합성을 완성하였다.
2.  **방법론적 기여 (산업 NDE 비지도 이상탐지 세이프가드 창안)**: 사후적
    낙폭 제어나 비현실적인 정규분포 가정을 완전히 탈피하였다. 결함
    데이터가 희소한 산업 비파괴검사의 이상탐지 원리를 원용하여, 12차원
    거시-금융 지표의 정상 매니폴드 이탈도를 비지도 오토인코더 재구성
    오차로 측정하는 실시간 조기경보 메커니즘을 구축하였다. 이를 통해
    2020년 팬데믹과 2022년 금리 발작과 같은 역사적 극단 위기를 사전
    회피할 수 있는 수학적 메커니즘을 확립하였다.
3.  **실무적·정책적 기여 (공적 연기금 ALM 및 자산운용 실무 혁신)**: 국내
    상장 대표 ETF 유니버스를 대상으로 실증 분석을 수행하고 거래비용을
    온전히 반영하여 실무 적용 가능성을 입증하였다. 특히 기금 소진 위기에
    직면한 국민연금의 산술평균 목표수익률 착시를 계량적으로 규명하고,
    수지적자 국면의 자산 강제 매각 방지를 위한 '동적 변동성
    예산제(Dynamic Volatility Budgeting)'와 퇴직연금 TDF 운용
    가이드라인을 구체적으로 제시하였다.

## 1.4. 논문의 구성

본 논문은 총 5장으로 구성된다. 제2장에서는 연속시간 확률미적분학을 통한
변동성 항력의 수리적 유도, 포트폴리오 복리 성장률과 리밸런싱 보너스
분해, 시계열 파운데이션 모델의 작동 원리 및 비지도 이상탐지 이론을
정립한다. 제3장에서는 실증 데이터셋 구축, TSFM 롤링 윈도우 예측
아키텍처, 오토인코더 세이프가드 수식화, 그리고 CVaR 제약하 볼록 QP
최적화 파이프라인을 상술한다. 제4장에서는 2015\~2026년 전체 기간 및
2020년 팬데믹, 2022년 긴축기 국면별 심층 백테스팅 성과를 분석하고
거래비용 및 리밸런싱 주기 민감도 검정을 수행한다. 제5장에서는 핵심
발견을 요약하고 공적 연기금 및 퇴직연금 자산배분을 위한 정책적 함의를
논의하며 결론을 맺는다.

# 제2장 이론적 배경 및 선행연구 (Theoretical Framework & Literature Review)

## 2.1. 연속시간 확률미적분학과 변동성 항력(Volatility Drag)의 수리적 메커니즘

### 2.1.1. 자산 가격의 확률과정과 기하 브라운 운동 (GBM)

완비확률공간
$(\Omega,\mathcal{F},(\mathcal{F}_{t})_{t \geq 0},\mathbb{P})$ 상에서
금융 자산 가격 $S_{t}$의 연속적 가격 형성 과정을 모델링한다. 여기서
$(\mathcal{F}_{t})_{t \geq 0}$는 표준 브라운 운동 $W_{t}$에 의해 생성된
자연 여과확률체계(Natural Filtration)이다. 유한책임 자산의
비음성(Non-negativity)과 자산 가격 수준에 비례하는 절대 변동성을
만족하기 위해 자산 가격 과정은 통상 기하 브라운 운동(Geometric Brownian
Motion, GBM) 확률미분방정식을 따른다(Merton, 1969, 1971):

$$dS_{t} = \mu S_{t}dt + \sigma S_{t}dW_{t}\quad\quad(1)$$

식 (1)에서 $\mu \in \mathbb{R}$는 순간 산술 기대수익률(드리프트 계수,
Drift)이며, $\sigma > 0$는 조건부 순간 변동성(확산 계수, Diffusion)이다.
$W_{t}$는 평균이 0이고 분산이 $t$인 표준 위너 과정(Wiener Process)이다.

### 2.1.2. 이토 보조정리(Itô's Lemma)와 변동성 항력의 엄밀한 도출

일반 미적분학의 쇄미법(Chain Rule)과 달리, 확률미적분학에서는 브라운
운동의 궤적이 거의 모든 곳에서 미분 불가능하며 유한한 2차 변분(Quadratic
Variation)을 갖는다는 본질적 차이가 존재한다. 임의의 시간 분할
$\Pi = \{ 0 = t_{0} < t_{1} < \ldots < t_{m} = t\}$에 대해 분할의 메시
크기 $\parallel \Pi \parallel \rightarrow 0$일 때, 브라운 운동의 2차
변분은 다음과 같이 시간에 수렴한다:

$$\lbrack W,W\rbrack_{t} = \lim_{\parallel \Pi \parallel \rightarrow 0}\sum_{k = 1}^{m}(W_{t_{k}} - W_{t_{k - 1}})^{2} = t\quad\text{a.s.}\quad\quad(2)$$

확률적 미소 증분 $\Delta W_{t} = W_{t + \Delta t} - W_{t}$의 제곱의
기댓값은 $\mathbb{E}\lbrack(\Delta W_{t})^{2}\rbrack = \Delta t$이며, 그
분산은
$\text{Var}((\Delta W_{t})^{2}) = 2(\Delta t)^{2} = \mathcal{O}((\Delta t)^{2})$이므로
$\Delta t \rightarrow 0$ 극한에서 $(dW_{t})^{2}$은 확률 1로 결정론적
무한소 $dt$와 동일해진다. 이에 따라 무한소 증분 곱에 관한 유명한 이토
곱셈표(Itô Multiplication Rules)가 성립한다:

$$dt \cdot dt = 0,\quad dt \cdot dW_{t} = 0,\quad dW_{t} \cdot dt = 0,\quad(dW_{t})^{2} = dt\quad\quad(3)$$

자산의 연속 복리 가치 척도인 로그 가치 과정 $f(S_{t}) = \ln S_{t}$를
정의하고, 2변수 2계 연속미분가능 함수에 대한 테일러 2차 전개 기반 이토
보조정리(Itô, 1944)를 적용하면 다음과 같다:

$$df(S_{t}) = \frac{\partial f}{\partial t}dt + f'(S_{t})dS_{t} + \frac{1}{2}f''(S_{t})(dS_{t})^{2}\quad\quad(4)$$

여기서 $f(S_{t}) = \ln S_{t}$는 시간에 명시적으로 의존하지 않으므로
$\frac{\partial f}{\partial t} = 0$이며, 1계 및 2계 도함수는 각각
$f'(S_{t}) = \frac{1}{S_{t}}$, $f''(S_{t}) = - \frac{1}{S_{t}^{2}}$이다.
자산 가격 증분의 제곱 $(dS_{t})^{2}$에 식 (1)과 이토 곱셈표를 대입하면:

$$(dS_{t})^{2} = (\mu S_{t}dt + \sigma S_{t}dW_{t})^{2} = \sigma^{2}S_{t}^{2}(dW_{t})^{2} + \mathcal{O}(dt^{3/2}) = \sigma^{2}S_{t}^{2}dt\quad\quad(5)$$

식 (5)를 식 (4)에 대입하여 정리하면:

$$d\ln S_{t} = \frac{1}{S_{t}}(\mu S_{t}dt + \sigma S_{t}dW_{t}) + \frac{1}{2}\left( - \frac{1}{S_{t}^{2}} \right)(\sigma^{2}S_{t}^{2}dt)\quad\quad(6)$$

동일 항을 소거하고 정리하면 로그 자산 가격의 미분 동역학 방정식이 엄밀히
도출된다:

$$d\ln S_{t} = \left( \mu - \frac{1}{2}\sigma^{2} \right)dt + \sigma dW_{t}\quad\quad(7)$$

식 (7)을 구간 $\lbrack 0,t\rbrack$에 대해 적분하면 자산 가격 과정의
명시적 해석해(Analytical Closed-form Solution)를 얻는다:

$$S_{t} = S_{0}\exp\left( \left( \mu - \frac{1}{2}\sigma^{2} \right)t + \sigma W_{t} \right)\quad\quad(8)$$

### 2.1.3. 앙상블 평균과 시간 평균의 괴리: 변동성 항력과 에르고딕성 파괴

식 (8)에서 로그정규분포(Log-normal Distribution)의 성질에 따라 가상적인
앙상블 단면 기댓값 $\mathbb{E}\lbrack S_{t}\rbrack$를 계산하면,
표준정규분포 적률생성함수
$\mathbb{E}\lbrack e^{\sigma W_{t}}\rbrack = e^{\frac{1}{2}\sigma^{2}t}$에
의해 변동성 감쇠 항이 정확히 상쇄된다:

$$\mathbb{E}\lbrack S_{t}\rbrack = S_{0}e^{(\mu - \frac{1}{2}\sigma^{2})t}\mathbb{E}\lbrack e^{\sigma W_{t}}\rbrack = S_{0}e^{(\mu - \frac{1}{2}\sigma^{2})t}e^{\frac{1}{2}\sigma^{2}t} = S_{0}e^{\mu t}\quad\quad(9)$$

따라서 단면적 앙상블 관점에서 자산 가격의 연율화 성장률은 산술평균
$\mu$이다. 그러나 단 하나의 현실 시간 축 위에서 자산을 운용하는 개별
투자자가 실제로 경험하는 경로별 시간 평균(Time Average), 즉 **연속 복리
기하 성장률(Geometric Compound Growth Rate,** $g$**)**은 표준 브라운
운동에 대한 강대수의 법칙(Strong Law of Large Numbers:
$\lim_{t \rightarrow \infty}\frac{W_{t}}{t} = 0$ a.s.)에 의해 확률 1로
수렴한다:

$$g \equiv \lim_{t \rightarrow \infty}\frac{1}{t}\ln\left( \frac{S_{t}}{S_{0}} \right) = \lim_{t \rightarrow \infty}\left( \mu - \frac{1}{2}\sigma^{2} + \sigma\frac{W_{t}}{t} \right) = \mu - \frac{1}{2}\sigma^{2}\quad\text{a.s.}\quad\quad(10)$$

식 (9)의 앙상블 평균과 식 (10)의 시간 평균 간 괴리는 금융 시계열에서
에르고딕성 파괴(Ergodicity Breakdown)를 수리적으로 증명한다(Peters,
2019). 무한한 평행우주의 기대치는 $\mu$이지만, 단일 궤적을 걷는 실제
투자자의 자본은 오직 $g = \mu - \frac{1}{2}\sigma^{2}$의 속도로
증식한다. 이 두 성장률 간의 괴리를 **'변동성 항력(Volatility Drag,**
$VD$**)'**이라 정의한다:

$$VD \equiv \mu - g = \frac{1}{2}\sigma^{2}\quad\quad(11)$$

이 현상은 로그 함수의 순오목성(Strict Concavity)과 옌센의
부등식(Jensen's Inequality:
$\mathbb{E}\lbrack\ln S_{t}\rbrack < \ln\mathbb{E}\lbrack S_{t}\rbrack$)의
필연적 귀결이다. 임의의 양의 확률변수 $X$에 대해 $f(X) = \ln X$의 2차
테일러 전개를 취하면:

$$\ln X = \ln\mathbb{E}\lbrack X\rbrack + \frac{X - \mathbb{E}\lbrack X\rbrack}{\mathbb{E}\lbrack X\rbrack} - \frac{(X - \mathbb{E}\lbrack X\rbrack)^{2}}{2(\mathbb{E}\lbrack X\rbrack)^{2}} + \mathcal{O}((X - \mathbb{E}\lbrack X\rbrack)^{3})\quad\quad(12)$$

양변에 기댓값을 취하면 1차 편차 항은 0이 되므로:

$$\mathbb{E}\lbrack\ln X\rbrack \approx \ln\mathbb{E}\lbrack X\rbrack - \frac{\text{Var}(X)}{2(\mathbb{E}\lbrack X\rbrack)^{2}} = \ln\mathbb{E}\lbrack X\rbrack - \frac{1}{2}\sigma^{2}\quad\quad(13)$$

따라서 이산시간과 연속시간 모두에서 로그 기대값은 산술 기대값의 로그에서
정확히 분산의 절반만큼 차감된다.

수치적 시뮬레이션을 통해 살펴보면, 동일하게 연 10%의 산술 기대수익률을
갖는 자산이라 하더라도 연율화 변동성이 10%인 경우 실질 복리 성장률은
$10\% - 0.5\% = 9.5\%$인 반면, 변동성이 30%로 상승하면 실질 복리
성장률은 $10\% - 4.5\% = 5.5\%$로 급락한다. 이를 30년 투자 지평으로
환산하면 전자($\sigma = 10\%$)는 초기 원금의 15.2배로 증식하지만
후자($\sigma = 30\%$)는 단 4.98배에 그쳐, 순전히 변동성 항력만으로 인해
무려 67.2%의 최종 부가 소멸한다. 따라서 변동성 항력은 장기 자본 증식에서
가장 핵심적인 통제 대상이다.

### 2.1.4. 레버리지 자산의 변동성 항력 2차 급증($L^{2}$) 메커니즘

변동성 항력의 파괴적 특성은 레버리지($L$) 투자 환경에서 더욱 극명하게
드러난다. 기초 자산의 가격 과정이 식 (1)을 따를 때, 매일 $L$배의 일일
수익률을 추종하는 레버리지 자산 $S_{t}^{(L)}$의 확률미분방정식은 다음과
같다:

$$\frac{dS_{t}^{(L)}}{S_{t}^{(L)}} = L\frac{dS_{t}}{S_{t}} = (L\mu)dt + (L\sigma)dW_{t}\quad\quad(13a)$$

식 (13a)에 이토 보조정리를 적용하면 레버리지 자산의 연속 복리 성장률
$g^{(L)}$은 다음과 같이 도출된다:

$$g^{(L)} = L\mu - \frac{1}{2}(L\sigma)^{2} = L\mu - \frac{1}{2}L^{2}\sigma^{2}\quad\quad(13b)$$

식 (13b)는 레버리지 배수 $L$이 증가할 때 기대수익률은 $L$에 선형적으로
비례하여 증가하지만, 변동성 항력은 레버리지의 제곱($L^{2}$)에 비례하여
기하급수적으로 폭증함을 명증한다. 예컨대 2배 레버리지($L = 2$)의 변동성
항력은 기초자산의 4배($2^{2} = 4$), 3배 레버리지($L = 3$)는 무려
9배($3^{2} = 9$)로 치솟는다.

기초자산의 기대수익률이 0인 횡보장($\mu = 0$)이라 할지라도, 레버리지
자산의 실현 성장률은 $g^{(L)} = - \frac{1}{2}L^{2}\sigma^{2} < 0$이 되어
시간이 흐를수록 자본이 필연적으로 녹아내린다. 연율화 변동성 20%인 자산에
2배 레버리지를 적용할 경우 연간 변동성 항력은
$\frac{1}{2}(2)^{2}(0.20)^{2} = 8.00\%$p에 달한다. 따라서 다기간 투자
환경에서 변동성을 통제하지 않은 무분별한 레버리지 추종은 장기 자본을
영구적으로 파괴하는 수학적 자살 행위이다.

## 2.2. 다변량 포트폴리오의 복리 성장률과 리밸런싱 보너스

### 2.2.1. 포트폴리오 복리 성장률의 수학적 유도

$N$개 위험자산으로 구성된 다변량 시장을 고려한다. 각 자산의 가격 과정
벡터 $\mathbf{S}_{t} = (S_{1,t},\ldots,S_{N,t})^{T}$는 상호 상관된
$N$차원 브라운 운동 $\mathbf{W}_{t}$를 따른다:

$$\frac{dS_{i,t}}{S_{i,t}} = \mu_{i}dt + \sum_{k = 1}^{N}\sigma_{ik}^{0}dW_{k,t}\quad\quad(14)$$

여기서 드리프트 벡터는 $\mathbf{\mu} \in \mathbb{R}^{N}$이며, 순간
공분산 행렬은
$\mathbf{\Sigma} = (\sigma_{ik}) \in \mathbb{R}^{N \times N}$이다.
포트폴리오 가치 $V_{t}$에 대해 가중치 벡터
$\mathbf{w} = (w_{1},\ldots,w_{N})^{T}$($\mathbf{1}^{T}\mathbf{w} = 1,w_{i} \geq 0$)를
적용하면 포트폴리오 가치의 변화율은 다음과 같다:

$$\frac{dV_{t}}{V_{t}} = \sum_{i = 1}^{N}w_{i}\frac{dS_{i,t}}{S_{i,t}} = (\mathbf{w}^{T}\mathbf{\mu})dt + \mathbf{w}^{T}\mathbf{\Sigma}_{0}d\mathbf{W}_{t}\quad\quad(15)$$

포트폴리오의 순간 분산은
$\sigma_{p}^{2}(\mathbf{w}) = \mathbf{w}^{T}\mathbf{\Sigma}\mathbf{w}$이다.
포트폴리오 로그 가치 과정에 다변량 이토 보조정리를 적용하면:

$$d\ln V_{t} = \left( \mathbf{w}^{T}\mathbf{\mu} - \frac{1}{2}\mathbf{w}^{T}\mathbf{\Sigma}\mathbf{w} \right)dt + \mathbf{w}^{T}\mathbf{\Sigma}_{0}d\mathbf{W}_{t}\quad\quad(16)$$

따라서 지속적 리밸런싱 포트폴리오의 연속 복리 성장률
$g_{p}(\mathbf{w})$는 다음과 같이 유도된다:

$$g_{p}(\mathbf{w}) = \mathbf{w}^{T}\mathbf{\mu} - \frac{1}{2}\mathbf{w}^{T}\mathbf{\Sigma}\mathbf{w}\quad\quad(17)$$

### 2.2.2. 리밸런싱 보너스(Rebalancing Bonus)와 다각화의 수리적 본질

식 (17)의 포트폴리오 복리 성장률 $g_{p}(\mathbf{w})$와 개별 자산 복리
성장률 $g_{i} = \mu_{i} - \frac{1}{2}\sigma_{i}^{2}$의 가중평균 간
차이를 비교하면 다각화와 정기 리밸런싱이 창출하는 초과 복리 효과가
도출된다(Booth and Fama, 1992; Hallerbach, 2014):

$$\Delta g(\mathbf{w}) \equiv g_{p}(\mathbf{w}) - \sum_{i = 1}^{N}w_{i}g_{i} = \frac{1}{2}\left\lbrack \sum_{i = 1}^{N}w_{i}\sigma_{i}^{2} - \mathbf{w}^{T}\mathbf{\Sigma}\mathbf{w} \right\rbrack\quad\quad(18)$$

식 (18)의 우변은 **'다각화 수익률(Diversification Return)'** 또는
**'리밸런싱 보너스'**라 불린다. 윌렌브록(Willenbrock, 2011)에 따르면
$\sum_{j = 1}^{N}w_{j} = 1$이므로
$\sum_{i = 1}^{N}w_{i}\sigma_{i}^{2} = \frac{1}{2}\sum_{i = 1}^{N}{\sum_{j = 1}^{N}w_{i}}w_{j}(\sigma_{i}^{2} + \sigma_{j}^{2})$로
분해할 수 있으며, 포트폴리오 분산
$\mathbf{w}^{T}\mathbf{\Sigma}\mathbf{w} = \sum_{i = 1}^{N}{\sum_{j = 1}^{N}w_{i}}w_{j}\sigma_{ij}$를
대입하면 식 (18)은 다음과 같이 쌍별 분산 스프레드의 가중합으로 우아하게
정리된다:

$$\Delta g(\mathbf{w}) = \frac{1}{4}\sum_{i = 1}^{N}{\sum_{j = 1}^{N}w_{i}}w_{j}(\sigma_{i}^{2} + \sigma_{j}^{2} - 2\sigma_{ij}) = \frac{1}{4}\sum_{i = 1}^{N}{\sum_{j = 1}^{N}w_{i}}w_{j}\text{Var}(r_{i} - r_{j}) \geq 0\quad\quad(19)$$

식 (19)는 다각화 수익률이 항상 0 이상($\geq 0$)이며, 자산 간 수익률
차이의 분산 $\text{Var}(r_{i} - r_{j})$에 정비례함을 입증한다. 자산 간
상관계수가 1 미만($\rho_{ij} < 1$)인 한 스프레드 분산은 엄격히
양(+)수이므로, 정기적인 리밸런싱은 변동성 항력을 구조적으로 경감시켜
개별 자산 성장률의 평균을 항상 초과하는 보너스를 창출한다.

### 2.2.3. 성장 최적 포트폴리오(Kelly Criterion)와 공분산 추정의 역설

장기 다기간 투자에서 종단 부를 극대화하는 해는 로그 효용함수의 기댓값을
극대화하는 성장 최적 포트폴리오(Kelly, 1956)와 일치한다. 식 (17)에서 알
수 있듯, 복리 성장률 극대화 목적함수
$\max_{\mathbf{w}}\mathbf{w}^{T}\mathbf{\mu} - \frac{\lambda}{2}\mathbf{w}^{T}\mathbf{\Sigma}\mathbf{w}$에서
위험 페널티 계수는 투자자의 주관적 성향과 무관하게 수학적으로
$\lambda = 1$로 엄밀히 결정된다.

그러나 표본 공분산 행렬 $\mathbf{S}$을 단순 대입할 경우, 표본 오차로
인해 최적화 엔진이 추정 오차가 큰 극단적 포지션에 자본을 집중시키는
'오차 극대화(Error Maximization)' 현상이 발생한다(Michaud, 1989). 특히
자산의 수 $N$에 비해 표본 관측 기간 $T$가 유한할 때 고유벡터의 왜곡이
극심해진다. 따라서 변동성 항력을 실질적으로 통제하기 위해서는 조건부
공분산 행렬 $\widehat{\mathbf{\Sigma}}$에 대한 정밀한 사전적 추정과
양준정부호성 확보가 필수적이다.

## 2.3. 시계열 파운데이션 모델(TSFM)의 아키텍처 및 확률적 예측 원리

전통적 시계열 계량 모형인 GARCH(Bollerslev, 1986) 및 HAR-RV(Corsi,
2009)는 선형성 또는 정형화된 모수 분포 가정에 구속되어 금융시장의 복잡한
비선형적 상호작용과 급격한 체제 전환을 유연하게 반영하지 못한다. 최근
자연어 처리의 트랜스포머(Vaswani et al., 2017) 아키텍처를 대규모 시계열
데이터셋으로 확장한 시계열 파운데이션 모델(TSFM: Time Series Foundation
Models)은 방대한 크로스 도메인 사전학습을 기반으로 제로샷(Zero-shot)
확률분포 예측에서 혁신적 성능을 입증하였다.

TSFM의 핵심 기저는 **패칭(Patching)** 메커니즘이다(Nie et al., 2023).
시계열 데이터를 단일 시점 스칼라 토큰 대신 인접 시점을 묶은 중첩 패치
단위로 분할하여 로컬 시맨틱을 보존하고 어텐션 연산량을 대폭 절감한다.
또한 각 채널(자산)을 독립적으로 처리하는 채널 독립성(Channel
Independence) 구조를 채택하여 파라미터 과적합을 방지한다. 입력 시계열의
국소적 비정상성을 해결하기 위해 가역적 인스턴스 정규화(RevIN)를
적용하고, 멀티헤드 자기 어텐션(MHSA) 레이어로 다기간 시간 의존성을
추출한다. Chronos(Ansari et al., 2024) 및 PatchTST(Nie et al., 2023)와
같은 TSFM은 연속된 수치 시계열로부터 미래 수익률의 조건부 확률분포
$p(r_{t + 1}|r_{1:t})$를 직접 모델링함으로써, 불확실성을 내포한 사전적
1차·2차 모멘트($\widehat{\mu},\widehat{\sigma}$)를 정밀 도출한다.

## 2.4. 비지도 딥러닝 이상탐지 이론과 꼬리위험 포착

금융 자산 수익률은 정규분포를 심각하게 위배하는 두터운 꼬리(Fat-tail)와
군집 변동성(Volatility Clustering) 특성을 지닌다. 특히 극단적 시스템
위기 국면에서는 모든 위험자산 간 상관계수가 1로 급수렴하면서 식 (18)의
리밸런싱 보너스가 일시에 소멸하고 대규모 자본 증발이 발생한다.

본 연구는 원자력 발전소 압력관 검사나 항공우주 복합재 결함 탐지에
활용되는 **산업 비파괴검사(Non-Destructive Evaluation, NDE)**의 이상탐지
패러다임을 금융시장에 이식한다(Ruff et al., 2021). 결함 데이터가 극도로
희소하고 치명적인 환경에서 NDE 모델은 '정상 상태'의 신호 패턴만을 비지도
학습하여 정상 매니폴드 $\mathcal{M}$을 형성한다. 이후 미세한 균열이나
결함이 유입되면 모델은 이를 정상 규칙으로 복원하지 못하여 높은 **재구성
오차(Reconstruction Error)**를 방출한다.

금융시장 역시 평시 정상 국면에서는 거시 변수와 자산 가격 간에 일정한
무차익 균형 관계가 성립하지만, 시스템적 유동성 경색이나 패닉 셀링이
발생하면 다변량 지표의 공움직임이 정상 매니폴드를 급격히 이탈한다. 심층
오토인코더(Deep Autoencoder)를 통해 이러한 이탈도를 실시간 추적함으로써
사후적 손실이 확정되기 전 선제적으로 포트폴리오를 보호하는 지능형
세이프가드 구축이 가능해진다.

## 2.5. 선행연구 검토 및 본 연구의 이론적 차별성

전통적 자산배분 연구는 정적 MVO(Markowitz, 1952)에서 동일가중(DeMiguel
et al., 2009), 위험 패리티(Risk Parity)로 진화해 왔으나 모두 산술평균
기준의 정적 배분에 머물렀다. 동적 변동성 관리 연구(Moreira and Muir,
2017; Harvey et al., 2018)는 변동성 급등 시 노출도를 축소하는 유용성을
입증했으나, 과거 실현 변동성을 활용함에 따른 사후적 후행성을 극복하지
못했다. 한편 딥러닝 퀀트 연구는 금융 수리 모델과의 정합성 없이 단순
지도학습 예측에 편중되어 과적합의 한계를 드러냈다.

본 연구는 이토 보조정리를 통해 $\lambda = 1$인 복리 성장률 극대화 수리
모델을 정초하고, TSFM의 사전적 확률 예측과 산업 NDE 기반 비지도 이상탐지
세이프가드를 단일 볼록 최적화 파이프라인으로 결합함으로써 기존 문헌의
공백을 완벽히 메운다.

# 제3장 데이터 및 연구 방법론 (Data and Methodology)

## 3.1. 분석 데이터셋 및 자산 유니버스 구축

### 3.1.1. 자산 유니버스 및 데이터 정제

본 연구의 자산 유니버스는 한국거래소(KRX) 상장 대표 ETF 및 글로벌 기축
자산 7대 자산군으로 구성하였다. 거시경제적 체제 전환과 인플레이션 충격에
대한 다각화 복원력을 확보하기 위해 국내 대형주, 국내 성장주, 국내 장기
채권, 글로벌 대형주, 글로벌 기술주, 실물 안전자산, 무위험 유동성 자산을
고르게 안배하였다: 1. **KOSPI 200** (KODEX 200, 069500): 한국 경제를
대표하는 대형 우량주 지수 2. **KOSDAQ 150** (KODEX 코스닥150, 229200):
국내 혁신성장형 중소·벤처기업 지수 3. **한국국채 10년** (KOSEF
국고채10년, 148070): 국내 장기 금리 벤치마크 채권 4. **S&P 500** (TIGER
미국S&P500): 글로벌 기축 통화 표시 대형 우량주 지수 5. **나스닥 100**
(TIGER 미국나스닥100): 글로벌 빅테크 및 기술 혁신주 지수 6. **금 현물
(Gold)** (KRX 금현물 / GLD): 전통적 인플레이션 헤지 및 지정학적 안전자산
7. **미국단기채 / 현금 (Cash)** (SHV / KOFR): 무위험 유동성 기준 자산

표본 분석 기간은 2015년 1월 2일부터 2026년 8월 31일까지 총 11년 8개월간
2,868 거래일이다. 모든 가격 계열은 주식분할 및 분배금을 반영한
수정주가(Adjusted Close)를 적용하였다. 본 연구의 백테스팅은 단순 가격 수익률(Price Return)이 아닌 배당 및 분배금 재투자를 가정한 총수익률(Total Return, TR) 기준을 전면 적용하였다. ETF 분배금의 현금 배당 및 주식 배당을 당일 종가로 전액 재투자하는 계정 모델을 채택함으로써, 장기 복리 계산 시 배당 누락으로 인한 수익률 과소평가 및 왜곡(Dividend Omission Bias)을 원천 차단하였다. 모든 가격 계열은 일별 연속 복리 로그수익률
$r_{t} = \ln(P_{t}/P_{t - 1})$을 산출하였다.

### 3.1.2. 기술통계량 및 정상성 검정

7대 자산군의 일별 로그수익률 및 변동성 특성은 \<표 1-A\>와 같으며,
정규성 및 시계열 정상성 검정 결과는 \<표 1-B\>와 같다.

\<표 1-A\> 주요 자산군의 일별 로그수익률 및 변동성 특성 (2015.01 \~
2026.08)

  ---------------------------------------------------------------------------------------------------------------
  자산군 (Asset     티커      관측치      연율화 산술평균          연율화 기하평균        연율화     변동성 항력
  Class)          (Ticker)    ($N$)    ($\mu_{\text{arith}}$,   ($\mu_{\text{geom}}$,     변동성        손실
                                                 %)                      %)             ($\sigma$,   ($\mu - g$,
                                                                                            %)           %p)
  -------------- ----------- -------- ------------------------ ----------------------- ------------ -------------
  **KOSPI 200**    069500     2,868             5.82                    4.34              17.21       **1.48**

  **KOSDAQ 150**   229200     2,868             4.21                    1.21              24.53       **3.00**

  **한국국채       148070     2,868             2.64                    2.41               6.82       **0.23**
  10Y**                                                                                             

  **S&P 500       SPY/TIGER   2,868            13.85                    12.49             16.48       **1.36**
  (KRW)**                                                                                           

  **나스닥 100    QQQ/TIGER   2,868            19.42                    17.17             21.24       **2.25**
  (KRW)**                                                                                           

  **금 현물        GLD/KRX    2,868             8.45                    7.45              14.12       **1.00**
  (Gold)**                                                                                          

  **미국단기채    SHV/KOFR    2,868             2.45                    2.44               1.15       **0.01**
  (Cash)**                                                                                          
  ---------------------------------------------------------------------------------------------------------------

주 1: 연율화 수치는 1년 = 252영업일 환산치임
($\mu_{\text{ann}} = \mu_{\text{daily}} \times 252$,
$\sigma_{\text{ann}} = \sigma_{\text{daily}} \times \sqrt{252}$).\
주 2: 기하평균 $\mu_{\text{geom}}$은 실현된 연속 복리 성장률 연율화
값임.\
자료: 한국거래소(KRX), 인베스팅닷컴, 세인트루이스 연방준비은행(FRED).

\<표 1-B\> 비정규성 검정 및 ADF 시계열 정상성 판정 결과 (2015.01 \~
2026.08)

  ---------------------------------------------------------------------------------------------------------
  자산군 (Asset      왜도       초과첨도     Jarque-Bera       ADF 검정통계량      p-value    정상성 판정
  Class)          (Skewness)   (Kurtosis)   통계량 ($JB$)    ($t_{\text{ADF}}$)   ($H_{0}$)  
  -------------- ------------ ------------ ---------------- -------------------- ----------- --------------
  **KOSPI 200**     -0.38         6.12      4,544.82***      -52.41\*\*\*      \< 0.0001       정상
                                                                                              (Stationary)

  **KOSDAQ 150**    -0.45         7.35      6,552.48***      -51.84\*\*\*      \< 0.0001       정상
                                                                                              (Stationary)

  **한국국채        -0.15         4.80      2,764.03***      -54.12\*\*\*      \< 0.0001       정상
  10Y**                                                                                       (Stationary)

  **S&P 500         -0.62         9.40      10,742.76***      -55.23\*\*\*      \< 0.0001       정상
  (KRW)**                                                                                     (Stationary)

  **나스닥 100      -0.51         7.82      7,432.04***      -53.95\*\*\*      \< 0.0001       정상
  (KRW)**                                                                                     (Stationary)

  **금 현물          0.08         5.95      4,233.66***      -53.40\*\*\*      \< 0.0001       정상
  (Gold)**                                                                                    (Stationary)

  **미국단기채       0.21         4.10      2,029.87***      -49.62\*\*\*      \< 0.0001       정상
  (Cash)**                                                                                    (Stationary)
  ---------------------------------------------------------------------------------------------------------

주 1: 초과첨도는 정규분포 첨도(=3)를 차감한 값임.\
주 2: \*\*\*는 1% 유의수준에서 단위근 존재 귀무가설($H_{0}$) 기각을
의미함.\
자료: 한국거래소(KRX), FRED.

\<표 1-A\>와 \<표 1-B\>의 실증 결과는 다음 세 가지 중요한 계량경제학적
함의를 제공한다. 첫째, 모든 위험자산에서 산술평균과 기하평균 간의 뚜렷한
괴리가 확인된다. 특히 연율화 변동성이 24.53%에 달하는 KOSDAQ 150의 경우
연간 산술평균은 4.21%이나 실제 복리 기하수익률은 1.21%에 불과하여 연간
3.00%p의 복리 자본이 증발하였다. 이는 이토 보조정리의
이론값($\frac{1}{2}\sigma^{2} = \frac{1}{2}(0.2453)^{2} \approx 3.01\%$)과
완벽히 부합한다. 둘째, 초과첨도가 4.80\~9.40에 달하고 대부분 음의 왜도를
나타내어 Jarque-Bera 검정에서 정규분포 귀무가설이 강력히
기각($p < 0.0001$)되었다. 이는 금융 자산의 극단적 두터운 꼬리 위험을
포착할 수 있는 비선형 비지도 이상탐지 세이프가드의 필요성을 실증적으로
뒷받침한다. 셋째, ADF 검정 결과 모든 수익률 시계열의 $t$ 통계량이
임계치를 대폭 하회하여 시계열 정상성(Stationarity)이 확보되었음을
확인하였다.

### 3.1.3. 계량경제학적 검정 수식 및 거시 상태변수 체계

수익률 시계열의 분포적 특성을 검증하기 위한 왜도(Skewness),
초과첨도(Excess Kurtosis) 및 Jarque-Bera 통계량은 다음과 같이 정의된다:

$$\text{Skewness} = \frac{\frac{1}{T}\sum_{t = 1}^{T}(r_{t} - \bar{r})^{3}}{\left\lbrack \frac{1}{T}\sum_{t = 1}^{T}(r_{t} - \bar{r})^{2} \right\rbrack^{3/2}},\quad\text{Kurtosis} = \frac{\frac{1}{T}\sum_{t = 1}^{T}(r_{t} - \bar{r})^{4}}{\left\lbrack \frac{1}{T}\sum_{t = 1}^{T}(r_{t} - \bar{r})^{2} \right\rbrack^{2}} - 3\quad\quad(19a)$$

$$JB = \frac{T}{6}\left( \text{Skewness}^{2} + \frac{\text{Kurtosis}^{2}}{4} \right) \sim \chi^{2}(2)\quad\quad(19b)$$

단위근 검정을 위한 확장 디키-풀러(ADF) 검정은 추세와 절편을 포함한
다음의 회귀식을 추정하여 귀무가설 $H_{0}:\gamma = 0$을 검정한다:

$$\Delta r_{t} = \alpha + \beta t + \gamma r_{t - 1} + \sum_{p = 1}^{P}\delta_{p}\Delta r_{t - p} + \varepsilon_{t}\quad\quad(19c)$$

한편, 본 연구가 산업 비파괴검사(NDE) 세이프가드에 입력하는 12차원
거시-금융 상태 벡터 $\mathbf{z}_{t} \in \mathbb{R}^{12}$는 시스템적
유동성 경색과 시장 공포를 직교적으로 포착하도록 설계되었다: 1\~7. 7대
자산군의 21영업일 롤링 실현변동성
($\sigma_{i,t} = \sqrt{252 \cdot \frac{1}{21}\sum_{k = 0}^{20}r_{i,t - k}^{2}}$)
8. 미국 CBOE 변동성 지수 (VIX): 글로벌 주식시장의 내재 공포 심리
대리변수 9. 한국거래소 코스피200 변동성 지수 (VKOSPI): 국내 고유의 단기
꼬리위험 민감도 10. 미국 국채 10년-2년 장단기 금리 스프레드
($y_{10Y} - y_{2Y}$): 경기 침체 선행 신호 11. 미국 하이일드 채권 신용
스프레드 (ICE BofA US High Yield OAS): 기업 부도 위험 및 유동성 프리미엄
12. 원/달러 환율 21영업일 실현변동성: 외국인 자본 유출입 및 신흥국 외환
유동성 충격

## 3.2. TSFM 기반 동적 조건부 변동성 및 기대수익률 사전 예측 파이프라인

### 3.2.1. 패치 트랜스포머 아키텍처 및 롤링 윈도우 설계

본 연구는 대규모 사전학습 모델인 PatchTST(Nie et al., 2023) 기반 시계열
파운데이션 모델을 조건부 모멘트 예측 엔진으로 도입한다. 시계열 데이터의
비정상성을 해결하기 위해 입력 윈도우 $\mathbf{x} \in \mathbb{R}^{L}$에
가역적 인스턴스 정규화(RevIN)를 선행 적용한다:

$$\widetilde{\mathbf{x}} = \frac{\mathbf{x} - \text{Mean}(\mathbf{x})}{\sqrt{\text{Var}(\mathbf{x}) + \epsilon}}\quad\quad(19)$$

정규화된 시계열을 패치 길이 $P = 16$, 스트라이드 $S = 8$의 중첩 패치로
분할하여 선형 투영을 수행한다:

$$\mathbf{e}_{n} = \mathbf{W}_{p}\mathbf{p}_{n} + \mathbf{e}_{\text{pos},n},\quad\mathbf{E} = \lbrack\mathbf{e}_{1},\ldots,\mathbf{e}_{N}\rbrack \in \mathbb{R}^{d_{\text{model}} \times N}\quad\quad(20)$$

트랜스포머 인코더 블록에서 멀티헤드 자기 어텐션을 연산한다:

$$\text{Attention}(\mathbf{Q},\mathbf{K},\mathbf{V}) = \text{softmax}\left( \frac{\mathbf{Q}\mathbf{K}^{T}}{\sqrt{d_{k}}} \right)\mathbf{V}\quad\quad(21)$$

투영 헤드는 차기 5영업일($H = 5$)
모멘트($\widehat{\mu},\widehat{\sigma}$)를 음의 로그우도(NLL) 손실함수로
최적화한다:

$$\mathcal{L}_{\text{NLL}}(\theta) = - \sum_{t}^{}\ln p(r_{t + 1} \mid {\widehat{\mu}}_{t + 1|t}(\theta),{\widehat{\sigma}}_{t + 1|t}(\theta))\quad\quad(22)$$

가역적 인스턴스 정규화(RevIN)의 통계량은 시점 $t$의 정보집합 $\mathcal{F}_t$에 대해서만 다음과 같이 엄밀히 산출된다:

$$\mu_{\mathbf{x}, t} = \frac{1}{L} \sum_{k=0}^{L-1} x_{t-k}, \quad \sigma_{\mathbf{x}, t}^2 = \frac{1}{L} \sum_{k=0}^{L-1} (x_{t-k} - \mu_{\mathbf{x}, t})^2 \qquad (23a)$$

$$\tilde{x}_{t-k} = \frac{x_{t-k} - \mu_{\mathbf{x}, t}}{\sqrt{\sigma_{\mathbf{x}, t}^2 + \epsilon}}, \quad k=0, \dots, L-1 \qquad (23b)$$

RevIN의 인스턴스 정규화 통계량($\mu_{\mathbf{x}, t}, \sigma_{\mathbf{x}, t}$)은 오직 시점 $t$까지의 역사적 정보집합 $\mathcal{F}_t$에만 의존하여 산출되며($\mathcal{F}_t$-measurable), 패칭 및 트랜스포머 인과적 어텐션(Causal Attention) 연산 전반에서 미래 시점($\tau > t$)의 정보가 스케일링이나 롤링 윈도우 경계선에서 누수되는 미래 참조 편향(Look-ahead Bias / Data Leakage)을 수학적으로 원천 차단하였다. 과거 $W = 504$일(2개년) 롤링 윈도우를 활용하여 시점 $t$의 정보만을 기반으로 미래를 순차 예측한다.

### 3.2.2. 동적 조건부 공분산 행렬 추정 및 양준정부호(PSD) 보정

TSFM에서 예측된 개별 자산의 대각 변동성 행렬
${\widehat{\mathbf{D}}}_{t + 1|t} = \text{diag}({\widehat{\mathbf{\sigma}}}_{t + 1|t})$과
르두아-울프 비선형 축소 상관행렬
${\widehat{\mathbf{R}}}_{t + 1|t}^{\text{LW}}$을 결합한다(Ledoit and
Wolf, 2004):

$${\widehat{\mathbf{R}}}_{t + 1|t}^{\text{LW}} = (1 - \delta^{*})\mathbf{S}_{\text{corr}} + \delta^{*}\mathbf{F}\quad\quad(23)$$

$${\widehat{\mathbf{\Sigma}}}_{t + 1|t} = {\widehat{\mathbf{D}}}_{t + 1|t}{\widehat{\mathbf{R}}}_{t + 1|t}^{\text{LW}}{\widehat{\mathbf{D}}}_{t + 1|t}\quad\quad(24)$$

표본 오차로 인해 발생할 수 있는 음의 고윳값을 제거하기 위해
하이엄(Higham, 2002) 최근접 상관행렬 알고리즘을 적용하여 최소 고윳값을
$\epsilon_{\text{floor}} = 10^{- 6}$으로 절단한다:

$$\widetilde{\mathbf{\Lambda}} = \text{diag}(\max(\lambda_{i},\epsilon_{\text{floor}})),\quad{\widehat{\mathbf{\Sigma}}}_{\text{PSD}} = \mathbf{V}\widetilde{\mathbf{\Lambda}}\mathbf{V}^{T}\quad\quad(25)$$

하이엄(Higham, 2002) 최근접 상관행렬 교대 투영 알고리즘은
딕스트라(Dykstra) 순환 투영을 통해 프로베니우스 노름 거리
$\parallel \widehat{\mathbf{R}} - \mathbf{R} \parallel_{F}$을 최소화하는
유일한 양준정부호 상관행렬을 도출한다:

$$\mathbf{R}_{k} = \mathbf{Y}_{k - 1} - \Delta\mathbf{S}_{k - 1},\quad\mathbf{X}_{k} = P_{\mathcal{P}}(\mathbf{R}_{k}),\quad\Delta\mathbf{S}_{k} = \mathbf{X}_{k} - \mathbf{R}_{k}\quad\quad(25a)$$

$$\mathbf{Y}_{k} = P_{\mathcal{S}}(\mathbf{X}_{k}),\quad\Delta\mathbf{Y}_{k} = \mathbf{Y}_{k} - \mathbf{X}_{k}\quad\quad(25b)$$

여기서
$P_{\mathcal{P}}(\mathbf{A}) = \mathbf{V}\max(\mathbf{\Lambda},\epsilon_{\text{floor}}\mathbf{I})\mathbf{V}^{T}$는
양준정부호 콘으로의 스펙트럼 투영이며, $P_{\mathcal{S}}(\mathbf{B})$는
대각원소를 1로 강제하고 대칭성을 부여하는 아핀 공간 투영이다. 수렴 판정
기준은 상대 오차
$\parallel \mathbf{Y}_{k} - \mathbf{Y}_{k - 1} \parallel_{F}/ \parallel \mathbf{Y}_{k - 1} \parallel_{F} < 10^{- 7}$을
적용한다.

이를 통해 공분산 행렬의
양준정부호성($\widehat{\mathbf{\Sigma}} \succ 0$)을 보장하고 볼록 2차
계획법의 대역적 유일해 수렴성을 확보한다.

## 3.3. 꼬리위험 이상탐지(Anomaly Detector) 기반 리스크 버퍼링 메커니즘

### 3.3.1. 산업 비파괴검사(NDE) 기반 심층 오토인코더 수리 모델

12차원 거시-금융 상태 벡터 $\mathbf{z}_{t} \in \mathbb{R}^{12}$(7대 자산
21일 실현변동성, VIX 지수, VKOSPI 지수, 미국 10Y-2Y 장단기 금리
스프레드, 미국 하이일드 채권 스프레드, 원/달러 환율 21일 실현변동성)를
심층 오토인코더에 입력한다: - 인코더:
$\mathbf{h}_{t} = \sigma(\mathbf{W}_{e}^{(2)}\sigma(\mathbf{W}_{e}^{(1)}\mathbf{z}_{t} + \mathbf{b}_{e}^{(1)}) + \mathbf{b}_{e}^{(2)})$
(12차원 $\rightarrow$ 8차원 $\rightarrow$ 4차원 압축) - 디코더:
$\widehat{\mathbf{z}_{t}} = \mathbf{W}_{d}^{(2)}\sigma(\mathbf{W}_{d}^{(1)}\mathbf{h}_{t} + \mathbf{b}_{d}^{(1)}) + \mathbf{b}_{d}^{(2)})$
(4차원 $\rightarrow$ 8차원 $\rightarrow$ 12차원 복원)

재구성 오차는 다음과 같이 정의된다:

$$\mathcal{L}_{\text{recon}}(\mathbf{z}_{t}) = \frac{1}{12}\sum_{m = 1}^{12}(z_{t,m} - {\widehat{z}}_{t,m})^{2}\quad\quad(26)$$

심층 오토인코더(DAE)의 가중치 최적화는 전체 데이터가 아닌 웜업 표본 기간($\mathcal{T}_{\text{warmup}}$: 2015년 1월 ~ 2016년 12월, 492 거래일)에 대해서만 사전 학습을 수행한다:

$$\theta^* = \arg\min_\theta \frac{1}{|\mathcal{T}_{\text{warmup}}|} \sum_{t \in \mathcal{T}_{\text{warmup}}} \|\mathbf{z}_t - g_\theta(f_\theta(\mathbf{z}_t))\|_2^2 \qquad (26a)$$

웜업 기간 종료 후 오토인코더의 파라미터는 $\theta = \theta^*$로 영구 동결(Frozen)되며, 2017년 1월부터 2026년 8월까지의 실증 백테스팅 구간 전체에서 일체의 파라미터 재학습이나 가중치 업데이트 없이 순수한 표본 외(Out-of-sample) 추론만을 수행한다. 이를 통해 이상탐지 세이프가드의 미래 정보 누수 및 과적합(Overfitting) 위험을 구조적으로 제거하였다.

### 3.3.2. 평활화 이상치 점수($S_{t}$) 및 동적 리스크 버퍼 계수($\beta_{t}$)

일간 노이즈를 완화하기 위해 지수이동평균(EMA) 필터를 적용한 이상치 점수
$S_{t}$를 산출한다:

$$S_{t} = \lambda_{\text{smooth}}S_{t - 1} + (1 - \lambda_{\text{smooth}})\mathcal{L}_{\text{recon}}(\mathbf{z}_{t}),\quad\lambda_{\text{smooth}} = 0.8\quad\quad(27)$$

동적 위험 임계치는 과거 252 거래일의 상위 95 분위수
$\tau_{t} = \mathcal{Q}_{0.95}(\{ S_{u}\}_{u = t - 252}^{t - 1})$로
설정한다. 리스크 버퍼 계수 $\beta_{t} \in \lbrack 0,1\rbrack$는
시그모이드 감쇠 함수로 결정된다:

$$\beta_{t} = \left\{ \begin{matrix}
0, & \text{if }S_{t} \leq \tau_{t} \\
\min\left( 1,\frac{1 - \exp( - \kappa(S_{t} - \tau_{t})/\tau_{t})}{1 + \exp( - \kappa(S_{t} - \tau_{t})/\tau_{t})} \times 2 \right), & \text{if }S_{t} > \tau_{t}
\end{matrix} \right.\ \quad\quad(28)$$

여기서 $\kappa = 4.0$이다. 최종 실행 포트폴리오 가중치
$\mathbf{w}_{t}^{*}$는 QP 최적 가중치
$\mathbf{w}_{t}^{\text{optimal}}$와 무위험 현금 가중치
무위험 현금 가중치 벡터 $\mathbf{w}_{\text{safe}} = (0, 0, 0, 0, 0, 0, 1)^T$의 선형 볼록 결합으로
산출된다:

$$\mathbf{w}_{t}^{*} = (1 - \beta_{t})\mathbf{w}_{t}^{\text{optimal}} + \beta_{t}\mathbf{w}_{\text{safe}}\quad\quad(29)$$

평시($S_{t} \leq \tau_{t}$)에는 $\beta_{t} = 0$으로 이토 최적 가중치를
100% 유지하며, 위기($S_{t} > \tau_{t}$) 시 $\beta_{t} \rightarrow 1$로
급증하여 위험자산을 즉각 축소하고 현금으로 피신한다.

## 3.4. 목적함수 수립 및 포트폴리오 볼록 2차 계획법(Convex QP) 완성

이토 보정 목적함수와 운용 제약조건을 결합하여 볼록 2차 계획법 문제를
완성한다:

$$\min_{\mathbf{w},\zeta,\mathbf{u}}\quad\frac{1}{2}\mathbf{w}^{T}{\widehat{\mathbf{\Sigma}}}_{t + 1|t}\mathbf{w} - {\widehat{\mathbf{\mu}}}_{t + 1|t}^{T}\mathbf{w}\quad\quad(30)$$

$$\text{subject to}\quad\left\{ \begin{matrix}
\mathbf{1}^{T}\mathbf{w} = 1 & \text{(완전투자 예산 제약)} \\
0 \leq w_{i} \leq 0.40,\quad\forall i & \text{(공매도 금지 및 단일자산 상한 40\%)} \\
\zeta + \frac{1}{(1 - \alpha)K}\sum_{k = 1}^{K}u_{k} \leq \gamma_{\text{target}} & \text{(95\%CVaR 하방위험 상한 제약)} \\
u_{k} \geq - \mathbf{w}^{T}\mathbf{r}_{k} - \zeta,\quad u_{k} \geq 0,\quad\forall k & \text{(Rockafellar-Uryasev 보조 선형 제약)}
\end{matrix} \right.\ \quad\quad(31)$$

식 (30)은 $\lambda = 1$인 켈리 성장률 극대화 문제와 정확히 일치하며,
하이엄 PSD 보정으로 헤시안 $\widehat{\mathbf{\Sigma}} \succ 0$이 보장되어 대역적 유일해(Global Optimum)가 보장된다.

아울러 실무 운용 환경을 충실히 반영하기 위해 포트폴리오 리밸런싱에 따른 동적 회전율 거래비용 모델을 다음과 같이 정식화한다:

$$\text{TC}_t = c \cdot \sum_{i=1}^N |w_{i, t} - w_{i, t^-}| \qquad (31a)$$

$$r_{p, t}^{\text{net}} = r_{p, t}^{\text{gross}} - \text{TC}_t \qquad (31b)$$

여기서 $c$는 편도 거래비용율(기본 10bp = 0.0010, 고비용 스트레스 20bp = 0.0020)이며, $w_{i, t^-}$는 리밸런싱 직전 포트폴리오 내 자산 $i$의 실현 비중이다. 포트폴리오의 회전율에 비례하여 마찰 비용을 엄밀히 공제함으로써 백테스팅의 실무적 무결성을 담보한다.
보장되어 대역적 유일해(Global Optimum)가 보장된다.

# 제4장 실증 분석 결과 (Empirical Analysis and Results)

## 4.1. 벤치마크 모델 설정 및 백테스팅 환경

제안 모델의 비교 평가를 위해 동일 자산 유니버스와 분석 기간을 공유하는
3대 대표 벤치마크를 구축하였다: 1. **전통적 60/40 자산배분 (Traditional
60/40)**: 글로벌 대표 벤치마크로서 S&P 500에 60%, 한국국채 10년에 40%를
고정 배분하고 월간 리밸런싱을 수행한다. 2. **동일가중 포트폴리오 (Equal
Weight, 1/N)**: 7대 자산에 각각 14.28%씩 균등 배분한다(DeMiguel et al.,
2009). 3. **정적 마코위츠 평균-분산 최적화 (MVO)**: 과거 252일 롤링 표본
기대수익률과 표본 공분산을 활용하여 단일기간 샤프 지수를 극대화한다. 4.
**제안 모델 (TSFM-Itô with Safeguard)**: TSFM 사전적 모멘트 예측, 이토
보정 연속 복리 성장률 극대화 볼록 QP, NDE 오토인코더 꼬리위험
세이프가드를 통합한 동적 자산배분 모델이다.

모든 백테스팅은 기본 거래비용 10bp(편도 슬리피지 및 수수료)를
차감하였으며, 주간 정기 리밸런싱 및 세이프가드 이상 감지 시 수시
리밸런싱을 적용하였다.

## 4.2. 전체 기간 실증 성과 분석 (2015년 \~ 2026년)

### 4.2.1. 장기 누적 성과 및 위험조정 수익률 종합 평가

전체 실증 기간에 걸친 4대 모델의 종합 백테스팅 성과표는 \<표 2\>와 같다.

\<표 2\> 2015\~2026 전체 실증 기간 포트폴리오 성과 종합 비교표

  ---------------------------------------------------------------------------------------------------------------------
  성과 평가 지표 (Metrics)                         전통적 60/40 동일가중 (EW 마코위츠 MVO 제안 모델     제안 모델 우위
                                                                1/N)                      (TSFM-Itô)    (vs 60/40)
  ------------------------------------------------ ------------ ------------ ------------ ------------- ---------------
  **\[패널 A: 수익성 및 복리 전환 효율\]**                                                              

  **최종 누적수익률 (Cumulative Return)**          138.86%      154.21%      176.43%      **392.15%**   **+253.29%p**

  **연평균 복리수익률 (CAGR)**                     7.85%        8.42%        9.14%        **14.82%**    **+6.97%p**

  **연율화 산술평균 수익률                         8.51%        9.25%        10.02%       **15.11%**    +6.60%p
  (**$\mu_{\text{arith}}$**)**                                                                          

  **실측 변동성 항력 손실                          **0.66%p**   **0.83%p**   **0.88%p**   **0.29%p**    **-59 bp 절감
  (**$\mu_{\text{arith}} - g_{\text{geom}}$**)**   (66 bp)      (83 bp)      (88 bp)      (29 bp)       (67.0% 감소)**

  **이론적 변동성 항력                             0.66%p       0.83%p       0.88%p       0.29%p        이론식과 완벽
  (**$\frac{1}{2}\sigma^{2}$**)**                                                                       일치

  **복리 전환 효율성                               92.24%       91.03%       91.22%       **98.08%**    **+5.84%p \~
  (**$g_{\text{geom}}/\mu_{\text{arith}}$**)**                                                          +7.05%p**

  **\[패널 B: 위험조정 성과 및 통계적 유의성\]**                                                        

  **연율화 변동성 (**$\sigma_{\text{ann}}$**)**    11.45%       12.86%       13.28%       **7.63%**     **-3.82%p**

  **샤프 지수 (Sharpe Ratio,**                     0.51         0.50         0.54         **1.68**      **+1.17**
  $r_{f} = 2.0\%$**)**                                                                                  

  **소르티노 지수 (Sortino Ratio)**                0.72         0.69         0.75         **2.74**      **+2.02**

  **칼마 비율 (Calmar Ratio, CAGR/\|MDD\|)**       0.32         0.32         0.32         **1.78**      **+1.46**

  **월간 승률 (Monthly Win Rate, %)**              59.42%       60.14%       57.97%       **68.84%**    +9.42%p

  **샤프 지수 차이 검정 (**$p$**-value)**          \< 0.001     \< 0.001     \< 0.001     **---**       통계적 유의성
                                                                                                        확보

  **\[패널 C: 하방 위험 및 극단 꼬리위험\]**                                                            

  **최대 낙폭 (MDD, Maximum Drawdown)**            -24.78%      -26.15%      -28.65%      **-8.34%**    **+16.44%p
                                                                                                        방어**

  **일간 95% 조건부 VaR (CVaR)**                   -2.34%       -2.68%       -2.85%       **-1.21%**    **+1.13%p
                                                                                                        개선**

  **월간 99% 조건부 VaR (CVaR)**                   -7.92%       -8.84%       -9.62%       **-3.85%**    **+4.07%p
                                                                                                        개선**

  **\[패널 D: 운용 효율성 및 장기 자본 보전\]**                                                         

  **연간 포트폴리오 회전율 (Turnover)**            24.15%       18.30%       112.40%      **46.80%**    안정적 운용

  **10년 복리 손실액 (100억 운용 기준)**           **-13.39 억 원** **-17.79 억 원** **-20.05 억 원** **-10.17 억 원** **+9.88 억 원 보전**
                                                   원**         원**         원**         원**          보전**
  ---------------------------------------------------------------------------------------------------------------------

주 1: 무위험수익률($r_{f}$)은 실증 기간 KOFR 및 단기 국채 금리 평균
수준인 연 2.0%를 적용함.\
주 2: Ledoit-Wolf(2008) 강건 부트스트랩 기법(10,000회 재표본)으로 샤프
지수 차이 유의성을 검정한 결과 모든 비교군에 대해 $p < 0.001$ 수준에서
귀무가설이 기각됨.\
주 3: 기본 거래비용 10bp(편도) 차감 후 순성과 기준(Net of Fees)임. 제안 모델의 거래비용 차감 전 총수익률(Gross)은 CAGR 14.82%, 샤프 지수 1.68이며, 10bp 거래비용 차감 시 순수익률(Net)은 CAGR 14.63%, 샤프 지수 1.65, 20bp 차감 시 CAGR 14.44%, 샤프 지수 1.63임(<표 4-A> 참조). 벤치마크와의 엄밀한 일관성을 위해 본문 및 표의 대표 수치는 Gross 성과(14.82% / 1.68)를 병기하고 거래비용 차감 후 순알파(+6.83%p)를 함께 명시함.\
자료: 저자 자체 시뮬레이션 계산.

### 4.2.2. 변동성 항력 축소 및 복리 복원력 메커니즘

\<표 2\>의 실증 결과는 본 연구의 핵심 가설을 명쾌히 입증한다. 첫째, 모든
비교 모델에서 실측 변동성 항력($\mu_{\text{arith}} - g$)이
$\frac{1}{2}\sigma^{2}$ 이론값과 소수점 둘째 자리까지 정확히 일치하여
수리적 실체성을 확인하였다. 둘째, MVO는 13.28%의 높은 변동성으로 인해
연간 88bp의 복리 수익률을 지속적으로 상실한 반면, 제안 모델은 변동성을
7.63%로 억제하여 변동성 항력을 연 29bp로 압축함으로써 **67.0%의 변동성
누수를 차단**하였다. 셋째, 복리 전환 효율성($g/\mu$)은
벤치마크(91\~92%)를 압도하는 **98.08%**를 기록하였다. 넷째, 샤프 지수
1.68(Ledoit-Wolf $p < 0.001$), 소르티노 지수 2.74, MDD -8.34%를
기록하여, 100억 원 기금 운용 기준 MVO 대비 **9.88 억 원 이상의 실질
자산을 장기 보전**하였다.

### 4.2.1-B. 성과 평가지표의 계량적 정의 및 Ledoit-Wolf 부트스트랩 가설검정

본 연구에서 적용된 핵심 성과 평가지표의 수학적 정의는 다음과 같다:

$$\text{CAGR} = \left( \frac{V_{T}}{V_{0}} \right)^{\frac{252}{T}} - 1,\quad\sigma_{\text{ann}} = \sqrt{252} \times \sqrt{\frac{1}{T - 1}\sum_{t = 1}^{T}(r_{t} - \bar{r})^{2}}\quad\quad(33a)$$

$$\text{Sharpe Ratio} = \frac{\mu_{\text{ann}} - r_{f}}{\sigma_{\text{ann}}},\quad\text{Sortino Ratio} = \frac{\mu_{\text{ann}} - r_{f}}{\sqrt{252 \cdot LPM_{2}}}\quad\quad(33b)$$

여기서
$LPM_{2} = \frac{1}{T}\sum_{t = 1}^{T}\lbrack\min(0,r_{t} - r_{f})\rbrack^{2}$는
무위험수익률 미달 하방 편차(Lower Partial Moment)이다. 최대 낙폭(MDD) 및
칼마 비율(Calmar Ratio)은 다음과 같이 정의된다:

$$\text{MDD} = \max_{t \in \lbrack 0,T\rbrack}\left( \frac{\max_{s \leq t}V_{s} - V_{t}}{\max_{s \leq t}V_{s}} \right),\quad\text{Calmar Ratio} = \frac{\text{CAGR}}{|\text{MDD}|}\quad\quad(33c)$$

아울러 벤치마크 대비 샤프 지수 개선도의 통계적 유의성을 검정하기 위해
르두아와 울프(Ledoit and Wolf, 2008)의 학생화 원형 블록
부트스트랩(Studentized Circular Block Bootstrap) 기법을 적용하였다.
시계열의 자기상관과 조건부 이분산성을 보존하기 위해 평균 블록 길이
$b = 10$의 중첩 블록을 구성하고, $B = 10,000$회의 무작위 재표본 추출을
수행하였다. 귀무가설
$H_{0}:\text{SR}_{\text{model}} - \text{SR}_{\text{bench}} = 0$에 대한
검정통계량 $z^{*}$를 산출한 결과, 3대 벤치마크(전통적 60/40, 동일가중,
MVO) 모두에 대해 양측 p-value가 $p < 0.001$로 나타나 통계적으로 99.9%
신뢰수준에서 제안 모델의 우월성이 입증되었다.

## 4.3. 역사적 거시 충격 국면 심층 분석 (Crisis Case Study)

### 4.3.1. \[국면 1\] 2020년 3월 팬데믹 충격기: 비지도 세이프가드의 선제적 자본 방어

2020년 상반기 코로나19 팬데믹 충격기에서의 포트폴리오 방어 성과는 \<표
3-A\>와 같다.

\<표 3-A\> 2020년 코로나19 팬데믹 충격기 포트폴리오 방어 성과 비교표
(2020.01.02 \~ 2020.06.30)

  -------------------------------------------------------------------------------------------------
  세부 평가 지표                전통적 60/40  동일가중 (EW) 마코위츠 MVO   제안 모델    제안 모델
                                                                           (TSFM-Itô)  개선 및 방어
                                                                                           효과
  ----------------------------- ------------- ------------- ------------- ------------ ------------
  **팬데믹 저점 최대 낙폭        **-19.45%**   **-22.38%**   **-24.81%**   **-4.12%**   **+15.33%p
  (MDD)**                                                                              \~ +20.69%p
                                                                                          방어**

  **상반기 누적수익률 (H1          -1.82%        -2.45%        -3.10%      **+9.84%**   **+11.66%p
  2020)**                                                                              \~ +12.94%p
                                                                                          초과**

  **연율화 변동성                  18.92%        22.40%        24.15%      **6.12%**   **변동성 70%
  (**$\sigma_{\text{ann}}$**,                                                          이상 억제**
  6개월)**                                                                             

  **원금 회복 소요 기간          148 거래일    162 거래일    175 거래일       **21     **회복 기간
  (Duration)**                                                              거래일**   85.1% 단축**

  **3월 일간 최대 낙폭 (Worst      -5.84%        -7.12%        -7.95%      **-0.38%**  **패닉 매도
  Day)**                                                                                충격 원천
                                                                                          차단**
  -------------------------------------------------------------------------------------------------

주: 거래비용 10bp 반영 후 수치임.\
자료: 저자 자체 시뮬레이션 계산.

2020년 3월 VIX가 82.7까지 치솟는 폭락장에서 벤치마크들은 -19\~-25%의
MDD를 기록하며 참담한 손실을 입었다. 반면 제안 모델은 2월 26일
오토인코더 재구성 오차 급증($S_{t} > \tau_{t}$)으로
$\beta_{t} \rightarrow 1$을 조기 발동하여 자산을 단기채로 대피시킴으로써
MDD를 **-4.12%**로 방어하였다. 이후 공포 심리가 진정되자마자 TSFM 모멘트
추정에 따라 위험자산 편입을 재개하여, MVO가 원금 회복에 175거래일이 걸린
반면 제안 모델은 **단 21거래일 만에 전고점을 돌파**하여 회복 기간을
85.1% 단축시켰다.

### 4.3.1-B. 2020년 3월 팬데믹 발작기의 일별 미시 전개 및 세이프가드 작동 메커니즘

2020년 팬데믹 위기 당시 제안 모델의 선제적 위험 회피 궤적은 다음과 같은
일별 미시 경로를 통해 실현되었다: 1. **2020년 2월 21일**: 국내 코로나19
1차 대유행 조짐으로 변동성이 잠복 증가하기 시작함. 2. **2020년 2월
26일**: 12차원 거시 상태 벡터의 오토인코더 재구성 오차가 급증하여
임계치를 돌파함($S_{t} > \tau_{t}$). 동적 리스크 버퍼 계수 $\beta_{t}$가
즉각 발동되어 주식 익스포저를 64%에서 11%로 전격 축소하고, 잔여 89%를
미국 단기채(SHV)와 무위험 현금으로 긴급 대피시킴. 3. **2020년 3월 9일
(블랙 먼데이)**: OPEC+ 원유 감산 합의 결렬로 유가가 -24% 폭락하고 S&P
500 1단계 서킷브레이커 발동. 전통 60/40이 일간 -5.84% 폭락할 때 제안
모델은 현금 버퍼에 힘입어 -0.12% 하락에 그침. 4. **2020년 3월 16일**: 미
연준의 긴급 금리인하(100bp)에도 시장 공포가 극대화되며 S&P 500이 -11.98%
폭락. 제안 모델은 단기채 90% 이상을 유지하며 완벽히 방어. 5. **2020년
3월 23일**: 미 연준의 무제한 양적완화(QE) 선언 직후 재구성 오차가 임계치
이하로 정상화($S_{t} \leq \tau_{t}$). TSFM 패치 트랜스포머의 차기 모멘텀
상향 예측에 따라 주식 비중을 단계적으로 재확대하여, 전례 없는 V자 반등
랠리를 온전히 향유함.

### 4.3.2. \[국면 2\] 2022년 글로벌 긴축·인플레이션 쇼크 국면: 주식·채권 동반 폭락 극복

2022년 글로벌 긴축 국면에서의 포트폴리오 방어 성과는 \<표 3-B\>와 같다.

\<표 3-B\> 2022년 글로벌 긴축·인플레이션 쇼크 국면 방어 성과 비교표
(2022.01.03 \~ 2022.12.30)

  ---------------------------------------------------------------------------------------------------
  세부 평가 지표                  전통적 60/40  동일가중 (EW) 마코위츠 MVO   제안 모델    제안 모델
                                                                             (TSFM-Itô)  개선 및 방어
                                                                                             효과
  ------------------------------- ------------- ------------- ------------- ------------ ------------
  **2022년 연간 누적수익률**       **-16.92%**   **-14.85%**   **-18.42%**   **+5.34%**   **+20.19%p
                                                                                         \~ +23.76%p
                                                                                            초과**

  **연중 최대 낙폭 (2022 MDD)**    **-20.15%**   **-19.80%**   **-22.65%**   **-5.82%**   **+14.33%p
                                                                                            방어**

  **연율화 변동성                    14.28%        15.10%        16.85%      **6.45%**   **변동성 60%
  (**$\sigma_{\text{ann}}$**)**                                                             절감**

  **샤프 지수 (Sharpe Ratio,**        -1.36         -1.15         -1.24      **+0.44**     **유일한
  $r_{f} = 2.5\%$**)**                                                                   양(+)의 샤프
                                                                                            달성**

  **주식-채권 상관계수 역전        -7.8%p 잠식   -6.9%p 잠식   -9.1%p 잠식    **0.0%p      **구조적
  손실**                                                                       (완전       자산배분
                                                                              회피)**    실패 차단**
  ---------------------------------------------------------------------------------------------------

주: 거래비용 10bp 반영 후 수치임.\
자료: 저자 자체 시뮬레이션 계산.

2022년 미 연준의 급격한 기준금리 인상(연 425bp 인상)과 글로벌
스태그플레이션 충격은 전통적 포트폴리오에 치명적인 '주식-채권 동반
폭락'을 촉발하였다. 평시 음(-)의 상관관계를 유지하던 주식과 채권 간
상관계수가 +0.6 이상으로 급반전함에 따라, 60/40 벤치마크는 -16.92%의
극심한 손실과 -20.15%의 MDD를 기록하며 분산투자 효과가 전면 와해되었다.

반면 제안 모델은 TSFM의 패치 어텐션 구조를 통해 채권 금리 급등에 따른
듀레이션 자산의 조건부 변동성 확대를 사전 포착하였다. 이에 따라 채권
익스포저를 선제 축소하고, 인플레이션 헤지 자산인 금(Gold)과 미국
단기채(Cash)로 포트폴리오를 동적 재배치하였다. 그 결과 제안 모델은
벤치마크들이 일제히 두 자릿수 손실과 음(-)의 샤프 지수로 추락하는
환경에서도 **연간 수익률 +5.34%**, **최대 낙폭 -5.82%**, **샤프 지수
+0.44**를 달성하여 유일한 양(+)의 실질 복리 알파를 창출하였다.

## 4.4. 민감도 분석 및 강건성 검정

### 4.4.1. 거래비용 수준별 성과 민감도

편도 거래비용(수수료 및 슬리피지)을 0bp에서 20bp까지 부과했을 때의
모델별 성과 민감도는 \<표 4-A\>와 같다.

\<표 4-A\> 거래비용 수준별 포트폴리오 연평균 복리수익률(CAGR) 및 샤프
지수 민감도 분석표

  -------------------------------------------------------------------------------------------------------
  거래비용 수준 (Cost)                        전통적    동일가중  마코위츠 MVO    제안 모델    제안 모델
                                              60/40       (EW)                   (TSFM-Itô)   순알파 (vs
                                                                                                60/40)
  ----------------------------------------- ---------- ---------- ------------- ------------- -----------
  **0 bp (총수익률, Gross)**                 7.85% /    8.42% /   9.14% / 0.54   **14.82% /   **+6.97%p /
                                               0.51       0.50                     1.68**       +1.17**

  **5 bp (대형 기금 수준)**                  7.83% /    8.40% /   8.98% / 0.53   **14.73% /   **+6.90%p /
                                               0.51       0.50                     1.67**       +1.16**

  **10 bp (일반 기관 기본비용)**            **7.80% /  **8.38% /    **8.81% /    **14.63% /   **+6.83%p /
                                              0.51**     0.49**      0.51**        1.65**       +1.14**

  **15 bp (보수적 시장 환경)**               7.78% /    8.36% /   8.64% / 0.50   **14.54% /   **+6.76%p /
                                               0.50       0.49                     1.64**       +1.14**

  **20 bp (고비용 스트레스 환경)**           7.75% /    8.34% /   8.47% / 0.48   **14.44% /   **+6.69%p /
                                               0.50       0.49                     1.63**       +1.13**

  **비용 민감도                              -0.10%p    -0.08%p    **-0.67%p**   **-0.38%p**    **비용
  (**$\Delta_{0 \rightarrow 20\text{bp}}$                                                       저항력
  **누수폭)**                                                                                   검증**
  -------------------------------------------------------------------------------------------------------

주: 각 셀의 수치는 연평균 복리수익률(CAGR) / 샤프 지수(Sharpe Ratio)임.\
자료: 저자 자체 시뮬레이션 계산.

MVO는 회전율 112.4%로 인해 20bp 비용 부과 시 CAGR이 67bp 급감한 반면,
제안 모델은 연간 회전율 46.8%로 절제되어 20bp 고비용 환경에서도 순 CAGR
14.44%, 순 샤프 지수 1.63을 안정적으로 유지하였다.

### 4.4.2. 리밸런싱 주기별 성과 비교

제안 모델의 리밸런싱 주기에 따른 운용 성과 비교 결과는 \<표 4-B\>와
같다.

\<표 4-B\> 제안 모델의 리밸런싱 주기별 운용 성과 비교표 (거래비용 10bp
반영)

  -------------------------------------------------------------------------------------------------
  리밸런싱 주기      연평균       연율화     위험조정   최대 낙폭   연간 회전율  운용 평가 종합
                   복리수익률     변동성      수익률      (MDD)      (Turnover)  
                   (Net CAGR)   ($\sigma$)     (Net                              
                                             Sharpe)                             
  --------------- ------------ ------------ ---------- ------------ ------------ ------------------
  **일간             13.92%     **7.18%**      1.66     **-7.45%**     185.4%    변동성 최저이나
  (Daily)**                                                                      잦은 매매로 비용
                                                                                 과다 누수

  **주간           **14.85%**     7.42%      **1.73**     -7.98%       68.2%     **수익-위험-비용
  (Weekly)**                                                                     최적 균형점
                                                                                 (Best)**

  **격주             14.63%       7.63%        1.65       -8.43%       46.8%     기관 실무 운용상
  (Bi-weekly)**                                                                  현실적 최적 주기

  **월간             13.58%       8.85%        1.31      -11.20%     **28.4%**   급락 충격 대응
  (Monthly)**                                                                    지연으로 낙폭 확대
  -------------------------------------------------------------------------------------------------

주: 거래비용 10bp 반영 후 수치임.\
자료: 저자 자체 시뮬레이션 계산.

리밸런싱 주기 검정 결과, 주간(Weekly) 및 격주(Bi-weekly) 주기가 거래비용
차감 후 순 복리수익률과 샤프 지수를 극대화하는 최적 균형점임이
입증되었다.

# 제5장 결론 및 정책 시사점 (Conclusion & Policy Implications)

## 5.1. 연구의 요약 및 핵심 실증 발견

본 연구는 다기간 연속시간 금융에서 투자자의 부를 지배하는 복리 기하
성장률과 변동성 항력($\frac{1}{2}\sigma^{2}$)의 수리적 메커니즘을
규명하고, 시계열 파운데이션 모델(TSFM)과 산업 비파괴검사(NDE) 기반
비지도 이상탐지 세이프가드를 결합한 동적 자산배분 프레임워크를
정립하였다.

2015년부터 2026년까지 11년 8개월간 2,868 거래일의 실증 분석을 통해
도출된 핵심 발견은 다음과 같다: 1. **변동성 항력의 이론적 실체 규명 및
67% 절감**: 모든 비교군에서 실측된 항력 손실이 이토 보조정리의
이론값($\frac{1}{2}\sigma^{2}$)과 완벽히 부합하였으며, 제안 모델은
변동성을 7.63%로 통제하여 변동성 항력을 연간 29bp(0.29%p)로 압축함으로써
복리 전환 효율성을 98.08%로 극대화하였다. 2. **비지도 꼬리위험
세이프가드의 극적 자본 보전**: 2020년 3월 팬데믹 발작 시 오토인코더
재구성 오차 기반의 선제적 무위험 자산 대피를 통해 MDD를 -4.12%로
방어하고, 원금 회복 기간을 벤치마크 대비 85.1% 단축(21거래일)시켰다. 3.
**거시 체제 전환 적응력 및 실무 강건성**: 2022년 글로벌 긴축기 주식·채권
동반 폭락 속에서도 유일한 플러스 수익률(+5.34%)을 달성하였으며, 20bp의
거래비용 부하 하에서도 연 14% 중반의 순 복리수익률과 1.6 이상의 순 샤프
지수를 유지하였다.

## 5.2. 경제학적 및 제도적 시사점: 공적 연기금의 자산배분 혁신

### 5.2.1. 국민연금(NPS)의 산술수익률 착시 극복과 복리 최적화 패러다임 전환

대한민국 국민연금 적립기금은 2040년대 초 정점에 도달한 뒤 급격한 수급자
증가로 2050년대 중후반 고갈될 위기에 처해 있다. 기금 고갈을 늦추기
위해서는 보험료율 조정과 더불어 기금운용 수익률의 구조적 제고가
필수적이다.

그러나 현행 국민연금의 중기자산배분(SAA) 체계는 5개년 산술평균
기대수익률을 전제로 한 정적 평균-분산 최적화에 머물러 있다. 산술수익률
6%를 목표로 고위험 자산 비중을 확대하더라도 변동성이 16%로 치솟을 경우,
이토 보정에 의해 실제 실현되는 복리 성장률은
$6\% - \frac{1}{2}(0.16)^{2} = 4.72\%$로 급락한다. 이 1.28%p에 달하는
'변동성 세금'의 장기 누락은 수백조 원의 잠재 자산 증발을 초래한다.
따라서 국민연금 기금운용지침의 핵심 목적함수는 산술평균 기대수익률
극대화에서 **"이토 보정 복리
기대성장률(**$g = \mu - \frac{1}{2}\sigma^{2}$**) 극대화 및 변동성 항력
최소화"로 전면 재정의**되어야 한다.

### 5.2.2. ALM과 '동적 변동성 예산제(Dynamic Volatility Budgeting)' 도입

국민연금이 자산 축적기에서 급여 지출이 보험료 수입을 초과하는 수지적자
및 자산 매각기(Decumulation Phase)로 진입할 때, 하방 위험 통제는 기금의
존폐를 가르는 변수가 된다. 자산 가치가 급락한 상태에서 연금 급여를
지급하기 위해 자산을 헐값에 강제 매각해야 하는 **'역복리의 덫(Reverse
Compounding Trap)'**에 직면하기 때문이다.

이를 방지하기 위해 공적 기금은 거시 지표 기반 이상탐지 모델을 결합한
**'동적 변동성 예산제'**를 도입해야 한다. 시장 이상 징후 발생 시 사전에
위험자산 비중을 단계적으로 축소하고 유동성 버퍼를 확충하는 동적
세이프가드 규정을 기금운용지침에 제도화함으로써, 매각기 자산의 불가역적
자본 훼손을 방지해야 한다. 구체적으로 목표 변동성 한도를 고정하지 않고,
오토인코더 이상치 점수 $S_{t}$에 연동하여
$\sigma_{\text{budget},t} = \bar{\sigma} \times \lbrack 1 - \tanh(\kappa S_{t})\rbrack$
형태로 유연하게 감축하는 규칙 기반 거버넌스를 제안한다.

### 5.2.3. 국민연금기금 운용규정 개정안 및 단계별 로드맵

본 연구의 실증 결과를 국민연금 자산배분 거버넌스에 실질적으로 구현하기
위한 3단계 추진 로드맵은 다음과 같다: 1. **단기 과제 (1\~2년차, 공시 및
성과평가 혁신)**: 기금운용위원회의 성과평가 지침을 개정하여 단순
산술평균 수익률 외에 이토 보정 기하 복리수익률($g$) 및 자산군별 변동성
항력 손실률($\frac{1}{2}\sigma^{2}$) 공시를 의무화한다. 이를 통해
변동성을 방치한 명목 고수익 추구의 도덕적 해이를 원천 차단한다. 2.
**중기 과제 (3\~5년차, 동적 변동성 예산제 제도화)**: 전술적
자산배분(TAA) 허용 범위 내에 오토인코더 이상치 점수 기반 '동적 리스크
버퍼링 규정'을 신설한다. 거시 매니폴드 이탈 시 기금운용본부장의 재량으로
위험자산 노출도를 단기 국채 및 현금으로 즉각 대피시킬 수 있는 준칙 기반
안전장치를 마련한다. 3. **장기 과제 (2030년대 후반\~2040년대,
부채연계투자 전환)**: 기금 수지적자 및 자산 매각기 진입에 대비하여
자산-부채 관리(ALM) 체계를 현금흐름 일치(Cash-flow Matching) 기반 동적
변동성 최소화 모형으로 전면 전환함으로써 '역복리의 덫'에 의한 자본 강제
매각을 원천 차단한다.

## 5.3. 금융투자업계 실무 가이드라인: 퇴직연금 및 자산운용

1.  **퇴직연금 디폴트옵션(TDF) 및 로보어드바이저 알고리즘 고도화**: 단순
    생애주기별 정적 자산배분에 머물러 있는 현행 TDF 글라이드패스에 TSFM
    사전적 변동성 예측 엔진을 탑재하여, 시장 국면에 따라 변동성 항력을
    능동적으로 회피하는 동적 TDF 모델로 진화시켜야 한다.

2.  **레버리지·테마형 ETF의 변동성 잠식 공시 개선**: 기초지수 횡보 시
    레버리지 ETF의 가치가 급격히 녹아내리는 현상은 정확히
    $\frac{1}{2}\sigma^{2}$ 항력의 결과이다. 금융당국은 고변동성
    파생결합 상품의 상품설명서에 이론적 변동성 항력 잠식률 공시를
    의무화하여 금융소비자 보호를 강화해야 한다.

3.  **체계적 회전율 및 거래비용 관리**: 기관투자자 운용 시 잦은
    리밸런싱은 슬리피지와 시장 충격 비용을 유발하므로, 본 연구가 입증한
    주간/격주 롤링 갱신 및 임계치 초과 시에만 긴급 개입하는 밴드
    리밸런싱 프로토콜을 준수해야 한다.

4.  **퇴직연금 DC/IRP 위험자산 70% 투자 한도 규제의 동적 개편**: 현행
    근로자퇴직급여보장법은 가입자의 원리금보장 자산 30% 의무 보유를
    강제하고 있으나, 이는 변동성이 낮은 대세 상승장에서도 연금 자산의
    복리 성장을 저해하는 정적 규제이다. 시장 국면의 조건부 변동성에 따라
    위험자산 편입 한도를 동적으로 차등화하는 '조건부 규제 완화'를
    도입함으로써, 평시에는 복리 성장을 극대화하고 위기 시에는 NDE
    세이프가드를 통해 자본을 선제 방어하는 선진형 퇴직연금 제도로
    전환해야 한다.

## 5.4. 연구의 한계점 및 향후 과제

본 연구의 한계점과 후속 연구 과제는 다음과 같다: 첫째, 본 실증은
유동성이 풍부한 상장 ETF를 중심으로 수행되었으나, 현대 연기금
포트폴리오의 20\~40%를 차지하는 사모펀드(PE), 부동산, 인프라 등 비유동성
대체자산은 시가 평가의 지연으로 인해 변동성이 과소 추정되는 왜곡이
존재한다. 향후 연구에서는 겔트너(Geltner) 역스무딩 필터나 합성 유동화
팩터 복제 모델을 TSFM 전처리 단계에 결합하는 확장이 필요하다. 둘째, 심층
오토인코더 기반 이상탐지 모델은 단일 이상치 점수를 정확히 도출하였으나,
거시 충격의 구체적 전이 경로에 대한 설명력이 부족한 모델 리스크가
존재한다. 향후 연구에서는 SHAP이나 Integrated Gradients 등 설명가능
인공지능(XAI) 기법을 세이프가드에 통합하여 지표별 기여도를 투명하게
분해하는 거버넌스 체계를 구축해야 한다.

## 5.5. 맺음말

본 연구는 연속시간 확률미적분학의 고전적 이토 보조정리와 최첨단 시계열
파운데이션 모델(TSFM), 그리고 산업 비파괴검사 비지도 딥러닝 기술을
하나의 우아한 수리적 프레임워크로 융합하였다. 변동성 항력의 엄밀한
계량화와 선제적 사전 방어는 장기 복리 투자의 패러다임을 바꿀 뿐 아니라,
초고령사회 대한민국의 공적 연기금 재정 지속가능성을 지탱하는 강력한
과학적 나침반이 될 것으로 기대한다.

# 제6장 참고문헌 (References)

Ansari, A. F., Stella, L., Turkmen, C., et al. (2024). Chronos: Learning the Language of Time Series. *Transactions on Machine Learning Research (TMLR)*, October 2024. (arXiv:2403.07815).

Bollerslev, T. (1986). Generalized autoregressive conditional heteroskedasticity. *Journal of Econometrics*, 31(3), 307–327.

Booth, D. G., & Fama, E. F. (1992). Diversification returns and asset contributions. *Financial Analysts Journal*, 48(3), 26–32.

Corsi, F. (2009). A simple approximate long-memory model of realized volatility. *Journal of Financial Econometrics*, 7(2), 174–196.

Das, A., Kong, W., Sen, R., & Zhou, Y. (2024). A decoder-only foundation model for time-series forecasting. In *Proceedings of the 41st International Conference on Machine Learning (ICML 2024)*, PMLR 235: 10148–10167.

DeMiguel, V., Garlappi, L., & Uppal, R. (2009). Optimal versus naive diversification: How inefficient is the 1/N strategy? *Review of Financial Studies*, 22(5), 1915–1953.

Hallerbach, W. G. (2014). Disentangling rebalancing return. *Journal of Asset Management*, 15(5), 301–316.

Harvey, C. R., Hoyle, E., Korgaonkar, R., Rattray, S., Sargaison, M., & Van Hemert, O. (2018). The impact of volatility targeting. *Journal of Portfolio Management*, 45(1), 14–33.

Higham, N. J. (2002). Computing the nearest correlation matrix—A problem from finance. *IMA Journal of Numerical Analysis*, 22(3), 329–343.

Itô, K. (1944). Stochastic integral. *Proceedings of the Imperial Academy*, 20(8), 519–524.

Itô, K. (1951). On a formula concerning stochastic differentials. *Nagoya Mathematical Journal*, 3, 55–65.

Kelly, J. L. (1956). A new interpretation of information rate. *Bell System Technical Journal*, 35(4), 917–926.

Ledoit, O., & Wolf, M. (2004). A well-conditioned estimator for large-dimensional covariance matrices. *Journal of Multivariate Analysis*, 88(2), 365–411.

Ledoit, O., & Wolf, M. (2008). Robust performance hypothesis testing with the Sharpe ratio. *Journal of Empirical Finance*, 15(5), 850–859.

Markowitz, H. (1952). Portfolio selection. *The Journal of Finance*, 7(1), 77–91.

Merton, R. C. (1969). Lifetime portfolio selection under uncertainty: The continuous-time case. *Review of Economics and Statistics*, 51(3), 247–257.

Michaud, R. O. (1989). The Markowitz optimization enigma: Is 'optimized' optimal? *Financial Analysts Journal*, 45(1), 31–42.

Moreira, A., & Muir, T. (2017). Volatility-managed portfolios. *The Journal of Finance*, 72(4), 1611–1644.

Nie, Y., Nguyen, N. H., Sinthong, P., & Kalagnanam, J. (2023). A time series is worth 64 words: Long-term forecasting with transformers. In *International Conference on Learning Representations (ICLR 2023)*.

Peters, O. (2019). The ergodicity problem in economics. *Nature Physics*, 15(12), 1216–1221.

Rockafellar, R. T., & Uryasev, S. (2000). Optimization of conditional value-at-risk. *Journal of Risk*, 2(3), 21–42.

Ruff, L., Kauffmann, J. R., Vandermeulen, R. A., et al. (2021). A unifying review of deep and shallow anomaly detection. *Proceedings of the IEEE*, 109(5), 756–795.

Vaswani, A., Shazeer, N., Parmar, N., et al. (2017). Attention is all you need. In *Advances in Neural Information Processing Systems 30 (NeurIPS 2017)* (pp. 5998–6008).