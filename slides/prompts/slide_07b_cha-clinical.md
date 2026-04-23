# S7B Prompt — 차지욱 Lab ② EEG/iEEG 파운데이션 + 임상·생성 응용

## API Configuration
- model: gemini-3.1-flash-image-preview (nanobanana2)
- resolution: 4K · aspect_ratio: 16:9 · thinking_mode: high · language: ko

## Rendering Rule (Phase 10)
- 발견 중심 · 명사형 종결 · AI hype 금지
- 3 행 구조, 각 행은 헤드라인 + 도식 + 2-3 핵심 bullet

## Prompt for nanobanana

16:9 horizontal Korean infographic, #FFFFFF background.

**Header**: "디코딩과제 3년차" 14pt #003380.

**Title (32pt Bold #003380)**: "차지욱 Lab ② — EEG/iEEG 파운데이션 + 임상·생성 응용"
**Subtitle (18pt #0072B2)**: "평가항목 제2·제4번 · 달성도 100% · 전기생리 사전학습의 멱법칙 스케일링 경향 보고"

**Left accent bar**: #CC79A7 · 8px.

**Top-right Hero 2단**:
- 상단 "대규모 전기생리 코퍼스" 14pt Bold #003380
- 하단 "iEEG 5,300시간 + EEG 54,000시간 · 17,700명" 10pt Bold #E69F00

**Row 1 — DIVER-1 파운데이션 (세로 약 34%)**:
- 배경 #EDF6FC, 마커 ① 18pt Bold #003380
- 헤드라인 16pt Bold #003380: "전기생리 사전학습의 멱법칙 스케일링과, 학습 반복 수 > 모델 크기 관계 관찰함"
- **가로 diagram (전폭 60%)**: **DIVER 3-Phase 흐름** — 3 개 연결 블록 (①사전학습 / ②정렬 / ③개인화) · 각 블록에 작은 아이콘 (전극 / 얼굴-뇌파 연결 / 사용자 피드백)
- 우측 3 bullets 11pt #282945:
  - "• 1,300만 param 모델이 BrainBERT (43M) · PopT (63M) 과 유사·개선 성능을 보임"
  - "• 컴퓨팅 1e20 FLOPs (GPT-1 대비 2배 · 전기생리 선행 최대 규모 대비 77배)"
  - "• Neuroprobe 15 과제 · FACED · PhysioNet-MI · MentalArithmetic 일관 결과 · 학습 반복 수 (epochs) > params · ICLR 2026 심사"

**Row 2 — 교차 모달 정렬 (세로 약 24%)**:
- 배경 #EDF6FC, 마커 ② 18pt Bold #003380
- 헤드라인 14pt Bold #003380: "언어 이해 뇌 활동의 의미 통합을 인공지능 정렬 성능으로 재현함"
- **좌 반쪽 — Language-Brain Alignment**:
  - 아이콘: 말풍선 + 뇌
  - "• **+14.4%p** 정확도 개선 · 선행 모델 (Antonello et al.) 대비 개선"
  - "• Damasio 수렴-발산 영역 이론이 정량 재현됨 · ICLR 2026 심사"
- **우 반쪽 — POYO-SSL (동물 칼슘)**:
  - 아이콘: 칼슘 세포 + 영화 프레임
  - "• **+12~13%p** 성능 향상 · SSIM 0.593 을 관찰함"
  - "• Allen Brain Observatory · 이질 세포 군집을 학습 신호로 활용함 · ICLR 2026 심사"

**Row 3 — 임상 · 생성 응용 (세로 약 22%)**:
- 배경 #EDF6FC, 마커 ③ 18pt Bold #003380
- 헤드라인 14pt Bold #003380: "개인별 정서 상태를 뇌전도·심전도로 디코딩하고, 유전형을 결합한 임상 예측으로 확장함"
- 3 chips (각 flat line 아이콘 + 짧은 텍스트 11pt #282945):
  - **아이콘 (음표 + 이미지 프레임)**: "RYM — EEG → Stable Diffusion + MusicGen · F1 = 0.9 · 9명 × 2세션"
  - **아이콘 (VR 헤드셋)**: "CEBRA 경외 + 내수용감각 · VR 360° + IS-RSA · *Communications Psychology* 2025"
  - **아이콘 (DNA 나선)**: "유전형 기반 임상 예측 · 청소년 우울증 · 주의력결핍 과잉행동장애 (ADHD) · 아동 polygenic risk"

**Bottom band** (전폭, 10pt #282945, 연한 라벤더 #EFEAF7, italic):
"주관: 서울대 차지욱 · 국외 공동: 프린스턴 Uri Hasson · 브룩헤이븐 Shinjae Yoo"

**Bottom-right**: "8 / 15" 12pt #5A5A6E.

## Style Rules
- Row 1 DIVER 3-Phase diagram 이 시각 앵커
- Row 2/3 의 아이콘은 flat line · 평면 실루엣 (실제 이모지 아닌 아이콘 렌더)
- 차지욱 Lab 분홍 accent bar 좌측

## Negative
- 실제 이모지 문자 렌더 금지 (아이콘으로만)
- AI hype 금지 · "...했다" 금지 · 3차원 효과 금지

## Review Status
PHASE 10 v1 (시각 축약)
