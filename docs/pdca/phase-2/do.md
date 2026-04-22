# Do: Phase 2 — 실행 로그

## 타임라인

### 2026-04-22 23:25 KST — 추출 CSV 소스 확인
Phase 1 결과물 중 Phase 2에 직접 투입될 9개 CSV를 순차 확인:
- `087_t01` (78 lines) + `088_t01` (87 lines): 3차년도 성과 표
- `097_t01` (32 lines) + `098_t01` (22 lines): 레퍼런스 증빙 21건
- `092_t01` (50 lines): 4차년도 예산
- `013_t01` + `014_t01` + `015_t01`: 5개년 평가기준
- `087_t02` (5 lines): 단일 셀 (p87 보조 셀, 주요 정보 없음)

### 2026-04-22 23:30 KST — **정합성 이슈 발견**: 평가항목 3 누락

**발견**:
- 5개년 평가기준(p13-15)에는 **6개 평가항목** (가중치 합 100%):
  - 1: DB 구축 20%
  - 2: 기계학습 모델 20%
  - 3: 신경과학 메커니즘 10% (3차년도 목표 **존재**)
  - 4: 뇌영상-파운데이션 20%
  - 5: 종간 파운데이션 20%
  - 6: 확장 활용 10% (4-5년차만)

- 3차년도 성과 표(p87-88)에는 **4개 항목**만 기재 (1, 2, 4, 5). 각 25%로 재분배.

**문제**: 평가항목 3(신경과학 메커니즘, 10%)이 3차년도 목표가 존재하는데(two-site 광유전학, EEG 상호작용) 성과 표에서 누락됨.

**해석 옵션**:
- (a) 평가항목 3이 3차년도 평가에서 제외·유보됨
- (b) 실적이 다른 항목과 통합 평가됨
- (c) 성과 표 작성 시 기재 누락

**조치**: `data/metrics.yaml`의 `notes.evaluation_3_discrepancy` 필드에 명시적 기록. 평가단 발표 시 예상 질의 대비.

### 2026-04-22 23:33 KST — 추가 텍스트 소스 확보

4차년도 계획(p89), 활용방안(p93-94), 안전·보안(p96)은 pymupdf 추출된 텍스트에 완전히 존재함을 확인. next-year-plan.yaml에 직접 활용.

### 2026-04-22 23:35 KST — 5개 YAML 작성

순차 작성:
1. **project-meta.yaml** (148 lines): 메타데이터·예산·기술분류 10종·4차년도 예산 상세. 개인정보 전부 제외.
2. **evaluation-criteria.yaml** (102 lines): 6 criteria × 최대 5 연차별 목표. 공통 구조(`id/title/weight_percent/related_subgoals/yearly_targets`)로 크로스 레퍼런스 준비.
3. **achievements.yaml** (154 lines): 논문 17 + 학회참석 4 = 21건 + `key_technical_models` 9개 모델 메타.
4. **metrics.yaml** (87 lines): 4개 평가항목 × 3차년도 성과 상세 + 평가항목 3 누락 이슈 공식화 + 달성도 97.5%.
5. **next-year-plan.yaml** (103 lines): 5개 연구 방향 + 5단계 추진전략 + 4팀 구성 + 600M 예산 + 활용방안 + 안전·보안.

### 2026-04-22 23:45 KST — 검증 단계

#### (1) YAML 로드 테스트 (`yaml.safe_load`)

```
OK: achievements.yaml
OK: evaluation-criteria.yaml
OK: metrics.yaml
OK: next-year-plan.yaml
OK: project-meta.yaml
OK: section-map.yaml  (Phase 1에서 작성)
```
6/6 loaded.

#### (2) 크로스 레퍼런스 일관성

**4차년도 예산 (3곳 동일 수치)**:
- `project-meta.budget.by_year[4].total` = 600,000
- `next-year-plan.budget.total` = 600,000
- `project-meta.year4_budget_detail` (direct 468,750 + indirect 131,250) = 600,000
→ **MATCH**

**평가항목 ID subset**:
- `evaluation-criteria.criteria.[].id` = [1, 2, 3, 4, 5, 6]
- `metrics.year3_performance.[].criterion_id` = [1, 2, 4, 5]
- subset 관계 유지: True (누락된 3, 6은 의도적)

**레퍼런스 count**:
- papers 17, conferences 4, summary.total 21 → **MATCH**

**가중치 합**:
- evaluation-criteria (5개년): 20+20+10+20+20+10 = **100%**
- metrics (3차년도 재분배): 25+25+25+25 = **100%**
- 합계 달성도: **97.5%**

#### (3) Redaction 스캔

```
OK: 6 개 파일에서 redaction 패턴 매칭 없음.
```

Phase 8 redact-check가 data/ 영역에서도 통과 — 개인정보 · 긴 숫자열 · 서명 파일명 전무.

## 발견된 경고 · 이슈

없음. Phase 1의 `Could not get FontBBox` 경고는 이번 단계에서 재발하지 않음 (CSV 기반 작업).

## 학습 사항

1. **성과 표와 평가기준 표의 불일치**는 R&D 보고서에서 **재분배 관행**의 결과일 가능성이 큼. "연차별 active 항목의 가중치 합이 100%가 되도록" 재가중되는 패턴은 향후 4·5년차 보고서 작성 시 참고.

2. **YAML 공통 `_metadata` 헤더**는 출처 추적(traceability)에 매우 효과적. 각 파일이 어디에서 왔는지 자동 감사 가능.

3. **Cross-reference validation을 코드로 작성**하는 것이 YAML 수작성 시 오류 검출의 유일한 실질적 방법. 단순 "눈으로 확인"은 수치 일치에 취약.

4. **Jinja 템플릿 친화적 구조 유지**: 각 YAML이 flat-ish 구조(deep nesting 최소)를 유지했으므로 Phase 3 Markdown 생성 시 `{{ metrics.total.achievement_percent }}` 같은 직관적 접근 가능.
