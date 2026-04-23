# S11 Prompt — 정량 실적 (Hero Slide)

## API Configuration
- model: gemini-3.1-flash-image-preview (nanobanana2)
- resolution: 4K (3840x2160)
- aspect_ratio: 16:9
- thinking_mode: high
- language: ko

## Rendering Rule
- 약어 없음 정책: 풀네임 + 수치 의미 부기
- Text with pt size + color specifications → RENDER in image
- **렌더 절대 금지**: hex 색상 코드 (예 #D55E00) · pt 크기 표기 (예 14pt) · "Bold" 같은 스타일 마커 · 의미 없는 한글 음절 조합 — 모두 디자인 지시이므로 시각적으로 텍스트로 그리지 말 것

## MASTER THEME (snu_neurox)
- Layout: 3개 대형 hero 수치 수평 정렬
- Page number: "12 / 14"

## Prompt for nanobanana

16:9 horizontal Korean hero-metric infographic, background.

**Top-left header**: "디코딩과제 3년차".

**Title**: "3차년도 정량 성과" .
**Subtitle**: "2025년 1월 1일 ~ 2025년 12월 31일 실적".

**Main area (세로 약 70%) — 3개 거대 Hero 수치 수평 배치**:

**왼쪽 수치 — 합계 달성도**:
- 상단 작은 아이콘: 타겟·체크 심볼
- 거대 숫자: "97.5%" Black - 하단 라벨: "합계 달성도"
- 부연 (12pt): "4개 평가항목 × 가중치 합 100% 기준 · 통상 95% 이상이 우수 평가"

**가운데 수치 — 공개 논문**:
- 상단 아이콘: 문서·종이 심볼
- 거대 숫자: "17" Black - 단위: "편" - 하단 라벨: "공개 논문 (Journal Papers)"
- 부연 (12pt): "국제 저널 중심 · 영향력 지수 (Impact Factor) 상위 다수"

**오른쪽 수치 — 국제 학회 참석**:
- 상단 아이콘: 마이크·발표대 심볼
- 거대 숫자: "4" Black - 단위: "건" - 하단 라벨: "국제 학회 참석 (Conference Presentations)"
- 부연 (12pt): "국제 학술대회 포스터·구두 발표"

**수직 구분선**: 매우 연한,, 3개 수치 블록 사이

**Bottom strip** (13pt, 왼쪽 정렬):
"3차년도 활성 평가항목 4개 (제1·제2·제4·제5번) 전수 달성도 100% · 평가항목 제3번 (신경과학 메커니즘 규명, 비중 10%) 은 4차년도 (2026) 개시 예정"

**Bottom-right**: "12 / 14".

## Style Rules
- 미니멀: 흰 배경 + 3개 거대 숫자
- Signal Orange는 hero 수치에만 사용
- 박스 없음 — 순수 타이포그래피

## Negative
- 추가 보조 지표 금지 (3개로 제한)
- 파이차트 금지 · 막대차트 금지
- 3차원 숫자 금지 · 그라데이션 금지
- 사진사실적 아이콘 금지

## Self-Validation
- [x] "합계 달성도", "공개 논문", "국제 학회" 모두 풀네임
- [x] 97.5% 의미 부기 (95%+ 우수)
- [x] Impact Factor = 영향력 지수 설명

## Review Status
PHASE 8 (no-acronym + 수치 의미 명시 완료)
