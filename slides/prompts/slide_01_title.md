# S1 Prompt — Title Slide (타이틀)

## API Configuration
- model: gemini-3.1-flash-image-preview
- resolution: 4K (3840x2160)
- aspect_ratio: 16:9
- thinking_mode: high
- language: ko
- max_word_count: 400

## Rendering Rule
- Text with pt size + color specifications → RENDER in image
- Text in Fallback Layout / Self-Validation sections → DO NOT render, context only
- Design instructions (layout, positioning, arrows) → DO NOT render, follow as structure guide

## MASTER THEME (snu_neurox)
- Background: #FFFFFF (white)
- Core palette: #003380 (SNU Blue, headings) · #E69F00 (Signal Orange, hero metrics) · #0072B2 (Neural Teal, secondary) · #282945 (text) · #EDF6FC (SNU Ice, card fill)
- Card system: rounded rectangle, thin outline, soft fill, no heavy shadow
- Icon system: flat line/silhouette icons only
- Layout: 16:9 widescreen, 0.7in margin, intentional whitespace

## Prompt for nanobanana2

16:9 horizontal Korean cover infographic, #FFFFFF background.

Top-left: "디코딩과제 3년차" 14pt #003380.

Upper 35%: large bold Korean title centered, 32pt Bold #003380:
"동물-사람 멀티스케일 신경과학 파운데이션 모델 기반 뇌-외부환경 상호작용 시 정서로 맥락화된 지각의 디코딩"

Below in 22pt #0072B2 centered: "Affect-contextualized perception decoding with cross-species multiscale neuroscience foundation model"

Bottom 40%: single horizontal rounded rectangle card, #EDF6FC fill, thin #0072B2 outline, 3 rows in 18pt #282945:
- 연구책임자: 차지욱 (서울대학교, 부교수)
- 과제번호: RS-2023-00265406 · 기간: 2023.07 — 2027.12 (54개월)
- 3차년도 (2025) · 예산: 453,500천원 · 주관: 과학기술정보통신부 · 한국연구재단

Top-right: flat-style single brain silhouette icon in #0072B2, generous whitespace around.

Bottom-right: "1 / 15" 12pt #5A5A6E.

No photorealistic images, no 3D, no gradients on text.

## Style Rules
- snu_neurox theme, 5-color palette, Pretendard Korean font, generous whitespace, 4.5:1 contrast.

## Consistency Lock
Same visual grammar as other 13 slides.

## Negative
- no dark bg, no 3D, no glossy, no poster, no gradients, no photorealistic icons, no multiple brain images.

## Fallback Layout
- Remove brain icon, center meta card, split title at "맥락화된".

## Self-Validation
- [x] Single structure: title + meta card + decorative icon
- [x] Single core message: "과제 메타 정보 한 눈에 전달"
- [x] Text density controlled
- [x] Word count ≤ 400 (Prompt for nanobanana2 section)
- [x] Colors ≤ 5 (+ text_secondary)
- [x] Icons ≤ 4 (1 brain icon)
- [x] Complexity: LOW

## Review Status
READY
