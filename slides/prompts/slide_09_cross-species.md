# S9 Prompt — 동물-사람 종간 파운데이션 · 최형진·차지욱 편도체 공동연구

## API Configuration
- model: gemini-2.5-flash-image (nanobanana)
- resolution: 4K (3840x2160)
- aspect_ratio: 16:9
- thinking_mode: high
- language: ko

## Rendering Rule
- Text with pt size + color specifications → RENDER in image
- Design instructions (layout, positioning) → DO NOT render, follow as structure guide

## MASTER THEME (snu_neurox)
- Layout: 공동연구 하이라이트 (상단) + Animal·Human 대비 (중단) + 공통 표현 (하단)
- Page number: "10 / 15"

## Prompt for nanobanana

Create a 16:9 horizontal Korean integration infographic on #FFFFFF background.

**Top-left header**: "디코딩과제 3년차" in 14pt #003380.

**Title**: "동물-사람 종간 파운데이션 모델 — 평가항목 #4 (25%)" in 32pt Bold #003380.
**Subtitle**: "최형진·차지욱 Lab 편도체 공동연구 + 종간 통합" in 22pt #0072B2.

**Top-right Hero**: "**5개 세부 연구**" 22pt Bold #E69F00 + "100%" 작은 원형 배지 우하단.

**Upper highlight band (세로 22%)** — 공동연구 신규:
- Background: linear gradient from #FDECE2 (left, 최형진) to #F4E3EE (right, 차지욱)
- Dual accent bars: 좌측 #D55E00 (vermillion) + 우측 #CC79A7 (Okabe pink) 각 8px
- Title (가운데 정렬): "🔬 편도체 개별신경 × 표정 기반 정서 디코딩" → 이모지 제거, 대신 "**[ 공동연구 ]**" 텍스트. 22pt Bold #003380
- Subtitle: "최형진·차지욱 Lab 공동 · 2023.10 ~ 2025.02 · 2024 iSRC 성과보고회" 14pt #5A5A6E
- 2열 (14pt #282945):
  - Left: "설치류 표정 (안구·입 주위 근육) + 개별 뉴런 앙상블 활동"
  - Right: "편도체 subpopulation · 공포/혐오 구별 · **negative valence encoding**"

**Middle area (세로 40%)** — Animal vs Human:

**LEFT panel (Animal 표현 학습)**:
- Background: #EDF6FC
- Left accent bar: #D55E00 (vermillion) · 8px
- Title: "동물 (Animal) 표현 학습" 22pt Bold #003380
- Bullets 14pt #282945:
  - "**POYO-SSL** — Cell-Pattern-Aware SSL"
  - "Allen Brain Observatory 칼슘 이미징"
  - "SST · VIP · PVALB · NTSR1 분류"
  - "**+12~13%** · SSIM 0.593 · 1.98× 효율"
  - "Skip-Connection U-Net 디코더"

**RIGHT panel (Human 표현 학습)**:
- Background: #EDF6FC
- Left accent bar: #CC79A7 (Okabe pink) · 8px
- Title: "사람 (Human) 표현 학습" 22pt Bold #003380
- Bullets 14pt #282945:
  - "**SwiFT** — 8.8B params · Power-law"
  - "UKB + HCP + ABCD 5만명 rs-fMRI"
  - "**DIVER-1** — 5.3k iEEG + 54k EEG hrs · 17.7k 피험자"
  - "Any-Variate Attention · STCPE · Multi-Domain Recon"
  - "Neuroprobe 15 과제 · FACED · PhysioNet-MI"

**Lower unified band (세로 20%)**:
- Background: #003380 (SNU Blue 반전)
- Title in white: "공통 표현 학습 기반" 22pt Bold
- Body in white: "구조 (sMRI) · 기능 (fMRI) · 전기생리 (iEEG/EEG) · 행동 (표정·video) 통합 → **Trimodal Alignment** → 종간 파운데이션 모델 핵심 토대 확보" 18pt

**Bottom-left** 12pt #5A5A6E: "증빙: 국제 발표 2 · 투고·리뷰 중 2 · 기술개발 1 · 공동연구 참여학생: 김유빈·서정우"

**Bottom-right**: "10 / 15" 12pt #5A5A6E.

## Style Rules
- 상단 공동연구 band: 최형진·차지욱 dual color bar
- 중단 Animal vs Human: 대칭 panels, 각 Lab color bar
- 하단 unified band: SNU Blue inversion (강조)
- 편도체 공동연구 → 핵심 narrative hook

## Consistency Lock
- Same Lab color coding as Slides 6, 7A, 7B, 8
- Same rounded panel style

## Negative
- no 3-level nested hierarchy
- no diagonal arrows
- no photorealistic mice / humans / brains
- no circular integration diagrams
- no emoji in actual rendering (text only)

## Fallback Layout
If 3-band vertical fails:
- Collapse to 2 bands: 공동연구 highlight 상단 + Animal-Human-Unified 하단 3-row grid

## Self-Validation
- [x] Single core message: "편도체 공동연구 + 종간 통합 = 95%+ 달성"
- [x] Word count ≤ 500
- [x] Colors ≤ 6 (SNU Blue, Signal Orange, LAB_VERMIL, PALETTE_PINK, BG_PEACH, SNU Ice)
- [x] Complexity: MED-HI
- [x] 공동연구 하이라이트 + 2 panel + 1 unified = 3-block 깔끔

## Review Status
GRANULAR (Phase 7 최형진·차지욱 편도체 공동연구 중심 재편 완료)
