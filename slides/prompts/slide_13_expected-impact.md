# S13 Prompt — 기대효과 (4축 매트릭스)

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
- Layout: 2×2 quadrant matrix

## Prompt for nanobanana2

Create a 16:9 horizontal Korean impact infographic on #FFFFFF background.

Top-left header: "디코딩과제 3년차" in 14pt #003380.

Title: "연구개발 성과의 기대효과" in 32pt Bold #003380.
Subtitle: "4개 축의 사회적·학문적 파급" in 22pt #0072B2.

Main area (center 75% of slide height): 2×2 equal-sized quadrant cards. Each quadrant has a distinct very light background tint and a top-left icon + category label.

Top-left quadrant (학문적):
- Light background: #EDF6FC (SNU Ice)
- Icon: flat graduation cap or book
- Category label: "학문적 효과" in 22pt Bold #003380
- 3 bullets in 18pt #282945:
  - "BrainLife 공유 · UKB · ABCD급 데이터 공유 촉진"
  - "정서 디코딩 후속연구 · 인지신경과학 메커니즘"
  - "아동 뇌인지 발달 · 성인 뇌노화 궤적 연구 적용"

Top-right quadrant (의과학):
- Light background: #FDECE2 (peach, D55E00 tint 10%)
- Icon: flat medical cross
- Category label: "의과학 기술 효과" in 22pt Bold #003380
- 3 bullets:
  - "정신질환 바이오마커 발굴 (재현 · 일반화)"
  - "비침습적 BCI 디코더 원천기술"
  - "개인 맞춤형 정신질환 치료 기여"

Bottom-left quadrant (교육):
- Light background: #E7F0ED (11604B tint 10%)
- Icon: flat lightbulb
- Category label: "교육적 효과" in 22pt Bold #003380
- 3 bullets:
  - "신경과학·초거대 AI 융합 박사급 인력 양성"
  - "윤리·가치 정렬형 인간형 AI 연구 기반"
  - "국제 공동연구 · 연구자 교류 네트워크"

Bottom-right quadrant (사회산업):
- Light background: #EFEAF7 (lavender, 584B9F tint 10%)
- Icon: flat factory/chart symbol
- Category label: "사회·산업적 효과" in 22pt Bold #003380
- 3 bullets:
  - "마케팅 · 엔터테인먼트 선호 예측 기술"
  - "소아청소년 정신건강 조기개입 도구"
  - "공공 안전 AI 응용 가능성 확보"

Bottom-right: "13 / 14" in 12pt #5A5A6E.

## Style Rules
- Equal 2×2 quadrants · 4 soft tint backgrounds · max 3 noun-phrase bullets.

## Consistency Lock
snu_neurox theme, same card sizing discipline as Slide 4.

## Negative
- no 5th quadrant, no complex hierarchy
- no overlapping regions, no Venn diagram
- no photorealistic images (graduation, hospital, factory)

## Fallback Layout
If 2×2 fails:
- Stack 4 horizontal bands instead

## Self-Validation
- [x] Single core message: "4축 기대효과"
- [x] 4 quadrants with 2-3 bullets each
- [x] Word count ≤ 400
- [x] Colors ≤ 5 (quadrant tints are very light, derived from palette)
- [x] Complexity: MED

## Review Status
READY
