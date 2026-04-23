# S6 Prompt — 데이터베이스 구축

## API Configuration
- model: gemini-3.1-flash-image-preview (nanobanana2)
- resolution: 4K · aspect_ratio: 16:9 · thinking_mode: high · language: ko

## Rendering Rule (Phase 10 — 텍스트 축약 + 아이콘·도식 우선)
- 발견 중심 · 명사형 종결 · AI hype 금지
- 긴 bullet 나열 지양. 핵심 수치·뇌영역·방법만 간결하게.
- 아이콘·도식 중심 레이아웃 (flat line minimal, 평면 실루엣, 3D·사진사실 금지)
- **렌더 절대 금지**: hex 색상 코드 (예 #D55E00) · pt 크기 표기 (예 14pt) · "Bold" 같은 스타일 마커 · 의미 없는 한글 음절 조합 — 모두 디자인 지시이므로 시각적으로 텍스트로 그리지 말 것

## Prompt for nanobanana

16:9 horizontal Korean infographic, background.

**Header**: "디코딩과제 3년차".

**Title (32pt **: "데이터베이스 구축 — 정서 맥락 디코딩의 양측 기반"
**Subtitle (18pt)**: "평가항목 제1번 (비중 25%) · 사람·동물 양측 공동 수행 · 달성도 100%"

**Top-right Hero**: 원형 "100%" + 하단 "달성도".

**Animal block (상단, 세로 약 26%)** — 동물:
- 배경, 좌측 bar
- 헤드라인: "동물 — 자유 행동 정서·신경 동시 측정 환경 구축"
- **중앙 diagram (가로 50%)**: flat line 설치류 실루엣 + 머리에 연결된 광섬유. 설치류 몸에 작은 골격 포인트 마커 표기.
- **우측 3 bullets**:
 - "• **3D 골격 DB** · DeepLabCut 멀티뷰 · 행동 4종 (그루밍·보행·rearing·drinking)"
 - "• **VTA-NAc 광유전학** · DAT-cre 마우스 · AAV5-ChrimsonR + AAV9-GRAB_DA1h 도파민 형광 센서"
 - "• 594 nm · 30s · 5/10/20 Hz 광자극 + fiber photometry 동시 측정"

**Human block (하단, 세로 약 54%)** — 사람:
- 배경, 좌측 bar
- 좌우 2개 패널, 얇은 테두리

**왼쪽 패널 — 실험 1: MixedEmo fMRI + EEG (n=92)**:
- 배지 "실험 1" - 헤드라인: "정서 연합 부호화와 기억 인출이 서로 다른 뇌 네트워크에 의해 매개됨을 관찰함"
- **중앙 diagram**: flat 뇌 옆면 실루엣 + 4 영역 하이라이트 (편도체 · 기본모드 네트워크 DMN · 후대상피질 PCC · 전대상피질 ACC 복/배측). 영역별 라벨 짧게.
- **본문 3 bullets**:
 - "• 연합 단계: 편도체·주의망 / 인출: 기본모드 네트워크 (DMN) · 후대상피질 (PCC)"
 - "• 전대상피질 (ACC) 복/배측 해리 · 긍정-부정 vs 부정-긍정 비교 p = 0.010"
 - "• 상태 불안 STAI-X1 ↔ 인출 방향성 (p = 0.002, 0.003) · EEG 32ch 2048Hz 바이오마커"

**오른쪽 패널 — 실험 2: 가상공간 탐험 EEG + 해마**:
- 배지 "실험 2" - 헤드라인: "가상공간 탐험 후 EEG 에서 기억 시간 구조의 순차 재활성을 포착함"
- **중앙 diagram**: 가로 시간축 (왼쪽 초반 사건 · 오른쪽 종반 사건 두 이벤트 표시) · 시간에 따라 reactivation bias 값이 0→1 로 상승하는 EEG 디코딩 곡선. 하단 VR 헤드셋 소아이콘.
- **본문 3 bullets**:
 - "• 4 랜드마크 조건 · 순차 재활성 (reactivation bias) 포착"
 - "• 디코딩 정확도 10–15% (chance 4%) · *Imaging Neuroscience* Lim et al. 2025"
 - "• 해마 CA2/3·치상회 (CA23DG)·CA1 맥락 범주화 · 청소년 CA23DG–안와전두피질 (OFC) 발달"

**하단 캡션** (14pt, 가운데):
"인간 92명 다중 모달리티 DB + 동물 자유 행동·도파민 회로 측정 프로토콜 구축"

**Bottom-right**: "6 / 14".

## Style Rules
- 모든 아이콘·도식 flat line · 평면 실루엣 · SNU Blue/Neural Teal/Lab color 팔레트 내
- 뇌 도식은 옆면·위면 단순 실루엣 (해부학 포스터 금지)
- 각 패널 아이콘·도식이 중앙에 시각 앵커 역할

## Negative
- 사진사실적 뇌 이미지 금지 · 3D 뉴런 금지 · 컬러풀 일러스트 금지
- "세계 최초", "최고" 금지 · "...했다" 금지

## Review Status
PHASE 10 v1 (시각 축약)
