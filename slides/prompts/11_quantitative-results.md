# S11 Prompt — 정량 실적 (Hero Slide)

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
- Layout: 3 oversized hero metrics horizontally aligned

## Prompt for nanobanana2

Create a 16:9 horizontal Korean hero-metric infographic on #FFFFFF background.

Top-left header: "디코딩과제 3년차" in 14pt #003380.

Title: "3차년도 정량 성과" in 32pt Bold #003380.

Subtitle below: "2025-01-01 ~ 2025-12-31 실적" in 18pt #5A5A6E.

Main area (center 70% of slide height): 3 giant hero metrics horizontally spaced with equal distance. No cards or boxes around them — pure typography on white.

LEFT metric:
- Tiny icon at top: flat "target" / checkmark symbol in #0072B2
- Giant number: "97.5%" in 120pt Black Bold #E69F00 (Signal Orange)
- Below number: "합계 달성도" in 22pt #003380
- Tiny caption under label: "4개 평가항목 × 가중치 100%" in 14pt #5A5A6E

CENTER metric:
- Tiny icon at top: flat document/paper symbol in #0072B2
- Giant number: "17" in 120pt Black Bold #E69F00
- Small unit: "편" in 32pt Bold #003380 positioned to the right of "17" baseline
- Below: "논문" in 22pt #003380
- Caption: "국제 저널 중심" in 14pt #5A5A6E

RIGHT metric:
- Tiny icon at top: flat microphone/speaker symbol in #0072B2
- Giant number: "4" in 120pt Black Bold #E69F00
- Small unit: "건" in 32pt Bold #003380 to the right
- Below: "학회참석" in 22pt #003380
- Caption: "국제 학술대회" in 14pt #5A5A6E

Vertical thin separators (very light #A0A0A0, 1px) between the 3 metric blocks.

Bottom strip (small 14pt #5A5A6E, left-aligned): "3차년도 active 평가항목 4개(#1·#2·#4·#5) 전수 달성도 100% · 평가항목 #3은 4차년도 개시 예정"

Bottom-right: "11 / 14" in 12pt #5A5A6E.

## Style Rules
- Minimal: white background + 3 huge numbers
- Signal Orange ONLY for the 3 giant numbers
- No decorative boxes — pure typographic impact

## Consistency Lock
Signal Orange reserved for killer metrics only (consistent with other slides).

## Negative
- no additional supporting metrics (strict 3-only)
- no pie charts, no bar charts, no cluttered data points
- no 3D numbers, no gradients, no metallic effects
- no photorealistic icons

## Fallback Layout
If 3-column layout fails:
- Stack vertically: 97.5% on top, 17편 and 4건 side by side below

## Self-Validation
- [x] Single core message: "97.5% · 17편 · 4건"
- [x] Only 3 hero metrics (no clutter)
- [x] Word count ≤ 400
- [x] Colors ≤ 5
- [x] Complexity: LOW

## Review Status
READY
