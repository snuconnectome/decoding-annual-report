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
- **렌더 절대 금지**: hex 색상 코드 (예 #D55E00) · pt 크기 표기 (예 14pt) · "Bold" 같은 스타일 마커 · 의미 없는 한글 음절 조합 — 모두 디자인 지시이므로 시각적으로 텍스트로 그리지 말 것

## MASTER THEME (snu_neurox)
- Layout: horizontal timeline with diamond markers

## Prompt for nanobanana2

Create a 16:9 horizontal Korean timeline infographic on background for a 5-year R&D roadmap.

Top-left header: "디코딩과제 3년차" in.

Title at top-center: "5개년 연구개발 로드맵" in .

Subtitle below title: "2023.07 ~ 2027.12 (54개월)" in.

Center main area: one horizontal thin line in (the timeline axis) spanning 80% of slide width. On this line, place 5 evenly-spaced diamond markers, each 40×40 pixels.

- Marker 1 (leftmost): Neural Teal, label above "1차년도 (2023.07-12)"
- Marker 2:, label above "2차년도 (2024)"
- Marker 3 (CENTER, HIGHLIGHTED): Signal Orange, LARGER (60×60 pixels), with a small "현재" pill ( fill, white text, , rounded) floating above the marker. Label above: "3차년도 (2025)"
- Marker 4:, label above "4차년도 (2026)"
- Marker 5 (rightmost):, label above "5차년도 (2027)"

Below each marker (approx below the timeline axis), place a small rounded rectangle card with fill, thin outline, containing:

Card 1: 예산 "3억원 (300,000천원)" in , below it "대규모 데이터 자동화 실험 환경 구축" in
Card 2: "4.535억원 (453,500천원)" + "고정 환경 지각 데이터베이스"
Card 3 (HIGHLIGHTED, outline instead of): "4.535억원 (453,500천원)" + "변동 환경 데이터베이스 + 다중 모달리티 기계학습 모델"
Card 4: "6억원 (600,000천원)" + "BrainLife 플랫폼 데이터 공개 · 종간 사전학습"
Card 5: "6억원 (600,000천원)" + "전이학습 검증 · 실험형 예술 전시"

Bottom-right: "3 / 14" in.

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
