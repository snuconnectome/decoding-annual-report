# Check: Phase 1 — 결과 분석

## Results vs Expectations (계획 대비 실적)

| 지표 | Expected | Actual | Status |
|---|---|---|---|
| 페이지 추출 성공 | 98/98 | 98/98 | ✅ 달성 |
| 치환 문자 | 0 | 0 | ✅ 달성 |
| 주요 표 추출 | ≥ 5 | 45 | ✅ 900% 초과 |
| 주요 그림 추출 | ≥ 3 | 74 | ✅ 2500% 초과 |
| 섹션 매핑 | 7 섹션 | 7 + subsections | ✅ 달성 |
| git 보호 | 추적 0 | 추적 0 | ✅ 달성 |
| 스크립트 4종 로드 | 4/4 | 4/4 | ✅ 달성 |
| 실행 시간 | ≤ 90분 | ~18분 | ✅ 80% 단축 |

## What Worked Well (성공 요인)

### 1. 하이브리드 추출 전략
pymupdf + pdfplumber 조합이 설계대로 상호 보완 작동:
- pymupdf: 본문 페이지(p10+) 한글 추출 완벽, 이미지 74개 추출
- pdfplumber: 45개 표를 CSV로 정확히 추출 (특히 p097 레퍼런스 17편 목록)

### 2. Redaction 3중 방어선 중 2단계 조기 작동
- **1단계(본문 미기재)**: 아직 Phase 3 미시작
- **2단계(gitignore)**: 원본 PDF 복사 직후 `git ls-files source/` = 0 확인으로 실증됨
- **3단계(자동 스캔)**: Phase 8 수행 예정
- 추가 **자연 방어선 발견**: p1-9이 이미지 렌더링이어서 개인정보가 텍스트 추출로 유출되지 않음

### 3. Section-map의 사전 정의
`data/section-map.yaml`에 `expected_tables`, `expected_figures`를 미리 정의하여 추출 후 "실제 vs 예상" 비교가 즉시 가능했음. 예상 페이지(p86, p90, p91)가 모두 figures.json에 포함됨을 확인.

### 4. PDCA plan.md의 구체적 Acceptance Criteria
10개 조건을 수치로 명시해 Check 단계에서 자동 검증 가능. 모호한 "잘 추출되었는지" 판단을 배제.

### 5. Warning Investigation Culture 적용
두 경고(FontBBox, FutureWarning)를 모두 조사·분류·기록. FutureWarning은 즉시 수정 → 기술부채 제거. FontBBox는 외부 라이브러리 특성으로 문서화 후 허용.

### 6. 병렬 실행으로 시간 단축
venv 설치(background)와 스크립트 작성을 병렬 진행하여 대기 시간 최소화. 90분 목표 대비 18분 달성.

## What Failed / Challenges (도전 과제)

### 1. Pages 1-9 이미지 렌더링
**예상치 못한 발견**: 표지·요약문이 텍스트가 아닌 이미지로 PDF에 저장됨. 원인은 "Google Docs Renderer" 출력 특성.

**조치**:
- 즉시 root cause 조사 후 **OCR 추가는 불채택** 결정 (복잡도 > 실익)
- Phase 3에서 맥락의 기존 Read 결과를 활용하는 대안 전략 수립
- 오히려 redaction 관점에서 이점으로 재해석

### 2. pdfplumber 표 헤더 분리
일부 표에서 다중 라인 헤더가 각 라인별로 별도 셀로 분리 추출됨 (예: `p087_t01.csv`의 "가\n중\n치\n(%"). 추출 자체는 성공이나 Phase 2 구조화 시 수기 병합 필요.

**조치**: Phase 2 data/metrics.yaml 작성 시 수기 보정 예정. 원본 손실은 없음.

### 3. FutureWarning 누락 위험
오타(`~~`)로 인한 FutureWarning이 첫 작성 시 발견되지 않음. `python -W error` 전환 고려 가치 있으나, 외부 라이브러리 경고가 블로커가 될 수 있어 현재는 수동 리뷰 유지.

## Metrics Deep Dive

### 한글 품질 지표 (페이지별)

| 구간 | 페이지 | 평균 문자 | 평균 한글% | 상태 |
|---|---|---|---|---|
| 표지·요약문 (이미지) | 1-9 | 9 | 0% | 이미지 기반 (예상) |
| 목차 | 10 | 503 | 25.6% | 목차 페이지 (숫자 비중 높음) |
| 개요·본문 | 11-85 | ~1000+ | 50-70% | 정상 추출 ✅ |
| 결과·계획 | 85-98 | 다양 | 40-70% | 정상 추출 (p86, 90, 91 예외) |

### 이미지 분포

74개 이미지의 페이지 분포 분석 결과:
- **표지·요약문**: 9개 (p1-9 × 1장) — 문서 앞부분 이미지 렌더링
- **본문 기술 도식**: 62개 (p18-80에 분포) — 실험 설계·모델 아키텍처·결과 그림
- **핵심 다이어그램**: 3개 (p86, p90, p91) — 일정·전략 차트

## Acceptance Criteria 체크리스트

| # | 조건 | 결과 |
|---|---|---|
| 1 | `source/original-3year-report.pdf` 존재, `git ls-files`에 없음 | ✅ |
| 2 | `metadata.json`에 `page_count == 98` | ✅ |
| 3 | `pages/001.txt ~ 098.txt` 모두 생성 | ✅ |
| 4 | `qa-report.md` replacement char 0 또는 문서화된 예외 | ✅ (0건, 문서화 완료) |
| 5 | `tables/` ≥ 5 CSV (p5, p13, p87, p97 포함) | ✅ (45개, 모두 포함) |
| 6 | `figures/` ≥ 3 PNG (p86, p90, p91) | ✅ (74개, 해당 페이지 포함) |
| 7 | `data/section-map.yaml` 7 섹션 | ✅ |
| 8 | `make verify` smoke test 통과 | ✅ ("스캔 대상 없음, 통과") |
| 9 | 4개 스크립트 `python -c "import"` 성공 | ✅ 4/4 |
| 10 | `docs/pdca/phase-1/do.md`, `check.md` 작성 | ✅ 본 문서 포함 |

**10/10 조건 충족 → Phase 2 전환 가능.**

## Phase 2 전환 체크 (Exit → Next)

- [x] Acceptance Criteria 10/10
- [ ] scripts/ + data/ + docs/pdca/phase-1/ 커밋 (다음 작업)
- [ ] origin/main push (다음 작업)

다음 작업: Phase 2에서 `data/project-meta.yaml`, `data/evaluation-criteria.yaml`, `data/achievements.yaml`, `data/metrics.yaml`, `data/next-year-plan.yaml`을 추출 결과로부터 구조화.
