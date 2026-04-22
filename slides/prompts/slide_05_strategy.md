# S5 Prompt — 연구개발 추진전략 (5단계 플로우)

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
- Layout: 5-step horizontal process flow

## Prompt for nanobanana2

Create a 16:9 horizontal Korean process flow infographic on #FFFFFF background.

Top-left header: "디코딩과제 3년차" in 14pt #003380.

Title at top-center: "연구개발 추진전략" in 32pt Bold #003380.

Main area: 5 numbered rounded rectangle cards horizontally arranged, connected by straight horizontal arrows in #003380 (no curves, no diagonals). Each card has #EDF6FC fill and thin outline.

Card 01: Label "데이터 생성" in 22pt Bold #003380, description below "동물·사람 신경과학 DB" in 14pt #282945. Number "01" in 32pt Bold #0072B2 at card top-left.

Card 02: "데이터 전처리" / "정제 · 표준화" / "02"

Card 03: "디코더 학습 · 검증" / "맥락화 지각 디코딩 모델" / "03"

Card 04: "파운데이션 모델" / "개발 · 검증" / "04"

Card 05: "모델 확장 · 활용" / "질환 예측 · 예술 전시" / "05" (this card gets #E69F00 accent outline instead of #0072B2 to mark the application stage)

Bottom legend area (small 14pt #5A5A6E): 4 tiny color squares in a row with labels. Use the HEX colors exactly as given, do NOT interpret color names.
- [swatch #11604B] "이상아 Lab (인간 기억·정서)"
- [swatch #D55E00] "최형진 Lab (동물 신경)"
- [swatch #CC79A7] "차지욱 Lab (ML foundation)"
- [swatch #584B9F] "문태섭 Lab (Vision-Language · SEED)"

Bottom-right: "5 / 15" in 12pt #5A5A6E.

## Style Rules
- 5 cards in horizontal row with straight arrows between them
- Card 05 emphasized with Signal Orange outline
- Team legend at bottom uses 4 team colors as small color swatches

## Consistency Lock
snu_neurox theme, straight arrows only.

## Negative
- no circular flow, no curved arrows, no diagonal connectors, no 3D steps, no complex team diagrams

## Fallback Layout
If 5-card flow + team legend fails:
- Remove team legend, keep only the 5-step flow
- Or reduce to 3 cards + "..." indicator

## Self-Validation
- [x] 5 horizontal cards with arrows
- [x] Word count ≤ 400
- [x] Colors ≤ 5 core (team colors are small swatches only)
- [x] Complexity: MED

## Review Status
READY
