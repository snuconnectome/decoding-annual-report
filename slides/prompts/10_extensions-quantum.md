# S10 Prompt — 확장적 활용 · Quantum ML

## API Configuration
- model: gemini-3.1-flash-image-preview
- resolution: 4K (3840x2160)
- aspect_ratio: 16:9
- thinking_mode: high
- language: ko

## MASTER THEME (snu_neurox)
- Layout: 3 application cards top, Quantum ML band bottom

## Prompt for nanobanana2

Create a 16:9 horizontal Korean infographic on #FFFFFF background.

Top-left header: "디코딩과제 3년차" in 14pt #003380.

Title: "확장적 활용 가능성" in 32pt Bold #003380.
Subtitle: "개발 모델의 다양한 응용 분야" in 22pt #0072B2.

Upper main area (55% of slide height): 3 equal-sized rounded rectangle cards horizontally arranged.

Card 1 — BCI:
- Icon top: flat line circuit / brain-with-chip symbol in #0072B2
- Title: "BCI 디코더" in 22pt Bold #003380
- Body in 18pt #282945: "비침습적 뇌-컴퓨터 인터페이스 · 운동·언어 신경보철 응용"

Card 2 — 정신질환 진단:
- Icon: flat medical symbol in #0072B2
- Title: "정신질환 바이오마커" in 22pt Bold #003380
- Body: "우울증 · 조현병 등 · 증상기반 진단체계의 한계 극복"

Card 3 — 예술 전시:
- Icon: flat frame / exhibition symbol in #0072B2
- Title: "실험형 전시" in 22pt Bold #003380
- Body: "예술 전시 실험 · 인간형 AI 전시 기획"

Lower band (30% of slide height): a single horizontal banner with #56B4E9 (Cognitive Blue) light fill, showing "Quantum ML 확장" section.

Banner title in 22pt Bold #003380 (left-aligned): "신기술 확장 — Quantum Machine Learning"

Below title, a single horizontal row of 3 compact chips/labels:
- "Quantum Mario" — scalable Quantum RL
- "Quantum Time-series Transformer" — resting-state fMRI
- "Hybrid Quantum RL" — explainable Quantum

Each chip in 14pt #282945 on #FFFFFF background with thin #56B4E9 outline.

Bottom-right: "10 / 14" in 12pt #5A5A6E.

## Style Rules
- 3 application cards equal width
- Quantum ML band uses Cognitive Blue (#56B4E9) light fill to distinguish category
- Chips are thin-bordered rectangles, not full cards

## Consistency Lock
Same card styling as other slides.

## Negative
- no 4th application card (keep to 3)
- no photorealistic exhibition images, no quantum atom renderings with orbits, no 3D effects
- no circular diagrams

## Fallback Layout
If card + band fails:
- Simplify to 3 cards only, drop Quantum band

## Self-Validation
- [x] Single core message: "3대 응용 분야 + Quantum ML 신기술 확장"
- [x] Word count ≤ 400
- [x] Colors ≤ 5 (+ #56B4E9 sixth color only for Quantum band)
- [x] Complexity: MED

## Review Status
READY
