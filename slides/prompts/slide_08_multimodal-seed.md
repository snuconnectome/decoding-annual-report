# S8 Prompt — 다중 모달리티 · 의미 평가 (SEED)

## API Configuration
- model: gemini-3.1-flash-image-preview (nanobanana2)
- resolution: 4K · aspect_ratio: 16:9 · thinking_mode: high · language: ko

## Rendering Rule (Phase 10)
- 발견 중심 · 명사형 종결 · AI hype 금지
- 3 지표 카드 + 하단 2 패널 구조, 아이콘 중심
- **렌더 절대 금지**: hex 색상 코드 (예 #D55E00) · pt 크기 표기 (예 14pt) · "Bold" 같은 스타일 마커 · 의미 없는 한글 음절 조합 — 모두 디자인 지시이므로 시각적으로 텍스트로 그리지 말 것

## Prompt for nanobanana

16:9 horizontal Korean infographic, background.

**Header**: "디코딩과제 3년차".

**Title (32pt **: "다중 모달리티 · 의미 평가 (SEED)"
**Subtitle (18pt)**: "평가항목 제5번 · 달성도 100% · 인간 판단 정렬 평가체계 + 시각-언어 모델"

**Left accent bar**: ·.

**Top-right Hero 2단**:
- 상단 "인간 판단 정렬 평가체계 확립" - 하단 "평가자 22명 × 이미지쌍 1,000 = 22,000 판단" **Upper — SEED 블록 (세로 약 50%)**:
- 헤드라인: "기존 지표가 인간 판단과 체계적으로 괴리됨을 드러내고, 객체·의미·지각 3축 통합 평가체계를 제안함"
- 풀네임: "SEED — Semantic Evaluation for Visual Brain Decoding"
- 기관: "서울대학교 + 미국 브룩헤이븐 국립연구소 (BNL) 공동"

**3 지표 카드** (, 테두리, 각 카드 중앙 아이콘):
- **카드 1 — Object F1**:
 - 아이콘 중앙: 객체 탐지 경계박스 (사각 테두리 + 라벨)
 - "• 핵심 객체 존재 확인 · 객체 탐지 모델 precision/recall"
- **카드 2 — Caption Similarity**:
 - 아이콘 중앙: 말풍선 + 벡터 화살표
 - "• 이미지 캡션 임베딩 유사도 · 핵심 의미만 통과"
- **카드 3 — SEED (통합)**:
 - 아이콘 중앙: 3 원 교집합 벤다이어그램 (Object · Caption · Perception) · 중앙 교집합에 "SEED" 라벨
 - Signal Orange 강조 "Object F1 + Cap-Sim + EffNet 평균 · 상호 보완"

**카드 하단 2줄**:
- "평가 대상 디코더: MindEye2 ('24) · NeuroPictor ('24) · UniBrain ('24) · MindBridge ('24) · BrainGuard ('25)"
- "관찰된 실패 유형: Semantic Near-Miss · Semantic Detail Confusion"

**Lower — VLM + SEED 메타평가 (세로 약 32%)**:

2 패널, SNU Blue 채우기 + 흰색 텍스트:

**왼쪽 — VLM (시각-언어 모델)**:
- 아이콘: 뇌 → 화살표 → 언어 상자
- 제목 흰색: "뇌영상-언어 임베딩 정렬 시도"
- 흰색:
 - "• LLaVA-Next-Interleave · sMRI + DTI + 휴지기 fMRI 의미 정렬"
 - "• UKB 42,794명 성별 분류 · CLIP-ViT 0.94 · LLaVA 0.787 · BLIP-2 0.779"
 - "• 프롬프트 전략: 단순 질의응답 > 연쇄 추론 (Chain-of-Thought, CoT) · 0.787 vs 0.732"

**오른쪽 — SEED 메타평가 결과**:
- 아이콘: 비교 막대 차트 (SEED vs 기존 8개 지표)
- 제목 흰색: "기존 지표의 인간 판단 괴리를 수치로 드러냄"
- 흰색:
 - "• SEED 가 PixCorr · SSIM · CLIP · EffNet 등 기존 8 지표 대비 정합 개선"
 - "• MindEye2 검색 평가 98%+ 는 의미 근접 오차·세부 혼동을 가림 · ICLR 2026 심사"

**Bottom-right**: "9 / 14".

## Style Rules
- 각 지표 카드 중앙 아이콘 (flat line · 평면 기하)
- SNU Blue 하단 패널 대비 강조

## Negative
- 사진사실적 뇌 재구성 이미지 금지 · 3D 효과 금지 · AI hype 금지 · "...했다" 금지

## Review Status
PHASE 10 v1 (시각 축약)
