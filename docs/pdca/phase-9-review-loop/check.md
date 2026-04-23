# Phase 9 Review Loop — 3회 독립 리뷰 + 수렴 결과

> 6개 핵심 슬라이드 프롬프트 (S6, S7A, S7B, S8, S9, S10) 의 **발견 중심 서사 · 진중한 차지욱 교수 어조 · 명사형 종결 · AI hype 금지** 원칙 적용 및 수렴 검증.
>
> 3인 독립 리뷰 패널:
> - **A: technical-writer** — 한국어 산문, 어조, 종결형, AI hype 검출
> - **B: quality-engineer** — 사실 정합, 약어 풀이, 수치 의미, 파일 간 일관성
> - **C: scientific-narrative** (general-purpose) — Discovery-Construction-Evidence 구조, 평가단 청중 적합성

## 수렴 matrix

| Iteration | Critical | Important | Minor | Regressions | 판단 |
|---|---|---|---|---|---|
| 0 (v1 draft) | — | — | — | — | 6개 prompt Phase 9 v1 작성 완료 |
| **1** | **12** | 9 | 7 | — | 대부분 수정 |
| **2** | **4** | 4 | 3 | 3 | 수정 진행 |
| **3** | **1** | 0 | 0 | **0** | 금지어 교체 → **승인** |

## Iteration 1 — 수렴 fix 표 (Critical + 주요 Important)

| # | 파일 | 발견 Reviewer | 문제 | 적용 수정 |
|---|---|---|---|---|
| 1-C1 | S7B L49 | A | "기존 **최고** 모델" — 금지어 "최고" 사용 | "선행 모델" 로 교체 |
| 1-C2 | S6 L60 | B | p=0.010 이 "분리"가 아닌 "비교"의 p값인데 귀속 오연결 | "긍정-부정 vs 부정-긍정 조건 비교 p=0.010" 로 정확화 |
| 1-C3 | S7A 카드 1 | C | "멱법칙 스케일링 경향을 보고함" 헤드라인에 실제 멱법칙 증거 본문 부재 | "3,700만→88억 4단계에서 손실이 로그-로그 선형으로 감소하는 멱법칙 경향 관찰" 추가 |
| 1-C4 | S7A 카드 4 | C | NeuroMamba 헤드라인 "성능 유지" 인데 증거 본문은 94.9% > 92.9% (개선) → 증거가 헤드라인을 초과 | "소폭 개선함을 관찰함" 로 헤드라인 강화 |
| 1-C5 | S7B bottom | B | 협력자 한글명 "정준기" 오기 (Chun Kee Chung = 정천기 교수) | "정천기" 로 교정 |
| 1-C6 | S7A 카드 2 | B | "선형 반복 신경망 (LSTM)" — 한국어 오역 (LSTM은 장단기기억) | "장단기기억 (LSTM, Long Short-Term Memory)" 로 정확화 |
| 1-C7 | S8 VLM 패널 | A | "0.94 관찰" 종결 어색 + 기준 부재 | "CLIP-ViT 모델이 0.94 (이항 분류 무작위 0.5 대비) 의 정확도를 보임" |
| 1-C8 | S10 카드 3 | C | "실험형 예술 전시" — 3년차 성과 증거 부재 | RYM 확장 맥락으로 재작성 (기억 재구성 대중 응용) |
| 1-C9 | S8 TabLeT | C | S7A 의 TabLeT 과 Lab 귀속 충돌 | S8 하단 우측을 "SEED 메타평가 결과" 로 교체 |
| 1-C10 | S9 Hero | C | "5개 세부 연구" 근거 부재 (실제 공동연구 1건) | "편도체 공동연구 1건 + 양측 표현 학습 2 트랙" 로 구체화 |
| 1-C11 | S7B L49-50 | A | Row 2 좌·우 subsection 명사 나열 (미종결) | "개선을 관찰함", "을 관찰함", "을 보임" 로 명사형 정리 |
| 1-C12 | S10 양자 칩 3 | C | "해석 가능한 양자 의사결정" — 증거 없는 결과 주장 | "혼합 양자-고전 강화학습의 해석 연구 (진행 중)" 로 단계 표기 |

Important (일부 수정): S7A "가능" → "가능함" · S7B ADHD 풀이 · S8 Hero 2단 · S7B epochs>params 한글 · S6 헤드라인 강화 · S9 SSL 완전 표기 · S10 3카드 종결 평행 등.

## Iteration 2 — 수렴 fix 표

| # | 파일 | 발견 Reviewer | 문제 | 적용 수정 |
|---|---|---|---|---|
| 2-C1 | S7A | A | "기반선" 한국어 표준 아님 → "기준선" | 전역 치환 |
| 2-C2 | S7A Hero | C | "약 5만명 사전학습" 수치 단독 Hero (style guide 위배) | "대규모 뇌영상 사전학습 · 범용 표상 확보" + 수치 2단 |
| 2-C3 | S7A 카드 1 | A | "7.6%p 무작위 50% 기준" 모호 (선행 대비 vs 무작위 대비) | "선행 모델 대비 7.6%p 의 절대 정확도 개선" 명시 |
| 2-C4 | S7A ASD | B | ASD 문장에서 "주의" 누락 | "고주파 언어·주의·작업기억·사회인지" 로 복원 |
| 2-C5 | S7B Hero | C | "5,300+54,000시간" 수치 단독 Hero | "대규모 전기생리 코퍼스 확립" + 수치 2단 |
| 2-C6 | S7B Row 3 | C | 헤드라인 Construction only | "개인별 정서 상태를 뇌전도·심전도로 디코딩하고, 유전형을 결합한 임상 예측으로 확장함" |
| 2-C7 | S7B bottom | A | 협력자 역할 계층 부재 (모두 동격 나열) | "주관: 서울대 차지욱 · 국내 공동 · 국외 공동" 계층화 |
| 2-C8 | S7B Row 2 | A | "고전 뇌과학 ... Convergence-Divergence-Zone" — 이론 제창자 미상 | "Damasio 의 수렴-발산 영역 이론" 으로 귀속 |
| 2-C9 | S8 Title | C | "SEED 구축" Construction only | "기존 디코딩 평가 지표가 인간 판단과 체계적으로 괴리됨을 드러내고, 이에 대응한 의미 평가 체계 (SEED) 를 확립함" |
| 2-C10 | S8 SEED 카드 3 | A | EfficientNet 이 실패 지표·통합 구성 양쪽 등장 (모순) | "EfficientNet 특징은 단독으로는 인간 판단과 괴리되나 SEED 안에서 객체·의미 지표와 결합 시 보완 역할" 로 해석 |
| 2-C11 | S9 Hero | C | "1건 + 2 트랙" counting only | "동물·사람 양측에서 멱법칙 스케일링 경향 관찰" + 구체 counts 2단 |
| 2-C12 | S9 하단 | A | Hero "2 트랙" 과 하단 "개별 확립" 논조 충돌 | "양측 (동물·사람) × 4 모달리티 개별 확립" 로 축 분리 |
| 2-C13 | S10 Title | C | "정리함" meta-action (Discovery·Construction 부재) | "... BCI·정신질환 바이오마커·대중 응용으로 확장하고, 양자 기계학습으로 ADHD 다중 시스템 관여 패턴을 보고함" |
| 2-C14 | S10 카드 2 | A | "보완함" (완료형) 과 제목 "지향" 충돌 | "보완하는 방향을 탐색함" |
| 2-C15 | S10 양자 칩 1 | A | "양자 마리오" 고유명 주어 | "확장 가능한 양자 강화학습 프레임워크 (코드명 Quantum Mario)" 로 기술명 주어화 |

## Iteration 3 — 최종 수렴 fix 표

| # | 파일 | 발견 Reviewer | 문제 | 적용 수정 |
|---|---|---|---|---|
| 3-C1 | S7A L40 | A | "R² = 0.96 (1.0이 **완벽** 예측)" — 금지어 "완벽" | "(결정계수 범위 0~1, 1.0이 이론적 상한)" |
| 3-C2 | S7B L50 | A | "SSIM 0.593 (1.0이 **완전** 일치)" — 금지어 "완전" | "(범위 0~1, 1.0이 이론적 상한)" |
| 3-C3 | S9 L40 | A | 동일 표현 | "(범위 0~1, 1.0이 이론적 상한)" |
| 3-C4 | S8 L30 | A | "Object F1 (0~1, 1.0=**완벽**)" — 금지어 | "(범위 0~1, 1.0이 이론적 상한)" |

Reviewer B·C: "Iter 3 Critical·Regression 없음. 승인 가능" 명시.

## 최종 판단

- **3인 패널 합의**: Phase 9 프롬프트 세트는 렌더 가능 상태에 도달함.
- 발견-구축-증거 구조, 명사형 종결, AI hype 금지, 약어 풀이, 수치 의미 부기의 5개 원칙이 6개 슬라이드 전반에 일관되게 반영됨.
- 잔존 사항은 모두 스타일 가이드 부합 확인 완료.

## 적용 파일

- `slides/prompts/slide_06_db-construction.md`
- `slides/prompts/slide_07a_cha-fmri.md`
- `slides/prompts/slide_07b_cha-clinical.md`
- `slides/prompts/slide_08_multimodal-seed.md`
- `slides/prompts/slide_09_cross-species.md`
- `slides/prompts/slide_10_extensions-quantum.md`

원칙 문서: `docs/narrative-style-guide.md` (Phase 9 확립).
