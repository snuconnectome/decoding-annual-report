# Plan: Phase 2 — 추출 결과의 구조화 (YAML 데이터 레이어)

## Hypothesis

Phase 1에서 추출된 비정형 자료(98 pages + 45 tables + 74 figures)를 **5개의 YAML 파일**로 재구조화하면, Phase 3(보고서 Markdown)과 Phase 5(슬라이드 스토리보드)가 동일한 단일 진실(single source of truth) 데이터층을 참조하여 일관된 수치와 텍스트를 생산할 수 있다.

## Expected Outcomes (정량)

| 지표 | 목표 |
|---|---|
| YAML 파일 수 | 5 (project-meta, evaluation-criteria, achievements, metrics, next-year-plan) |
| `yaml.safe_load()` 통과 | 5/5 |
| `redact-check.py data/` | 0 findings |
| 레퍼런스 항목 | 논문 17 + 학회참석 4 = 21 |
| 평가항목 (5개년) | 6 (p13–15 기반) |
| 3차년도 성과 평가항목 | 4 (p87–88 기반, 합계 달성도 97.5%) |
| 작업 시간 | ≤ 60분 |

## Design

### Source-of-truth 계층 (우선순위)

1. **1차**: 추출된 pages/*.txt (기계 truthful, redaction 자연 통과)
2. **2차**: 추출된 tables/*.csv (구조화된 수치·레퍼런스)
3. **3차 (보완)**: Claude 이전 Read 결과 (p1–9 이미지 페이지 한정, public 정보만)

개인정보가 포함될 수 있는 p1–2 이미지 페이지는 **어떠한 YAML에도 직접 기재하지 않는다**. 연구책임자 식별 정보는 이름·직위·기관(공개 정보)만 포함.

### 공통 YAML 스키마

모든 YAML은 다음 공통 헤더를 가진다:

```yaml
_metadata:
  file: data/<name>.yaml
  purpose: <한 줄 설명>
  sourced_from:
    - "source/original-3year-report.pdf pXX-YY"
    - "source/extracted-text/tables/NNN_tNN.csv"
  generated_by: Phase 2 manual structuring
  last_updated: 2026-04-22
```

### 각 YAML 설계

#### data/project-meta.yaml
- **출처**: 표지 p1-2 (이미지, Claude 사전 Read 활용) + 요약문 p3-11
- **내용**: 과제번호, 제목(국문·영문), 기관명, 기간(전체·3차년도), 책임자(공개 정보), 예산(연차별), 기술분류
- **크기**: ~50 lines
- **Redaction**: 연구책임자 전화·연구자번호 완전 제외

#### data/evaluation-criteria.yaml
- **출처**: p13-15 tables 013_t01, 014_t01, 015_t01 (평가기준 표)
- **내용**: 6개 평가항목 × 5개년 목표 + 가중치 + 관련 세부목표
- **크기**: ~200 lines (상세 목표 포함)
- **구조**: 각 criterion이 id/title/weight_percent/subgoal_ids/yearly_targets를 가짐

#### data/achievements.yaml
- **출처**: p97-98 tables 097_t01, 098_t01 (레퍼런스 증빙)
- **내용**: 논문 17편 + 학회참석 4편 = 21건 (ID, 제목, 유형)
- **크기**: ~60 lines
- **특이사항**: p98 CSV에 빈 행 6줄 존재 — 아티팩트로 무시

#### data/metrics.yaml
- **출처**: p87-88 tables 087_t01, 088_t01 (정성적 성과)
- **내용**: 3차년도 평가항목별 목표·실적·달성도·증빙
- **크기**: ~150 lines
- **중요 플래그**: p87-88 성과 표는 4개 평가항목만 다룸. 5개년 평가기준(p13-15)의 **평가항목 3(신경과학 메커니즘, 10%)이 3차년도 타겟 존재함에도 성과 표에서 누락**. 이를 `notes.evaluation_3_discrepancy` 필드로 명시하여 평가단 질의 대응 대비.

#### data/next-year-plan.yaml
- **출처**: p89-92 (4차년도 목표·전략·일정·예산)
- **내용**: 5개 연구 방향, 추진전략 요지, 일정, 예산 내역(인건비·장비비 등)
- **크기**: ~80 lines

### 크로스 레퍼런스 일관성

- `evaluation-criteria.yaml`의 `criterion.id` ↔ `metrics.yaml`의 `year3_performance.criterion_id`
- `achievements.yaml`의 `paper.id` ↔ `metrics.yaml`의 `evidence.paper_ids` (추적 가능)
- `project-meta.yaml`의 `budget.by_year[year=4]` ↔ `next-year-plan.yaml`의 `budget.total_thousands_krw` (동일 수치 600,000)

## Risks & Mitigation

| 위험 | 대응 |
|---|---|
| 다중 라인 셀로 인한 CSV 파싱 어려움 | 수동 병합 후 YAML 작성. 원본 그대로가 아닌 정돈된 형태 목표 |
| 평가항목 3 누락 정합성 문제 | `notes.evaluation_3_discrepancy` 필드 + Phase 3/5에서 명시적 언급 검토 |
| YAML 키 이름 불일치로 인한 Phase 3 템플릿 실패 | 공통 스키마 위·pydantic 모델 작성은 오버엔지니어링. safe_load + 수동 키 일치 검증으로 충분 |
| 영문·국문 혼재 | 국문이 원본. 영문은 논문 제목·핵심 학술 용어에만 유지 |
| 예산 수치 오류 | 복수 출처 대조 (p2 요약표 vs p92 상세표 vs next-year-plan) |

## Acceptance Criteria

1. `data/project-meta.yaml` — 메타데이터·예산·기술분류 완비
2. `data/evaluation-criteria.yaml` — 6항목 × 5개년 완전
3. `data/achievements.yaml` — 21건 (17+4)
4. `data/metrics.yaml` — 4항목 성과 + 달성도 97.5% + 평가항목 3 누락 플래그
5. `data/next-year-plan.yaml` — 5개 방향 + 예산 600,000천원
6. 5/5 YAML `yaml.safe_load()` 성공
7. `scripts/redact-check.py data/` → 0 findings
8. 크로스 레퍼런스 일관성 (예산·항목 ID·달성도) 일치
9. `docs/pdca/phase-2/do.md`, `check.md` 완성
