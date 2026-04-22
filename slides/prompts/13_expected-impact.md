# S13 Prompt — 기대효과 (4축 매트릭스)

## API Configuration
- model: gemini-3.1-flash-image-preview
- resolution: 4K (3840x2160)
- aspect_ratio: 16:9
- thinking_mode: high
- language: ko

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
  - "UKB · ABCD급 대규모 데이터 공유 촉진"
  - "한국인 특이 신경과학 지식 획득 기여"
  - "파운데이션 모델 → 뇌인지 메커니즘 연구 가속"

Top-right quadrant (의과학):
- Light background: very light peach/cream
- Icon: flat medical cross
- Category label: "의과학 기술 효과" in 22pt Bold #003380
- 3 bullets:
  - "정신질환 바이오마커 발굴 (재현 · 일반화)"
  - "비침습적 BCI 디코더 원천기술"
  - "개인 맞춤형 정신질환 치료 기여"

Bottom-left quadrant (교육):
- Light background: very light green tint
- Icon: flat lightbulb
- Category label: "교육적 효과" in 22pt Bold #003380
- 2 bullets:
  - "신경과학 초거대 인공지능 박사급 인력 양성"
  - "인간형 AI: 자주적 윤리·도덕·심리 탑재"

Bottom-right quadrant (사회산업):
- Light background: very light purple/lavender tint
- Icon: flat factory/chart symbol
- Category label: "사회·산업적 효과" in 22pt Bold #003380
- 3 bullets:
  - "마케팅 · 엔터테인먼트 선호도 예측"
  - "소아청소년 자살 예방 상담 도구"
  - "자살·범죄 예방 AI 기술 응용"

Bottom-right: "13 / 14" in 12pt #5A5A6E.

## Style Rules
- Equal-sized 2×2 quadrants
- 4 distinct soft-tint backgrounds to differentiate categories
- Max 3 bullets per quadrant
- Short noun-phrase bullets (no long sentences)

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
