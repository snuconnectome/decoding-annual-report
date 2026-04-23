# S7A Prompt — 차지욱 Lab ① fMRI 파운데이션 모델

## API Configuration
- model: gemini-3.1-flash-image-preview (nanobanana2)
- resolution: 4K (3840x2160) · aspect_ratio: 16:9 · thinking_mode: high · language: ko

## Rendering Rule (Phase 9)
- 발견 중심 헤드라인 (수치/모델명 단독 금지)
- 약어 풀이 + 수치 의미 부기
- 명사형 종결 ("...함"), AI hype ("세계 최초"·"최고"·"능가") 금지
- 진중한 관찰자 어조 (`docs/narrative-style-guide.md` 준수)

## Prompt for nanobanana

16:9 horizontal Korean infographic, #FFFFFF background.

**Header (좌상단)**: "디코딩과제 3년차" 14pt #003380.

**Title (28pt Bold #003380)**: "기능적 자기공명영상 (fMRI) 신호의 대규모 사전학습으로 범용 뇌 표상 확보"
**Subtitle (16pt #0072B2)**: "차지욱 Lab ① · 평가항목 제2·제4번 · 달성도 100%"

**Left accent bar** (전체 세로): #CC79A7 (차지욱 Lab) · 8px.

**Hero (우상단 2단)**: 상단 "대규모 뇌영상 사전학습 · 범용 표상 확보" 13pt Bold #003380, 하단 "영국 바이오뱅크 + 인간 커넥톰 + 청소년기 뇌 인지 발달 코호트 통합 약 5만명" 10pt Bold #E69F00.

**Main 2×2 grid** (#EDF6FC 배경, 얇은 #0072B2 테두리):

**카드 1 — SwiFT 파운데이션**:
- 헤드라인 14pt Bold #003380: "뇌영상 파운데이션 모델의 스케일 확대가 다운스트림 성능 개선으로 일관되게 이어짐을 관찰함"
- 본문 11pt #282945:
  - "스윈-트랜스포머 기반 fMRI 파운데이션 모델 (SwiFT) 을 4단계 확장 (3,700만 → 1억 1,800만 → 12억 → 88억 파라미터)"
  - "각 단계에서 손실이 로그-로그 선형으로 감소하는 멱법칙 경향이 관찰됨"
  - "최대 업데이트 파라미터화 (muP) 로 거대 모델의 안정 학습이 가능함을 확인함"
  - "성별 분류·알츠하이머병 전환·통증 상태·항우울 치료반응 예측에서 선행 모델 (BrainLM, Brain-JEPA) 대비 개선된 성능을 관찰함 — 인간 커넥톰 프로젝트 (HCP) 성별 분류에서 선행 모델 대비 7.6%p 의 절대 정확도 개선"

**카드 2 — SwiFT-IO 시계열 디코딩**:
- 헤드라인 14pt Bold #003380: "영화 시청 중 연속 정서가를 fMRI 신호로부터 개인 단위 회귀하는 모델을 확립함"
- 본문 11pt #282945:
  - "Perceiver IO 인코더를 결합하여 Sequence-to-Sequence 출력이 가능함"
  - "장단기기억 (LSTM, Long Short-Term Memory) 기준선이 결정계수 R² 음수 수준 (평균 예측보다 나쁨) 에 머물던 과제에서 R² = 0.96 (결정계수 범위 0~1, 1.0이 이론적 상한) 의 설명력을 보임"
  - "Healthy Brain Network 코호트 영화 시청 fMRI · 677명 × 약 12분 · 인지신경과학 학술대회 (CCN, Cognitive Computational Neuroscience) 2025 발표"

**카드 3 — MBBN 주파수 분리**:
- 헤드라인 14pt Bold #003380: "주의력결핍 과잉행동장애의 연결성 장애가 주파수 대역별로 분리되어 나타남을 관찰함"
- 본문 11pt #282945:
  - "fMRI 신호를 주파수 대역으로 분리해 학습하는 다중 주파수 대역 뇌 네트워크 (MBBN) 구축"
  - "고주파: 실행기능 / 저주파: 운동지각·사회인지 / 초저주파: 내장감각·항상성"
  - "자폐스펙트럼장애에서는 고주파 언어·주의·작업기억·사회인지 영역의 변화가 일관되게 관찰됨"
  - "Communications Biology · 2026.1 출판 예정"

**카드 4 — NeuroMamba 효율화**:
- 헤드라인 14pt Bold #003380: "상태공간 모델로 fMRI 사전학습의 연산 비용을 절반 가까이 줄이면서도 분류 성능을 소폭 개선함을 관찰함"
- 본문 11pt #282945:
  - "Mamba2 + 신경방사장 (NeRF, Neural Radiance Fields) 기반 주파수 위치 인코딩"
  - "인간 커넥톰 프로젝트 (HCP) 성별 분류 정확도 94.9% · 선행 SwiFT 92.9% · NeuroSTORM 93.3% 와 유사하거나 개선된 수준을 보임"
  - "부동소수점 연산량 (FLOPs) 46.5% 감소 (연산 효율 약 2배 개선)"

**Bottom band** (전폭, 11pt #282945, 연한 민트 #E7F0ED):
"**TabLeT** (2차원 딥 압축 오토인코더 기반 fMRI 토크나이징 + 트랜스포머): 영국 바이오뱅크 8,178명 · HCP 1,061명 · 주의력결핍 과잉행동장애 데이터셋 (ADHD-200) 533명 · 컴퓨터비전·패턴인식 학술대회 (CVPR) 심사 중   ·   **잠재 확산 트랜스포머**: 3차원 VQ-GAN + 잠재 확산 · 4차원 시공간 fMRI 생성 시도"

**Bottom-right**: "7 / 15" 12pt #5A5A6E.

## Negative
- "세계 최초", "최고", "압도", "능가" (rhetorical) 금지
- "...했다" 종결 금지 (명사형 사용)
- 약어 단독, 수치 단독 헤드라인 금지

## Review Status
PHASE 9 v1 (review iteration 0)
