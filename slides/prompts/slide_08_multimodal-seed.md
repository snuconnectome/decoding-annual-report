# S8 Prompt — 다중 모달리티 · 의미 평가 · 문태섭 Lab

## API Configuration
- model: gemini-3.1-flash-image-preview (nanobanana2)
- resolution: 4K · aspect_ratio: 16:9 · thinking_mode: high · language: ko

## Rendering Rule (Phase 9)
- 발견 중심 헤드라인 · 약어 풀이 · 수치 의미 부기
- 명사형 종결 · AI hype 금지 · 진중한 어조

## Prompt for nanobanana

16:9 horizontal Korean infographic, #FFFFFF background.

**Header**: "디코딩과제 3년차" 14pt #003380.

**Title (24pt Bold #003380)**: "기존 디코딩 평가 지표가 인간 판단과 체계적으로 괴리됨을 드러내고, 이에 대응한 의미 평가 체계 (SEED) 를 확립함"
**Subtitle (16pt #584B9F)**: "문태섭 Lab · 평가항목 제5번 · 다중 모달리티 통합 · 달성도 100%"

**Left accent bar**: #584B9F (문태섭 Lab 보라) · 8px.

**Hero 우상단 2단**: 상단 "인간 판단과 정렬된 평가체계 확립" 14pt Bold #003380, 하단 "평가자 22명 × 이미지쌍 1,000개 = 22,000건 수집" 11pt Bold #E69F00.

**Upper half — SEED 블록**:
- 제목 18pt Bold #003380: "SEED — 시각 뇌 디코딩 의미 평가 (Semantic Evaluation for Visual Brain Decoding)"
- 저자 11pt #5A5A6E: "Juhyeon Park · Peter Yongho Kim · Jiook Cha · Shinjae Yoo · Taesup Moon (교신저자) · 서울대학교 + 미국 브룩헤이븐 국립연구소"
- 헤드라인 12pt #282945: "기존 평가 지표 (PixCorr 픽셀 상관 · SSIM 구조 유사도 · CLIP · EfficientNet 등) 는 인간 판단과 체계적으로 불일치하는 경향이 관찰됨. 이에 대응하여 객체·의미·지각 세 축을 통합한 신규 평가 체계를 제안함."

**3 지표 카드** (#EDF6FC 배경, #56B4E9 테두리):
- **카드 1 — Object F1 (범위 0~1, 1.0이 이론적 상한)**: "핵심 객체 존재 확인을 수행함 · 정밀도·재현율의 조화평균 · 객체 탐지 모델 기반"
- **카드 2 — Caption Similarity (0~1)**: "이미지 캡션 임베딩 유사도를 측정함 · 캡션이 핵심 의미만 통과시키는 요약 역할을 함"
- **카드 3 — SEED (통합 지표)**: "Object F1 + Caption Similarity + EfficientNet 특징의 평균을 집계함. 단, EfficientNet 특징은 단독으로는 인간 판단과 괴리되나 SEED 안에서 객체·의미 지표와 결합될 때 상호 보완 역할을 수행함"

**카드 하단 캡션** 10pt #5A5A6E:
"평가 대상 선행 디코더: MindEye2 (국제 머신러닝 학술대회 ICML 2024) · NeuroPictor (유럽 컴퓨터비전 학술대회 ECCV 2024) · UniBrain (arXiv 2024) · MindBridge (컴퓨터비전·패턴인식 학술대회 CVPR 2024) · BrainGuard (AAAI 인공지능 학술대회 2025)   ·   관찰된 실패 유형: 의미 근접 오차 (Semantic Near-Miss) · 의미 세부 혼동 (Semantic Detail Confusion)"

**Lower half — 시각-언어 모델 + TabLeT 블록**:

2개 패널, SNU Blue (#003380) 채우기 + 흰색 텍스트:

**왼쪽 패널 — 시각-언어 모델 (VLM)**:
- 제목 흰색 18pt Bold: "뇌영상-언어 임베딩 정렬을 시도함"
- 본문 흰색 11pt:
  - "자연 이미지로 사전학습된 시각-언어 모델 (Vision-Language Model, VLM) 을 뇌영상 도메인에 전이"
  - "LLaVA-Next-Interleave 아키텍처 (다중 영상 입력)"
  - "구조적 MRI + 확산텐서영상 (DTI) + 휴지기 fMRI 의미 정렬"
  - "영국 바이오뱅크 42,794명 성별 분류 정확도: CLIP-ViT 모델이 0.94 (이항 분류 무작위 수준 0.5 대비 안정적 개선) 의 정확도를 보임"
  - "프롬프트 전략 비교: 단순 질의응답 > 연쇄 추론 (Chain-of-Thought) · LLaVA 0.787 vs 0.732"

**오른쪽 패널 — SEED 메타평가 결과**:
- 제목 흰색 18pt Bold: "기존 지표의 인간 판단 불일치를 수치로 드러냄"
- 본문 흰색 11pt:
  - "인간 평가자 판단과의 일치도에서 SEED 가 PixCorr · SSIM · AlexNet · CLIP · EfficientNet 등 기존 8개 지표 대비 개선된 정합을 보임"
  - "MindEye2 는 검색 기반 정량 평가에서는 98% 이상의 정확도를 보고하나, SEED 및 Object F1 기반 정성 평가에서는 의미 근접 오차·세부 혼동이 드러남"
  - "SEED 는 MindEye2·NeuroPictor·UniBrain·MindBridge·BrainGuard 5개 디코더 전반에서 실패 유형 진단 도구로 활용 가능함"
  - "국제 학습표현 학술대회 (ICLR) 2026 심사 중"

**Bottom-right**: "9 / 15" 12pt #5A5A6E.

## Negative
- AI hype 금지 · "...했다" 금지 · 약어 단독 금지

## Review Status
PHASE 9 v1 (review iteration 0)
