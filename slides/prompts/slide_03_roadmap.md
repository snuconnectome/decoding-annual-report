# S3 Prompt — 5개년 로드맵 (타임라인)

## API Configuration
- model: gemini-3.1-flash-image-preview
- resolution: 4K (3840x2160)
- aspect_ratio: 16:9
- thinking_mode: high
- language: ko
- max_word_count: 400

## Rendering Rule
- Text with pt size + color specifications → RENDER
- Design instructions → DO NOT render

## MASTER THEME (snu_neurox)
- Layout: horizontal timeline with diamond markers

## Prompt for nanobanana2

Create a 16:9 horizontal Korean timeline infographic on #FFFFFF background for a 5-year R&D roadmap.

Top-left header: "디코딩과제 3년차" in 14pt #003380.

Title at top-center: "5개년 연구개발 로드맵" in 32pt Bold #003380.

Subtitle below title: "2023.07 ~ 2027.12 (54개월)" in 18pt #5A5A6E.

Center main area: one horizontal thin line in #003380 (the timeline axis) spanning 80% of slide width. On this line, place 5 evenly-spaced diamond markers, each 40×40 pixels.

- Marker 1 (leftmost): #0072B2 Neural Teal, label above "1차년도 (2023.07-12)"
- Marker 2: #0072B2, label above "2차년도 (2024)"
- Marker 3 (CENTER, HIGHLIGHTED): #E69F00 Signal Orange, LARGER (60×60 pixels), with a small "현재" pill (#E69F00 fill, white text, 14pt Bold, 8px rounded) floating 8px above the marker. Label above: "3차년도 (2025)"
- Marker 4: #0072B2, label above "4차년도 (2026)"
- Marker 5 (rightmost): #0072B2, label above "5차년도 (2027)"

Below each marker (approx 40px below the timeline axis), place a small rounded rectangle card with #EDF6FC fill, thin #0072B2 outline, containing:

Card 1: Budget "300,000천원" in 18pt Bold #003380, below it "빅데이터 자동화 실험환경" in 14pt #282945
Card 2: "453,500천원" + "고정 환경 지각 DB"
Card 3 (HIGHLIGHTED, outline #E69F00 instead of #0072B2): "453,500천원" + "변동 환경 DB + 멀티 모달리티 ML"
Card 4: "600,000천원" + "BrainLife 공개 · 종간 사전학습"
Card 5: "600,000천원" + "전이학습 검증 · 실험형 전시"

Bottom-right: "3 / 15" in 12pt #5A5A6E.

## Style Rules
- Single horizontal axis line
- Diamond markers, NOT circles
- 3차년도 marker emphasized with Signal Orange + larger size + "현재" badge
- Equal horizontal spacing between markers

## Consistency Lock
Reuse the snu_neurox theme typography and card style.

## Negative
- no circular timeline, no 3D timeline, no glossy, no photorealistic markers, no complex milestone icons

## Fallback Layout
If markers-with-cards layout fails:
- Simplify to horizontal axis + 5 labeled nodes only (no cards)
- Keep year3 highlighted

## Self-Validation
- [x] Single timeline axis
- [x] 5 evenly-spaced markers with year 3 emphasized
- [x] Word count ≤ 400
- [x] Colors ≤ 5
- [x] Complexity: MED

## Review Status
READY
