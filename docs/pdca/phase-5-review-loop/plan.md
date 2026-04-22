# Plan: Phase 5 Review Loop — 3회 반복 독립 리뷰

## Hypothesis

Phase 5에서 작성된 14개 Gemini 프롬프트 + storyboard.md는 `prompt_constraints.py` (구조적 제약: 단어 수, 색상 수)만 검증되었을 뿐, **의미론적 품질**(한글 명료성, narrative 일관성, 데이터 정확성, 시각 문법 준수, 평가단 청중 적합성)은 검증되지 않았다.

3명의 독립 리뷰어(quality-engineer + technical-writer + superpowers:code-reviewer)를 **순차 3회 반복**으로 투입하면 Gemini API 호출($10-40) 이전에 의미론적 결함을 감지·교정할 수 있어 Phase 6 재생성 루프의 비용·시간을 절감한다.

**핵심 원리**: 단일 패스 작성 = blind spots 필연. Review-Revise-Revalidate 사이클은 편향을 축소.

## Why "3 iterations"?

| Iteration | Focus | Expected Severity Distribution |
|---|---|---|
| **1 (Major)** | 중대 결함: 데이터 불일치, 한글 오류, Lab 귀속 오류, 계획 일탈 | critical > important > info |
| **2 (Consistency)** | 일관성: 시각 문법, 용어, hero 지표 포맷, 번역 표현, narrative flow | important > info |
| **3 (Polish)** | 미세 정제: 단어 선택, 평가단 톤, 시각적 일관성 최종 | info 위주 |

Findings 감소 추세가 명확하면 수렴 증명. 반대로 iteration 3에서도 critical 발견 시 **추가 iteration 필요성 시사**.

## Panel Design

### Consistent panel for comparability (모든 iteration에 동일 구성)

| Reviewer | Subagent Type | 관점 | 주요 탐지 목표 |
|---|---|---|---|
| A | `quality-engineer` | 엔지니어링 디스시플린 · 엣지케이스 · 일관성 | 크로스 슬라이드 불일치, 데이터 mismatch, 테스트 가능성 결여 |
| B | `technical-writer` | 한글 프로즈 품질 · 평가단 청중 적합성 · 병렬 구조 | 어색한 표현, 병렬구조 위반, 과도한 기술 용어, 수동태, 애매한 대명사 |
| C | `superpowers:code-reviewer` | 원 계획(storyboard) 대비 구현 정합성 · 공식 표준 | 슬라이드 번호 오류, YAML 데이터 소스 이탈, 제출본과의 불일치 |

모두 **병렬 실행** (단일 메시지에서 3개 Agent 호출). 결과 수집 후 내가 synthesis.

### Loop invariant

각 iteration N에서:
1. **Review (parallel)**: 3개 에이전트 동시 실행
2. **Synthesize**: 중복 제거, 심각도 순위
3. **Revise**: Edit tool로 프롬프트/스토리보드 수정
4. **Revalidate**: `prompt_constraints.py` 재실행, 14/14 PASS 유지 검증
5. **Document**: `iteration-N/findings.md`, `iteration-N/changes.md`

N+1 iteration 시작 시 N의 수정 결과가 리뷰 대상.

## Expected Outcomes (정량)

| 지표 | 목표 |
|---|---|
| 총 반복 수 | 3 |
| 각 iteration PASS 유지 | 14/14 `prompt_constraints.py` |
| Findings 감소 추세 | Iter 1 > Iter 2 > Iter 3 |
| Critical findings in Iter 3 | 0 |
| 작업 시간 | ≤ 45분 |

## Scope (무엇을 review할까)

### Primary (매 iteration 검토)
- `slides/prompts/01_title.md ~ 14_wrap-up.md` — 14 파일
- `slides/storyboard.md` — 설계 문서

### Secondary (참조용)
- `data/*.yaml` — 데이터 정확성 대조
- `source/extracted-text/pages/*.txt` — 원본 narrative 대조
- `docs/redaction-policy.md` — 개인정보 제거 정책 준수

### Out of scope
- 이미지 자체 (아직 생성 전)
- 빌드 스크립트 (이미 동작 검증됨)

## Risks & Mitigation

| 위험 | 대응 |
|---|---|
| Agent 리뷰가 context 부족으로 피상적 | 각 agent prompt에 구체적 파일 경로·기대·평가 기준 명시 |
| 서로 모순되는 findings | Synthesis 단계에서 우선순위화 · 주관적 판단 최소화 |
| Iteration 간 findings가 수렴 안 됨 | 각 iteration 마무리 시 수렴 체크 · 필요 시 iteration 4 고려 |
| 과도한 수정으로 본래 의도 훼손 | "Preserve author intent" 원칙 · 구조·메시지 보존 + 표현만 개선 |
| Findings 문서 간 일관성 저해 | 공통 템플릿 `findings.md` 사용 (severity, file:line, issue, fix) |

## Acceptance Criteria

1. 각 iteration에서 `iteration-N/findings.md` + `iteration-N/changes.md` 작성
2. 매 iteration 종료 시 `prompt_constraints.py` 14/14 PASS 유지
3. Iteration 3 결과에 critical 0
4. `docs/pdca/phase-5-review-loop/check.md`에 3회 findings 추세 시각화 (table)
5. 커밋·push 후 GitHub에서 전체 리뷰 이력 재현 가능

## Exit → Phase 6

- 3회 반복 완료 + 수렴 증명 → Phase 6 (이미지 생성) 실행 준비 완료
- 각 프롬프트에 "REVIEW_PASSED (3 iterations)" 메타 추가 검토
