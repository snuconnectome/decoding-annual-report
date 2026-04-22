# Iteration 1 Changes Applied

## Summary
- 14/14 PASS maintained after fixes
- 13 distinct edits across 7 files (+ storyboard)
- 0 validation regressions
- Warnings stable (52 total, mostly color-count informational)

## Edit Log

### Critical fixes (7 edits)

| # | File | Change |
|---|---|---|
| 1 | `prompts/08_multimodal-seed.md` | "평가항목 4 (25%)" → "평가항목 #5 (25%)" |
| 2 | `prompts/09_cross-species.md` | "평가항목 3 (25%)" → "평가항목 #4 (25%)" |
| 3 | `prompts/11_quantitative-results.md` | Bottom strip reframed: "누락 이슈" → "평가항목 #3은 4차년도 개시 예정" |
| 4 | `prompts/04_year3-goals.md` | Cards ①②③④ → "평가항목 #1/#2/#4/#5" + 세부목표 중복 제거 (card 4: 2-1,2-2 → 2-3) + 하단 주석 강화 |
| 5 | `prompts/14_wrap-up.md` | "5 종" → "5개", 모델 리스트 정정 (SwiFT · DIVER-1 · NeuroMamba · TabLeT) |
| 6 | `prompts/14_wrap-up.md` | "600M" → "6억원" + 라벨 "600,000천원" 병기 |
| 7 | `prompts/14_wrap-up.md` | "connectome Lab" 제거 (data에 없는 fabrication) |

### Important fixes (6 edits)

| # | File | Change |
|---|---|---|
| 8 | `prompts/05_strategy.md` | Team legend 자연언어 색상명 ("green", "orange") 제거, [swatch HEX] 패턴으로 |
| 9 | `prompts/05_strategy.md` | 차지욱 Lab 색상 #0072B2 → #CC79A7 (Okabe-Ito pink, Neural Teal 충돌 해소) |
| 10 | `prompts/07_ml-models.md` | Subtitle "SOTA 성능 달성" → "4개 모델 성능 향상 (벤치마크 대비 최고)" |
| 11 | `prompts/07_ml-models.md` | SwiFT-IO / MBBN 카드 description softening ("SOTA" 단독 사용 제한) |
| 12 | `prompts/12_year4-plan.md` | Subtitle 색상 #E69F00 → #0072B2 (Signal Orange reservation 준수) |
| 13 | `prompts/13_expected-impact.md` | "한국인 특이 신경과학" → YAML backed bullets; "자살·범죄 예방" → "공공 안전 AI 응용" |

### Storyboard 동기화

| # | File | Change |
|---|---|---|
| 14 | `storyboard.md` L264 | "평가항목 4 (25%)" → "평가항목 #5 (25%)" (Slide 8 section) |
| 15 | `storyboard.md` L309 | "평가항목 3 (25%)" → "평가항목 #4 (25%)" (Slide 9 section) |

## Validation Results

### Before iteration 1
- 14/14 PASS, 52 warnings
- 4 critical convergent findings unresolved

### After iteration 1
- 14/14 PASS (maintained)
- 52 warnings (unchanged, mostly color-count informational)
- All 7 critical items resolved
- All 6 priority important items resolved
- 7 important + 7 info items deferred to Iteration 2/3

## Deferred Items for Iteration 2

- Slide 6 bullet 조사·parallelism 정리
- Slide 1 "상호작용시의" → "상호작용 시"
- Number+unit spacing 컨벤션 통일
- Slide 14 "Q & A", "감사합니다·Thank you" 처리
- Slide 9 #FFF4DD cream tint 팔레트 정리
- Slide 2 두 캡션 정리
- Slide 3 "현재" 배지 Signal Orange 사용 검토
- Slide 7 Lab color marker 강화
- Rendering Rule 섹션 일관성

## Convergence Indicator

Iteration 1이 **critical severity를 0으로 감소**시킴 (7 → 0). 수렴 진행 중. Iteration 2는 important를 주 target.
