# S7B Prompt — 차지욱 Lab ② 뇌전도·두개내 뇌전도 + 임상·생성 응용

## API Configuration
- model: gemini-3.1-flash-image-preview (nanobanana2)
- resolution: 4K · aspect_ratio: 16:9 · thinking_mode: high · language: ko

## Rendering Rule (Phase 9)
- 발견 중심 헤드라인
- 약어 풀이 + 수치 의미 부기
- 명사형 종결 ("...함"), AI hype 표현 금지
- 진중한 관찰자 어조

## Prompt for nanobanana

16:9 horizontal Korean infographic, #FFFFFF background.

**Header**: "디코딩과제 3년차" 14pt #003380.

**Title (32pt Bold #003380)**: "차지욱 Lab ② — EEG/iEEG 파운데이션 + 임상·생성 응용"
**Subtitle (18pt #0072B2)**: "평가항목 제2·제4번 · 달성도 100% · 전기생리 사전학습의 멱법칙 스케일링 경향 보고"

**Left accent bar**: #CC79A7 · 8px.

**Hero (우상단 2단)**:
- 상단: "대규모 전기생리 코퍼스 확립" 13pt Bold #003380
- 하단: "두개내 뇌전도 5,300시간 + 두피 뇌전도 54,000시간 · 17,700명 피험자 · 160만 채널-시간" 10pt Bold #E69F00

**Main — 3 horizontal rows (#EDF6FC 배경)**:

**Row 1 — DIVER-1 파운데이션**:
- 마커 ① 18pt Bold #003380
- 헤드라인 16pt Bold #003380: "전기생리 신호 사전학습의 멱법칙 스케일링과, 학습 반복 수가 모델 크기보다 중요함을 관찰함"
- 본문 11pt #282945 (2열):
  - 좌열:
    - "임의 변량 어텐션 (Any-Variate Attention)"
    - "슬라이딩 시간 조건부 위치 인코딩 (STCPE)"
    - "다중 영역 복원 목표 (원시 시계열 + 고속 푸리에 변환 FFT + 단시간 푸리에 변환 STFT)"
  - 우열:
    - "1,300만 파라미터 모델이 선행 BrainBERT (4,300만) · PopT (6,300만) 와 유사하거나 개선된 성능을 보임"
    - "Neuroprobe 벤치마크 15개 과제 (청각·시각·언어 디코딩) 에서 일관된 결과를 관찰함"
    - "두피 뇌전도: 감정 인식 FACED · 운동 상상 PhysioNet-MI · 인지 부하 MentalArithmetic 에서 검증됨"
    - "제한된 연산 예산에서 학습 반복 수 (epochs) 가 파라미터 수 (params) 보다 성능 기여가 큰 경향을 보임 (Data-constrained Scaling Law)"
- 하단 강조 12pt #E69F00: "ICLR 2026 심사 · DIVER-2 로드맵 두개내 뇌전도 50,000시간 확장 진행"

**Row 2 — 교차 모달 정렬**:
- 마커 ② 18pt Bold #003380
- 헤드라인 14pt Bold #003380: "언어 이해 뇌 활동의 의미 통합 이론을 인공지능 정렬 성능으로 재현"
- 2 subsection:
  - 좌: "**Language-Brain Alignment** — 선행 모델 (Antonello et al.) 대비 정확도 14.4%p 개선을 관찰함. 상대 오차 차분 (RED, Relative Error Difference) + 군집화 적용. Damasio 의 수렴-발산 영역 이론 (Convergence-Divergence-Zone) 이 정량 재현됨."
  - 우: "**POYO-SSL** (자기지도학습) — 동물 신경 이질성을 대비 학습 신호로 활용함. 무학습 기준선 대비 12~13%p 성능 향상 · 영화 프레임 복원 구조적 유사도 SSIM 0.593 을 관찰함. Allen Brain Observatory · ICLR 2026 심사 중."

**Row 3 — 임상·생성 응용**:
- 마커 ③ 18pt Bold #003380
- 헤드라인 14pt Bold #003380: "개인별 정서 상태를 뇌전도·심전도로 디코딩하고, 유전형을 결합한 임상 예측으로 확장함"
- 3 chips:
  - "**RYM (Revisit Your Memory)**: 뇌전도 → Stable Diffusion + MusicGen. 개인 정서 F1 = 0.9. 참가자 9명 × 2세션."
  - "**CEBRA 경외 + 내수용감각**: VR 360° + 뇌전도 + 심전도. IS-RSA · Claude 3.5 Sonnet 언어 분석. *Communications Psychology* 출판."
  - "**유전형-뇌영상 임상 예측**: 청소년 우울증 (백질 연결) · 주의력결핍 과잉행동장애 (ADHD) 개인차 · 아동 다유전자 위험도 (polygenic risk) 구조 연구."

**Bottom band** (전폭, italic 10pt #282945, 연한 라벤더 #EFEAF7):
"DIVER 3단계 전략 — 1단계 사전학습 (비레이블 신경 데이터) → 2단계 정렬 (iEEG-Video-Speech 3중 모달, 100명 × 24시간) → 3단계 개인화 (실시간 피드백 닫힌 고리)   ·   주관: 서울대 차지욱 · 국외 공동: 프린스턴 Uri Hasson · 브룩헤이븐 Shinjae Yoo"

**Bottom-right**: "8 / 15" 12pt #5A5A6E.

## Negative
- AI hype ("세계 최초" 등) 금지 · "...했다" 금지 · 약어 단독 금지

## Review Status
PHASE 9 v1 (review iteration 0)
