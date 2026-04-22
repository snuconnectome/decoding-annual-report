# Plan: Phase 5 — 스토리보드 + Gemini 프롬프트 (14장)

## Hypothesis

Phase 2에서 구조화된 `data/*.yaml` 5개 + Phase 1의 추출 자료를 기반으로, `infographics` 스킬(Gemini Flash Image Preview / nanobanana2)이 요구하는 정확한 구조의 프롬프트 14개를 작성하면, Phase 6에서 자동화된 단일 실행으로 품질 높은 한국어 평가단 발표 슬라이드 시리즈를 생성할 수 있다.

**핵심 원리**: 슬라이드 품질은 **프롬프트 품질**이 70% 결정. 프롬프트 품질은 **사전 설계된 스토리보드**가 70% 결정. 따라서 스토리보드에 집중.

## Expected Outcomes

| 지표 | 목표 |
|---|---|
| 스토리보드 문서 | 1 (14장 상세 설계) |
| 프롬프트 파일 | 14 (`slides/prompts/01_*.md ~ 14_*.md`) |
| 테마 | `snu_neurox` (SNU Blue + Okabe-Ito 색맹 안전) |
| Aspect ratio | 16:9 |
| 단일 슬라이드 프롬프트 단어 수 | ≤ 400 |
| `prompt_constraints.py` 통과 | 14/14 |
| 작업 시간 | ≤ 2시간 |

## Design

### 테마 결정: `snu_neurox`

- Primary: SNU Blue `#003380` (headings)
- Accent: Signal Orange `#E69F00` (hero metrics만)
- Secondary: Neural Teal `#0072B2` (subheadings, diagrams)
- Text: SNU Dark `#282945`
- Background: White `#FFFFFF`
- Colorblind-safe (8% 남성 색각이상 대응)
- Header logo: "디코딩과제 3년차" 14pt
- Slide number: bottom-right 12pt

### 슬라이드 유형 매핑 (14장)

| # | 슬라이드 | 유형 | YAML 데이터 소스 |
|---|---|---|---|
| 1 | 타이틀 | cover | project-meta.yaml |
| 2 | 연구 개요 (contextualized 지각) | 구조/아키텍처 | project-meta + Phase1 p11 |
| 3 | 5개년 로드맵 | 타임라인 | project-meta.period + evaluation-criteria |
| 4 | 3차년도 목표 (평가항목 테이블) | 데이터 | evaluation-criteria.yaml |
| 5 | 추진전략 다이어그램 | 구조/아키텍처 | next-year-plan.strategy |
| 6 | DB 구축 성과 | 나열/분류 | metrics.yaml criterion_id=1 |
| 7 | 기계학습 모델 성과 | 데이터 (막대차트) | achievements.key_technical_models + metrics 2 |
| 8 | 다중 모달리티 모델 | 구조/아키텍처 | metrics.yaml criterion_id=5 |
| 9 | 동물-사람 종간 | 비교 (Animal vs Human) | metrics.yaml criterion_id=4 |
| 10 | 확장적 활용 + Quantum ML | 나열/분류 | achievements (Quantum Mario 등) |
| 11 | 정량 실적 (97.5%, 17편, 4건) | 결론/요약 (킬러 수치) | metrics.total + achievements.summary |
| 12 | 4차년도 계획 | 나열/분류 | next-year-plan.research_directions |
| 13 | 기대효과 (4축) | 나열/분류 | next-year-plan.utilization |
| 14 | Wrap-up / Q&A | 결론/요약 | (반복 재사용) |

### 슬라이드 수 재평가

14장은 평가단 발표(보통 15-30분) 관점에서 적절 범위(권장 ≤20장). 각 장 1-1.5분 할당 가정.

만약 10장으로 축소 권장 시: 슬라이드 3 (로드맵)과 4 (목표)를 합치고, 슬라이드 8 (다중모달리티)를 슬라이드 7에 통합 가능. 현재는 **상세 version 14장**으로 진행. 사용자 요청 시 축소.

### 프롬프트 구조 (infographics 스킬 규약)

각 `slides/prompts/NN_*.md`는 다음 섹션 포함:

1. **API Configuration** — 테마에서 자동
2. **Rendering Rule** — 고정 규칙
3. **MASTER THEME** — snu_neurox
4. **Prompt for nanobanana2** — ⭐ 핵심 (≤400 words)
5. **Style Rules** — 테마 자동
6. **Consistency Lock** — 테마 자동
7. **Negative** — 테마 자동
8. **Fallback Layout** — 슬라이드별 설계
9. **Self-Validation** — 체크리스트
10. **Review Status** — READY 표기

### Hard Constraints (infographics 스킬)

- 총 단어 수 (Prompt 섹션) ≤ 400
- 색상 수 ≤ 5
- 아이콘 수 ≤ 4
- 복잡도 LOW or MED
- 핵심 메시지 1개/슬라이드

## Risks & Mitigation

| 위험 | 영향 | 대응 |
|---|---|---|
| 한글 400+ 단어 초과 시 렌더링 실패 급증 | 높 | 각 프롬프트 작성 후 단어 수 자동 검증 |
| 수치 오류 (97.5% vs 95% 등) | 높 | YAML에서 직접 인용, 프롬프트에 `{{metrics.total.achievement_percent}}` 형식 주석 |
| 14장 style drift | 중 | `Consistency Lock` 섹션 + 동일 테마 전 슬라이드 적용 |
| 평가항목 3 누락 이슈 노출 | 중 | Slide 4·11에서 "평가항목 1, 2, 4, 5 (재분배 25%×4)" 명시, 주석 언급 |
| Gemini API 비용 | 낮 | 14 × 1 variant ≈ $3-5. 재생성 2-3회 포함 총 $10-20 예상 |

## Acceptance Criteria

1. `slides/storyboard.md` — 14장 상세 설계 완성
2. `slides/prompts/01_*.md ~ 14_*.md` — 14 파일 작성
3. 각 프롬프트 `prompt_constraints.py` 통과
4. snu_neurox 테마 일관 적용 (14/14)
5. 모든 수치가 `data/*.yaml` 또는 `source/extracted-text/`에서 추적 가능
6. `docs/pdca/phase-5/do.md`, `check.md` 완성
