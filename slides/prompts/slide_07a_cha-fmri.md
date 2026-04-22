# S7A Prompt — 차지욱 Lab ① fMRI Foundation Models (평가항목 #2·#4)

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
- Layout: 2×2 model grid + side hero + bottom chip row
- Page number: "7 / 15"

## Prompt for nanobanana

Create a 16:9 horizontal Korean technical-results infographic on #FFFFFF background.

**Top-left header**: "디코딩과제 3년차" in 14pt #003380.

**Title**: "차지욱 Lab ① fMRI Foundation Models" in 32pt Bold #003380.
**Subtitle**: "평가항목 #2·#4 · 달성도 100% · UKB·HCP·ABCD 5만명 기반 파운데이션" in 22pt #0072B2.

**Left accent bar** (vertical, whole slide): #CC79A7 (Okabe-Ito pink, 차지욱 Lab) · 8 pixels wide.

**Top-right Hero badge**: circular badge "**8.8B**" in 48pt Bold #E69F00, label "파라미터 · 5만명 사전학습" in 14pt #5A5A6E. Radius ~100 pixels.

**Main area — 2×2 grid of rounded rectangle cards** (#EDF6FC fill, thin #0072B2 outline, 24px padding, equal size):

**Card Top-Left — SwiFT**:
- Icon: brain + upward staircase (scaling)
- Name: "SwiFT" in 22pt Bold #003380
- Hero metric: "8.8B params" in 28pt Bold #E69F00
- Description lines (14pt #282945):
  - "37M → 118M → 1.2B → 8.8B · muP scaling"
  - "UKB + HCP + ABCD 5만명 rs-fMRI"
  - "Power-law 확인 · BrainLM·Brain-JEPA 상회"
  - "HCP 성별 +7.6% · 알츠하이머·통증·항우울 SOTA"

**Card Top-Right — SwiFT-IO**:
- Icon: film reel + brain (movie fMRI)
- Name: "SwiFT-IO" in 22pt Bold #003380
- Hero metric: "R² = 0.96" in 28pt Bold #E69F00
- Description (14pt #282945):
  - "Perceiver IO · Sequence-to-Sequence"
  - "HBN movie fMRI · 677명 × 12분"
  - "LSTM baseline R² = -0.135"
  - "CCN 2025 발표"

**Card Bottom-Left — MBBN**:
- Icon: wavy lines (frequency bands)
- Name: "MBBN" in 22pt Bold #003380
- Hero metric: "ADHD/ASD SOTA" in 24pt Bold #E69F00
- Description (14pt #282945):
  - "Frequency-Specific Multi-Band Attention"
  - "ADHD 고주파 → 실행기능"
  - "저주파 → 운동지각 · 사회인지"
  - "초저주파 → 내장감각 · 항상성"
  - "*Communications Biology* 2026.1"

**Card Bottom-Right — NeuroMamba**:
- Icon: curved arrow + gear (efficient)
- Name: "NeuroMamba" in 22pt Bold #003380
- Hero metric: "94.9%" in 28pt Bold #E69F00
- Description (14pt #282945):
  - "HCP 성별 분류 94.9%"
  - "SwiFT 92.9% · NeuroSTORM 93.3% 상회"
  - "Mamba2 + NeRF 주파수 위치 인코딩"
  - "FLOPs −46.5%"

**Bottom band** (16:1 전폭, #E7F0ED 연한 mint 배경, 14pt #282945):
"**TabLeT** (2D DCAE · UKB 8,178 + HCP 1,061 + ADHD-200 533 · CVPR 심사)   ·   **Latent Diffusion Transformer** (3D VQ-GAN · 세계 최초 4D fMRI 생성)"

**Bottom-right**: "7 / 15" in 12pt #5A5A6E.

## Style Rules
- 2×2 grid · hero metrics in Signal Orange #E69F00 · model name above, description below
- 차지욱 Lab pink accent bar 좌측 세로 유지
- 모든 수치는 `report/03_lab-research-detail.md` §3.1 추적 가능

## Consistency Lock
Same card styling as Slide 4 · Slide 7B 와 동일 grid 구조

## Negative
- no line charts (4 모델 서로 다른 축)
- no 3D bars, no pie chart
- no photorealistic brain scans
- no emoji

## Fallback Layout
If 2×2 + 4 hero metrics fails:
- Reduce to 2-row horizontal card list (4 cards)
- Keep hero metrics Bold Signal Orange

## Self-Validation
- [x] Single core message: "fMRI 파운데이션 모델 풀스택 (사전학습·디코딩·주파수 분리·효율화)"
- [x] Word count ≤ 450
- [x] Colors ≤ 5 (SNU Blue, Neural Teal, Signal Orange, Okabe pink, mint)
- [x] Complexity: MED-HI
- [x] 5 모델 이름 중 4개 카드 + TabLeT·Latent Diffusion 하단 띠

## Review Status
GRANULAR (Phase 7 Lab 자료 반영 완료)
