# S4 Prompt — 3차년도 평가 구조

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
- Layout: 2x2 grid of cards with weight badges

## Prompt for nanobanana2

Create a 16:9 horizontal Korean infographic on #FFFFFF background showing 3rd-year evaluation structure.

Top-left header: "디코딩과제 3년차" in 14pt #003380.

Title at top-center: "3차년도 평가 구조" in 32pt Bold #003380.

Subtitle below title: "4개 평가항목 · 각 비중 25% · 합계 달성도 97.5%" in 22pt #0072B2.

Main area (central 70% of slide): 2×2 grid of 4 rounded rectangle cards with equal sizes. Each card has #EDF6FC fill, thin #0072B2 outline, 24px padding.

Top-left card (평가항목 제1번):
- Top-left corner: "비중 25%" badge in 18pt Bold on circular #E69F00 background (white text inside)
- Card center title: "뇌-환경 상호작용 데이터베이스 구축" in 20pt Bold #003380
- Small subtitle: "평가항목 제1번 · 세부목표 1-1 (동물) + 1-2 (사람)" in 12pt #5A5A6E

Top-right card (평가항목 제2번):
- "비중 25%" badge
- Title: "기계학습 모델 개발 및 검증" in 20pt Bold #003380
- Subtitle: "평가항목 제2번 · 세부목표 1-3 (행동-신경 통합) + 1-4 (모달리티 융합)" in 12pt #5A5A6E

Bottom-left card (평가항목 제4번):
- "비중 25%" badge
- Title: "뇌영상 파운데이션 (Foundation) 모델" in 20pt Bold #003380
- Subtitle: "평가항목 제4번 · 세부목표 2-1 (동일종) + 2-2 (사람 다중 모달)" in 12pt #5A5A6E

Bottom-right card (평가항목 제5번):
- "비중 25%" badge
- Title: "다중 모달리티 통합 모델" in 20pt Bold #003380
- Subtitle: "평가항목 제5번 · 세부목표 2-3 (통합 디코더)" in 12pt #5A5A6E

Bottom annotation (small 11pt #5A5A6E, left-aligned): "※ 5개년 기준 평가항목 6개 (제1·2·3·4·5·6번) 중 3차년도 활성 4개 (제1·2·4·5번) 에 비중 100% 재분배 · 평가항목 제3번 '신경과학 메커니즘 규명' (비중 10%) 은 4차년도 (2026) 개시 예정"

Bottom-right: "4 / 14" in 12pt #5A5A6E.

## Style Rules
- Equal-sized cards in 2×2 grid
- Each card has a circular [25%] badge in Signal Orange
- Numbered circles ①②③④ small badge also acceptable

## Consistency Lock
snu_neurox theme, card styling, Signal Orange for killer metrics only.

## Negative
- no pie chart (4 equal slices is uninteresting)
- no 3D cards
- no complex table rendering

## Fallback Layout
If 2×2 grid fails:
- Stack 4 cards vertically on left, weight badges on right

## Self-Validation
- [x] 4 cards with equal weights 25%
- [x] Single core message: "평가 구조 한 눈에"
- [x] Word count ≤ 400
- [x] Colors ≤ 5
- [x] Complexity: LOW

## Review Status
READY
