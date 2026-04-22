# Iteration 1 Findings — 3인 병렬 리뷰 종합

## 리뷰어 패널 (parallel, independent)

| Reviewer | Subagent | Findings | Critical |
|---|---|---|---|
| A | quality-engineer | 12 | 4 |
| B | technical-writer | 14 | 3 |
| C | superpowers:code-reviewer | 13 | 5 |
| **Total (dedup)** | — | **26 unique** | **7 convergent** |

## Convergence Analysis

3명 이상 또는 2명 동시 탐지된 **high-confidence** findings:

### Triple-convergence (3/3 agents)
- **CRITICAL-01**: Slide 8 "평가항목 4" 잘못된 번호 (실제 criterion_id=5)
- **CRITICAL-02**: Slide 9 "평가항목 3" 잘못된 번호 (실제 criterion_id=4)
- **CRITICAL-03**: Slide 14 "5 종" 모델 수·naming 불일치

### Double-convergence (2/3 agents)
- **CRITICAL-04**: Slide 14 "600M" 예산 표기 모호성
- **IMPORTANT-01**: Slide 5 team legend 색상 #0072B2 ↔ Neural Teal 충돌
- **IMPORTANT-02**: "SOTA" 과용 (Slide 7 "차지욱 Lab SOTA 달성")
- **IMPORTANT-03**: Slide 13 YAML에 없는 bullet ("한국인 특이", "자살·범죄 예방")

### Single-reviewer-only (1/3)
- (quality) Slide 4 ①②③④ 번호 misleading
- (quality) Slide 11 "평가항목 3 누락 이슈" forward reference
- (quality) Slide 3 "현재" badge Signal Orange 남용
- (writer) Slide 1 "상호작용시의" 구식 Korean
- (writer) Slide 6 bullet 조사·parallelism
- (writer) Slide 14 "Q & A" 공백·"감사합니다·Thank you" bilingual padding
- (writer) Number+unit spacing (천원/편/건/종) 컨벤션 미통일
- (code) Slide 14 "connectome Lab" YAML에 없음 (fabrication)
- (code) Slide 12 subtitle Signal Orange (killer metric rule 위반)
- (code) Slide 9 #FFF4DD cream color 팔레트 외부
- (code) Slide 7 Lab-color marker 부재
- (info) Slide 1 "제출일" 누락
- (info) Rendering Rule 섹션 일부 누락
- (info) Model ID `gemini-3.1-flash-image-preview` 미검증

## Severity Distribution

| Severity | Count | Action in Iter-1 |
|---|---|---|
| CRITICAL | 7 (4 convergent + 3 extra) | 전부 수정 |
| IMPORTANT | 12 | 상위 6개 수정, 나머지 Iter-2로 |
| INFO | 7 | Iter-2/3로 연기 |

## Priority Fix List for Iteration 1

1. **Slide 8 title**: "평가항목 4" → "평가항목 5"
2. **Slide 9 title**: "평가항목 3" → "평가항목 4"
3. **Slide 14 "600M" card**: → "600,000" with unit caption
4. **Slide 14 "5 종" card**: → "5개 세부 연구" (matches Slide 9) + 모델 리스트 정정
5. **Slide 14 "connectome Lab"**: 삭제, "서울대학교 · @snu.ac.kr"만 유지
6. **Slide 4 cards**: ①②③④ 유지하되 각 카드 상단에 "평가항목 #1/#2/#4/#5" 레이블 추가
7. **Slide 4 subgoal**: "세부목표 2-1, 2-2" 중복 수정 (카드 3 → 기존, 카드 4 → "2-3" 또는 다른 적절한 값)
8. **Storyboard Slide 8·9 heading**: 번호 수정
9. **Slide 13**: "자살·범죄 예방" → "공공 안전 AI 응용"으로 softening, "한국인 특이" bullet은 YAML-backed으로 교체
10. **Slide 5 team colors**: #0072B2 차지욱 Lab 충돌 해결 — 자연언어 색상명("green", "orange") 제거, HEX로만 지시
11. **Slide 7 subtitle "SOTA"**: softening "세계 최고 수준 성능 달성 (SOTA)"으로 1회 설명 + 각 카드 softening
12. **Slide 12 subtitle 색상**: #E69F00 → #0072B2 (Signal Orange reservation 준수)
13. **Slide 3 "현재" 배지**: Signal Orange 사용은 유지하되 marker 색상은 Neural Teal로 환원 (중복 방지)

## Deferred to Iteration 2

- Slide 6 bullet 조사·parallelism 정리
- "상호작용시의" → "상호작용 시" 정규화
- Number+unit spacing 컨벤션 통일 (전체 슬라이드)
- Slide 11 "평가항목 3 누락 이슈" phrasing softening
- Slide 14 "Q & A", "감사합니다·Thank you" 정리
- Slide 9 #FFF4DD 팔레트 정리
- Slide 2 두 캡션 정리

## Deferred to Iteration 3

- Slide 1 "제출일" 추가 여부
- Rendering Rule 섹션 일관성
- Model ID 검증 (외부 의존)
- Em-dash vs tilde 통일
- 기타 미세 polish
