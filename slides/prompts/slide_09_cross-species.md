# S9 Prompt — 동물-사람 종간 파운데이션 모델

## API Configuration
- model: gemini-3.1-flash-image-preview
- resolution: 4K (3840x2160)
- aspect_ratio: 16:9
- thinking_mode: high
- language: ko

## Rendering Rule
- Text with pt size + color specifications → RENDER in image
- Design instructions (layout, positioning) → DO NOT render, follow as structure guide

## MASTER THEME (snu_neurox)
- Layout: Animal vs Human side-by-side + unified integration box below

## Prompt for nanobanana2

Create a 16:9 horizontal Korean integration infographic on #FFFFFF background.

Top-left header: "디코딩과제 3년차" in 14pt #003380.

Title: "뇌영상-파운데이션 모델 — 평가항목 #4 (25%)" in 32pt Bold #003380.
Subtitle: "동물-사람 종간 파운데이션 모델의 토대 확립" in 22pt #0072B2.

Top-right: "100%" circular badge (48pt Bold #E69F00), small label "달성도".

Hero metric strip at right side of title area: "5개 세부 연구" in 22pt Bold #E69F00.

Main upper area (50% of slide height): 2 rounded rectangle panels side by side with equal width.

LEFT panel — 동물 트랙:
- Background: #EDF6FC
- Left-side 4px vertical bar in #D55E00 (vermillion, Lab-color cue)
- Icon top: flat mouse silhouette in #D55E00
- Title: "동물 (Animal)" in 22pt Bold #003380
- Body bullets in 18pt #282945:
  - "대규모 행동 · 신경신호 데이터"
  - "사전학습 → 전이학습 디코딩"
  - "NeuroMamba (CausalMamba 기반)"

RIGHT panel — 사람 트랙:
- Background: #EDF6FC
- Left-side 4px vertical bar in #0072B2 (Neural Teal)
- Icon top: flat human profile in #0072B2
- Title: "사람 (Human)" in 22pt Bold #003380
- Body bullets in 18pt #282945:
  - "대규모 다중 모달리티 (휴지기 / 과제 / 영화 / 자연자극)"
  - "fMRI · sMRI · EEG 통합"
  - "SwiFT · DIVER-1 · TabLeT"

Lower area (30% of slide height): a single wide unified panel spanning full width with #003380 fill and white text:
- Title: "공통 표현 학습 기반" in 22pt Bold white
- Body: "구조 · 기능 · 전기생리 신호 통합 → 종간 파운데이션 모델 핵심 토대 확보" in 18pt white

Bottom-left 14pt #5A5A6E: "증빙: 국제 발표 2 · 투고·리뷰 중 2 · 기술개발 1"

Bottom-right: "10 / 15" in 12pt #5A5A6E.

## Style Rules
- 2 panels + 1 unified panel · SNU Blue inversion for integration · max 3 bullets.

## Consistency Lock
Same card styling as Slides 6, 8.

## Negative
- no 3-level nested hierarchy
- no diagonal arrows
- no photorealistic mice/humans
- no circular integration diagrams

## Fallback Layout
If upper 2-panel + lower 1-panel fails:
- Use 3 stacked horizontal bands: Animal, Human, Integrated

## Self-Validation
- [x] Single core message: "동물·사람 트랙 통합 → 종간 파운데이션 토대"
- [x] Word count ≤ 400
- [x] Colors ≤ 5
- [x] Complexity: MED

## Review Status
READY
