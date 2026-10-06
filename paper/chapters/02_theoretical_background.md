# 제2장 이론적 배경 및 선행연구 (Theoretical Framework & Literature Review)

---

## 2.1. 연속시간 확률미적분학과 변동성 항력(Volatility Drag)의 수리적 메커니즘

장기 다기간(Multi-period) 투자 환경에서 포트폴리오의 실질 부(Terminal Wealth)를 결정짓는 핵심 동역학은 단기 산술평균 수익률이 아닌 연속 복리 성장률(Continuous Compound Growth Rate)이다. 전통적 이산시간 재무론에서는 복리 효과를 직관적인 기하평균의 관점에서 다루어 왔으나, 자산 가격의 미세한 동적 거동과 이에 수반되는 분산의 부정적 외부효과를 엄밀하게 규명하기 위해서는 연속시간 확률미적분학(Continuous-time Stochastic Calculus)의 공리적 체계가 필수적이다. 

본 절에서는 자산 가격이 표준 확률공간 상에서 기하 브라운 운동(Geometric Brownian Motion, GBM)을 따른다는 기본 공준 하에, 확률미분방정식(SDE)에 작용하는 이토 보조정리(Itô's Lemma)를 수학적으로 엄밀히 유도한다. 이를 통해 로그 자산 가격의 드리프트 항에서 필연적으로 발생하는 변동성 감쇄분, 즉 **'변동성 항력(Volatility Drag)'**의 수리적 실체를 도출하고 그 경제학적 함의를 논증한다.

### 2.1.1. 자산 가격의 확률과정과 기하 브라운 운동 (GBM)

자산 가격의 동적 궤적을 묘사하기 위해 완비확률공간 \((\Omega, \mathcal{F}, (\mathcal{F}_t)_{t \ge 0}, \mathbb{P})\)를 정의한다. 여기서 \(\Omega\)는 표본공간, \(\mathcal{F}\)는 \(\sigma\)-대수, \(\mathbb{P}\)는 실제 확률측도(Physical Probability Measure)이며, \((\mathcal{F}_t)_{t \ge 0}\)는 표준 브라운 운동(Brownian Motion, Wiener Process) \(W = (W_t)_{t \ge 0}\)에 의해 생성된 자연 여과확률체계(Natural Filtration)로서 시장 참여자에게 시간 \(t\)까지 축적된 모든 과거 정보의 집합을 대변한다.

표준 브라운 운동 \(W_t\)는 다음의 네 가지 수학적 공리를 만족하는 연속시간 확률과정이다:
1. \(W_0 = 0\) a.s. (almost surely).
2. 독립 증분(Independent Increments): 임의의 시점 \(0 \le s < t \le u < v\)에 대해 증분 \(W_t - W_s\)와 \(W_v - W_u\)는 상호 독립이다.
3. 정상 정규 증분(Stationary Normal Increments): 임의의 \(0 \le s < t\)에 대해 \(W_t - W_s \sim \mathcal{N}(0, t - s)\)를 따른다.
4. 연속 경로(Continuous Sample Paths): 거의 모든 사건 \(\omega \in \Omega\)에 대해 궤적 \(t \mapsto W_t(\omega)\)는 연속함수이다.

금융 자산 가격 \(S_t\)의 연속적 거동을 모델링할 때, 가장 단순한 산술 브라운 운동(Arithmetic Brownian Motion, ABM: \(dS_t = \mu dt + \sigma dW_t\))은 두 가지 치명적인 경제학적 결함을 지닌다. 첫째, 주식이나 ETF와 같은 유한책임(Limited Liability) 자산은 가격이 결코 음(-)이 될 수 없으나, ABM은 유한한 시간 내에 음의 가격을 가질 양의 확률을 배제하지 못한다. 둘째, 주가의 절대적 변동 폭은 자산 가격의 수준에 비례하여 확장되는 것이 일반적이나, ABM은 주가가 1,000원이든 100,000원이든 동일한 절대적 분산을 가정한다.

따라서 자산 가격의 절대적 변화량 대신 상대적 수익률(Relative Return) \(\frac{dS_t}{S_t}\)이 기대수익률(드리프트) \(\mu \in \mathbb{R}\)와 조건부 변동성(확산 계수) \(\sigma > 0\)를 갖는 확률과정을 따른다고 모델링하는 것이 타당하다. 이를 기하 브라운 운동(Geometric Brownian Motion, GBM)이라 하며, 다음과 같은 확률미분방정식(Stochastic Differential Equation, SDE)으로 정식화된다:

$$dS_t = \mu S_t dt + \sigma S_t dW_t \quad \text{--- (식 1)}$$

(식 1)에서 \(\mu S_t dt\)는 시장의 추세적 기대를 나타내는 유한변분(Finite Variation) 결정론적 성분이며, \(\sigma S_t dW_t\)는 예측 불가능한 시장 충격을 반영하는 비유한변분(Infinite Variation) 마틴게일(Martingale) 성분이다.

### 2.1.2. 테일러 전개와 이토 보조정리(Itô's Lemma)의 엄밀한 유도

고전 미적분학의 연쇄 법칙(Chain Rule)은 미분 가능한 매끄러운 함수에 국한된다. 그러나 브라운 운동의 궤적은 횔더 연속성(Hölder Continuity) 지수가 \(\gamma < 1/2\)에 불과하여 르베그 측도 상에서 거의 모든 곳(almost everywhere)에서 미분 불가능하며, 2차 변분(Quadratic Variation)이 유한한 양의 값을 갖는다.

구간 \([0, t]\)의 임의의 분할 \(\Pi_n = \{0 = t_0 < t_1 < \dots < t_n = t\}\)에 대해 분할의 메쉬(Mesh Size)를 \(\|\Pi_n\| = \max_{1 \le k \le n} (t_k - t_{k-1})\)이라 하자. 브라운 운동 \(W_t\)의 2차 변분 \([W, W]_t\)는 다음과 같이 정의된다:

$$[W, W]_t = \lim_{\|\Pi_n\| \to 0} \sum_{k=1}^n (W_{t_k} - W_{t_{k-1}})^2$$

이 극한의 성질을 규명하기 위해 확률변수 \(Q_n = \sum_{k=1}^n (\Delta W_k)^2\)의 기댓값과 분산을 유도한다 (단, \(\Delta W_k = W_{t_k} - W_{t_{k-1}}\), \(\Delta t_k = t_k - t_{k-1}\)). 브라운 운동의 성질에 의해 \(\Delta W_k \sim \mathcal{N}(0, \Delta t_k)\)이므로, \(\mathbb{E}[(\Delta W_k)^2] = \Delta t_k\)이며 \(\mathbb{V}ar[(\Delta W_k)^2] = 2(\Delta t_k)^2\)이다.

$$\mathbb{E}[Q_n] = \sum_{k=1}^n \mathbb{E}[(\Delta W_k)^2] = \sum_{k=1}^n \Delta t_k = t$$

$$\mathbb{V}ar[Q_n] = \sum_{k=1}^n \mathbb{V}ar[(\Delta W_k)^2] = 2 \sum_{k=1}^n (\Delta t_k)^2 \le 2 \|\Pi_n\| \sum_{k=1}^n \Delta t_k = 2 t \|\Pi_n\|$$

따라서 분할의 메쉬가 0으로 수렴할 때(\(\|\Pi_n\| \to 0\)), \(\mathbb{V}ar[Q_n] \to 0\)이 성립하므로 체비쇼프 부등식(Chebyshev's Inequality)에 의해 \(Q_n\)은 상수 \(t\)로 확률수렴(in probability) 및 \(L^2(\mathbb{P})\) 수렴한다:

$$[W, W]_t = t \quad \text{a.s.}$$

이를 무한소 증분(Infinitesimal Increment) 표기법으로 환원하면 고전 미적분학과 결정적으로 구별되는 **이토의 곱셈 규칙(Itô Multiplication Rules)**이 성립한다:

$$dW_t \cdot dW_t = dt, \quad dt \cdot dW_t = 0, \quad dt \cdot dt = 0 \quad \text{--- (식 2)}$$

이제 임의의 2계 연속 미분가능 함수 \(f(t, x) \in C^{1,2}([0, \infty) \times \mathbb{R})\)에 대해 다변수 테일러 전개(Taylor Expansion)를 2차 항까지 수행한다:

$$df(t, X_t) = \frac{\partial f}{\partial t}dt + \frac{\partial f}{\partial x}dX_t + \frac{1}{2}\frac{\partial^2 f}{\partial x^2}(dX_t)^2 + \mathcal{O}(|dX_t|^3)$$

고전 미적분학에서는 \((dX_t)^2 \sim \mathcal{O}((dt)^2)\)로 간주되어 고차 무한소로서 소거되지만, 확률과정 \(X_t\)가 확산항 \(\sigma dW_t\)를 포함할 경우 \((dW_t)^2 = dt\)에 의해 2차 항이 1차 무한소 \(dt\)의 차수로 살아남는다. 이것이 바로 **이토 보조정리(Itô's Lemma)**의 본질이다:

$$df(t, X_t) = \left( \frac{\partial f}{\partial t} + \frac{1}{2}\sigma^2 \frac{\partial^2 f}{\partial x^2} \right) dt + \frac{\partial f}{\partial x}dX_t \quad \text{--- (식 3)}$$

자산 가격 \(S_t\)가 (식 1)의 GBM을 따를 때, 자산의 2차 증분 \((dS_t)^2\)은 (식 2)의 곱셈 규칙에 의해 다음과 같이 계산된다:

$$(dS_t)^2 = (\mu S_t dt + \sigma S_t dW_t)^2 = \mu^2 S_t^2 (dt)^2 + 2\mu\sigma S_t^2 (dt)(dW_t) + \sigma^2 S_t^2 (dW_t)^2 = \sigma^2 S_t^2 dt \quad \text{--- (식 4)}$$

이제 자산의 연속 복리 누적 가치를 평가하기 위해 변환함수를 로그 함수 \(f(S_t) = \ln S_t\)로 정의한다. 이 함수의 편도함수는 다음과 같다:

$$\frac{\partial f}{\partial t} = 0, \quad \frac{\partial f}{\partial S} = \frac{1}{S_t}, \quad \frac{\partial^2 f}{\partial S^2} = -\frac{1}{S_t^2}$$

위 도함수들과 (식 1), (식 4)를 이토 공식 (식 3)에 대입하면 다음과 같은 전개가 이루어진다:

$$d(\ln S_t) = \frac{1}{S_t} dS_t + \frac{1}{2}\left(-\frac{1}{S_t^2}\right)(dS_t)^2$$

$$d(\ln S_t) = \frac{1}{S_t} (\mu S_t dt + \sigma S_t dW_t) - \frac{1}{2 S_t^2} (\sigma^2 S_t^2 dt)$$

$$d(\ln S_t) = \left( \mu - \frac{1}{2}\sigma^2 \right) dt + \sigma dW_t \quad \text{--- (식 5)}$$

(식 5)의 양변을 시점 \(0\)부터 \(t\)까지 르베그-이토 적분(Lebesgue-Itô Integration)을 취하면 다음과 같다:

$$\int_0^t d(\ln S_u) = \int_0^t \left( \mu - \frac{1}{2}\sigma^2 \right) du + \int_0^t \sigma dW_u$$

$$\ln S_t - \ln S_0 = \left( \mu - \frac{1}{2}\sigma^2 \right) t + \sigma W_t$$

양변에 지수함수 \(\exp(\cdot)\)를 취함으로써 기하 브라운 운동의 엄밀한 닫힌 형태 해(Closed-form Solution)를 최종 도출할 수 있다:

$$S_t = S_0 \exp\left( \left( \mu - \frac{1}{2}\sigma^2 \right) t + \sigma W_t \right) \quad \text{--- (식 6)}$$

### 2.1.3. 산술평균과 기하평균의 괴리: 변동성 항력의 본질과 에르고딕성 파괴

(식 6)의 수학적 구조는 장기 투자자에게 극히 중요한 이론적 통찰을 제공한다. 지수 내부의 확률변수 \(\sigma W_t\)는 평균이 0이고 분산이 \(\sigma^2 t\)인 정규분포를 따르므로, 자산 가격 \(S_t\)는 로그정규분포(Lognormal Distribution)를 추종한다.

로그정규분포의 성질에 따라 자산 가격의 조건부 앙상블 기댓값(Ensemble Average) \(\mathbb{E}[S_t]\)를 계산하면 다음과 같다. 정규분포 확률변수 \(Z \sim \mathcal{N}(0, 1)\)에 대한 적률생성함수(Moment Generating Function) \(\mathbb{E}[e^{a Z}] = e^{\frac{1}{2}a^2}\)를 활용한다:

$$\mathbb{E}[S_t] = S_0 e^{(\mu - \frac{1}{2}\sigma^2)t} \mathbb{E}\left[ e^{\sigma \sqrt{t} Z} \right] = S_0 e^{(\mu - \frac{1}{2}\sigma^2)t} e^{\frac{1}{2}\sigma^2 t} = S_0 e^{\mu t} \quad \text{--- (식 7)}$$

(식 7)에 따르면, 수많은 평행우주(Ensemble of Realizations)에 존재하는 모든 투자자의 자산 가격 평균은 연율 \(\mu\)의 속도로 성장한다. 이것이 바로 전통적 MVO 및 단일 기간 금융 이론이 주목하는 산술 기대수익률(Arithmetic Expected Return)이다.

그러나 단 한 번뿐인 현실의 단일 우주 속에서 시간 축을 따라 생존해야 하는 단일 투자자가 실현하는 경로별 시간 평균(Pathwise Time Average), 즉 **연속 복리 성장률(Geometric Compound Growth Rate, \(g\))**은 브라운 운동에 대한 강대수의 법칙(Strong Law of Large Numbers for Brownian Motion: \(\lim_{t \to \infty} \frac{W_t}{t} = 0\) a.s.)에 의해 결정된다:

$$g \equiv \lim_{t \to \infty} \frac{1}{t} \ln\left( \frac{S_t}{S_0} \right) = \lim_{t \to \infty} \left[ \left( \mu - \frac{1}{2}\sigma^2 \right) + \sigma \frac{W_t}{t} \right] = \mu - \frac{1}{2}\sigma^2 \quad \text{a.s.} \quad \text{--- (식 8)}$$

(식 7)과 (식 8)의 괴리는 통계물리학 및 이론경제학에서 다루는 **'에르고딕성 파괴(Ergodicity Breaking)'** 현상의 전형이다(Peters, 2019). 즉, 앙상블 평균 성장률은 \(\mu\)이지만, 거의 모든 개별 투자자가 겪는 장기 시간 평균 성장률은 \(\mu - \frac{1}{2}\sigma^2\)로 수렴한다.

$$\text{변동성 항력 (Volatility Drag, } VD \text{)} \equiv \mu - g = \frac{1}{2}\sigma^2$$

수학적으로 이 페널티는 로그 함수의 엄격한 오목성(Strict Concavity)과 옌센의 부등식(Jensen's Inequality)에 기인한다:

$$\mathbb{E}[\ln S_t] < \ln \mathbb{E}[S_t]$$

$$\ln \mathbb{E}[S_t] - \mathbb{E}[\ln S_t] = \ln(S_0 e^{\mu t}) - \left[ \ln S_0 + \left( \mu - \frac{1}{2}\sigma^2 \right)t \right] = \frac{1}{2}\sigma^2 t \quad \text{--- (식 9)}$$

이산시간(Discrete-time) 환경에서도 이러한 관계는 완벽히 보존된다. 연속된 기간 \(t=1, \dots, T\) 동안의 단순 산술수익률을 \(R_t = \frac{S_t - S_{t-1}}{S_{t-1}}\)이라 할 때, 산술평균은 \(\bar{R}_A = \frac{1}{T}\sum_{t=1}^T R_t\), 표본분산은 \(\hat{\sigma}^2 = \frac{1}{T}\sum_{t=1}^T (R_t - \bar{R}_A)^2\)이다. 복리 기하수익률 \(R_G = \left( \prod_{t=1}^T (1 + R_t) \right)^{1/T} - 1\)에 대해 \(\ln(1+R_t)\)를 2차 테일러 전개(\(\ln(1+x) \approx x - \frac{1}{2}x^2\))하면 다음과 같다:

$$\ln(1 + R_G) = \frac{1}{T}\sum_{t=1}^T \ln(1 + R_t) \approx \frac{1}{T}\sum_{t=1}^T \left( R_t - \frac{1}{2}R_t^2 \right) = \bar{R}_A - \frac{1}{2}\left( \hat{\sigma}^2 + \bar{R}_A^2 \right)$$

일반적으로 1일 혹은 1개월 단위의 수익률 제곱 \(\bar{R}_A^2\)은 분산 \(\hat{\sigma}^2\)에 비해 무시할 수 있을 정도로 작으므로, 친숙한 이산 변동성 항력 근사식이 유도된다:

$$R_G \approx \bar{R}_A - \frac{1}{2}\hat{\sigma}^2 \quad \text{--- (식 10)}$$

(식 8)과 (식 10)은 중대한 시사점을 던진다. 만약 어떤 공격적 성장 자산의 연간 기대수익률이 \(\mu = 20\%\)에 달한다 하더라도, 연간 변동성이 \(\sigma = 70\%\)로 치솟는다면 실질 복리 성장률은 \(g = 0.20 - \frac{1}{2}(0.70)^2 = 0.20 - 0.245 = -4.5\%\)로 전락하여 장기적으로 파산에 이르게 된다. 특히 레버리지 ETF(2X, 3X) 상품들이 횡보장이나 고변동성 국면에서 기초지수 대비 심각한 가치 침식(Decay)을 겪는 현상은 정확히 이토 보조정리의 \(\frac{1}{2}\sigma^2\) 항력에 의한 필연적 귀결이다.

---

## 2.2. 포트폴리오 수준에서의 변동성 항력과 다각화 이론

개별 자산 차원에서 변동성 항력이 자본 축적을 방해하는 '마찰적 손실'이라면, 다수의 자산으로 구성된 포트폴리오 수준에서는 분산투자(Diversification)와 지속적 리밸런싱(Rebalancing)을 통해 변동성 항력을 적극적으로 축소하고 부가적인 성장률을 창출할 수 있는 수리적 기회가 열린다.

### 2.2.1. 다자산 확률과정과 다변량 이토 보조정리

시장 내에 존재하는 \(N\)개의 위험자산 벡터 \(S_t = (S_{1,t}, S_{2,t}, \dots, S_{N,t})^T\)를 고려하자. 각 자산은 \(M\)차원 독립 브라운 운동 벡터 \(W_t = (W_{1,t}, \dots, W_{M,t})^T\)에 의해 구동되는 다음의 연립 SDE를 만족한다:

$$\frac{dS_{i,t}}{S_{i,t}} = \mu_i dt + \sum_{j=1}^M \sigma_{ij} dW_{j,t}, \quad i = 1, \dots, N \quad \text{--- (식 11)}$$

여기서 기대수익률 벡터는 \(\mu = (\mu_1, \dots, \mu_N)^T\)이며, 확산 행렬은 \(\Sigma_0 = (\sigma_{ij}) \in \mathbb{R}^{N \times M}\)이다. 자산 간의 순간 공분산 행렬(Instantaneous Covariance Matrix) \(\Sigma \in \mathbb{R}^{N \times N}\)는 다음과 같이 대칭 양의 준정부호(Symmetric Positive Semi-definite) 행렬로 정의된다:

$$\Sigma = \Sigma_0 \Sigma_0^T = (\sigma_{ik})_{N \times N}, \quad \text{where } \sigma_{ik} = \sum_{j=1}^M \sigma_{ij}\sigma_{kj} = \frac{1}{dt} \mathbb{C}ov\left( \frac{dS_{i,t}}{S_{i,t}}, \frac{dS_{k,t}}{S_{k,t}} \right)$$

투자자의 총 포트폴리오 가치를 \(V_t\)라 하고, 각 자산에 배분된 자본 비중 벡터를 \(w_t = (w_{1,t}, \dots, w_{N,t})^T\)라 하자. 이때 포트폴리오는 레버리지가 없고 공매도가 제한된 표준 완전투자 가정을 따른다:

$$\mathbf{1}^T w_t = \sum_{i=1}^N w_{i,t} = 1, \quad w_{i,t} \ge 0$$

외부로부터의 추가 자금 유출입이 없는 자체자금조달(Self-financing) 및 연속적 리밸런싱(Continuous Rebalancing) 가정 하에서, 포트폴리오 가치 \(V_t\)의 상대적 미분 변화율은 다음과 같다:

$$\frac{dV_t}{V_t} = \sum_{i=1}^N w_{i,t} \frac{dS_{i,t}}{S_{i,t}} = w_t^T \mu dt + w_t^T \Sigma_0 dW_t \quad \text{--- (식 12)}$$

포트폴리오의 순간 기대수익률은 \(\mu_p(w_t) = w_t^T \mu\)이며, 포트폴리오의 순간 분산 \(\sigma_p^2(w_t)\)는 다음과 같이 2차 형식(Quadratic Form)으로 표현된다:

$$\sigma_p^2(w_t) = \frac{1}{dt} (dV_t / V_t)^2 = (w_t^T \Sigma_0 dW_t)(w_t^T \Sigma_0 dW_t)^T = w_t^T \Sigma_0 \Sigma_0^T w_t = w_t^T \Sigma w_t$$

이제 포트폴리오 가치의 자연로그 함수 \(f(V_t) = \ln V_t\)에 다변량 이토 보조정리를 적용한다:

$$d(\ln V_t) = \frac{1}{V_t} dV_t - \frac{1}{2 V_t^2} (dV_t)^2 = \left( w_t^T \mu - \frac{1}{2} w_t^T \Sigma w_t \right) dt + w_t^T \Sigma_0 dW_t \quad \text{--- (식 13)}$$

### 2.2.2. 포트폴리오 연속 복리 성장률과 리밸런싱 보너스의 분해

(식 13)으로부터 고정된 비중 벡터 \(w\)를 유지하는 동적 리밸런싱 포트폴리오의 장기 연속 복리 성장률 \(g_p(w)\)가 즉각적으로 도출된다:

$$g_p(w) = \lim_{t \to \infty} \frac{1}{t} \ln\left( \frac{V_t}{V_0} \right) = w^T \mu - \frac{1}{2} w^T \Sigma w \quad \text{--- (식 14)}$$

이제 포트폴리오의 복리 성장률 \(g_p(w)\)를 각 개별 자산 복리 성장률 \(g_i = \mu_i - \frac{1}{2}\sigma_i^2\)의 단순 가중평균과 비교해 보자:

$$\sum_{i=1}^N w_i g_i = \sum_{i=1}^N w_i \left( \mu_i - \frac{1}{2}\sigma_i^2 \right) = w^T \mu - \frac{1}{2} \sum_{i=1}^N w_i \sigma_i^2 \quad \text{--- (식 15)}$$

(식 14)에서 (식 15)를 차감하면, 다각화된 동적 포트폴리오가 창출해 내는 초과 성장률의 수리적 원천이 명확하게 드러난다:

$$g_p(w) - \sum_{i=1}^N w_i g_i = \frac{1}{2} \left[ \sum_{i=1}^N w_i \sigma_i^2 - w^T \Sigma w \right] \quad \text{--- (식 16)}$$

(식 16)의 대괄호 내부를 공분산 \(\sigma_{ij} = \rho_{ij}\sigma_i\sigma_j\)와 \(\sum_{i=1}^N w_i = 1\)의 제약을 이용하여 전개하면 다음과 같다:

$$\sum_{i=1}^N w_i \sigma_i^2 - w^T \Sigma w = \sum_{i=1}^N w_i \sigma_i^2 \left( \sum_{j=1}^N w_j \right) - \sum_{i=1}^N \sum_{j=1}^N w_i w_j \sigma_{ij} = \sum_{i=1}^N \sum_{j=1}^N w_i w_j (\sigma_i^2 - \sigma_{ij})$$

대칭성을 고려하여 행렬을 재구성하면:

$$\sum_{i=1}^N w_i \sigma_i^2 - w^T \Sigma w = \frac{1}{2} \sum_{i=1}^N \sum_{j=1}^N w_i w_j \left( \sigma_i^2 + \sigma_j^2 - 2\sigma_{ij} \right) = \frac{1}{2} \sum_{i=1}^N \sum_{j=1}^N w_i w_j \mathbb{E}\left[ \left( \frac{dS_i}{S_i} - \frac{dS_j}{S_j} \right)^2 \frac{1}{dt} \right] \ge 0$$

따라서 개별 자산 간의 상관계수가 완전 일치(\(\rho_{ij} = 1\))하지 않는 한, (식 16)은 엄격한 양수(\(> 0\))가 된다. 금융 문헌에서는 이를 **'리밸런싱 보너스(Rebalancing Premium)'** 또는 **'다각화 수익률(Diversification Return)'**이라 부른다(Booth & Fama, 1992; Fernholz, 2002).

이 현상의 대표적인 극단적 예시가 바로 정보이론의 창시자 클로드 섀넌이 고안한 **'섀넌의 도깨비(Shannon's Demon)'** 사고실험이다. 기대수익률이 0(\(\mu_1 = \mu_2 = 0\))이고 변동성만 높은 두 개의 비상관 자산이 존재한다고 하자. 개별 자산에 단순히 거치식 투자를 할 경우 변동성 항력(\(g_i = -1/2\sigma_i^2 < 0\))으로 인해 자산은 장기적으로 0으로 수렴한다. 그러나 두 자산의 비중을 50:50으로 끊임없이 리밸런싱하면, 포트폴리오의 분산은 절반으로 감소(\(\sigma_p^2 = 1/4\sigma_1^2 + 1/4\sigma_2^2\))하는 반면, 상대적으로 오른 자산을 팔아 떨어진 자산을 매수하는 '변동성 수확(Volatility Harvesting)'이 발생하여 포트폴리오 전체는 \(g_p = +1/8\sigma^2 > 0\)의 지수적 복리 성장을 구가하게 된다.

### 2.2.3. 성장 최적 포트폴리오(Kelly Criterion)와 공분산 추정 오차의 역설

장기 복리 성장률 \(g_p(w) = w^T \mu - \frac{1}{2} w^T \Sigma w\)를 최대화하는 문제를 정식화하면, 이는 정보이론의 켈리 기준(Kelly, 1956)을 다변량 연속시간으로 확장한 **성장 최적 포트폴리오(Growth-Optimal Portfolio, GOP)** 문제가 된다:

$$\max_{w} \quad \mathcal{J}(w) = w^T \mu - \frac{1}{2} w^T \Sigma w \quad \text{s.t.} \quad \mathbf{1}^T w = 1$$

라그랑주 승수법(Lagrange Multiplier)을 적용하여 라그랑지안을 설정한다:

$$\mathcal{L}(w, \lambda) = w^T \mu - \frac{1}{2} w^T \Sigma w - \lambda (\mathbf{1}^T w - 1)$$

1계 조건(First-order Condition)은 다음과 같다:

$$\nabla_w \mathcal{L} = \mu - \Sigma w - \lambda \mathbf{1} = \mathbf{0} \implies w^* = \Sigma^{-1}(\mu - \lambda \mathbf{1}) \quad \text{--- (식 17)}$$

만약 무위험 자산 대출이 자유로운 비제약(Unconstrained) 조건이라면 순수 켈리 최적해는 간단히 \(w^* = \Sigma^{-1}\mu\)로 귀결된다. 

그러나 현실에서 성장 최적 포트폴리오 이론이 직면하는 근본적인 장벽은 바로 **'추정 오차의 극대화(Maximization of Estimation Error)'**이다(Michaud, 1989). 특히 공분산 행렬 \(\Sigma\)의 역행렬 \(\Sigma^{-1}\)을 계산하는 과정에서, 표본 추정치의 미세한 노이즈는 고유값(Eigenvalue)의 역수를 취하는 과정에서 기하급수적으로 증폭된다. 만약 미래의 조건부 변동성 및 공분산을 사후적(Ex-post) 이동평균으로 잘못 추정할 경우, 최적화 엔진은 변동성 항력을 낮추기는커녕 잘못된 가중치 배분으로 인해 포트폴리오를 거대한 꼬리위험의 파멸로 몰고 가게 된다. 

따라서 다기간 복리 성장률을 진정으로 극대화하기 위해서는 단순한 과거 표본 통계량이 아니라, 미래 시점의 조건부 변동성 행렬 \(\hat{\Sigma}_{t+1}\)을 고도의 정밀도로 사전 예측(Ex-ante Forecasting)할 수 있는 차세대 시계열 파운데이션 모델(TSFM)의 도입이 강력히 요구된다.

---

## 2.3. 시계열 파운데이션 모델(TSFM)의 아키텍처 및 확률적 예측 원리

전통적 금융공학에서 조건부 변동성을 추정하기 위해 널리 사용되어 온 GARCH(Bollerslev, 1986), EGARCH(Nelson, 1991), HAR-RV(Corsi, 2009) 모형들은 시계열의 자기회귀적 구조에 의존하는 선형 또는 단순 비선형 파라메트릭 모형이다. 이러한 모형들은 정상성(Stationarity) 가정에 취약하며, 극심한 시장 체제 변화(Regime Shift) 시 파라미터가 급격히 왜곡되는 한계를 지닌다. 

최근 자연어 처리(NLP) 및 컴퓨터 비전(CV) 분야를 혁신한 대규모 사전학습 트랜스포머 아키텍처는 시계열 영역으로 확장되어 **시계열 파운데이션 모델(Time Series Foundation Models, TSFM)**로 진화하였다. TSFM은 수십억 개의 다양한 도메인 시계열 데이터를 사전학습(Pre-training)함으로써, 미지의 금융 시계열에 대해서도 파인튜닝 없이 즉각적으로 뛰어난 일반화 성능을 발휘하는 제로샷(Zero-shot) 확률분포 예측 능력을 보유하고 있다.

```
+----------------------------------------------------------------------------------------------------+
|                                     TSFM Architecture Overview                                     |
+----------------------------------------------------------------------------------------------------+
|                                                                                                    |
|  [Input Time Series] : X = (x_1, x_2, ..., x_L)                                                    |
|         │                                                                                          |
|         ▼                                                                                          |
|  [Instance Normalization] : RevIN (Mitigating Non-stationarity)                                    |
|         │                                                                                          |
|         ▼                                                                                          |
|  [Patching / Tokenization] : Length P, Stride S  ──>  Token Sequence: (x_p^(1), ..., x_p^(N_p))    |
|         │                                                                                          |
|         ├────────────────────────────────┬────────────────────────────────┐                        |
|         ▼                                ▼                                ▼                        |
|  [PatchTST Framework]           [Chronos Framework]              [TimesFM Framework]              |
|  - Channel-Independent          - Uniform/Quantile Bins          - Decoder-only Transformer        |
|  - Linear Patch Projection      - Tokenization: c_t = Q(x_t)     - Input Patch 32 / Output 128     |
|  - O(N_p^2) Self-Attention      - Autoregressive T5 Backbone     - Long-context Attention          |
|  - Masked Pre-training          - Cross-Entropy Softmax          - Direct Quantile / Pinball Loss  |
|         │                                │                                │                        |
|         └────────────────────────────────┼────────────────────────────────┘                        |
|                                          ▼                                                         |
|  [Probabilistic Forecast Output] : P(X_{t+1:t+H} | X_{1:t})                                        |
|  ──> Ex-ante Conditional Mean (mu_{t+1}) & Conditional Variance (sigma^2_{t+1})                   |
+----------------------------------------------------------------------------------------------------+
```

### 2.3.1. 시계열 데이터의 토큰화와 패치(Patching) 메커니즘

자연어 처리에서 텍스트는 명확한 의미 단위를 갖는 형태소나 서브워드(Subword) 단위로 쉽게 토큰화(Tokenization)될 수 있다. 반면 연속적인 금융 시계열 데이터는 단일 시점 관측치 \(x_t \in \mathbb{R}\) 그 자체로는 어떠한 의미론적 맥락도 제공하지 못하며, 신호대잡음비(SNR)가 극히 낮다는 치명적 특성을 갖는다. 만약 시계열의 각 시점을 단일 토큰으로 트랜스포머에 입력할 경우, 셀프 어텐션(Self-Attention)의 계산 복잡도는 시계열 길이 \(L\)에 대해 \(\mathcal{O}(L^2)\)로 폭증하며, 인접 시점 간의 국소적 동역학(Local Dynamics)을 포착하지 못하고 고주파 잡음에 심각하게 과적합된다.

PatchTST(Nie et al., 2023)는 컴퓨터 비전의 Vision Transformer(ViT) 개념을 시계열로 이식하여 **패치화(Patching)** 메커니즘을 정식화하였다. 길이 \(L\)의 단변량 시계열 시퀀스 \(X = (x_1, x_2, \dots, x_L) \in \mathbb{R}^L\)가 주어졌을 때, 패치 길이(Patch Length)를 \(P\), 인접 패치 간 이동 간격인 스트라이드(Stride)를 \(S\)로 설정한다. 이때 생성되는 패치의 총 개수 \(N_p\)는 다음과 같다 (단, 경계 처리를 위해 말단에 \(S\)만큼 패딩을 적용할 수 있다):

$$N_p = \left\lfloor \frac{L - P}{S} \right\rfloor + 1 \quad \text{또는 패딩 포함 시 } N_p = \left\lfloor \frac{L - P}{S} \right\rfloor + 2$$

각각의 \(i\)번째 패치 벡터 \(x_p^{(i)} \in \mathbb{R}^P\) (\(i = 1, \dots, N_p\))는 시계열의 국소적 추세와 변동성 프로파일을 담고 있는 하위 연속 시퀀스이다. 이 패치 벡터는 학습 가능한 선형 투영 행렬(Linear Projection Matrix) \(W_p \in \mathbb{R}^{P \times D}\)와 가산적 위치 임베딩(Positional Embedding) \(W_{pos} \in \mathbb{R}^{N_p \times D}\)을 통해 \(D\)차원의 잠재 토큰 벡터 \(h_0^{(i)}\)로 매핑된다:

$$h_0^{(i)} = x_p^{(i)} W_p + W_{pos}^{(i)}, \quad i = 1, \dots, N_p \quad \text{--- (식 18)}$$

이러한 패치 토큰화는 세 가지 결정적인 수학적·계량적 우월성을 제공한다:
1. **계산 복잡도의 획기적 단축**: 어텐션 맵의 크기가 \(\mathcal{O}(L^2)\)에서 \(\mathcal{O}(N_p^2) \approx \mathcal{O}\left((L/S)^2\right)\)로 축소된다. 예를 들어 \(P=16, S=8\)인 경우 어텐션 연산량은 약 \(1/64\)로 급감하여, 장기 과거 맥락(Look-back Window)을 극도로 길게 확장할 수 있다.
2. **국소적 의미 맥락(Local Semantic Context) 보존**: 단일 수치가 아닌 연속된 \(P\)개 시점의 파형 전체를 하나의 토큰으로 취급함으로써 모멘텀, 국소 변동성 터짐, 기하학적 형상 등의 의미론적 특징이 보존된다.
3. **채널 독립성(Channel Independence, CI)의 강건성**: 다변량 시계열 \(X \in \mathbb{R}^{L \times M}\)을 처리할 때, 서로 다른 자산 간의 어텐션을 직접 연산(Channel Mixing)하는 대신 모든 채널이 트랜스포머의 가중치를 공유하되 독립적으로 입력되는 CI 설계를 적용한다. 이는 금융 데이터의 시변 교차상관 노이즈에 대한 과적합을 차단하고 모델의 파라미터 일반화 성능을 극대화한다.

### 2.3.2. Chronos: 시계열의 언어화와 이산 확률분포 생성

Amazon Research가 제안한 Chronos(Ansari et al., 2024)는 시계열을 자연어와 완벽히 동일한 이산 토큰 시퀀스로 변환하여 대규모 사전학습 언어 모델(T5, GPT 등)의 생성 메커니즘을 직접 활용하는 파운데이션 아키텍처이다.

Chronos의 핵심은 **스케일링(Mean-scaling)과 양자화(Quantization)** 파이프라인에 있다. 임의의 시계열 시퀀스 \(X = (x_1, \dots, x_L)\)가 입력되면, 먼저 스케일 불변성을 확보하기 위해 시퀀스의 절댓값 평균으로 정규화를 수행한다:

$$\tilde{x}_t = \frac{x_t}{\frac{1}{L}\sum_{\tau=1}^L |x_\tau| + \epsilon}$$

정규화된 연속형 실수 \(\tilde{x}_t \in \mathbb{R}\)는 미리 정의된 \(B\)개의 이산 빈(Bin) 경계 \(\{q_0 = -\infty, q_1, q_2, \dots, q_{B-1}, q_B = \infty\}\)를 기준으로 양자화 함수 \(Q(\cdot)\)를 통해 어휘 사전(Vocabulary)의 토큰 ID \(c_t \in \{1, 2, \dots, B\}\)로 매핑된다:

$$c_t = Q(\tilde{x}_t) = k \quad \iff \quad q_{k-1} \le \tilde{x}_t < q_k \quad \text{--- (식 19)}$$

이로써 시계열 예측 문제는 언어 모델의 표준적인 **자기회귀적 다음 토큰 예측(Autoregressive Next-Token Prediction)** 문제로 완전히 치환된다. 과거 토큰 시퀀스 \(c_{1:L}\)이 주어졌을 때, 미래 지평 \(H\)까지의 토큰 시퀀스 \(c_{L+1:L+H}\)에 대한 결합확률분포는 연쇄 법칙에 의해 전개된다:

$$P(c_{L+1:L+H} | c_{1:L}) = \prod_{h=1}^H P(c_{L+h} | c_{1:L+h-1}) \quad \text{--- (식 20)}$$

모델의 최종 출력층은 소프트맥스(Softmax)를 통해 \(B\)개 빈에 대한 이산 확률분포 벡터 \(p_{t+h} = (p_{t+h, 1}, \dots, p_{t+h, B}) \in \Delta^{B-1}\)를 출력한다:

$$p_{t+h, k} = P(c_{t+h} = k | c_{1:t+h-1}) = \frac{\exp(z_{t+h, k})}{\sum_{j=1}^B \exp(z_{t+h, j})}$$

Chronos가 출력하는 소프트맥스 확률분포는 사전에 특정 모수적 분포(가우시안, t-분포 등)를 강제하지 않는 **비모수적 전밀도 사후분포(Non-parametric Full Posterior Distribution)**이다. 각 빈의 대표값을 \(d_k = \frac{q_{k-1} + q_k}{2}\)라 할 때, 역스케일링을 거쳐 복원된 차기 시점의 조건부 기대수익률 \(\hat{\mu}_{t+1|t}\)과 조건부 변동성 \(\hat{\sigma}^2_{t+1|t}\)은 이산분포의 1차 및 2차 중심적률로부터 직접 도출된다:

$$\hat{\mu}_{t+1|t} = \mathbb{E}[\tilde{X}_{t+1} | \mathcal{F}_t] \cdot \left( \frac{1}{L}\sum_{\tau=1}^L |x_\tau| \right) = \left( \sum_{k=1}^B d_k \cdot p_{t+1, k} \right) \cdot \left( \frac{1}{L}\sum_{\tau=1}^L |x_\tau| \right) \quad \text{--- (식 21)}$$

$$\hat{\sigma}^2_{t+1|t} = \mathbb{V}ar[\tilde{X}_{t+1} | \mathcal{F}_t] \cdot \left( \frac{1}{L}\sum_{\tau=1}^L |x_\tau| \right)^2 = \left( \sum_{k=1}^B (d_k - \mathbb{E}[\tilde{X}_{t+1}|\mathcal{F}_t])^2 \cdot p_{t+1, k} \right) \cdot \left( \frac{1}{L}\sum_{\tau=1}^L |x_\tau| \right)^2 \quad \text{--- (식 22)}$$

이러한 특성은 금융 시장의 팻테일(Fat-tail)이나 다봉성(Multimodality)을 어떠한 정보 왜곡 없이 고스란히 포착하여 이토 보정 목적함수의 사전적 입력치로 직결시킬 수 있는 독보적 강점을 제공한다.

### 2.3.3. TimesFM 및 연속적 제로샷(Zero-shot) 확률분포 예측

Google Research가 개발한 TimesFM(Time-series Foundation Model; Das et al., 2024)은 양자화 방식 대신 연속형 실수 공간에서 직접 작동하는 디코더 전용(Decoder-only) 패치 트랜스포머 아키텍처이다.

TimesFM의 독창적인 구조적 특징은 **비대칭 패치 프레임워크(Asymmetric Patching)**에 있다. 입력 시계열에 대해서는 상대적으로 조밀한 입력 패치 길이 \(P_{in} = 32\)를 사용하여 세밀한 패턴을 포착하되, 미래 예측을 출력할 때는 확장된 출력 패치 길이 \(P_{out} = 128\)을 한 번의 피드포워드 연산으로 생성한다. 이는 자기회귀적 반복 호출에 따른 오차 누적(Error Accumulation) 현상을 원천 차단한다.

확률적 예측을 위해 TimesFM은 다중 분위수 손실(Multi-Quantile Pinball Loss) 또는 비대칭 라플라스/Student-t 분포의 파라미터를 출력 헤드에서 직접 학습한다. 분위수 지수 \(\tau \in (0, 1)\)에 대한 핀볼 손실함수는 다음과 같다:

$$\mathcal{L}_{pinball}(y, \hat{y}_\tau) = \max\left( \tau (y - \hat{y}_\tau), (\tau - 1)(y - \hat{y}_\tau) \right) \quad \text{--- (식 23)}$$

모델이 복수의 분위수 \(\tau \in \{0.1, 0.2, \dots, 0.9\}\)에 대해 \(\hat{y}_\tau\)를 동시에 예측함으로써, 사후 예측 구간(Prediction Interval)의 상단과 하단을 형성할 수 있다. 특히 꼬리 변동성의 정량화를 위해 사분위수 범위(Interquartile Range, IQR) 또는 90% 신뢰구간 폭을 통해 조건부 표준편차를 로버스트하게 추정한다:

$$\hat{\sigma}_{t+1|t} \approx \frac{\hat{y}_{0.841}(t+1) - \hat{y}_{0.159}(t+1)}{2}$$

TimesFM과 Chronos를 아우르는 TSFM의 가장 거대한 이론적 의의는 **수십억 시점의 다도메인 합성 및 실세계 시계열 데이터로부터 시계열 생성 과정의 범용 기저 작용소(Universal Basis Operators)를 학습했다는 점**이다. 이에 따라 특정 자산의 국소적 과거 데이터에 갇히지 않고, 역사상 경험하지 못한 시장 변동성의 발산 징후를 사전적으로 감지하여 변동성 항력 완화 알고리즘에 안정적으로 공급할 수 있다.

---

## 2.4. 비지도 딥러닝 이상탐지(Anomaly Detection) 이론과 꼬리위험 포착

TSFM이 정상적 시장 동역학 및 완만한 변동성 클러스터링을 정밀하게 예측한다 하더라도, 2020년 3월 팬데믹 쇼크나 2008년 리먼 브라더스 파산과 같은 극단적인 시스템적 위기(Systemic Crisis / Black Swan) 국면에서는 금융 자산 간의 결합 확률분포 자체가 순간적으로 파괴된다. 이러한 꼬리위험(Tail Risk) 하에서는 모든 위험자산 간의 상관계수가 1로 수렴하면서 분산투자의 리밸런싱 보너스가 무력화되고 변동성 항력이 폭발하게 된다.

따라서 포트폴리오의 생존을 보장하기 위해서는 정상적인 확률분포의 예측 범위를 벗어나는 구조적 충격을 밀리초 단위로 감지하여 위험자산 비중을 강제 축소하는 독립적인 **세이프가드(Safeguard)**가 반드시 병행되어야 한다. 본 연구는 제조업 및 고신뢰성 비파괴검사(NDE)에서 극미한 물리적 균열을 탐지하는 최첨단 비지도 딥러닝 이상탐지 메커니즘을 금융 거시 시스템에 이식한다.

### 2.4.1. 금융 시계열의 팻테일(Fat-tail) 현상과 렙토쿠르틱(Leptokurtic) 특성

고전 정규분포 가설 하에서 수익률이 평균으로부터 4표준편차(\(4\sigma\)) 이상 벗어나는 사건의 발생 확률은 약 \(0.0063\%\)(약 63년에 1회)에 불과하다. 그러나 실제 글로벌 금융시장에서 \(4\sigma\) 이상의 일일 폭락 사건은 수년에 한 번꼴로 빈번히 관측된다. 

실제 금융 수익률의 확률밀도함수 \(f(x)\)는 정규분포에 비해 중심부가 뾰족하고 꼬리가 극도로 두터운 **렙토쿠르틱(Leptokurtic)** 특성을 지닌다. 극단값 이론(Extreme Value Theory, EVT)에 따르면, 팻테일 분포의 우측/좌측 꼬리는 파레토 멱법칙(Power Law)을 따른다:

$$\mathbb{P}(|X| > x) \sim L(x) x^{-\alpha}, \quad \text{as } x \to \infty \quad (\alpha > 0)$$

여기서 꼬리 지수(Tail Index) \(\alpha\)가 작을수록 꼬리가 두터워지며, \(\alpha \le 4\)인 경우 첨도(Kurtosis)가 무한대로 발산한다. 시스템적 위기 국면에서 발생하는 이러한 극단적 잔차는 전통적 선형 필터나 단순 통계적 신뢰구간을 완전히 무력화하므로, 다차원 거시 지표들의 비선형적 공움직임(Co-movement)을 비지도 방식으로 감시하는 딥러닝 잠재 공간 모델이 요구된다.

### 2.4.2. 오토인코더(Autoencoder)와 재구성 오차(Reconstruction Error) 메커니즘

비지도 이상탐지의 핵심 가설은 **매니폴드 가설(Manifold Hypothesis)**이다. 즉, 고차원 금융 거시 상태 공간 \(\mathbb{R}^D\) (단기/장기 국채금리, 신용스프레드, 환율, VIX, 원자재 가격, 은행간 유동성 지표 등)에서 시장이 정상적으로 작동하는 대다수의 데이터 포인트들은 실제로는 훨씬 낮은 내재적 차원을 갖는 저차원 부분 다양체(Low-dimensional Submanifold) \(\mathcal{M} \subset \mathbb{R}^D\)의 근방에 밀집하여 분포한다는 원리이다.

오토인코더(Autoencoder, AE)는 이러한 정상 다양체를 스스로 학습하기 위해 설계된 병목 신경망 구조이다. 인코더 신경망 \(f_\theta: \mathbb{R}^D \to \mathbb{R}^d\)는 고차원 입력 벡터 \(z_t \in \mathbb{R}^D\)를 저차원 잠재 공간(Bottleneck Latent Space) \(h_t \in \mathbb{R}^d\) (\(d \ll D\))로 압축하며, 디코더 신경망 \(g_\phi: \mathbb{R}^d \to \mathbb{R}^D\)는 잠재 벡터로부터 원래의 입력을 복원한다:

$$h_t = f_\theta(z_t), \quad \hat{z}_t = g_\phi(h_t) = g_\phi(f_\theta(z_t))$$

네트워크의 파라미터 \(\{\theta, \phi\}\)는 과거 정상 시장 국면으로 구성된 훈련 데이터셋 \(\mathcal{D}_{normal}\)에 대해 평균제곱오차(MSE)를 최소화하도록 학습된다:

$$\min_{\theta, \phi} \quad \frac{1}{|\mathcal{D}_{normal}|} \sum_{t \in \mathcal{D}_{normal}} \| z_t - g_\phi(f_\theta(z_t)) \|_2^2 \quad \text{--- (식 24)}$$

정보 병목(Information Bottleneck) 제약으로 인해 오토인코더는 정상 시장에서 공통적으로 나타나는 변수 간의 강한 비선형 상관관계 패턴만을 보존하도록 압축 메커니즘을 형성한다.

새로운 시점 \(t\)의 시장 관측치 \(z_t\)가 입력되었을 때, **재구성 오차(Reconstruction Error)** 기반의 이상 점수 \(s_t^{recon}\)은 다음과 같이 정의된다:

$$s_t^{recon} = \| z_t - \hat{z}_t \|_2^2 = \sum_{j=1}^D (z_{t,j} - \hat{z}_{t,j})^2 \quad \text{--- (식 25)}$$

만약 시장에 전례 없는 유동성 경색이나 시스템적 뱅크런 등 구조적 이상 징후가 발생하면, 입력 벡터 \(z_t\)는 학습된 정상 다양체 \(\mathcal{M}\)에서 크게 이탈하게 된다. 디코더 \(g_\phi\)는 정상 영역 밖의 잠재 벡터를 올바르게 복원할 수 없으므로, 재구성 오차 \(s_t^{recon}\)은 급격히 폭발하게 된다.

### 2.4.3. 마할라노비스 거리(Mahalanobis Distance)와 잠재 공간 꼬리위험 정량화

재구성 오차가 관측 공간(Input Space) 상에서의 복원 실패를 측정한다면, 압축된 저차원 잠재 공간(Latent Space) 내부에서도 데이터 포인트의 통계적 이탈도를 독립적으로 감시해야 한다. 인코더를 통과한 잠재 벡터 \(h_t = f_\theta(z_t) \in \mathbb{R}^d\)는 고차원 노이즈가 제거된 거시 경제의 핵심 상태 변수이다.

단순 유클리드 거리는 잠재 변수 간의 분산 차이와 잔여 상관관계를 반영하지 못하므로, 정상 상태 데이터들의 결합 공분산을 고려하는 **마할라노비스 거리(Mahalanobis Distance)**를 도입한다. 훈련 셋의 잠재 벡터 집합 \(\{h_\tau\}_{\tau \in \mathcal{D}_{normal}}\)에 대한 표본 평균 벡터 \(\mu_h\)와 표본 공분산 행렬 \(\Sigma_h\)를 계산한다:

$$\mu_h = \frac{1}{N_{norm}} \sum_{\tau=1}^{N_{norm}} h_\tau, \quad \Sigma_h = \frac{1}{N_{norm}-1} \sum_{\tau=1}^{N_{norm}} (h_\tau - \mu_h)(h_\tau - \mu_h)^T \quad \text{--- (식 26)}$$

시점 \(t\)의 잠재 벡터 \(h_t\)에 대한 마할라노비스 이상 점수 \(s_t^{maha}\)는 다음과 같이 정식화된다:

$$s_t^{maha} = \sqrt{ (h_t - \mu_h)^T \Sigma_h^{-1} (h_t - \mu_h) } \quad \text{--- (식 27)}$$

만약 잠재 공간의 차원 \(d\)에 비해 정상 표본 수가 충분치 못하여 공분산 행렬의 역행렬 연산이 불안정할 경우, 르두아-울프 수축 추정량(Ledoit-Wolf Shrinkage Estimator; Ledoit & Wolf, 2004)을 적용하여 정칙성(Well-conditionedness)을 보장한다:

$$\Sigma_h^{shrunk} = (1 - \rho^*) \Sigma_h + \rho^* \left( \frac{\text{Tr}(\Sigma_h)}{d} \right) I_d$$

최종적으로 본 연구는 관측 공간의 재구성 오차와 잠재 공간의 마할라노비스 거리를 z-score 표준화하여 결합한 **하이브리드 이상 점수(Hybrid Anomaly Score, \(S_t\))**를 산출한다:

$$S_t = \alpha \cdot \frac{s_t^{recon} - \bar{s}^{recon}}{\sigma_{s}^{recon}} + (1 - \alpha) \cdot \frac{s_t^{maha} - \bar{s}^{maha}}{\sigma_{s}^{maha}} \quad \text{--- (식 28)}$$

여기서 \(\alpha \in [0, 1]\)는 가중치 파라미터이다. 산출된 종합 이상 점수 \(S_t\)가 사전 설정된 임계치(극단값 이론의 Peak-Over-Threshold 기법 적용)를 상향 돌파할 경우, 포트폴리오 최적화 엔진은 자산 간 상관관계 붕괴 및 극단적 변동성 항력 폭증을 회피하기 위해 위험자산 가중치를 강제로 현금성 자산(무위험 채권)으로 청산시키는 안전 차단막을 기계적으로 가동하게 된다.

---

## 2.5. 선행 연구 검토 및 본 연구의 이론적 차별성

### 2.5.1. 전통적 동적 자산배분 및 변동성 제어(Volatility Targeting) 연구

자산배분 이론의 기원은 마코위츠(Markowitz, 1952)의 평균-분산 최적화(MVO)로 거슬러 올라간다. 그러나 MVO의 단일 기간 정적 프레임워크는 다기간 투자자의 효용 극대화와 괴리된다는 비판에 직면하였다. 로버트 머튼(Merton, 1969, 1971)은 연속시간 확률 제어 이론(Stochastic Optimal Control)과 해밀턴-자코비-벨만(HJB) 방정식을 통해 상대적 위험회피도(CRRA)를 가진 투자자의 최적 소비 및 동적 포트폴리오 규칙을 수학적으로 확립하였다.

실무 및 실증 금융에서는 변동성의 시간 가변적 군집성(Volatility Clustering)에 대응하기 위해 포트폴리오의 전체 위험 노출도를 일정하게 통제하는 **변동성 타겟팅(Volatility Targeting)** 전략이 광범위하게 연구되었다(Moreira & Muir, 2017). 변동성 타겟팅은 차기 기간의 예상 변동성 \(\hat{\sigma}_t\)에 반비례하도록 위험자산 비중을 동적으로 조절한다:

$$w_t^{VT} = \min\left( \frac{\sigma_{target}}{\hat{\sigma}_t}, c_{max} \right) \quad \text{--- (식 29)}$$

Moreira와 Muir(2017)는 주식 시장에서 변동성이 높아질 때 기대수익률이 변동성 증가폭만큼 비례하여 상승하지 않기 때문에, 고변동성 국면에서 비중을 축소하고 저변동성 국면에서 비중을 확대하는 전략이 전통적 매수-보유(Buy-and-Hold) 대비 샤프 비율을 획기적으로 개선함을 실증하였다. 

한편, 변동성 항력 그 자체를 완화하려는 연구도 진행되었다. Booth와 Fama(1992)는 분산투자가 제공하는 초과 수익이 자산 간 공분산의 절감에 의해 발생하는 다각화 수익률(Diversification Return)임을 정량화하였고, Hallerbach(2014) 및 Bouchey et al.(2012)은 정기적인 재균형(Rebalancing)이 변동성 항력을 회피하여 복리 성장을 촉진하는 메커니즘을 분석하였다. 그러나 이들 선행연구는 모두 변동성 예측을 위해 단순 과거 실현 변동성(Rolling Historical Volatility)이나 전통적 GARCH 계열 모형에 의존하였다. 이로 인해 충격 발생 시점의 심각한 후행성(Lagging)을 피하지 못했으며, 정규분포 가설이 붕괴되는 꼬리위험 국면에서 치명적인 하방 드로다운을 초래하는 근본적 취약점을 노출하였다.

### 2.5.2. 머신러닝·딥러닝 기반 금융 시계열 예측 연구의 흐름과 한계

2010년대 이후 딥러닝 기술의 폭발적 발전과 함께 금융 시계열 예측 연구는 순환신경망(RNN), LSTM(Hochreiter & Schmidhuber, 1997), GRU(Cho et al., 2014)를 거쳐 트랜스포머(Vaswani et al., 2017) 기반 모형(Informer, Autoformer, FEDformer 등)으로 빠르게 전환되었다. 

그러나 대다수의 기존 머신러닝 기반 퀀트 투자 연구들은 다음과 같은 세 가지 구조적 병폐를 노출하며 학술적·실무적 한계에 부딪혔다:

1. **점 추정(Point Estimation) 및 방향성 예측 편향**: 선행 연구들은 내일의 주가 등락 부호(Sign)를 맞추는 이진 분류(Binary Classification)나 단일 점 추정치 \(\hat{y}_{t+1}\)의 MSE를 최소화하는 데 집착하였다. 그러나 금융 시장은 신호대잡음비(SNR)가 극도로 낮아 점 추정의 신뢰도가 매우 떨어지며, 방향성을 55% 맞춘다 하더라도 꼬리위험 국면에서의 단 한 번의 대폭락 오판으로 전체 포트폴리오가 파멸하는 위험을 제어하지 못했다.
2. **과적합(Overfitting)과 일반화 실패**: 복잡한 딥러닝 모델을 특정 기간의 개별 주식 시계열에 직접 지도학습(Supervised Learning)시킴으로써, 금융 시장의 잡음과 특이적 패턴(Spurious Correlation)을 암기하여 샘플 외(Out-of-sample) 구간에서 성능이 급격히 붕괴하는 현상이 반복되었다.
3. **금융경제학적 목적함수와의 단절**: 딥러닝 모델의 손실함수(MSE, MAE, Cross-Entropy)는 투자자의 궁극적 목표인 다기간 복리 성장률 극대화나 변동성 항력 억제와 수학적으로 연결되어 있지 않은 블랙박스(Black-box) 상태로 방치되었다.

### 2.5.3. 본 연구의 이론적 위치 및 통합 프레임워크의 독창성

본 연구는 이러한 기존 연구들의 파편화된 한계를 근본적으로 극복하기 위해, **연속시간 수리금융학의 엄밀성(이토 보정)**, **최신 시계열 파운데이션 모델의 비모수적 확률 예측력(TSFM)**, 그리고 **고신뢰성 산업 AI의 결함 탐지 철학(비지도 꼬리위험 세이프가드)**을 유기적으로 융합하는 차세대 지능형 자산배분 프레임워크를 제안한다.

<br>

**[표 2-1] 기존 선행연구와 본 연구 프레임워크의 비교**

| 비교 차원 | 전통적 MVO 및 자산배분 | 변동성 타겟팅 (VT) 연구 | 기존 딥러닝 퀀트 연구 | 본 연구 제안 프레임워크 (TSFM-VolDrag) |
| :--- | :--- | :--- | :--- | :--- |
| **핵심 목적함수** | 단일 기간 산술 평균-분산 효용 | 목표 변동성 대비 과거 실현 분산 제어 | 지도학습 손실함수 (MSE, Cross-entropy) | **이토 보정 다기간 연속 복리 성장률 (\(g_p\)) 극대화** |
| **변동성 항력 처리** | 무시 (산술평균의 함정 노출) | 사후적 간접 완화 (후행적 노출도 축소) | 이론적 고려 전무 (블랙박스 접근) | **목적함수 내 \(\frac{1}{2}w^T\Sigma w\) 항력 명시적 페널티화** |
| **변동성 예측 기법** | 과거 표본 분산 (Rolling Window) | GARCH, HAR-RV 등 파라메트릭 모형 | 개별 종목 훈련 LSTM / CNN 점 추정 | **대규모 사전학습 TSFM 제로샷 확률분포 예측** |
| **예측 출력 형태** | 스칼라 고정값 | 조건부 분산 점 추정치 | 스칼라 점 추정치 / 상승 확률 | **전밀도 사후 확률분포 (Full Posterior Density)** |
| **꼬리위험 대응** | 정규분포 가정 (무방비 노출) | 변동성 급등 후 사후적 비중 축소 | 드롭아웃 / 정규화 의존 (블랙스완 취약) | **오토인코더 재구성 오차 & 마할라노비스 세이프가드** |
| **과적합 통제력** | 낮음 (공분산 추정 오차 극대화) | 보통 (파라미터 불안정성 존재) | 매우 취약 (금융 잡음 암기 현상) | **파운데이션 제로샷 일반화 + 비지도 매니폴드 감시** |

<br>

본 연구가 정립하는 통합 최적화의 이론적 골격은 다음과 같은 동적 제어 문제로 완결된다. 시점 \(t\)에서 TSFM(Chronos, TimesFM)이 산출한 차기 기대수익률 벡터 \(\hat{\mu}_{t+1}\)과 조건부 공분산 행렬 \(\hat{\Sigma}_{t+1}\), 그리고 비지도 이상탐지 엔진이 산출한 종합 시스템 충격 점수 \(S_t\)가 결합된 통합 목적함수를 구성한다:

$$\max_{w_t} \quad \mathcal{J}(w_t) = \left[ w_t^T \hat{\mu}_{t+1} - \frac{1}{2} w_t^T \hat{\Sigma}_{t+1} w_t \right] \cdot \left( 1 - \Phi(S_t) \right) \quad \text{--- (식 30)}$$

$$\text{s.t.} \quad \mathbf{1}^T w_t = 1, \quad 0 \le w_{i,t} \le w_{max}, \quad \forall i$$

여기서 \(\Phi(\cdot): \mathbb{R} \to [0, 1]\)는 이상 점수 \(S_t\)가 극단적 임계치를 넘을 때 위험자산의 허용 한도를 0(현금 100% 대피)으로 매끄럽게 수축시키는 세이프가드 감쇠 함수(Safeguard Attenuation Function)이다.

결론적으로 본 연구의 이론적 위치는 단순한 인공지능 알고리즘의 적용에 머무르지 않는다. 노벨경제학상에 빛나는 연속시간 수리금융학의 정통 정리(이토 보조정리)를 확고한 나침반으로 삼고, 최첨단 시계열 파운데이션 모델과 산업 안전 AI의 이상탐지 이론을 결합함으로써, 학술적 엄밀성과 실무적 생존성을 동시에 달성하는 혁신적 자산배분 방법론의 이론적 초석을 놓는다.
