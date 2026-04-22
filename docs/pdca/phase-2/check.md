# Check: Phase 2 — 결과 분석

## Results vs Expectations

| 지표 | Expected | Actual | Status |
|---|---|---|---|
| YAML 파일 수 | 5 | 5 (+ section-map from P1) | ✅ |
| `yaml.safe_load()` 통과 | 5/5 | 6/6 | ✅ |
| `redact-check.py data/` 매칭 | 0 | 0 | ✅ |
| 레퍼런스 총수 | 21 (17+4) | 21 (17+4) | ✅ |
| 평가항목 (5개년) | 6 | 6 | ✅ |
| 평가항목 가중치 합 | 100% | 100% | ✅ |
| 3차년도 성과 평가항목 | 4 | 4 | ✅ |
| 3차년도 재분배 가중치 합 | 100% | 100% | ✅ |
| 합계 달성도 | 97.5% | 97.5% | ✅ |
| 4차년도 예산 3곳 일치 | 600,000 | 600,000 | ✅ |
| 작업 시간 | ≤ 60분 | ~25분 | ✅ (58% 단축) |

## What Worked Well

### 1. 공통 `_metadata` 헤더
모든 YAML에 `file/purpose/sourced_from/generated_by/last_updated` 5필드 공통 헤더를 적용. 향후 어느 파일을 열어도 출처·목적·갱신 시기를 즉시 파악 가능. Phase 3·5에서 자동 감사(audit) 스크립트 작성 시 재사용 가능.

### 2. 크로스 레퍼런스를 코드로 검증
`data/*.yaml`을 하나하나 눈으로 확인하지 않고 Python으로:
- 4차년도 예산 3곳 일치 검증
- 평가항목 ID subset 관계 검증 (metrics ⊂ evaluation-criteria)
- 레퍼런스 count 검증 (17+4=21)
- 가중치 합 100% 검증

→ 수동 작업에서 흔히 놓치는 수치 오류를 기계적으로 차단.

### 3. Redact-check 재활용
Phase 1에서 선작성한 `scripts/redact-check.py`가 Phase 2에서 그대로 사용되어 `data/` 영역 0건 확인. 미래 단계에서 재사용 가능한 자산.

### 4. "재분배 정합성 이슈"의 명시적 공식화
평가항목 3(신경과학 메커니즘) 누락 문제를 "의도적 제외"로 처리하지 않고 **`notes.evaluation_3_discrepancy`** 필드로 문서화. 평가단 발표 시 예상 질의에 대한 선제 대응 가능.

### 5. 선택적 건너뛰기 결정 (Phase 3·4 skip)
사용자 확인 후 Track A(보고서 Markdown/PDF)가 필수 아님을 판단 → Phase 3·4 skip. 절약된 3-5시간을 Phase 6(실제 슬라이드 생성)에 재투자 가능.

## What Failed / Challenges

### 1. CSV의 다중 라인 셀 파싱 난이도
pdfplumber가 셀 안의 줄바꿈을 각 줄로 분리하는 경우(예: `가\n중\n치\n(%)` → 4 rows in CSV) 존재. Python CSV reader로 읽을 때는 정상 복원되지만 **첫 줄 헤더만 보고 해석하면 오판 가능**. 수동 병합 필요했음.

**대응**: 헤더 행이 여러 줄인 표는 CSV 원본이 아닌 `pages/*.txt` 원문을 참고해 정확한 의미 파악.

### 2. 평가항목 3의 누락 이슈 (문서 원본 이슈)
R&D 보고서 제출본 자체의 일관성 문제. 해결은 불가능하고 **명시적 기록 + 예상 질의 대비**가 최선.

### 3. 4차년도 예산 상세 항목의 테이블 레이아웃
p92의 예산 표가 pdfplumber로 추출되었으나 헤더가 복잡하게 분리됨 (`092_t01.csv` 보면 직접비/간접비/합계 구조가 row 단위로 잘림). 수동으로 `year4_budget_detail` YAML 구조 정돈.

**해결**: `project-meta.yaml`과 `next-year-plan.yaml` 두 곳에 예산 기재 → 교차 검증으로 수치 일관성 확보.

## Acceptance Criteria Checklist

| # | 조건 | 결과 |
|---|---|---|
| 1 | `project-meta.yaml` 메타·예산·기술분류 완비 | ✅ |
| 2 | `evaluation-criteria.yaml` 6항목 × 5개년 완전 | ✅ |
| 3 | `achievements.yaml` 21건 (17+4) | ✅ |
| 4 | `metrics.yaml` 4항목 성과 + 97.5% + 평가항목 3 누락 플래그 | ✅ |
| 5 | `next-year-plan.yaml` 5 방향 + 600,000천원 | ✅ |
| 6 | 5/5 YAML `yaml.safe_load()` 성공 | ✅ (실제 6/6) |
| 7 | `redact-check.py data/` → 0 | ✅ |
| 8 | 크로스 레퍼런스 정합성 | ✅ (4개 축 모두) |
| 9 | `docs/pdca/phase-2/do.md`, `check.md` 완성 | ✅ |

**9/9 조건 충족 → Phase 5 전환 가능.**

## Phase 3·4 Skip 결정의 근거

- 원본 제출본 PDF(2025-12-08)가 이미 **공식 버전** — 공개 재작성은 중복
- 평가단은 원본을 이미 보유 (제출 시스템 경유) — 별도 보고서 재구성 불필요
- data/*.yaml + source/extracted-text/pages/*.txt 조합이 **슬라이드 narrative의 단일 진실 소스** 역할 충분 수행
- `Makefile`의 `make report` 타겟은 stub으로 유지 — 향후 필요 시 수행 가능한 상태 보존

## Phase 5 이행 준비 상태

- ✅ `data/*.yaml`에 모든 정량 수치·문구 구조화
- ✅ `source/extracted-text/figures/`에 74개 참조 이미지 (p86, p90, p91 등)
- ✅ `scripts/build-slides.py` 선작성 완료
- ✅ `infographics` 스킬 활용 가능
- ⏳ `slides/storyboard.md` 작성 (Phase 5 첫 작업)
- ⏳ `slides/prompts/01_*.md ~ 14_*.md` 작성

다음 작업: `docs/pdca/phase-5/plan.md` 작성 → 14장 스토리보드 → 장별 프롬프트.
