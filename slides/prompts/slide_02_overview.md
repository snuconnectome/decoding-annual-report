# S2 Prompt — 연구 개요 (Contextualized 지각 디코딩)

## API Configuration
- model: gemini-3.1-flash-image-preview
- resolution: 4K (3840x2160)
- aspect_ratio: 16:9
- thinking_mode: high
- language: ko
- max_word_count: 400

## Rendering Rule
- Text with pt size + color specifications → RENDER in image
- Design instructions (layout, positioning) → DO NOT render

## MASTER THEME (snu_neurox)
- Background: #FFFFFF
- Palette: #003380, #E69F00, #0072B2, #282945, #EDF6FC
- Layout: 3-step horizontal flow (structure diagram type)

## Prompt for nanobanana2

16:9 horizontal Korean conceptual infographic, #FFFFFF background, 3-stage horizontal flow.

Top-left: "디코딩과제 3년차" 14pt #003380.

Title: "본 연구의 핵심 개념" 32pt Bold #003380 centered.
Subtitle: "정서에 의해 맥락화된 지각의 디코딩" 22pt #0072B2.

Center 60%: 3 equal rounded rectangle cards horizontally spaced, #EDF6FC fill with thin #0072B2 outline. Each card has flat-line icon on top, Bold label 22pt #003380 middle, 18pt #282945 description bottom.

Card 1 (eye+ear icon): "외부환경" / "시각·청각·복합 자극"
Card 2 (brain icon): "뇌의 능동적 추론" / "불완전 감각 → 예측 → 내부 표상 갱신"
Card 3 (heart icon in #0072B2): "정서에 의한 맥락화" / "신체 반응 유도"

Between cards: straight horizontal arrows pointing right (no curves, no diagonals).

Bottom caption centered 18pt #282945: "기존 디코딩은 수동적 지각에 국한 → 본 연구는 능동적 추론과 정서 맥락을 반영"

Bottom-right: "2 / 15" 12pt #5A5A6E.

## Style Rules
- Background white, three equally-sized cards
- Straight horizontal arrows only (NO curves, NO diagonals)
- Icons are minimal flat silhouettes
- Card icon on top, label middle, description bottom
- Equal whitespace between cards

## Consistency Lock
Identical card style, arrow style, typography, and color usage as other slides in the deck.

## Negative
- no curved arrows, no circular flow diagrams, no 3D, no glossy, no photorealistic icons, no stock photos, no gradients on text, no complex nested structures

## Fallback Layout
If 3-card flow fails:
- Reduce to 3 large text blocks with dividers instead of cards
- Remove icons if they fail to render cleanly

## Self-Validation
- [x] Single structure: 3 cards + 2 arrows
- [x] Single core message: "환경 → 뇌 → 정서" 개념 한 장 전달
- [x] Word count ≤ 400
- [x] Colors ≤ 5
- [x] Icons ≤ 3 (eye, brain, heart)
- [x] Complexity: LOW

## Review Status
READY
