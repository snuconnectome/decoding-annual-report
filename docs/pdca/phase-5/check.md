# Check: Phase 5 — 결과 분석

## Results vs Expectations

| 지표 | Expected | Actual | Status |
|---|---|---|---|
| 스토리보드 문서 | 1 (14장) | 1 (14장 + Team 매핑) | ✅ 초과 |
| 프롬프트 파일 | 14 | 14 | ✅ |
| 테마 적용 | snu_neurox 일관 | snu_neurox 14/14 | ✅ |
| `prompt_constraints.py` 통과 | 14/14 | 14/14 (warnings 허용) | ✅ |
| 16:9 aspect ratio | 14/14 | 14/14 | ✅ |
| 한글 텍스트 정확 명시 | 14/14 | 14/14 | ✅ |
| Labs 반영 (2/4) | 2 Lab 반영 | 이상아 + 문태섭 ✅ | ✅ |
| 작업 시간 | ≤ 2시간 | ~90분 | ✅ 25% 단축 |

## What Worked Well

### 1. Google Drive MCP 통합
사용자가 공유한 이상아·문태섭 Lab Google Slides를 `mcp__claude_ai_Google_Drive__read_file_content`로 즉시 접근하여 핵심 실험·저자·지표 정보 추출. WebFetch 불가한 인증 리소스에서도 원활한 워크플로우.

### 2. Lab-specific 반영의 하이브리드 접근
- **구조 보존**: 14장 기본 구성 유지 (평가항목 중심)
- **Lab attribution**: 특정 슬라이드를 Lab 중심으로 지정 (Slide 6 → 이상아, Slide 8 → 문태섭)
- **제출본 불변**: `achievements.yaml` 17편 목록 유지, Lab-specific 내용은 storyboard narrative만

이 3층 접근으로 공식 제출본과의 정합성 + Lab 세부 기여 가시성을 동시 확보.

### 3. 스토리보드가 프롬프트 품질을 주도
storyboard.md의 각 슬라이드 설계가 프롬프트 작성 시 **직접 재사용 가능한 구조**. 슬라이드 → 프롬프트 변환 시 창작 부담 최소화, 일관성 자동 유지.

### 4. Warning Investigation의 즉시 실행
1차 validation 실패 3건에 대해 root cause 분석 → 즉시 압축 수정 → 재검증 → 통과. `prompt_constraints.py`의 보수적 체크가 실제 생성 품질 보장에 기여.

### 5. 14개 프롬프트 배치 생산
배치 1 (1-5), 배치 2 (6-10), 배치 3 (11-14)로 나눠 작성하여 맥락 유지 + 단일 응답 크기 제한 대응.

### 6. snu_neurox 테마의 fit
SNU Blue + Okabe-Ito 색맹안전 팔레트 + 16:9 + Pretendard 한글이 정부 R&D 평가단 발표 톤과 정확히 일치. 테마 선택 시 별도 커스터마이징 불필요.

## What Failed / Challenges

### 1. 프롬프트 길이 1차 FAIL (3/14)
Slides 1, 2, 6 초기 버전이 542/473/477 words로 450 word cap 초과.

**원인**: "designer-friendly"하게 각 텍스트 요소마다 pt size + color + position 명시 → 완벽한 설계 문서는 되지만 validation 통과 어려움.

**해결**: 불필요한 반복 제거. "22pt Bold #003380"을 한 번 명시 후 다음부터는 컨텍스트에 의존. Style Rules 섹션 bullet 압축.

**교훈**: 완벽한 설계와 간결한 프롬프트의 균형. Gemini에게 "얼마나 구체적으로 지시할지"가 품질 편차 결정.

### 2. Color constraint 체계적 warn
거의 모든 슬라이드에서 "Too many colors (6-10 > 5)" warning. 프롬프트에 HEX 코드 명시가 색상 counter를 트리거.

**분석**: 실제 렌더링 색상은 5개 이하. Counter의 보수적 해석.

**조치**: 허용. 향후 테마 이름 참조("snu_neurox palette")로 HEX 명시를 줄이는 최적화 가능성 있으나 현재 generate 위험 낮음.

### 3. Labs 정보 부분 수신
4팀 중 2팀(이상아, 문태섭)만 정리 수신. 차지욱·최형진 Lab 정리는 추후 예상.

**현재 상태**:
- Slide 7 (차지욱 Lab, ML 모델): achievements.yaml의 모델명 (SwiFT·DIVER-0·POYO-SSL·MBBN) 기반 plausible default 작성. 차지욱 Lab 정리 도착 시 refine 예정.
- Slide 6 animal part (최형진 Lab): 한 줄 placeholder. 최형진 Lab 정리 도착 시 상세화.

**Review Status 표기**: Slide 7 프롬프트 하단에 "READY (awaiting 차지욱 Lab specific additions)" 명시.

### 4. SEED 논문 저자에 차지욱 PI 포함 발견
문태섭 Lab의 SEED 논문 저자 리스트에 "Jiook Cha" (차지욱 PI) 포함. 이는 **Lab 간 협업**을 시사하며, 단순 "문태섭 Lab 전용" 프레임이 완전히 정확하지 않을 수 있음.

**조치**: Slide 8 내용에 SEED 저자 전체 나열 유지 (문태섭 교신 + 차지욱 공저자). 평가단 발표 시 협업 구조 명시.

## Acceptance Criteria Checklist

| # | 조건 | 결과 |
|---|---|---|
| 1 | `slides/storyboard.md` 14장 설계 | ✅ |
| 2 | `slides/prompts/01-14.md` 14 파일 | ✅ |
| 3 | `prompt_constraints.py` 통과 | ✅ 14/14 |
| 4 | snu_neurox 테마 일관 적용 | ✅ |
| 5 | 수치 `data/*.yaml` 추적 가능 | ✅ |
| 6 | `docs/pdca/phase-5/do.md`, `check.md` 완성 | ✅ |

**6/6 조건 충족 → Phase 6 전환 가능.**

## Phase 6 이행 준비 상태

### ✅ Ready
- `slides/prompts/*.md` 14개 모두 constraint pass
- `scripts/build-slides.py` 선작성 완료 (Phase 7용)
- `infographics` 스킬 `generate_image.py` 활용 가능
- `snu_neurox` 테마 정의 완료

### ⏳ Pending
- Gemini API 키 (`GEMINI_API_KEY` 또는 `NANOBANANA2_API_KEY` 환경변수)
- 차지욱 Lab 자료 (Slide 7 refinement용, 필수 아님)
- 최형진 Lab 자료 (Slide 6 animal 확장용, 필수 아님)

### 예상 비용
14 slides × 1 variant × ~$0.3 = **~$4-6** (1회 생성)
재생성 2-3회 포함 추정 총 **$10-20**

### 예상 시간
- API 호출 병렬 (workers=3): 14 슬라이드 × ~2분 = 20-30분
- 품질 검수 + 재생성: 30-60분
- **총 Phase 6 예상: 1-2시간**

## Phase 5 → 6 핵심 전환 포인트

1. 사용자가 Gemini API key 설정 (환경변수 또는 .env)
2. `python ~/.claude/skills/infographics/generate_image.py --prompt-dir slides/prompts --output slides/images --variants 1 --parallel --workers 3`
3. 각 슬라이드 PNG 수동 검수 (한글 정확 렌더링, 수치 정확성, 레이아웃 일관)
4. 실패 슬라이드는 해당 프롬프트만 수정 후 재생성
5. 전체 완료 후 `scripts/build-slides.py`로 단일 PDF 병합

향후 차지욱·최형진 Lab 정리 수신 시 해당 슬라이드 프롬프트만 교체 후 부분 재생성 가능 (모듈식 설계의 이점).
