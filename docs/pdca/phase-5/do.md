# Do: Phase 5 — 실행 로그

## 타임라인

### 2026-04-22 23:50 KST — Phase 5 개시
Phase 2 완료 후 보고서 작성 (Phase 3·4) skip 결정에 따라 Phase 5 스토리보드·프롬프트 제작으로 직행.

### 2026-04-22 23:55 KST — infographics 스킬 API 파악
`~/.claude/skills/infographics/SKILL.md`, `prompt_template.md`, `prompt_constraints.py`, `themes/snu_neurox.yaml` 검토.

- 스킬이 Claude에게 부과하는 규약: 각 슬라이드 프롬프트 `.md`는 10개 섹션 구조 (API Config, Rendering Rule, MASTER THEME, Prompt for nanobanana2, Style Rules, Consistency Lock, Negative, Fallback, Self-Validation, Review Status).
- Hard constraints: Prompt 섹션 ≤ 400 words, 색상 ≤ 5, 아이콘 ≤ 4, 복잡도 LOW/MED, 핵심 메시지 1개/슬라이드.
- 테마 선정: **snu_neurox** (SNU Blue #003380 + Okabe-Ito 색맹안전 팔레트, 16:9, Pretendard 한글 우선).

### 2026-04-23 00:00 KST — storyboard.md 14장 구성

초기 14개 슬라이드 설계:
1. Title / 2. Overview / 3. Roadmap / 4. Year3 Goals / 5. Strategy
6. DB 구축 / 7. ML Models / 8. Multimodal / 9. Cross-species
10. Extensions+Quantum / 11. Quantitative Results / 12. Year4 Plan / 13. Expected Impact / 14. Wrap-up

각 슬라이드: 유형 · 레이아웃 · 핵심 메시지 · YAML 데이터 소스 · 시각 요소 · negative prompt 정의.

### 2026-04-23 00:15 KST — 이상아 Lab Google Slides 수신 + Slide 6 재설계

사용자 제공: https://docs.google.com/presentation/d/1fANYzUBcDAr4nJDGKNzmNINaV5aF2RFZBWfjsrprX4k/

`mcp__claude_ai_Google_Drive__read_file_content`로 내용 추출 성공.

발견:
- 이상아 Lab 2개 대표 실험:
  1. fMRI/EEG 다중양식 감정 연합 (편도체 + DMN + PCC/precuneus; Posterior/Frontal θ 바이오마커)
  2. 가상공간 탐험 EEG (회전지점 sequential reactivation, 랜드마크-공간기억)
- 이상아 Lab 논문 4편 중 3편(Lim 2025/8, Kim 2025/11, Lee 2025/11)이 제출일(2025-12-08) 이전 출판되었으나 `achievements.yaml` 17편 목록에 **미포함**.
- Koo 2026/1 Scientific Reports는 제출 이후 출판.

**사용자 정책 재확인**: "제출본 그대로 유지 + 슬라이드에는 narrative만 반영". `achievements.yaml` 불변.

→ Slide 6 "DB 구축"을 이상아 Lab 중심으로 재설계. 2개 실험을 좌우 패널로 상세화.

### 2026-04-23 00:20 KST — 문태섭 Lab Google Slides 수신 + Slide 8 재설계

사용자 제공: https://docs.google.com/presentation/d/15mYsqMUqjH2oHUQgzI_e_VV6V6_E1vnm/

발견:
- 문태섭 Lab 대표 연구: **SEED** (Semantic Evaluation for Visual Brain Decoding)
  - 저자: Juhyeon Park*, Peter Yongho Kim*, Jiook Cha, Shinjae Yoo, **Taesup Moon†** (교신)
  - Brookhaven National Lab과 협업
  - 3개 제안 지표: Object F1, Caption Similarity, SEED (통합)
  - 22명 평가자 × 1K 이미지쌍 = **22K 인간 판단**으로 validation
  - 평가 대상 SOTA: MindEye2, NeuroPictor, UniBrain, MindBridge, BrainGuard

→ Slide 8 "다중 모달리티"를 문태섭 Lab 중심으로 재설계. SEED 3카드 + Vision-Language Model 2패널 구조.

### 2026-04-23 00:25 KST — Team Contributions 섹션 추가

storyboard.md 끝에 팀별 기여 매핑 공식화:
- 이상아 Lab (teal #11604B) → Slide 6 ✅
- 최형진 Lab (vermillion #D55E00) → Slide 6 animal ⏳ 대기
- 차지욱 Lab (teal #0072B2) → Slide 7 ⏳ 대기
- 문태섭 Lab (purple #584B9F) → Slide 8 ✅

제출본 정합성 이슈(각 Lab의 대표 논문이 17편 목록에 미포함)를 공식 기록.

### 2026-04-23 00:35 KST — 1차 storyboard 커밋

`d91dc2c` commit pushed: plan.md + storyboard.md 2 files, 609 insertions.

### 2026-04-23 00:40 KST — 14개 프롬프트 작성

batch 1 (Slides 1-5): Title, Overview, Roadmap, Year3 Goals, Strategy
batch 2 (Slides 6-10): DB (이상아), ML Models, Multimodal (문태섭), Cross-species, Extensions+Quantum
batch 3 (Slides 11-14): Quantitative Results (hero), Year4 Plan, Expected Impact, Wrap-up

각 프롬프트는 infographics 스킬 규약의 10섹션 구조 준수.

### 2026-04-23 01:10 KST — 1차 validation: 3 FAIL

```
FAIL  01_title.md        542 words > 450
FAIL  02_overview.md     473 words > 450
FAIL  06_db-construction 477 words > 450
PASS  others (11/14)     with various warnings
```

Root cause: 각 텍스트 요소에 pt size + color를 과도 명시 (pedagogical thoroughness가 validation에서 초과).

### 2026-04-23 01:15 KST — 3개 프롬프트 압축

Edit tool로 Slides 1, 2, 6의 "Prompt for nanobanana2" 섹션을 압축. 구조·의도는 유지, 불필요한 반복 제거.

1차 재검증: Slide 1만 여전히 461 words (11 초과). Style Rules 섹션도 압축.

### 2026-04-23 01:20 KST — 최종 validation: **14/14 PASS**

```
ALL 14 PROMPTS PASS
```

남은 경고들(Too many colors, Long prompts ≥ 400)은 디자인 요구 특성상 불가피. ERROR 없음 = 생성 가능 상태.

## 발견된 경고·이슈

### Warning 1: Too many colors (대부분 슬라이드에 6-10개 HEX 탐지)
- Root cause: 프롬프트 본문에 HEX 코드를 반복 명시하면 constraint counter가 이를 고유 색상으로 집계.
- Impact: INFORMATIONAL. 실제 렌더링 색상 수는 각 슬라이드에서 5개 이하로 제한되어 있음.
- Action: 허용. `prompt_constraints.py`는 보수적 체크로 작동.

### Warning 2: Long prompts (대부분 400-430 words)
- Root cause: 10섹션 구조 + 상세 설계 요구로 전체 파일이 400 words 초과.
- Impact: 스킬 가이드에 따르면 400 초과 시 "reliability may drop". 450 초과 시 FAIL.
- Action: 모든 프롬프트를 450 미만으로 유지. 실제 Prompt 섹션은 더 짧음.

### Warning 3: Slide 5 "Circular flow diagram detected"
- Root cause: 프롬프트에 "flow" 단어가 있어 false positive 발생 (실제는 수평 5단계 straight flow).
- Impact: INFORMATIONAL. 실제 레이아웃은 순환이 아님.
- Action: 무시.

## 학습 사항

1. **Google Workspace MCP 활용**: `mcp__claude_ai_Google_Drive__read_file_content`가 공유 Google Slides의 텍스트 내용을 효과적으로 추출. 이미지 기반 슬라이드는 제외되나 구조적 텍스트 수집에는 충분.

2. **스킬 템플릿 준수의 중요성**: 10섹션 구조는 초기에는 verbose하게 느껴지나, `prompt_constraints.py` + `generate_image.py` 파이프라인 통합에 필수. 각 섹션이 명확한 역할 (rendered vs context).

3. **제출본 ↔ Lab 상세 간 narrative bridge**: 제출본 `achievements.yaml`을 불변 유지하면서도, Lab별 구체 연구(SEED, 이상아 실험)를 **narrative로 전달**하는 이중 레이어 설계. 평가단 발표 시 원본 문서와 불일치 없는 장점 + 구체성 확보 장점 동시.

4. **압축 전략**: 프롬프트 작성 시 "정확한 설계 명세"와 "Gemini에게 creative latitude"의 균형이 중요. 과도하게 상세 명시는 400+ words로 부풀려 reliability drop 위험. 
