# 이토 보조정리 × TSFM 동적 자산배분: 변동성 항력(Volatility Drag) 제어 프레임워크

**2026 연합 경제 학술제** (서강대 · 성균관대 · 이화여대) 출품 소논문 저장소
팀 **알파퀀트** (서강대학교 경제학과): 박재현 (대표), 강명서 (공동연구 · 본선 발표)

> 『이토 보조정리와 시계열 파운데이션 모델(TSFM)을 결합한 동적 자산배분 및 변동성 항력(Volatility Drag) 제어 프레임워크: 산업 비파괴검사 기반 비지도 꼬리위험 세이프가드를 중심으로』

## 연구 개요

장기 복리 성과는 산술평균 μ가 아니라 기하성장률 `g = μ − ½σ²`가 지배한다. 정적 평균-분산 최적화(MVO)는 분산이 성장률을 잠식하는 **변동성 항력 ½σ²**을 직접 통제하지 못한다. 본 연구는 다음 세 층을 결합한 프레임워크를 제안한다.

| 층 | 내용 |
|---|---|
| 목적함수 | 이토 보조정리로 유도한 켈리(λ=1) 기하성장률 극대화 + Rockafellar–Uryasev CVaR(95%) 제약 볼록 QP |
| 사전적 모멘트 | 시계열 파운데이션 모델(Chronos, PatchTST) + RevIN, Ledoit-Wolf 축소 및 PSD 보정 공분산 |
| 꼬리위험 세이프가드 | 비파괴검사(NDE) 결함 탐지 개념을 차용한 오토인코더 재구성 오차 기반 현금 전환 |

분석 대상은 KRX 접근 가능 7대 자산군(KOSPI 200, KOSDAQ 150, 국고채 10Y, S&P 500, 나스닥 100, 금, 미국 단기채), 2015-01 ~ 2026-08 (N = 2,868 거래일)이다.

## ⚠️ 한계 고지 (Limitations)

본 저장소의 실증 수치(CAGR 14.82%, 샤프 1.68, MDD −8.34%, 변동성 항력 0.88%p → 0.29%p, 위기 국면 방어, 거래비용 민감도 등)는 **원시 가격 데이터와 모델 학습·최적화 코드로부터 산출된 것이 아니다.**

- `data/backtest_results.json`은 `scripts/calculate_empirical_metrics.py`에 **입력 상수로 기재된** 자산·전략별 모멘트(μ, σ, 왜도, 첨도)로부터 파생 지표를 계산한 결과이다.
- 저장소에는 원시 가격 시계열, TSFM 체크포인트, 오토인코더 학습 코드, QP 실행 코드, 부트스트랩 결과가 **포함되어 있지 않다.**
- `scripts/verify_integrity.py`의 통과(47 PASS)는 저장값 · 수식 · 문서 간 **내부 산술 정합성**만을 의미하며, 실제 시장 성과의 재현을 의미하지 않는다.

세부 판정과 남아 있는 정의상 결함(Sharpe 정의, CAGR–누적수익률 기간 불일치, 인용 누락 등)은 [`audit/verification_ledger.md`](audit/verification_ledger.md)를 참조. 실데이터 기반 재현은 향후 과제이다.

## 저장소 구조

```
paper/
  chapters/01_introduction.md … 05_conclusion_and_policy.md   장별 원고
  FINAL_PAPER_CONSOLIDATED.md                                전체 통합본 (~97p)
  FINAL_PAPER_COMPRESSED_30P.md                              심사 규격(25–35p) 제출본 원문 ← 기준 문서
data/backtest_results.json                                   표·본문 수치의 단일 진실 공급원(SSOT)
scripts/
  calculate_empirical_metrics.py                             입력 상수 → 파생 지표 산출 (JSON 덮어씀)
  verify_integrity.py                                        수식·표·문서 간 정합성 감사 (읽기 전용)
  build_full_30p_final.py                                    30P 원문 → Word 빌드 (pandoc)
audit/
  verification_ledger.md                                     최종 감사 원장 (판정 기준 문서)
  verification_report_at_261003_2147.md                      1차 감사 보고서
archive/legacy_scripts/                                      10/3 분량 캘리브레이션용 일회성 스크립트 (대체됨)
```

Word(docx)·PDF 제출물, 증빙자료, 신청서 등은 `.gitignore`로 저장소에서 제외된다.

## 실행

Python 3.12, [`uv`](https://docs.astral.sh/uv/), [`pandoc`](https://pandoc.org/) 필요.

```bash
# 정합성 감사 (표준 라이브러리만 사용, 읽기 전용)
uv run python scripts/verify_integrity.py

# 입력 상수로부터 data/backtest_results.json 재생성
uv run --with-requirements requirements.txt python scripts/calculate_empirical_metrics.py

# 30P 원문을 Word로 빌드 (출력: _local/submissions/, git 제외)
uv run python scripts/build_full_30p_final.py
```

수치를 수정할 때는 `data/backtest_results.json` → `paper/` 각 원고 순으로 반영한 뒤 감사를 다시 실행한다.

## 인용

```
박재현, 강명서 (2026). 이토 보조정리와 시계열 파운데이션 모델(TSFM)을 결합한 동적 자산배분 및
변동성 항력(Volatility Drag) 제어 프레임워크. 2026 연합 경제 학술제 소논문, 서강대학교.
```
