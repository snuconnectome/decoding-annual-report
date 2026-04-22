# S6 Prompt — DB 구축 · 이상아 Lab (사람) + 최형진 Lab (동물) 공동

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
- Layout: Animal block (상단 띠) + Human block (하단 2-panel)
- Page number: "6 / 15"

## Prompt for nanobanana

16:9 horizontal Korean research-results infographic, #FFFFFF background.

**Top-left header**: "디코딩과제 3년차" 14pt #003380.

**Title**: "데이터베이스 구축 — 평가항목 #1 (25%)" 32pt Bold #003380.
**Subtitle**: "이상아 Lab (사람) · 최형진 Lab (동물) 공동 수행 · 달성도 100%" 22pt #0072B2.

**Top-right Hero badge**: circular "**100%**" 48pt Bold #E69F00 with label "달성도" 14pt #5A5A6E.

**Animal block (상단, 세로 25%)** — 최형진 Lab:
- Background: #FDECE2 (BG_PEACH)
- Left accent bar: #D55E00 (LAB_VERMIL, vermillion) · 8px wide
- Title (좌상단): "동물 (최형진 Lab) — 3D 골격 DB + VTA-NAc two-site 광유전학" 18pt Bold #003380
- 좌우 2열 (14pt #282945):
  - **Left column**:
    - "**3D 골격 DB**: 자유 행동 설치류"
    - "DeepLabCut 멀티뷰 3D 포즈"
    - "코·귀·척추·앞/뒷발·꼬리 트래킹"
    - "그루밍 · 보행 · rearing · drinking (positive)"
  - **Right column**:
    - "**VTA-NAc two-site 광유전학**"
    - "DAT-cre 마우스 · AAV5-ChrimsonR (VTA) + AAV9-GRAB_DA1h (NAc)"
    - "594 nm · 30s · 5/10/20 Hz 광자극"
    - "Fiber photometry 실시간 도파민 측정"

**Human block (하단, 세로 55%)** — 이상아 Lab:
- Background: #EDF6FC (SNU Ice)
- Left accent bar: #11604B (LAB_TEAL) · 8px wide
- 2 equal rounded rectangle panels side by side, thin #0072B2 outline, 24px padding

**LEFT panel — 실험 1**:
- Badge (좌상단): "실험 1" 18pt Bold #E69F00
- Title: "MixedEmo fMRI + EEG (n=92)" 20pt Bold #003380
- Design bullet (12pt italic #5A5A6E): "Scene 80 × IAPS 감정자극 160 · 5조건"
- Main bullets (14pt #282945):
  - "**fMRI**: 편도체 · 전두/두정 (지각)"
  - "**fMRI**: DMN · PCC · precuneus (인출)"
  - "**ACC** 복측/배측 해리 · p = 0.010"
  - "**STAI-X1 불안** ↔ 인출 편향 · p=0.002, 0.003"
  - "**EEG 32ch 2048Hz**: Posterior θ (감정 처리) · Frontal θ (감정 충돌)"

**RIGHT panel — 실험 2**:
- Badge: "실험 2" 18pt Bold #E69F00
- Title: "가상공간 탐험 EEG + 해마 OCAT" 20pt Bold #003380
- Design bullet: "4 랜드마크 (근접·원격·혼합·없음) · 1분 VR"
- Main bullets (14pt #282945):
  - "**Sequential reactivation**: reactivation bias (시간 ↑)"
  - "**디코딩 정확도 10-15%** (chance 4%)"
  - "*Imaging Neuroscience* · Lim et al. 2025"
  - "**해마 OCAT**: CA23DG · CA1 맥락 범주화"
  - "**청소년**: CA23DG ↔ OFC · 정서적 학대 결여"

**Bottom caption** (18pt #282945):
"인간 n=92 fMRI·EEG DB + 동물 3D 골격·VTA-NAc two-site 프로토콜 구축 완료"

**Bottom-right**: "6 / 15" 12pt #5A5A6E.

## Style Rules
- Animal block 상단 얇은 띠 (BG_PEACH 배경, LAB_VERMIL 좌측 bar)
- Human block 하단 넓은 영역 (SNU Ice 배경, LAB_TEAL 좌측 bar)
- Hero 100% badge 우상단 원형 (Signal Orange)
- 실험 번호 Signal Orange 배지
- 핵심 수치 (p-값, n=92) bold로 강조

## Consistency Lock
- Lab 색 bar 체계: vermillion (최형진) + teal (이상아) 동시 표기
- 동일 panel card style (S8·S9와 대비되는 3-block 구조)

## Negative
- no photorealistic brain images
- no 3D neurons
- no complex fMRI rendering
- no stock medical photos
- no circular diagrams
- no cluttered bullets (최대 5 per panel)

## Fallback Layout
If animal top band + 2 human panels overflow:
- Reduce animal block to 1줄 (좌우 2열 → 1열)
- Shrink human bullets (5 → 4 per panel)

## Self-Validation
- [x] Single core message: "사람 MixedEmo + 동물 two-site 양축 DB 100% 달성"
- [x] Word count ≤ 500 (granular detail 포함)
- [x] Colors ≤ 6 (SNU Blue, Signal Orange, LAB_TEAL, LAB_VERMIL, BG_PEACH, SNU Ice)
- [x] Complexity: MED-HI
- [x] Lab별 수치 정합: n=92 · 32ch 2048Hz · p=0.010 · p=0.002 · 10-15% · CA23DG

## Review Status
GRANULAR (Phase 7 animal block 확장 + human 수치 구체화 완료)
