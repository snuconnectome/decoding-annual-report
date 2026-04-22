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

Subtitle below title: "4개 평가항목 · 각 25% · 합계 달성도 97.5%" in 22pt #0072B2.

Main area (central 70% of slide): 2×2 grid of 4 rounded rectangle cards with equal sizes. Each card has #EDF6FC fill, thin #0072B2 outline, 24px padding.

Top-left card (평가항목 #1):
- Top-left corner: [25%] badge in 22pt Bold on circular #E69F00 background (white text inside)
- Card center title: "뇌-환경 상호작용 데이터베이스 구축" in 22pt Bold #003380
- Small subtitle: "평가항목 #1 · 세부목표 1-1, 1-2" in 14pt #5A5A6E

Top-right card (평가항목 #2):
- [25%] badge
- Title: "기계학습 모델 개발 및 검증" in 22pt Bold #003380
- Subtitle: "평가항목 #2 · 세부목표 1-3, 1-4" in 14pt #5A5A6E

Bottom-left card (평가항목 #4):
- [25%] badge
- Title: "뇌영상-파운데이션 기계학습 모델" in 22pt Bold #003380
- Subtitle: "평가항목 #4 · 세부목표 2-1, 2-2" in 14pt #5A5A6E

Bottom-right card (평가항목 #5):
- [25%] badge
- Title: "다중 모달리티 통합 모델" in 22pt Bold #003380
- Subtitle: "평가항목 #5 · 세부목표 2-3" in 14pt #5A5A6E

Bottom annotation (small 12pt #5A5A6E, left-aligned): "※ 5개년 기준 6개 평가항목(#1·#2·#3·#4·#5·#6) 중 3차년도 active 4개(#1·#2·#4·#5)에 가중치 100% 재분배 · #3 신경과학 메커니즘(10%)은 4차년도 개시 예정"

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
