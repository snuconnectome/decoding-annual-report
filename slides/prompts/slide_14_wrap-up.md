# S14 Prompt — 종합 요약 (Wrap-up) · 질의응답

## API Configuration
- model: gemini-3.1-flash-image-preview (nanobanana2)
- resolution: 4K (3840x2160)
- aspect_ratio: 16:9
- thinking_mode: high
- language: ko

## Rendering Rule
- 약어 없음 정책: 풀네임 + 수치 의미 부기

## MASTER THEME (snu_neurox)
- Layout: 3개 핵심 메시지 카드 + 감사 인사
- Page number: "15 / 15"

## Prompt for nanobanana

16:9 horizontal Korean closing-summary infographic, #FFFFFF background.

**Top-left header**: "디코딩과제 3년차" 14pt #003380.

**Main title** (상단 20% 가운데 정렬): "종합 요약 (Summary)" 44pt Bold #003380.
**Subtitle**: "3차년도 핵심 성과 요약" 20pt #0072B2.

**Main area (세로 약 50%) — 3개 동일 크기 둥근 사각형 카드** (#EDF6FC 배경, 얇은 #0072B2 테두리, 28px 패딩):

**카드 1 — 달성도**:
- 상단 대형 숫자: "97.5%" 44pt Black Bold #E69F00
- 라벨: "합계 달성도" 20pt Bold #003380
- 설명 13pt #282945:
  - "4개 활성 평가항목 (제1·제2·제4·제5번) 전부 100% 달성"
  - "통상 95% 이상이 '우수' 평가"

**카드 2 — 파운데이션 모델**:
- 상단 대형 텍스트: "5개 이상" 40pt Black Bold #E69F00
- 라벨: "멀티스케일 파운데이션 모델" 20pt Bold #003380
- 설명 13pt #282945:
  - "기능적 자기공명영상: SwiFT · SwiFT-IO · MBBN · NeuroMamba · TabLeT"
  - "뇌전도·두개내 뇌전도: DIVER-1 (160만 채널-시간)"

**카드 3 — 4차년도 예산**:
- 상단 대형 숫자: "6억원" 44pt Black Bold #E69F00
- 라벨: "4차년도 (2026) 예산" 20pt Bold #003380
- 설명 13pt #282945:
  - "600,000천원 (천원 단위)"
  - "직접비 468,750 + 간접비 131,250"
  - "종간 파운데이션 모델 사전학습 진행"

**하단 영역 (세로 약 25%)**:
- 가운데 대형 텍스트: "감사합니다" 40pt Bold #003380
- 그 아래: "질의응답 (Q&A)" 26pt Bold #E69F00 가운데
- 최하단 소형 캡션 12pt #5A5A6E: "서울대학교 · snu.ac.kr"

**Bottom-right**: "15 / 15" 12pt #5A5A6E.

## Style Rules
- 3개 요약 카드가 스토리보드 핵심 메시지와 일치
- "감사합니다 · 질의응답" 시각적으로 두드러지게
- 개인 연락처는 기관 도메인만

## Negative
- 개인 전화·이메일 금지 (기관 도메인만)
- 사진사실적 악수·감사 이미지 금지
- 3차원 "Thank You" 금지
- 복잡한 명함 금지

## Self-Validation
- [x] SwiFT, DIVER-1, MBBN, NeuroMamba, TabLeT 풀네임 부기
- [x] 97.5% 의미 (95% 이상 우수)
- [x] 6억원 = 600,000천원 단위 환산
- [x] Q&A = 질의응답 풀네임

## Review Status
PHASE 8 (no-acronym + 수치 의미 명시 완료)
