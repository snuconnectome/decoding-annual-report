# S12 Prompt — 4차년도 연구개발계획

## API Configuration
- model: gemini-3.1-flash-image-preview
- resolution: 4K (3840x2160)
- aspect_ratio: 16:9
- thinking_mode: high
- language: ko

## MASTER THEME (snu_neurox)
- Layout: 5 direction cards horizontal + budget bar below

## Prompt for nanobanana2

Create a 16:9 horizontal Korean forward-plan infographic on #FFFFFF background.

Top-left header: "디코딩과제 3년차" in 14pt #003380.

Title: "4차년도(2026) 연구개발계획" in 32pt Bold #003380.
Subtitle: "예산 600,000천원 · 5개 핵심 방향" in 22pt #E69F00.

Main area (55% of slide height): 5 numbered compact cards arranged horizontally with equal spacing. Each card has #EDF6FC fill, thin #0072B2 outline, small icon + number at top.

Card 01:
- Icon: flat database/cylinder in #0072B2
- Title: "DB BrainLife 공개" in 18pt Bold #003380
- 1-line desc: "자연환경 지각·정서 DB 오픈" in 14pt #282945

Card 02:
- Icon: flat network/graph
- Title: "다중 입력 분포 ML"
- Desc: "동일종 다중 모달리티 디코더 검증"

Card 03:
- Icon: flat light/beam (two-site 광유전학)
- Title: "신경과학 메커니즘"
- Desc: "two-site 광유전학 · 칼슘이미징"

Card 04:
- Icon: flat layered box (foundation)
- Title: "파운데이션 전이학습"
- Desc: "대규모 사전학습 + 전이 성능 검증"

Card 05:
- Icon: flat connected-species symbol
- Title: "동물-사람 종간 통합"
- Desc: "종간 파운데이션 모델 사전학습"

Bottom area (25% of slide height): horizontal budget bar (single bar, 300px height).

- Left 78% (direct): SNU Blue #003380 fill with white label inside "직접비 468,750천원" in 18pt Bold white
- Right 22% (indirect): Neural Teal #0072B2 fill with white label "간접비 131,250천원" in 18pt Bold white
- Above bar, right-aligned total: "합계 600,000천원" in 22pt Bold #E69F00

Below bar, small 14pt #5A5A6E: "주요 항목: 인건비 64,896 · 학생인건비 189,520 · 연구활동비 95,081 · 연구수당 51,352 · 장비비 32,000 · 재료비 35,901 (단위: 천원)"

Bottom-right: "12 / 14" in 12pt #5A5A6E.

## Style Rules
- 5 compact cards horizontally
- Single stacked budget bar showing direct/indirect split

## Consistency Lock
snu_neurox theme, numbered cards match Slide 5.

## Negative
- no 6th direction card (strict 5-only)
- no pie chart for budget
- no nested budget breakdowns
- no photorealistic scientific images

## Fallback Layout
If 5-card + bar fails:
- Reduce to 5 vertical labels on left + budget bar on right

## Self-Validation
- [x] Single core message: "2026 5개 방향 + 600,000천원"
- [x] Word count ≤ 400
- [x] Colors ≤ 5
- [x] Complexity: MED

## Review Status
READY
