# S7A Prompt — fMRI 파운데이션 모델 ①

## API Configuration
- model: gemini-3.1-flash-image-preview (nanobanana2)
- resolution: 4K · aspect_ratio: 16:9 · thinking_mode: high · language: ko

## Rendering Rule (Phase 10)
- 발견 중심 헤드라인 · 수치/모델명 단독 금지
- 명사형 종결 · AI hype 금지
- 각 카드에 아이콘·도식 중앙 배치, 텍스트는 헤드라인 + 2 bullet

## Prompt for nanobanana

16:9 horizontal Korean infographic, #FFFFFF background.

**Header**: "디코딩과제 3년차" 14pt #003380.

**Title (32pt Bold #003380)**: "기능적 자기공명영상 (fMRI) 파운데이션 모델 ①"
**Subtitle (18pt #0072B2)**: "평가항목 제2·제4번 · 달성도 100% · UKB+HCP+ABCD 약 5만명 사전학습으로 범용 뇌 표상 확보"

**Left accent bar**: #CC79A7 · 8px.

**Top-right Hero 2단**:
- 상단 "대규모 뇌영상 사전학습" 13pt Bold #003380
- 하단 "UKB + HCP + ABCD 약 5만명 · 88억 파라미터" 10pt Bold #E69F00

**Main 2×2 grid** (#EDF6FC 배경, 얇은 #0072B2 테두리, 각 카드 아이콘·도식 좌상단):

**카드 1 — SwiFT**:
- 아이콘: 평면 뇌 + 오름차순 계단
- 헤드라인 14pt Bold #003380: "스케일 확대가 다운스트림 성능 개선으로 이어짐을 관찰함"
- **중앙 소형 그래프**: 로그-로그 축 (X: params, Y: loss) · 4 점 (37M → 118M → 1.2B → 8.8B) 직선 하강 · 끝점 라벨 "88억"
- 2 bullets 11pt #282945:
  - "• 최대 업데이트 파라미터화 (muP) 로 거대 모델 안정 학습"
  - "• HCP 성별 분류 선행 모델 대비 7.6%p 개선 · 알츠하이머 전환·통증·항우울 예측에서 선행 연구 대비 개선"

**카드 2 — SwiFT-IO**:
- 아이콘: 영화 프레임 + 뇌 파형
- 헤드라인 14pt Bold #003380: "영화 시청 중 연속 정서가를 개인 단위 회귀하는 모델을 확립함"
- 핵심 수치 "R² = 0.96" 22pt Bold #E69F00
- **중앙 도식**: 수평 축 (−0.2 ~ 1.0) 위에 두 점 — LSTM 기준선 R² ≈ −0.14 (좌측) · SwiFT-IO R² = 0.96 (우측 끝) · 0.0 기준선 점선
- 2 bullets 11pt #282945:
  - "• Perceiver IO 인코더 결합 · Sequence-to-Sequence 출력"
  - "• HBN 677명 × 약 12분 · CCN 2025"

**카드 3 — MBBN**:
- 아이콘: 3층 주파수 파형
- 헤드라인 14pt Bold #003380: "ADHD 연결성 장애가 주파수 대역별로 분리됨을 관찰함"
- **중앙 도식 3 수평 띠**: 고주파 (실행기능) · 저주파 (운동지각·사회인지) · 초저주파 (내장감각) — 3 띠 우측에 단일 "ADHD ↔ 정상" 대비 쌍
- 2 bullets 11pt #282945:
  - "• ASD 고주파 언어·주의·작업기억·사회인지 변화 일관"
  - "• *Communications Biology* 2026.1 출판 예정"

**카드 4 — NeuroMamba**:
- 아이콘: 감소 화살표 + 기어
- 헤드라인 14pt Bold #003380: "상태공간 모델로 연산 비용 절반, 분류 성능 소폭 개선을 관찰함"
- 핵심 수치 "94.9%" 22pt Bold #E69F00 + "FLOPs −46.5%" 12pt #E69F00
- 2 bullets 11pt #282945:
  - "• Mamba2 + 신경방사장 (NeRF, Neural Radiance Fields) 주파수 위치 인코딩"
  - "• HCP 성별 분류 · 선행 SwiFT 92.9% · NeuroSTORM 93.3% 대비 소폭 개선"

**Bottom band** (전폭, 10pt #282945, 연한 민트 #E7F0ED):
"**TabLeT** (2D DCAE 토크나이저) · UKB 8,178 + HCP 1,061 + ADHD-200 533 · CVPR 심사 중  |  **잠재 확산 트랜스포머** · 3D VQ-GAN · 4D 시공간 fMRI 생성"

**Bottom-right**: "7 / 14" 12pt #5A5A6E.

## Style Rules
- 각 카드 중앙에 작은 도식 (그래프·게이지·띠·아이콘) — 텍스트 밀도 감축 시각 앵커
- flat line minimal · SNU Blue / Neural Teal / Signal Orange 팔레트

## Negative
- 3D 효과 금지 · 사진사실 금지 · 카툰 스타일 금지
- AI hype 금지 · 약어 단독 금지

## Review Status
PHASE 10 v1 (시각 축약)
