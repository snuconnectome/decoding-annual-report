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
- **렌더 절대 금지**: hex 색상 코드 (예 #D55E00) · pt 크기 표기 (예 14pt) · "Bold" 같은 스타일 마커 · 의미 없는 한글 음절 조합 — 모두 디자인 지시이므로 시각적으로 텍스트로 그리지 말 것

## MASTER THEME (snu_neurox)
- Layout: 5-step horizontal process flow

## Prompt for nanobanana2

Create a 16:9 horizontal Korean process flow infographic on background.

Top-left header: "디코딩과제 3년차" in.

Title at top-center: "연구개발 추진전략" in .

Main area: 5 numbered rounded rectangle cards horizontally arranged, connected by straight horizontal arrows in (no curves, no diagonals). Each card has fill and thin outline.

Card 01: Label "데이터 생성" in , description below "동물·사람 신경과학 DB" in. Number "01" in at card top-left.

Card 02: "데이터 전처리" / "정제 · 표준화" / "02"

Card 03: "디코더 학습 · 검증" / "맥락화 지각 디코딩 모델" / "03"

Card 04: "파운데이션 모델" / "개발 · 검증" / "04"

Card 05: "모델 확장 · 활용" / "질환 예측 · 예술 전시" / "05" (this card gets accent outline instead of to mark the application stage)

Bottom legend area (small): 4 tiny color squares in a row with labels. Use the HEX colors exactly as given, do NOT interpret color names.
- [swatch] "인간 기억·정서 · 기능적 자기공명영상 (fMRI)·뇌전도 (EEG)"
- [swatch] "동물 칼슘이미징 · 광유전학"
- [swatch] "fMRI·뇌전도 파운데이션 모델"
- [swatch] "시각-언어 모델 · 시맨틱 평가 (SEED)"

Bottom-right: "5 / 14" in.

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
