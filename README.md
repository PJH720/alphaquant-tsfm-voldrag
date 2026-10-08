# 이토 보조정리 × TSFM 동적 자산배분: 변동성 항력(Volatility Drag) 제어 프레임워크

**2026 연합 경제 학술제** (서강대 · 성균관대 · 이화여대) 출품 소논문 저장소
팀 **알파퀀트** (서강대학교 경제학과): 박재현 (대표, 연구총괄), 강명서 (본선 발표)

> 『이토 보조정리와 시계열 파운데이션 모델(TSFM)을 결합한 동적 자산배분 및 변동성 항력(Volatility Drag) 제어 프레임워크: 산업 비파괴검사 기반 비지도 꼬리위험 세이프가드를 중심으로』

## 연구 개요

장기 복리 성과는 산술평균 μ가 아니라 기하성장률 `g = μ − ½σ²`가 지배한다. 정적 평균-분산 최적화(MVO)는 분산이 성장률을 잠식하는 **변동성 항력 ½σ²**을 직접 통제하지 못한다. 본 연구는 다음 세 층을 결합한 프레임워크를 제안한다.

| 층 | 내용 |
|---|---|
| 목적함수 | 이토 보조정리로 유도한 켈리(λ=1) 기하성장률 극대화 + Rockafellar–Uryasev CVaR(95%) 제약 볼록 QP |
| 사전적 모멘트 | 시계열 파운데이션 모델(Chronos, PatchTST) + RevIN, Ledoit-Wolf 축소 및 PSD 보정 공분산 |
| 꼬리위험 세이프가드 | 비파괴검사(NDE) 결함 탐지 개념을 차용한 오토인코더 재구성 오차 기반 현금 전환 |

분석 대상은 KRX 접근 가능 7대 자산군(KOSPI 200, KOSDAQ 150, 국고채 10Y, S&P 500, 나스닥 100, 금, 미국 단기채), 2015-01 ~ 2026-08 (N = 2,868 거래일)이다.

## ⚠️ 수치의 성격: 시뮬레이션 파라미터 기반 (실측 백테스트 아님)

**본 연구의 수치는 시뮬레이션 파라미터 기반이며, 실데이터 재현은 후속 과제이다.**

| 수치 유형 | 예시 | 성격 | 근거 |
|---|---|---|---|
| 자산·전략 파라미터 | 전략별 μ, σ, 자산별 왜도·첨도 | **시뮬레이션 입력 파라미터** (실측 추정치 아님) | `scripts/calculate_empirical_metrics.py` 상수 |
| 파라미터의 해석적 함의 | CAGR 14.82% (= μ − ½σ²), 변동성 항력 0.29%p, 10년 복리 손실액, JB 통계량 | 파라미터로부터의 **해석적 계산** | `data/backtest_results.json` |
| 몬테카를로 분포 | 성장률·10년 자산·MDD·샤프의 분포, 제안 모델 우위 경로 비율 | 파라미터 기반 **GBM 시뮬레이션 결과** (10,000 경로, seed 고정) | `scripts/simulate_gbm_mc.py` → `data/simulation_results.json` |
| 위기 국면 서술 | 2020년 3월 팬데믹·2022년 긴축기 방어, 세이프가드 발동일, 거래비용·리밸런싱 민감도 | **예시적 시나리오 서술** (시뮬레이션도, 역사적 백테스트도 아님) | 본문 서술 |

- 저장소에는 원시 가격 시계열, TSFM 체크포인트, 오토인코더 학습 코드, QP 실행 코드, 부트스트랩 결과가 **포함되어 있지 않다.**
- `scripts/verify_integrity.py` 통과(48 PASS)는 파라미터 · 수식 · 시뮬레이션 · 문서 간 **내부 정합성**을 의미하며, 실제 시장 성과의 재현을 의미하지 않는다.
- 세부 판정과 남은 정의상 결함(Sharpe 정의, CAGR–누적수익률 기간 불일치, 인용 누락 등)은 [`audit/verification_ledger.md`](audit/verification_ledger.md) 참조.

### 몬테카를로 결과 요약 (`data/simulation_results.json`)

| 전략 | 이론 g = μ − ½σ² | MC 평균 성장률 (±SE) | 10년 자산 평균 (앙상블) | 10년 자산 중앙값 (전형 경로) | MDD 중앙값 |
|---|---:|---:|---:|---:|---:|
| 전통적 60/40 | 7.85% | 7.93% (±0.03) | 235.7억 | 221.6억 | −21.1% |
| 동일가중 | 8.42% | 8.41% (±0.04) | 251.8억 | 231.6억 | −23.8% |
| MVO | 9.14% | 9.13% (±0.04) | 272.2억 | 248.6억 | −24.2% |
| 제안 모델 | 14.82% | 14.78% (±0.02) | 451.6억 | 437.9억 | −8.6% |

앙상블 평균과 전형 경로(중앙값)의 차이가 곧 변동성 항력이며, 이는 σ가 큰 전략일수록 커진다(본문 제2장의 비에르고딕성 논의). 10년 자산은 연속복리 `exp(10·g)` 기준이므로, 이산복리 `(1+g)^10`을 쓴 본문 표 4-2와 수치가 다르다.

## 두 저장소의 관계

| | 본 저장소 (발표용) | 실데이터 재현 저장소 (후속 과제) |
|---|---|---|
| 저장소 | `PJH720/alphaquant-tsfm-voldrag` | [`PJH720/alphaquant-tsfm-voldrag-empirical`](https://github.com/PJH720/alphaquant-tsfm-voldrag-empirical) |
| 수치 출처 | 시뮬레이션 파라미터 + 해석적 계산 + GBM 몬테카를로 | 원시 시장 데이터 (지수·ETF 수정주가, FRED 거시지표) |
| 모델 | 이론·수식 정식화 | Chronos 제로샷 예측, 이토-켈리 CVaR QP, 오토인코더 세이프가드 실제 구현 |
| 원칙 | 본선 심사본과 동일한 수치 유지 | 하이퍼파라미터 사전 등록, 결과가 논문과 달라도 그대로 보고 |
| 시연 사이트 | [제출본 시뮬레이션 모드](https://alphaquant-voldrag-demo.vercel.app) | [실데이터 사전등록 재현 모드](https://alphaquant-voldrag-demo.vercel.app) |

## 저장소 구조

```
paper/
  chapters/01_introduction.md … 05_conclusion_and_policy.md   장별 원고
  FINAL_PAPER_CONSOLIDATED.md                                전체 통합본 (~97p)
  FINAL_PAPER_COMPRESSED_30P.md                              심사 규격(25–35p) 제출본 원문 ← 기준 문서
slides/                                                      학교 공식 Beamer(Berlin/beaver) 발표 슬라이드 소스
  main.tex, Section/*.tex, Mybib.bib                         XeLaTeX 슬라이드 소스 (16:9 와이드, 26쪽)
  MyFigure/                                                  벡터 차트 및 QR 코드
  make_figures.py                                            슬라이드용 벡터 차트 생성 스크립트
  generate_scripts_and_notes.py                              발표자 대본 및 노트 생성기
data/backtest_results.json                                   표·본문 수치의 단일 진실 공급원(SSOT, 시뮬레이션 파라미터)
data/simulation_results.json                                 GBM 몬테카를로 결과
scripts/
  calculate_empirical_metrics.py                             입력 상수 → 파생 지표 산출 (JSON 덮어씀)
  simulate_gbm_mc.py                                         파라미터 기반 GBM 몬테카를로 (10,000 경로)
  verify_integrity.py                                        수식·표·시뮬레이션·문서 간 정합성 감사 (읽기 전용)
  build_full_30p_final.py                                    30P 원문 → Word 빌드 (pandoc)
  export_web_bundle.py                                       제출본 시뮬레이션 수치 → web_export/submission_simulation.json (시연 사이트용)
  build_presentation.sh                                      본선 발표자료 원클릭 전체 빌드 파이프라인
  package_submission.py                                      제출 파일 무결성·용량·노트 전수 검사 및 해시 출력
audit/
  verification_ledger.md                                     최종 감사 원장 (판정 기준 문서)
  verification_report_at_261003_2147.md                      1차 감사 보고서
docs/
  presentation_disclosure.md                                 본선 발표용 수치 성격 고지·질의응답 문안
  presentation_script_cuesheet.md                            14분 상세 발표 대본, 타임라인 큐 시트, 12대 질의응답
  speaker_pocket_cue_card.md                                 발표자(강명서)용 단면 1장 모바일/인쇄 포켓 큐 카드
out/                                                         발표 최종 산출물 ([서강대]_알파퀀트_발표자료.pptx, .pdf, zip)
pdf_to_pptx.py                                               Beamer PDF → PPTX 변환 및 슬라이드 노트 주입기
archive/legacy_scripts/                                      10/3 분량 캘리브레이션용 일회성 스크립트 (대체됨)
```

Word(docx)·PDF 제출물, 증빙자료, 신청서 등은 `.gitignore`로 저장소에서 제외된다.

## 실행

Python 3.12, [`uv`](https://docs.astral.sh/uv/), [`pandoc`](https://pandoc.org/), MacTeX/XeLaTeX 필요.

```bash
# 정합성 감사 (표준 라이브러리만 사용, 읽기 전용, 50 PASS 체계)
uv run python scripts/verify_integrity.py

# 본선 발표자료 원클릭 빌드 (차트 생성 → XeLaTeX → 대본 동기화 → PPTX 노트 주입)
bash scripts/build_presentation.sh

# 최종 제출물 무결성·규격 자동 검사 및 체크섬 산출
uv run --with python-pptx --with pymupdf python scripts/package_submission.py

# 시뮬레이션 파라미터로부터 GBM 몬테카를로 실행 → data/simulation_results.json
uv run --with-requirements requirements.txt python scripts/simulate_gbm_mc.py

# 입력 상수로부터 data/backtest_results.json 재생성
uv run --with-requirements requirements.txt python scripts/calculate_empirical_metrics.py

# 30P 원문을 Word로 빌드 (출력: _local/submissions/, git 제외)
uv run python scripts/build_full_30p_final.py

# 제출본 시뮬레이션 수치를 시연 사이트용 JSON 하나로 내보내기 → web_export/submission_simulation.json
uv run python scripts/export_web_bundle.py
```


수치를 수정할 때는 `data/backtest_results.json` → `paper/` 각 원고 순으로 반영한 뒤 감사를 다시 실행한다.

## 인용

```
박재현, 강명서 (2026). 이토 보조정리와 시계열 파운데이션 모델(TSFM)을 결합한 동적 자산배분 및
변동성 항력(Volatility Drag) 제어 프레임워크. 2026 연합 경제 학술제 소논문, 서강대학교.
```
