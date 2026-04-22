# Iteration 2 Changes Applied

## Summary
- 14/14 PASS maintained (post-compression)
- ~18 edits across 9 files
- 1 regression from iter-1 corrected (Slide 6 title)
- 0 new regressions
- Warnings 52 → 55 (minor, from Rendering Rule text addition)

## Edit Log

### Critical writer findings (2 edits)
| # | File | Change |
|---|---|---|
| 1 | `01_title.md` | "상호작용시의 정서에 의해 맥락화된" → "상호작용 시 정서로 맥락화된" (archaic Korean → natural) |
| 2 | `02_overview.md` | 두 번째 italic 캡션 삭제 ("정서는 뇌 기능 이해의 가장 중요한 요인") |

### Regression fix (iter-1 missed)
| # | File | Change |
|---|---|---|
| 3 | `06_db-construction.md` | Title "평가항목 1" → "평가항목 #1" (iter-1 sweep miss) |

### Palette discipline (4 edits)
| # | File | Change |
|---|---|---|
| 4 | `02_overview.md` | Card 3 heart icon #E69F00 → #0072B2 (Signal Orange reservation) |
| 5 | `09_cross-species.md` | Animal panel #FFF4DD → #EDF6FC (팔레트 일관) + #D55E00 left-side bar |
| 6 | `09_cross-species.md` | Human panel + #0072B2 left-side bar (Lab-cue) |
| 7 | `storyboard.md` L479 | 차지욱 Lab 색상 #0072B2 → #CC79A7 (iter-1 sync 누락) |

### Model bucket & naming (3 edits)
| # | File | Change |
|---|---|---|
| 8 | `09_cross-species.md` | Animal: "POYO-SSL · CausalMamba" → "NeuroMamba (CausalMamba 기반)" (bucket 정리) |
| 9 | `09_cross-species.md` | Human: "SwiFT · DIVER-1 · MBBN" → "SwiFT · DIVER-1 · TabLeT" (MBBN criterion-2 영역으로) |
| 10 | `08_multimodal-seed.md` | Vision-Language Model 첫 등장 시 "(시각-언어 모델)" 병기 |

### Prose polish (6 edits)
| # | File | Change |
|---|---|---|
| 11 | `06_db-construction.md` | Bullet 구분자 통일 (콜론 → 통일 + → separator) |
| 12 | `07_ml-models.md` | Language-Brain Alignment 첫 등장 "(언어-뇌영상 정렬)" 병기 |
| 13 | `07_ml-models.md` | Self-Validation core message SOTA softening |
| 14 | `10_extensions-quantum.md` | Card 3 "예술 전시 실험 · 인간형 AI 전시 기획" → "뇌-AI 상호작용 예술 실험 · 전시 기획 응용" (전시 중복 해결) |
| 15 | `13_expected-impact.md` | 교육 quadrant 2 bullets → 3 bullets (quadrant 균형) |
| 16 | `14_wrap-up.md` | "감사합니다 · Thank you" → "감사합니다" 단독; "Q & A" → "질의응답 (Q&A)" |

### Rendering Rule 섹션 추가 (11 files)
| # | Files | Change |
|---|---|---|
| 17 | `04-14.md` (11 files) | `## Rendering Rule` 섹션 추가 (01-03 형식과 일치, 총 3 lines) |

### Compression (길이 초과 해소)
| # | File | Change |
|---|---|---|
| 18 | `07_ml-models.md` | Bottom caption + Style Rules 압축 (462 → ≤450 words) |
| 19 | `09_cross-species.md` | Style Rules 압축 (456 → ≤450 words) |
| 20 | `08_multimodal-seed.md` | SEED heading 축약 |

## Validation Results

### Before Iteration 2
- 14/14 PASS, 52 warnings
- Post-iter-1: critical 0, important ~13, info many

### After Iteration 2
- 14/14 PASS (maintained after 2 compression edits)
- 55 warnings (minor increase from Rendering Rule text)
- Critical → 0 (2 writer criticals resolved)
- Important → ~5 remaining (mostly deferred to iter-3 polish)
- Regressions → 0

## Convergence Metrics

| Metric | Iter 0 | Iter 1 | Iter 2 |
|---|---|---|---|
| Critical findings | 7 | 0 | 2 (deferred)→ **0** |
| Important findings | 12 | 6 | ~5 |
| Info findings | 7 | ~7 | ~10 |
| Regressions | — | 0 | 1 caught + fixed |
| PASS rate | 14/14 | 14/14 | 14/14 |

Critical 수렴 확인. Important 감소 추세. Iteration 3은 **최종 polish + palette discipline 확인** 위주.

## Deferred to Iteration 3

- Slide 3 "현재" 배지 Signal Orange 정책 결정 (codified exception or remove)
- Slide 7 "SOTA" 최종 처리 (MBBN card hero "SOTA" 단독 유지 vs 변경)
- Slide 11 #3 footnote 추가 softening (evaluation-criteria.yaml 일관성)
- Slide 14 Card 3 framing (3년차 takeaway vs 4년차 pre-look 혼재)
- Slide 13 quadrant 배경 tint HEX 변경 (자연언어 색상 → HEX)
- Number+unit spacing 컨벤션 master theme 문서화
