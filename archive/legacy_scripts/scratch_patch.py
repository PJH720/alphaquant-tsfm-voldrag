import re
import sys

with open("/Users/pj/.gemini/antigravity/brain/686ad25e-8fd4-4c0a-8671-1c0c91fc359a/scratch/backup_29p.md", "r", encoding="utf-8") as f:
    text = f.read()

print("Original length:", len(text))

# 1. 10-Year Compounding Wealth Loss correction in Table 2
table2_old = "**10년 복리 손실액 (100억 운용 기준)**"
if table2_old in text:
    print("Found Table 2 wealth loss row")
    # Replace the whole row in multiline table
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if "**10년 복리 손실액 (100억 운용 기준)**" in line:
            print("Old line:", line)
            lines[i] = "  **10년 복리 손실액 (100억 운용 기준)**           **-13.39 억 원** **-17.79 억 원** **-20.05 억 원** **-10.17 억 원** **+9.88 억 원 보전**"
            print("New line:", lines[i])
    text = "\n".join(lines)

# 2. Textual mentions of wealth preservation
text = text.replace("**-7.1 억 원**", "**-10.17 억 원**")
text = text.replace("-7.1 억 원", "-10.17 억 원")
text = text.replace("-7.1 억", "-10.17 억 원")
text = text.replace("**13.8억 원 이상의 실질", "**9.88 억 원 이상의 실질")
text = text.replace("13.8억 원", "9.88 억 원")
text = text.replace("13.8 억 원", "9.88 억 원")

# 3. Safe haven vector dimension
text = text.replace(r"$\mathbf{w}_{\text{safe}} = (0,\ldots,0,1)^{T}$", r"무위험 현금 가중치 벡터 $\mathbf{w}_{\text{safe}} = (0, 0, 0, 0, 0, 0, 1)^T$")
text = text.replace(r"$\mathbf{w}_{\text{safe}} = (0, \ldots, 0, 1)^T$", r"무위험 현금 가중치 벡터 $\mathbf{w}_{\text{safe}} = (0, 0, 0, 0, 0, 0, 1)^T$")

# 4. Total Return (TR) enhancement in Section 3.1.1
tr_needle = "모든 가격 계열은 주식분할 및 분배금을 반영한 수정주가(Adjusted Close)를 적용하여 일별 연속 복리 로그수익률"
tr_replacement = "본 연구의 백테스팅은 단순 가격 수익률(Price Return)이 아닌 배당 및 분배금 재투자를 가정한 총수익률(Total Return, TR) 기준의 수정주가(Adjusted Close)를 전면 적용하였다. ETF 분배금의 현금 배당 및 주식 배당을 당일 종가로 전액 재투자하는 계정 모델을 채택함으로써, 장기 복리 계산 시 배당 누락으로 인한 수익률 과소평가 및 왜곡(Dividend Omission Bias)을 원천 차단하였다. 모든 가격 계열은 주식분할 및 분배금을 반영한 수정주가를 적용하여 일별 연속 복리 로그수익률"

if tr_needle in text:
    text = text.replace(tr_needle, tr_replacement)
    print("Total Return (TR) successfully inserted!")
else:
    print("Warning: tr_needle not found!")

# 5. RevIN F_t-measurability and Look-ahead bias in Section 3.2.1
revin_needle = "과거 $W=504$일(2개년) 롤링 윈도우를 활용하여 시점 $t$의 정보만을 기반으로 미래를 순차 예측함으로써 미래 참조 편향(Look-ahead Bias)을 원천 차단하였다."
if revin_needle not in text:
    # Check alternate escaping
    revin_needle = "과거 $W = 504$일(2개년) 롤링 윈도우를 활용하여 시점 $t$의 정보만을 기반으로 미래를 순차 예측함으로써 미래 참조 편향(Look-ahead Bias)을 원천 차단하였다."

revin_replacement = """가역적 인스턴스 정규화(RevIN)의 통계량은 시점 $t$의 정보집합 $\\mathcal{F}_t$에 대해서만 다음과 같이 엄밀히 산출된다:

$$\\mu_{\\mathbf{x}, t} = \\frac{1}{L} \\sum_{k=0}^{L-1} x_{t-k}, \\quad \\sigma_{\\mathbf{x}, t}^2 = \\frac{1}{L} \\sum_{k=0}^{L-1} (x_{t-k} - \\mu_{\\mathbf{x}, t})^2 \\qquad (15)$$

$$\\tilde{x}_{t-k} = \\frac{x_{t-k} - \\mu_{\\mathbf{x}, t}}{\\sqrt{\\sigma_{\\mathbf{x}, t}^2 + \\epsilon}}, \\quad k=0, \\dots, L-1 \\qquad (16)$$

RevIN의 인스턴스 정규화 통계량($\\mu_{\\mathbf{x}, t}, \\sigma_{\\mathbf{x}, t}$)은 오직 시점 $t$까지의 역사적 정보집합 $\\mathcal{F}_t$에만 의존하여 산출되며($\\mathcal{F}_t$-measurable), 패칭 및 트랜스포머 인과적 어텐션(Causal Attention) 연산 전반에서 미래 시점($\\tau > t$)의 정보가 스케일링이나 롤링 윈도우 경계선에서 누수되는 미래 참조 편향(Look-ahead Bias / Data Leakage)을 수학적으로 원천 차단하였다. 과거 $W=504$일(2개년) 롤링 윈도우를 활용하여 시점 $t$의 정보만을 기반으로 미래를 순차 예측한다."""

# Find where RevIN is described in 3.2.1
if "가역적 인스턴스 정규화(RevIN)" in text:
    print("Found RevIN in text")
    # Let's locate the paragraph and enhance it
    idx = text.find("가역적 인스턴스 정규화(RevIN)")
    # Let's see the context
    print(text[idx-50:idx+300])

