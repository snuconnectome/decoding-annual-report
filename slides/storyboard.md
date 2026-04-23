# 디코딩과제 3년차 발표 슬라이드 스토리보드

> 과기부/연구재단 평가단용 15장 인포그래픽 슬라이드 발표 설계
>
> **테마**: `snu_neurox` (SNU Blue + Okabe-Ito 색맹안전 팔레트, 16:9)
> **총 장수**: 15장 (차지욱 Lab 연구 분량으로 S7을 S7A·S7B로 분할)
> **예상 발표 시간**: 18–22분 (장당 1–1.5분)
> **서술 톤**: **과학적 발견 중심 · 진중한 관찰자 어조 · 명사형 종결 ("...함")**. AI hype 표현 ("세계 최초", "최고", "능가", "압도") 금지. 자세한 원칙: `docs/narrative-style-guide.md`
> **약어 정책**: 풀네임 + (영문 약어). 모든 수치는 의미·비교기준 부기.
> **원천 자료**: `report/03_lab-research-detail.md` (4 Lab × granular 실험 기술)

---

## 공통 디자인 원칙

- **Header logo**: 좌상단 "디코딩과제 3년차" 14pt #003380 (SNU Blue)
- **Slide number**: 우하단 12pt #5A5A6E
- **Margin**: 0.7 inch
- **Whitespace**: 의도적 여백 (밀도 낮게)
- **Korean font**: Pretendard → 맑은 고딕 → 나눔고딕 fallback
- **English font**: Calibri
- **Contrast**: ≥ 4.5:1
- **Hero metrics**: 32pt Bold #E69F00 (Signal Orange)
- **Consistency lock**: 14장 전체 동일 시각 문법. 스타일 편차 0.

---

## Slide 1 — 타이틀

**유형**: Cover (단일 대형 타이틀 + 메타 정보)

**핵심 메시지**: 과제의 존재와 책임자를 단 한 장으로 전달

**레이아웃**:
- 상단 1/3: 과제 제목 (국문) - 큰 타이틀 (32pt Bold SNU Blue)
- 중앙 1/3: 영문 제목 (22pt Neural Teal)
- 하단 1/3: 메타 정보 박스 (책임자, 기관, 기간, 예산, 과제번호)

**구체 내용**:
- 국문 제목: "동물-사람 멀티스케일 신경과학 파운데이션 모델 기반 뇌-외부환경 상호작용 시 정서로 맥락화된(contextualized) 지각의 디코딩"
- 영문 제목: "Affect-contextualized perception decoding with cross-species multiscale neuroscience foundation model"
- 연구책임자: 차지욱 (서울대학교, 부교수)
- 과제번호: RS-2023-00265406
- 기간: 2023.07 — 2027.12 (54개월) · 해당 연차: 3년차 (2025)
- 3년차 예산: 453,500천원
- 주관: 과학기술정보통신부 · 한국연구재단
- 제출일: 2025.12.08

**시각 요소**:
- 뇌 아이콘 (flat 실루엣) — 배경 반투명 워터마크 혹은 우측 정렬
- SNU 로고 자리 (실제 로고 이미지는 삽입 어려울 수 있음, 텍스트로 처리)

**데이터 소스**: `data/project-meta.yaml`

**Negative**: 3D 뇌 렌더링 금지, 그라디언트 텍스트 금지, 사진사실적 이미지 금지

---

## Slide 2 — 연구 개요 (contextualized 지각 디코딩이란?)

**유형**: 구조/아키텍처 (3단 플로우 도식)

**핵심 메시지**: "외부환경 → 뇌 → 정서 맥락화" 삼단 개념 구조 한 눈에 전달

**레이아웃**:
- 상단: 짧은 주제 문장 (22pt) "본 연구의 핵심 개념"
- 중앙: 수평 3단 플로우 (좌 → 우)
  - 박스 1: [환경 자극] 시각·청각·복합
  - 박스 2: [뇌의 추론] 불완전 감각 → 예측 → 업데이트
  - 박스 3: [정서 맥락화] 신체 반응 유도
- 하단: 핵심 명제 1줄 (18pt) "정서 맥락은 지각 디코딩의 핵심 변인"

**구체 내용** (from p11 `연구개발과제의 개요`):
- 박스 1 라벨: "외부환경"
- 박스 2 라벨: "뇌의 능동적 추론"
- 박스 3 라벨: "정서에 의한 맥락화"
- 하단 캡션: "기존 디코딩은 수동적 지각에 국한 → 본 연구는 능동·정서 맥락을 반영"

**시각 요소**:
- 박스 3개 (SNU Ice #EDF6FC 배경, 얇은 테두리)
- 수평 직선 화살표 × 2 (SNU Blue)
- 아이콘: ① 귀/눈 (감각) ② 뇌 ③ 하트 (정서)

**데이터 소스**: `source/extracted-text/pages/011.txt`, `data/project-meta.yaml`

**Negative**: 곡선 화살표 금지, 원형 다이어그램 금지

---

## Slide 3 — 5개년 로드맵

**유형**: 타임라인 (수평 5단계)

**핵심 메시지**: 3년차가 전체 여정에서 어디 위치하는지 강조

**레이아웃**:
- 상단: 제목 "5개년 연구개발 로드맵" (32pt Bold)
- 중앙: 수평 타임라인 (왼쪽 2023.07 → 오른쪽 2027.12)
  - 다이아몬드 마커 5개 (1년차 ~ 5년차)
  - 각 마커 아래: 연도·예산·핵심 목표 1줄
- **3년차 마커는 Signal Orange로 강조** (현재 위치)

**구체 내용**:
- 1년차 (2023.07~12): 300,000천원 — 빅데이터 자동화 실험 환경 조성
- 2년차 (2024): 453,500천원 — 고정 환경 지각 데이터베이스 구축
- **3년차 (2025): 453,500천원 — 변동 환경 데이터베이스 + 멀티 모달리티 ML 모델** ← 강조
- 4년차 (2026): 600,000천원 — BrainLife 공개 + 종간 파운데이션 사전학습
- 5년차 (2027): 600,000천원 — 전이학습 검증 + 실험형 전시 활용

**시각 요소**:
- 수평 타임라인 축 (얇은 SNU Blue 선)
- 다이아몬드 마커 × 5 (기본 Neural Teal, 3년차만 Signal Orange)
- "현재" 배지 (3년차 위)

**데이터 소스**: `data/project-meta.period`, `data/project-meta.budget`, `data/evaluation-criteria`

**Negative**: 3D 타임라인 금지, 원형 연표 금지

---

## Slide 4 — 3차년도 목표 (평가항목)

**유형**: 데이터 (표 + 가중치 시각화)

**핵심 메시지**: 3차년도에는 4개 평가항목 × 25%씩 = 100% 재분배

**레이아웃**:
- 상단: "3차년도 평가 구조" 타이틀
- 중앙: 2×2 그리드 카드 (4개 평가항목, 각 25%)
  - 카드 1 [25%]: 뇌-환경 상호작용 데이터베이스 구축 (세부목표 1-1, 1-2)
  - 카드 2 [25%]: 기계학습 모델 개발 및 검증 (세부목표 1-3, 1-4)
  - 카드 3 [25%]: 뇌영상-파운데이션 모델 (세부목표 2-1, 2-2)
  - 카드 4 [25%]: 다중 모달리티 통합 모델 (세부목표 2-1, 2-2)
- 하단 주석 (12pt): "※ 5개년 기준 6개 평가항목 중 3차년도 active 항목에 가중치 100% 재분배"

**시각 요소**:
- 카드 4개 (SNU Ice 배경, 둥근 모서리)
- 각 카드 좌상단에 [25%] 배지 (Signal Orange)
- 번호 ① ② ③ ④

**데이터 소스**: `data/metrics.yaml year3_performance`, `data/evaluation-criteria.yaml`

**Negative**: 원형 파이차트 금지 (4개×25%는 너무 단조로움), 복잡 표 금지

---

## Slide 5 — 추진전략 다이어그램

**유형**: 구조/아키텍처 (5단계 수평 플로우)

**핵심 메시지**: 데이터 → 전처리 → 디코더 → 파운데이션 → 활용의 표준 파이프라인

**레이아웃**:
- 상단: "연구개발 추진전략" 타이틀
- 중앙: 수평 5단계 플로우 (번호 카드 + 화살표)
  - ① 데이터 생성
  - ② 데이터 전처리
  - ③ 디코더 학습 및 검증
  - ④ 파운데이션 모델 학습 및 검증
  - ⑤ 파운데이션 모델 확장 및 활용
- 하단: 팀 구성 4색 범례 (최형진·이상아·차지욱·문태섭 연구팀)

**구체 내용**:
- 팀 색상: 빨강 (최형진), 초록 (이상아), 파랑 (차지욱), 보라 (문태섭)
  - → 색맹 대응 위해 Okabe-Ito로 변환: 빨강 → D55E00, 초록 → 11604B, 파랑 → 0072B2, 보라 → 차선 색 선택

**시각 요소**:
- 번호 카드 5개 (SNU Ice 배경)
- 수평 화살표 × 4 (SNU Blue, 직선)
- 하단 팀 범례 (4개 작은 색 박스 + 이름)

**데이터 소스**: `data/next-year-plan.strategy`

**Negative**: 순환 흐름 금지 (스킬 가이드), 곡선 화살표 금지, 3D 금지

**주의**: 원본 p90 다이어그램을 단순화. 원본은 동물/사람 2트랙이 복잡하게 얽혀 있음 → 축약 필요.

---

## Slide 6 — DB 구축 성과 · 이상아 Lab 중심 (목표 1-1, 1-2)

**유형**: 데이터 (2개 실험 패널 + 하단 주석)

**핵심 메시지**: 이상아 Lab이 이끈 2개 인간 실험으로 정서 맥락화 지각 디코딩 DB 핵심 구축 완료 · 달성도 100%

**레이아웃**:
- 상단: "데이터베이스 구축 — 평가항목 #1 (25%)" + 부제 "이상아 Lab (사람) · 최형진 Lab (동물) 공동 수행 · 달성도 100%"
- 상단 우측: "**100%**" 킬러 수치 배지 (Signal Orange)
- 중앙 상단 띠 — 최형진 Lab **animal block** (확장):
  - 타이틀: "동물 (최형진 Lab) — 3D 골격 DB + VTA-NAc two-site 광유전학"
  - 내용 좌: "자유 행동 설치류 · DeepLabCut 멀티뷰 3D 포즈 (코·귀·척추·앞/뒷발·꼬리) · 그루밍·보행·rearing·drinking"
  - 내용 우: "VTA-NAc 도파민 축삭 광유전학 (DAT-cre · AAV5-ChrimsonR + AAV9-GRAB_DA1h · 594 nm · 5/10/20 Hz · fiber photometry)"
  - 색 bar: LAB_VERMIL (#D55E00) 좌측
- 중앙 메인 영역: 이상아 Lab **human block** 2개 패널 수평:
  - **실험 1 [좌]: MixedEmo fMRI + EEG (n=92)**
    - 설계: "Scene 80종 × IAPS 감정자극 160종 · 5조건 (중립·부정·긍정·긍정-부정·부정-긍정)"
    - fMRI: 편도체·전두두정 (지각) / DMN·PCC·precuneus (인출) / ACC 복측 vs 배측 해리 (**p=0.010**)
    - 개인차: STAI-X1 불안 → 인출 편향 (**p=0.002, 0.003**)
    - EEG (32ch · 2048Hz): **Posterior θ** (두정엽·후두엽, 감정 처리 우선) · **Frontal θ** (감정 충돌)
  - **실험 2 [우]: 가상공간 탐험 EEG + 해마 OCAT**
    - 설계: "4가지 랜드마크 (근접·원격·혼합·없음) · 1분 VR 비디오 + sequential reactivation 분석"
    - Sequential reactivation: **reactivation bias** (시간에 따른 증가 = 성공 재활성)
    - 디코딩 정확도: **10-15%** (chance 4%) · *Imaging Neuroscience* (Lim et al. 2025)
    - 해마 OCAT: **CA23DG · CA1**에서 물체-환경 패턴 유사성 (맥락 범주화)
    - 청소년: CA23DG ↔ **OFC** 연결 발달 · 정서적 학대 집단 결여
- 하단: 증빙 "인간 n=92 fMRI·EEG DB + 동물 3D 골격·VTA-NAc two-site 프로토콜 구축 완료"

**시각 요소**:
- 상단 animal block: LAB_VERMIL (#D55E00) 좌측 색 bar, 카드 배경 BG_PEACH (#FDECE2) 연하게
- 하단 human block 2개 박스: SNU Ice #EDF6FC, LAB_TEAL (#11604B) 세로 bar (이상아 Lab)
- 각 실험 박스 상단 번호 배지 (Signal Orange)
- 우상단 "100%" 배지 (32pt Bold Signal Orange)
- 아이콘: animal (쥐 실루엣 + 광섬유 표기), 실험 1 (뇌 + 파동), 실험 2 (공간 탐험 시점)

**구체 내용** (from `report/03_lab-research-detail.md` §1 이상아 + §2 최형진):
- **최형진 Lab 핵심 수치**: 자유 행동 멀티뷰, DAT-cre, ChrimsonR-tdTomato, GRAB_DA1h, 594 nm, fiber photometry
- **이상아 Lab 실험 1**: amygdala · DMN · PCC · precuneus · ACC 복측/배측 해리 p=0.010 · STAI-X1 p=0.002, 0.003 · Posterior θ · Frontal θ
- **이상아 Lab 실험 2**: Lim et al. 2025 *Imaging Neuroscience* · reactivation bias · CA23DG · CA1 · CA23DG ↔ OFC 청소년 발달

**데이터 소스**:
- `report/03_lab-research-detail.md` §1 (이상아 Lab) + §2 (최형진 Lab)
- `data/metrics.yaml year3_performance[0]` (criterion_id=1)
- 이상아 Lab Google Slides (사용자 제공, 2026-04-22)
- 최형진 Lab BK21 자체평가 (Google Sheet `1lLcfs...`, 2025-10-16)
- 공식 제출본 Google Docs `1TwvN0...` (섹션 세부연구 1·2·5)

**주의**:
- 이상아 Lab 대표 논문 4편 (Lim 2025/8 *Imaging Neuroscience*, Kim 2025/11 *iScience*, Lee 2025/11 *Neuropsychologia*, Koo 2026/1 *Scientific Reports*)은 공식 `achievements.yaml` 17편 목록에 **미포함**. 사용자 결정: 제출본 그대로 유지. 슬라이드에서는 실험·결과 중심 narrative.
- 최형진 Lab의 CeA-Glp1R · NAc-NPY · LH CaMKIIα+ · AgRP 회로는 본문 미기재지만 BK21 자료에 풍부. 평가단 질의 시 구두 보완 가능 (전체 내용은 `report/03_lab-research-detail.md` §2.4).

**Negative**: 상세 데이터 표 금지, 사진사실적 뇌 이미지 금지, 3단 이상 중첩 구조 금지

---

## Slide 7A — 차지욱 Lab ① fMRI 파운데이션 모델 (평가항목 #2·#4)

**유형**: 데이터 + 구조 (4 모델 카드 + hero scaling card)

**핵심 메시지**: UKB·HCP·ABCD 5만명 기반 8.8B 스케일링 → sequence decoding (R²=0.96) · 주파수 분리 (ADHD/ASD SOTA) · Mamba 효율화 (HCP 94.9%)

**레이아웃**:
- 상단 타이틀: "차지욱 Lab ① fMRI Foundation Models" + 부제 "평가항목 #2·#4 · 달성도 100%"
- 우상단 Hero 배지: "**8.8B params · 5만명**" (SwiFT 스케일링)
- 중앙 2×2 grid + 우측 side column:
  - **Top-L [SwiFT]**: "8.8B params · muP · UKB+HCP+ABCD 5만명 · Power-law"
    - 부가: "BrainLM·Brain-JEPA 상회 · HCP 성별 +7.6%"
  - **Top-R [SwiFT-IO]**: "R² = 0.96 · HBN 677명 movie fMRI · Perceiver IO"
    - 부가: "Sequence-to-Sequence 정서가 디코딩 · CCN 2025"
  - **Bot-L [MBBN]**: "Frequency-Specific Multi-Band Attention"
    - 부가: "ADHD: 고주파 실행기능·저주파 운동지각·초저주파 내장감각 · *Communications Biology* 2026.1"
  - **Bot-R [NeuroMamba]**: "HCP 성별 94.9% · FLOPs −46.5%"
    - 부가: "Mamba2 + NeRF 위치 인코딩 · SwiFT 92.9% 상회"
- 하단 얇은 띠: "**TabLeT** (2D DCAE · UKB 8,178 + HCP 1,061 + ADHD-200 533 · CVPR 심사) · **Latent Diffusion Transformer** (3D VQ-GAN · 4D fMRI 생성 세계 최초)"

**시각 요소**:
- 4 카드 동일 크기 (SNU Ice #EDF6FC 배경, Neural Teal 테두리)
- Hero 배지: Signal Orange circle, 32pt Bold
- 모델명: 22pt Bold SNU Blue; hero metric: 28pt Bold Signal Orange; 본문: 13pt TEXT_DARK
- 차지욱 Lab color bar: 좌측 얇은 Okabe-Ito pink (#CC79A7) 세로줄

**구체 내용 (numeric anchors)**:
- SwiFT: 37M → 118M → 1.2B → 8.8B 파라미터 scaling
- 알츠하이머병 전환 예측 · 통증 상태 분류 · 항우울제 치료 반응 SOTA
- HBN movie fMRI 12분 × 677명
- MBBN ASD 고주파 언어·주의·작업기억·사회 인지
- NeuroMamba NeuroSTORM 93.3% 상회

**데이터 소스**:
- `report/03_lab-research-detail.md` §3.1 (fMRI Foundation Models)
- `data/metrics.yaml year3_performance[1,2]` (criterion 2·4)
- 공식 제출본 SwiFT-IO 벤치마크 표 (MSE 0.125 · MAE 0.137)

**Negative**: 5개 이상 카드 금지 (2×2 기준), 3D 뇌 렌더링·사진사실적 이미지 금지, 막대그래프 과밀 금지

**주의**: MBBN의 ADHD 주파수별 바이오마커는 평가단 질의 대비 핵심 포인트. 구두 발표 시 강조.

---

## Slide 7B — 차지욱 Lab ② EEG/iEEG Foundation + 동물·임상·생성 응용 (평가항목 #2·#4)

**유형**: 데이터 + 나열 (Hero scaling + 3 라인)

**핵심 메시지**: DIVER-1이 ephys 최초 정량적 scaling law 확립 (5.3k iEEG + 54k EEG hrs) · Language-Brain +14.4% · POYO-SSL +12~13% · RYM F1=0.9 등 멀티도메인 확장

**레이아웃**:
- 상단 타이틀: "차지욱 Lab ② EEG/iEEG + 동물·임상 응용" + 부제 "ephys 최초 Scaling Law · Multi-Modal Generative"
- 우상단 Hero 2개 배지 (세로 스택):
  - "**5.3k iEEG**" (17.7k명 · 1.6M 채널-시간)
  - "**54k EEG hrs**" (FACED · PhysioNet-MI · MentalArithmetic)
- 중앙 3개 수평 행:
  - **Row 1 — DIVER-1**: "Any-Variate Attention · STCPE · Multi-Domain Reconstruction"
    - 킬러: "13M 파라미터로 BrainBERT 43M · PopT 63M 능가 (Neuroprobe 15 과제)"
    - 부가: "**Data-constrained Scaling Law** 최초 정량 · epochs > model size"
  - **Row 2 — Cross-Modal Alignment**:
    - Language-Brain Alignment: "**+14.4%** (Antonello et al. 상회) · Convergence-Divergence-Zone Theory"
    - POYO-SSL: "**+12~13%** · SSIM 0.593 · Drifting Gratings 55.5% · 1.98× 데이터 효율 (Allen Brain Observatory)"
  - **Row 3 — 임상·생성 응용**:
    - RYM (EEG → Stable Diffusion · MusicGen): "F1=0.9 · 56% 선호도 향상"
    - CEBRA 경외 (*Communications Psychology* 2025) + 내수용감각 ECG-EEG (IS-RSA · Claude 3.5 Sonnet)
    - Polygenic-informed 임상: 우울증·ADHD·아동 polygenic architecture (논문 #1·#5·#14·#15)
- 하단 얇은 띠: "DIVER 3-Phase 전략 — Foundation (Pre-Train) → Alignment (iEEG-Video-Speech Trimodal) → Personalization (closed-loop)"

**시각 요소**:
- Hero 2 배지: 세로 stack, Signal Orange
- Row 라벨: 좌측 22pt Bold SNU Blue 번호 마커 ①②③
- DIVER-1 행은 더 큰 영역 (핵심 임팩트)
- 차지욱 Lab 좌측 색 bar 유지 (Okabe-Ito pink)

**구체 내용 (numeric anchors)**:
- DIVER-1: ICLR 2026 심사 중, 1e20 FLOPs (GPT-1 × 2배, 이전 SOTA × 77배)
- DIVER-2 로드맵: 50k hrs iEEG 확장 (10× scale-up)
- POYO-SSL: ICLR 2026 심사 중
- Language-Brain: openreview.net forum id hgBVVAJ1ym
- RYM 9명 2세션 · r=0.265 p<.012
- 협력 PI: Jay-Yoon Lee · Chun Kee Chung · Uri Hasson · Shinjae Yoo (SNU + Brookhaven)

**데이터 소스**:
- `report/03_lab-research-detail.md` §3.2 (EEG/iEEG + Clinical)
- 차지욱 Lab ephys FM 슬라이드 (Google Slides `1LTc1e...`)
- `data/achievements.yaml` key_technical_models

**Negative**: 대각선 화살표 금지, 3단 이상 중첩 구조 금지, Quantum 관련 내용은 Slide 10에 배치 (중복 금지)

**주의**: DIVER-1의 "First Quantified Scaling Laws for Ephys"는 ephys FM 슬라이드의 핵심 Novelty — 구두 강조 포인트. "epochs > params" 메시지는 LLM Kaplan Scaling Law와 명시적 대비.

---

## Slide 8 — 다중 모달리티 · 시맨틱 평가 체계 · 문태섭 Lab 중심

**유형**: 데이터 + 구조 혼합 (상단 평가 지표 + 하단 아키텍처)

**핵심 메시지**: 문태섭 Lab의 SEED 평가 체계 + Vision-Language Model로 뇌 디코딩의 semantic alignment 기반 확립 · 달성도 100%

**레이아웃**:
- 상단: "다중 모달리티 통합 · 시맨틱 평가 — 평가항목 #5 (25%) · 문태섭 Lab 중심" + 우측 "100%" 배지
- 중앙 상부 띠: **SEED — Semantic Evaluation for Visual Brain Decoding**
  - 부제: "22명 평가자 × 1K 이미지쌍 × 22K 판단 = 인간 정합 평가 체계"
  - 3개 지표 카드 (수평 나열):
    - **Object F1**: 핵심 객체 존재 (object detector 기반 precision/recall)
    - **Caption Similarity**: 이미지 캡션 embedding 유사도 (semantic bottleneck)
    - **SEED**: 3개 지표 통합 averaging (object + semantic + perceptual)
  - 하단 참조: "MindEye2, NeuroPictor, UniBrain, MindBridge, BrainGuard 등 SOTA 디코더에 적용"
- 중앙 하부: **Vision-Language Model + TabLeT**
  - 좌: "대규모 뇌영상 기반 Vision-Language Model" (sMRI·DTI·fMRI semantic alignment)
  - 우: "TabLeT — 효율적 토크나이징 + Transformer (장기 시계열 뇌영상)"
- 하단 주석 (작은 글씨): "기존 평가 지표(PixCorr, SSIM, CLIP, EffNet 등)는 인간 판단과 불일치 → SEED로 semantic 정합 평가 확립"

**시각 요소**:
- 상단 SEED 카드 3개 (Cognitive Blue #56B4E9 테두리, 아이콘: ① 객체 ② 텍스트 ③ 레이더 합성)
- 하단 Vision-Language + TabLeT 2개 박스 (SNU Blue 채우기)
- 보라색 세로 bar (문태섭 Lab 색상, 차선 Okabe-Ito 대체 사용)
- 작은 아이콘: 22K 숫자 배지 (Signal Orange)

**구체 내용** (from 문태섭 Lab Google Slides + `data/metrics.yaml criterion_id=5`):
- SEED 저자: Juhyeon Park*, Peter Yongho Kim*, Jiook Cha, Shinjae Yoo, **Taesup Moon†** (교신저자)
- 기관: Seoul National University + Brookhaven National Lab
- 평가 대상 SOTA 디코더: MindEye2 (ICML 24), NeuroPictor (ECCV 24), UniBrain (arXiv 24), MindBridge (CVPR 24), BrainGuard (AAAI 25)
- 발견 failure modes: Semantic Near-Miss Phenomenon, Semantic Detail Confusion
- TabLeT + Vision-Language Model: metrics.yaml criterion_id=5 성과

**데이터 소스**:
- `data/metrics.yaml year3_performance[3]` (criterion_id=5)
- 문태섭 Lab Google Slides (사용자 제공, 2026-04-23)
- `data/achievements.key_technical_models` (TabLeT, Vision-Language Model)

**주의**:
- SEED 논문은 현재 공식 제출본 `achievements.yaml` 17편 목록에 **미포함** (이상아 Lab과 동일 패턴). 사용자 결정: **제출본 그대로 유지**. 슬라이드에서 특정 논문 번호 명시하지 않고 방법·결과 중심 narrative.

**Negative**: 5개 이상 지표 과밀 금지 (3개 SEED 지표로 제한), 원형 다이어그램 금지, 3D 차트 금지

---

## Slide 9 — 동물-사람 종간 파운데이션 · 편도체 공동연구 (평가항목 #4)

**유형**: 비교 · 통합 (Animal × Human + 공동연구 하이라이트)

**핵심 메시지**: 최형진·차지욱 Lab **편도체 표정-뉴런 정서 디코딩 공동연구**로 종간 신경 표상 연결 입증. sMRI·fMRI·EEG·iEEG 파운데이션 모델로 공통 표현 학습 기반 확보.

**레이아웃**:
- 상단: "동물-사람 종간 파운데이션 — 평가항목 #4 · 달성도 100%"
- 상단 highlight 박스 (**신규**): "**편도체 개별신경 × 표정 기반 정서 디코딩** (최형진·차지욱 공동, 2023.10–2025.02)"
  - 좌: "설치류 표정 (안구·입 주위 근육) + 개별 뉴런 앙상블 활동"
  - 우: "편도체 subpopulation이 공포·혐오 카테고리 구별 · negative valence encoding"
  - 발표: "2024.01 iSRC 동계 성과보고회"
- 중앙 좌우 분할:
  - **좌 (Animal 표현 학습)**: 
    - "POYO-SSL (Allen Brain Observatory) · Cell-Pattern-Aware SSL · +12~13%"
    - "Skip-Connection U-Net 디코더 · SSIM 0.593 · Drifting Gratings 55.5%"
  - **우 (Human 표현 학습)**:
    - "SwiFT (UKB+HCP+ABCD 5만명 · 8.8B params) · Power-law"
    - "DIVER-1 (5.3k iEEG + 54k EEG hrs · 17.7k 피험자) · Data-constrained Scaling Law"
- 하단 통합 박스: "**공통 표현 학습**: 구조 (sMRI) · 기능 (fMRI) · 전기생리 (iEEG/EEG) · 행동 (표정·video) 신호의 **Trimodal Alignment** → 종간 파운데이션 모델 핵심 토대"
- 킬러 수치 배지 (우상단): "**5개 세부 연구**" (Signal Orange)

**시각 요소**:
- 상단 공동연구 박스: LAB_VERMIL (최형진) + PALETTE_PINK (차지욱) 2색 세로 bar
- 좌우 박스: 각 Lab 색 코딩
- 하단 통합: SNU Blue 채우기 (강조)
- 모델명 chip (작은 rounded rectangle, 18pt)

**구체 내용** (from `report/03_lab-research-detail.md` §2.3 + §3.1/§3.2):
- 편도체 공동연구 학생: 김유빈, 서정우
- POYO-SSL 분류 뉴런: SST · VIP · PVALB · NTSR1 (왜도·첨도 기준)
- DIVER 3-Phase: Foundation (unlabeled) → Alignment (paired iEEG-Video) → Personalization
- 증빙: 국제 발표 2건, 투고/리뷰 중 2편, 기술개발 1건

**데이터 소스**: 
- `data/metrics.yaml year3_performance[2]` (criterion_id=4)
- 최형진 Lab BK21 자체평가 (공동연구 기술)
- 차지욱 Lab ephys FM 슬라이드 (DIVER 3-Phase)

**Negative**: 대각선 화살표 금지, Quantum 내용 금지 (S10으로 이관), 중첩 3단 계층 금지

**주의**: 편도체 공동연구는 본 과제의 "종간 통합" narrative의 핵심 증거. 구두 발표 강조.

---

## Slide 10 — 확장적 활용 · Quantum ML

**유형**: 나열/분류 (3개 확장 영역)

**핵심 메시지**: BCI / 정신질환 진단 / 예술 전시 + 신기술(Quantum ML) 확장성

**레이아웃**:
- 상단: "확장적 활용 가능성"
- 중앙: 3분면 카드
  - 카드 1: BCI (비침습적 뇌-컴퓨터 인터페이스 디코더)
  - 카드 2: 정신질환 진단 (우울증·조현병 바이오마커)
  - 카드 3: 예술 전시 (실험형 전시 기획)
- 하단: Quantum ML 가로 띠 — Quantum Mario, Quantum Time-series Transformer, Quantum RL

**시각 요소**:
- 상단 3개 카드 (수평 나열)
- 하단 Quantum 영역은 별도 색상 띠 (Cognitive Blue #56B4E9)
- 아이콘: BCI (회로), 진단 (가운), 전시 (프레임), Quantum (원자)

**데이터 소스**: `data/next-year-plan.utilization`, `data/achievements` (Quantum 관련 논문 11, 12, 13)

**Negative**: 4개 이상 확장 영역 금지 (카드 수 ≤4 제한)

---

## Slide 11 — 정량 실적 (Hero Slide)

**유형**: 결론/요약 (초대형 킬러 수치)

**핵심 메시지**: 97.5% 달성 · 17편 논문 · 4건 학회

**레이아웃**:
- 상단: "3차년도 정량 성과" (32pt Bold)
- 중앙: 초대형 킬러 수치 3개 (수평 나열, 각 1/3 영역)
  - 달성도 97.5%
  - 논문 17편
  - 학회참석 4건
  각 수치 아래에 짧은 라벨 (18pt)
- 하단: 4개 평가항목 요약 (작은 텍스트)

**시각 요소**:
- 중앙 수치는 48-64pt Bold Signal Orange
- 수치 위 작은 아이콘 (목표·논문·발표대)
- 배경: 흰 바탕, 강한 대비

**데이터 소스**: `data/metrics.total`, `data/achievements.summary`

**Negative**: 작은 부가 지표 과밀 금지 (3개 수치만 부각), 파이차트 금지

---

## Slide 12 — 4차년도 계획

**유형**: 나열/분류 (5개 아이콘 + 설명)

**핵심 메시지**: 2026년 5개 핵심 방향

**레이아웃**:
- 상단: "4차년도(2026) 연구개발계획 — 예산 600,000천원"
- 중앙: 5개 방향 수평 나열 (각 카드에 아이콘 + 1줄 설명)
  - ① DB 브레인라이프 공개
  - ② 다중 입력 분포 ML 모델
  - ③ 신경과학 메커니즘 two-site 광유전학
  - ④ 사전학습 + 전이학습 성능 검증
  - ⑤ 동물-사람 종간 모델 통합
- 하단: 예산 간단 내역 (직접 468,750 + 간접 131,250 = 600,000천원)

**시각 요소**:
- 5개 번호 카드 (수평 나열)
- 각 카드 아이콘
- 하단 예산 수평 바 (직접/간접 비율 시각화)

**데이터 소스**: `data/next-year-plan.research_directions`, `data/next-year-plan.budget`

**Negative**: 카드 6개 이상 금지 (5개로 제한)

---

## Slide 13 — 기대효과 (4축)

**유형**: 나열/분류 (2×2 매트릭스)

**핵심 메시지**: 학문 · 의과학 · 교육 · 사회산업 4축 효과

**레이아웃**:
- 상단: "연구개발 성과의 기대효과"
- 중앙: 2×2 매트릭스 (4개 사분면)
  - 학문적: UKB·ABCD 급 데이터 공유 → 뇌인지 발달 연구 촉진
  - 의과학: 정신질환 진단·BCI·BCI 디코더
  - 교육: 박사급 인력·인간형 AI
  - 사회산업: 마케팅·엔터테인먼트·소아청소년 자살 예방

**시각 요소**:
- 2×2 그리드 (각 사분면 다른 연한 색상 배경)
- 각 사분면 상단에 큰 카테고리 아이콘

**데이터 소스**: `data/next-year-plan.utilization` (4축)

**Negative**: 5축 이상 금지, 복잡 계층 구조 금지

---

## Slide 14 — Wrap-up / Q&A

**유형**: 결론/요약 (메인 3 takeaway + 감사 메시지)

**핵심 메시지**: 핵심 3줄 요약 + 질의응답 초대

**레이아웃**:
- 상단: "Summary"
- 중앙: 3개 주요 성과 카드
  - 3차년도 달성도 97.5%
  - 멀티스케일 파운데이션 모델 5개 개발
  - 4차년도 예산 600,000천원 확보 · 종간 통합 사전학습 진행
- 하단: "감사합니다 · 질의응답 (Q&A)" + 책임자 기관·도메인 정보만 (개인 연락처 제외)

**시각 요소**:
- 중앙 3개 카드 (SNU Ice 배경)
- 하단 "감사합니다" 큰 글씨 (SNU Blue)
- Q&A 아이콘

**데이터 소스**: `data/metrics.total`, `data/project-meta`

**Negative**: 개인 연락처 기재 금지 (이메일 도메인만 허용)

---

## 일관성 체크리스트 (15장 전체)

- [ ] 모든 슬라이드 snu_neurox 테마 준수
- [ ] 모든 수치 `data/*.yaml` 또는 `report/03_lab-research-detail.md` 추적 가능
- [ ] 97.5% 수치는 Slide 4, 11, 14 3곳에 일관 표기
- [ ] 논문 17편·학회 4건은 Slide 11, 14에 동일 표기
- [ ] 600,000천원은 Slide 3, 12에 일관 표기
- [ ] 평가항목 3 누락 이슈는 Slide 4 하단 주석으로 공식화
- [ ] 페이지 번호: 1/15 ~ 15/15 형식 우하단 (S7A=7/15, S7B=8/15, S8=9/15 ... S14=15/15)
- [ ] 제목 폰트: 32pt Bold SNU Blue (일관)
- [ ] 킬러 메트릭: 32pt+ Bold Signal Orange (일관)
- [ ] 본문: 18pt #282945 (일관)
- [ ] 차지욱 Lab (S7A·S7B): 좌측 Okabe-Ito pink #CC79A7 세로 bar
- [ ] 이상아 Lab (S6 human): 좌측 #11604B teal bar
- [ ] 최형진 Lab (S6 animal): 좌측 #D55E00 vermillion bar
- [ ] 문태섭 Lab (S8): 좌측 #584B9F purple bar
- [ ] S7A·S7B 수치 정합: SwiFT 8.8B · DIVER-1 5.3k+54k · R²=0.96 · +14.4% · +12~13%

## 팀별 기여 매핑 (2026-04-23 updated)

본 과제는 4개 연구팀 공동 수행. Phase 7 (granularity 보강) 후 각 Lab의 granular 내용이 slide-level 반영:

| Lab | 색상 | 전문 영역 | 슬라이드 매핑 | 정리 상태 |
|---|---|---|---|---|
| **이상아 Lab** | #11604B (teal) | 인간 기억·정서 fMRI/EEG, 해마, 공간 탐험 | **Slide 6 human block** | ✅ Google Slides + 제출본 본문 반영 |
| **최형진 Lab** | #D55E00 (vermillion) | 동물 칼슘이미징·광유전학, 섭식·정서 회로 | **Slide 6 animal block** + **Slide 9** (편도체 공동연구) | ✅ BK21 자체평가 + 제출본 본문 반영 |
| **차지욱 Lab** | #CC79A7 (Okabe-Ito pink) | fMRI·EEG·iEEG 파운데이션, 임상 예측, 생성 | **Slide 7A** (fMRI FM) + **Slide 7B** (EEG/iEEG + 임상) | ✅ ephys FM 슬라이드 + 제출본 본문 반영 |
| **문태섭 Lab** | #584B9F (purple, Okabe-Ito 차선) | Vision-Language, SEED, Quantum ML | **Slide 8** (다중 모달리티) | ✅ SEED poster + 제출본 본문 반영 |

### 주요 성과 Highlights (Lab별)

#### 이상아 Lab (Slide 6 human)
- **MixedEmo fMRI/EEG (n=92, 32ch, 2048Hz)**: 편도체·DMN·PCC·precuneus; Posterior/Frontal θ 바이오마커; ACC 복측/배측 해리 p=0.010; STAI-X1 불안 p=0.002, 0.003
- **가상공간 탐험 EEG**: 4개 랜드마크 조건, reactivation bias, 디코딩 10-15% (chance 4%), *Imaging Neuroscience* Lim 2025
- **해마 OCAT**: CA23DG·CA1 맥락 범주화; 청소년 CA23DG-OFC 발달·정서적 학대 결여

#### 최형진 Lab (Slide 6 animal + Slide 9)
- **3D 골격 DB**: DeepLabCut · 자유 행동 설치류 · 4+ 행동 분류
- **VTA-NAc Two-site**: DAT-cre · AAV5-ChrimsonR + AAV9-GRAB_DA1h · 594nm · fiber photometry
- **편도체 정서 디코딩 (차지욱 공동)**: 표정 × single-neuron ensemble · negative valence

#### 차지욱 Lab (Slide 7A + 7B, 2 슬라이드)
- **S7A fMRI FM**: SwiFT 8.8B params + 5만명 Power-law · SwiFT-IO R²=0.96 · MBBN ADHD/ASD 주파수별 SOTA · NeuroMamba HCP 94.9%+FLOPs -46.5% · TabLeT CVPR 심사
- **S7B EEG/iEEG + 임상**: DIVER-1 5.3k iEEG+54k EEG hrs · First Ephys Scaling Law · Language-Brain +14.4% · POYO-SSL +12~13% SSIM 0.593 · RYM F1=0.9 · Polygenic-informed 임상 예측

#### 문태섭 Lab (Slide 8)
- **SEED** (Juhyeon Park* · Peter Yongho Kim* · Taesup Moon† corresponding, SNU+Brookhaven): Object F1 + Cap-Sim + EffNet · **22K 판단** (22명 × 1K 이미지쌍) · 5 SOTA 디코더 (MindEye2/NeuroPictor/UniBrain/MindBridge/BrainGuard) · failure modes (Semantic Near-Miss, Detail Confusion)
- **VLM**: LLaVA-Next-Interleave · CLIP-ViT UKB 0.94 · BLIP-2 vs LLaVA 비교 · Simple QnA > CoT
- **Quantum Time-series Transformer**: Unitary Temporal Embedding + LCU + QSVT · ADHD multi-system involvement

### 논문 · 제출본 정합성 이슈 (공식화됨)

`achievements.yaml`의 17편 공식 레퍼런스 목록에는 각 Lab의 대표 연구 논문이 **모두 포함되지는 않음**:
- 이상아 Lab 4편 (Lim 2025/8 *Imaging Neuroscience*, Kim 2025/11 *iScience*, Lee 2025/11 *Neuropsychologia*, Koo 2026/1 *Scientific Reports*)
- 문태섭 Lab SEED 논문 (ICLR 2026 심사 중)
- 최형진 Lab BK21 신규 논문 (CeA-Glp1R, LH CaMKIIα+, NAc-NPY 등)

사용자 결정: **제출본 그대로 유지** (achievements.yaml 불변). 슬라이드에서는 논문 번호 명시 없이 **방법·결과 중심 narrative**로 전달. 평가단이 구체 논문을 질의하면 구두로 보완.

---

## 축약 옵션 (사용자 요청 시)

**10장 버전으로 축소할 경우**:
- Slide 3 (로드맵) + Slide 4 (목표) 통합
- Slide 8 (다중 모달리티) + Slide 9 (종간) 통합
- Slide 10 (확장 활용) 삭제 또는 Slide 13 (기대효과)에 통합
- Slide 14 (Wrap-up) 삭제, Slide 11 (정량 실적)로 대체

축약 후: 1, 2, 3+4, 5, 6, 7, 8+9, 11, 12, 13 = 10장
