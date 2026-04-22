# S7B Prompt — 차지욱 Lab ② EEG/iEEG Foundation + 동물·임상 응용 (평가항목 #2·#4)

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
- Layout: Hero 2-badge stack + 3 horizontal rows
- Page number: "8 / 15"

## Prompt for nanobanana

Create a 16:9 horizontal Korean technical-results infographic on #FFFFFF background.

**Top-left header**: "디코딩과제 3년차" in 14pt #003380.

**Title**: "차지욱 Lab ② EEG/iEEG + 동물·임상 응용" in 32pt Bold #003380.
**Subtitle**: "ephys 최초 정량적 Scaling Law · Multi-Modal Generative" in 22pt #0072B2.

**Left accent bar** (vertical, whole slide): #CC79A7 (Okabe-Ito pink, 차지욱 Lab) · 8 pixels wide.

**Top-right Hero stack** (2 vertical badges):
- Top badge: "**5.3k**" in 40pt Bold #E69F00, label "iEEG hrs · 17.7k 피험자 · 1.6M 채널-시간" in 11pt #5A5A6E
- Bottom badge: "**54k**" in 40pt Bold #E69F00, label "EEG hrs · FACED·PhysioNet·MentalArithmetic" in 11pt #5A5A6E
- Divider: thin horizontal #0072B2 line

**Main area — 3 horizontal rows** (각 row = full-width rounded rectangle):

**Row 1 — DIVER-1 (가장 큰 영역, 세로 35%)**:
- Background: #EDF6FC (SNU Ice)
- Row marker (좌상단): circular "①" in 24pt Bold #003380
- Title: "DIVER-1 — ephys 최초 Scaling Law" in 24pt Bold #003380
- Technical bullets (14pt #282945, 2열 배치):
  - 좌열:
    - "Any-Variate Attention"
    - "Sliding Temporal Conditional Positional Encoding (STCPE)"
    - "Multi-Domain Reconstruction (raw · FFT · STFT)"
  - 우열:
    - "**13M params** → BrainBERT 43M · PopT 63M 능가"
    - "Neuroprobe 15 청각·시각·언어 과제 SOTA"
    - "Data-constrained Scaling Law · **epochs > params**"
- Hero footer 문구 (16pt Bold #E69F00): "ICLR 2026 심사 · DIVER-2 50k iEEG hrs 확장"

**Row 2 — Cross-Modal Alignment (세로 25%)**:
- Background: #EDF6FC
- Row marker: "②" in 24pt Bold #003380
- Title: "Cross-Modal Semantic Alignment" in 22pt Bold #003380
- 2 subsections (좌/우 분할):
  - **Left — Language-Brain Alignment**:
    - Name: "Language-Brain" 18pt Bold SNU Blue
    - Metric: "**+14.4%**" 28pt Bold Signal Orange
    - "Antonello et al. 상회 · RED + Clustering"
    - "Convergence-Divergence-Zone Theory 부합"
    - "ICLR 2026 심사"
  - **Right — POYO-SSL**:
    - Name: "POYO-SSL (동물 칼슘)" 18pt Bold SNU Blue
    - Metric: "**+12~13%**" 28pt Bold Signal Orange
    - "Allen Brain Observatory · Cell-Pattern-Aware SSL"
    - "SSIM 0.593 · Drifting 55.5% · 1.98× 효율"
    - "ICLR 2026 심사"

**Row 3 — 임상·생성 응용 (세로 25%)**:
- Background: #EDF6FC
- Row marker: "③" in 24pt Bold #003380
- Title: "임상 · 생성 응용" in 22pt Bold #003380
- 3 small chips 수평 배치:
  - **Chip 1 — RYM**: "EEG → Stable Diffusion + MusicGen · **F1 = 0.9** · 56% 선호도"
  - **Chip 2 — CEBRA 경외 + 내수용감각**: "*Communications Psychology* 2025 · VR 360° + IS-RSA + Claude 3.5"
  - **Chip 3 — Polygenic 임상**: "우울증(Youth) · ADHD · 아동 polygenic architecture (논문 #1·#5·#14·#15)"

**Bottom band** (16:1 전폭, #EFEAF7 연한 lavender 배경, 14pt #282945, italic):
"DIVER 3-Phase Strategy: Foundation (Pre-Train) → Alignment (iEEG-Video-Speech Trimodal, 100 subjects × 24/7) → Personalization (real-time closed-loop)   ·   협력 PI: Jay-Yoon Lee · Chun Kee Chung · Uri Hasson · Shinjae Yoo (SNU + Brookhaven National Lab)"

**Bottom-right**: "8 / 15" in 12pt #5A5A6E.

## Style Rules
- 3-row vertical stack · each row uses SNU Ice fill with numbered circular marker
- Hero metrics always Signal Orange Bold
- 차지욱 Lab pink accent bar 좌측 유지
- 모든 수치는 `report/03_lab-research-detail.md` §3.2 추적 가능

## Consistency Lock
Same pink accent bar · Same hero-metric style as Slide 7A · Slide 9 의 Animal/Human pre-train 모델과 cross-reference

## Negative
- no diagonal arrows
- no 3D brain renders
- no Quantum ML content (Slide 10으로 이관)
- no photorealistic SEED decoded images (문태섭 Lab S8에만 해당)
- no emoji

## Fallback Layout
If 3 horizontal rows fails:
- Convert to 2×3 grid
- Move bottom band to footnote (10pt)

## Self-Validation
- [x] Single core message: "DIVER-1 ephys Scaling Law + Language-Brain/POYO-SSL + 임상 생성 응용"
- [x] Word count ≤ 520 (granular detail)
- [x] Colors ≤ 6 (SNU Blue, Neural Teal, Signal Orange, Okabe pink, lavender, SNU Ice)
- [x] Complexity: HI
- [x] 8개 주요 연구 (DIVER-1, Language-Brain, POYO-SSL, RYM, CEBRA, 내수용감각, Polygenic 4 논문) 가시

## Review Status
GRANULAR (Phase 7 차지욱 Lab ephys FM 슬라이드 + 제출본 § 반영)
