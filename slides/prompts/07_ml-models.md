# S7 Prompt — 기계학습 모델 성과 · 차지욱 Lab 중심

## API Configuration
- model: gemini-3.1-flash-image-preview
- resolution: 4K (3840x2160)
- aspect_ratio: 16:9
- thinking_mode: high
- language: ko

## MASTER THEME (snu_neurox)
- Layout: 4 model cards with hero metric numbers (2x2 grid)

## Prompt for nanobanana2

Create a 16:9 horizontal Korean technical-results infographic on #FFFFFF background.

Top-left header: "디코딩과제 3년차" in 14pt #003380.

Title: "기계학습 모델 — 평가항목 2 (25%)" in 32pt Bold #003380.
Subtitle: "차지욱 Lab 중심 · SOTA 성능 달성" in 22pt #0072B2.

Top-right: circular badge "100%" in 48pt Bold #E69F00, label "달성도" in 14pt #5A5A6E.

Main area: 2×2 grid of 4 equal-sized rounded rectangle cards. Each card has #EDF6FC fill, thin #0072B2 outline, 24px padding.

Card top-left — SwiFT-IO:
- Icon (top): minimal line icon representing brain + signal
- Model name: "SwiFT-IO" in 22pt Bold #003380
- Hero metric: "R² = 0.96" in 32pt Bold #E69F00 (centered)
- Description: "fMRI 파운데이션 모델 · 정서·언어·인지 예측 SOTA" in 14pt #282945

Card top-right — POYO-SSL:
- Model name: "POYO-SSL" in 22pt Bold #003380
- Hero metric: "+12 ~ 13%" in 32pt Bold #E69F00
- Description: "칼슘이미징 Cell-Pattern-Aware SSL · 동적 시각 디코딩" in 14pt #282945

Card bottom-left — 언어-뇌영상 정렬:
- Model name: "Language-Brain Alignment" in 22pt Bold #003380
- Hero metric: "+14.4%" in 32pt Bold #E69F00
- Description: "언어-뇌영상 semantic 정렬 · 정서 예측 성능 향상" in 14pt #282945

Card bottom-right — MBBN:
- Model name: "MBBN" in 22pt Bold #003380
- Hero metric: "SOTA" in 32pt Bold #E69F00
- Description: "Frequency-Specific Multi-Band Attention for fMRI" in 14pt #282945

Bottom caption (small 14pt #5A5A6E, left-aligned): "증빙: 국제 발표 1건, 리뷰 중 2편, 출판 예정 1편 · 총 4개 세부 연구 통합"

Bottom-right: "7 / 14" in 12pt #5A5A6E.

## Style Rules
- 2×2 grid, equal cards
- Hero metrics in 32pt Signal Orange centered in each card
- Model name above, description below hero metric

## Consistency Lock
Same card styling as Slide 4, Signal Orange for killer metrics.

## Negative
- no line charts (too dense for 4 models with different axes)
- no 3D bars, no pie chart
- no photorealistic ML diagrams

## Fallback Layout
If 2×2 + detailed metrics fails:
- Reduce to 4 cards in a single horizontal row with model name + single metric each

## Self-Validation
- [x] Single core message: "4개 모델 모두 SOTA 성능 달성"
- [x] Word count ≤ 400
- [x] Colors ≤ 5
- [x] Complexity: MED

## Review Status
READY (awaiting 차지욱 Lab specific additions from user)
