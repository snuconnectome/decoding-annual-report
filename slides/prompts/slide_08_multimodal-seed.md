# S8 Prompt — 다중 모달리티 · 시맨틱 평가 · 문태섭 Lab 중심

## API Configuration
- model: gemini-3.1-flash-image-preview
- resolution: 4K (3840x2160)
- aspect_ratio: 16:9
- thinking_mode: high
- language: ko

## Rendering Rule
- Text with pt size + color specifications → RENDER in image
- Design instructions (layout, positioning) → DO NOT render, follow as structure guide

## MASTER THEME (snu_neurox)
- Layout: upper SEED metric cards + lower Vision-Language model panel

## Prompt for nanobanana2

Create a 16:9 horizontal Korean technical infographic on #FFFFFF background.

Top-left header: "디코딩과제 3년차" in 14pt #003380.

Title: "다중 모달리티 · 시맨틱 평가 — 평가항목 #5 (25%)" in 32pt Bold #003380.
Subtitle: "문태섭 Lab 중심 · SEED 평가 체계 + Vision-Language Model" in 22pt #584B9F (purple Lab color).

Top-right: "100%" circular badge (48pt Bold #E69F00), label "달성도".

Upper half — SEED block:
Heading 22pt Bold #003380: "SEED — Semantic Evaluation for Visual Brain Decoding"
Subheading 18pt #0072B2: "22명 × 1K 이미지쌍 = 22K 인간 판단"

3 horizontal cards of equal size with #EDF6FC fill and thin #56B4E9 (Cognitive Blue) outline:

Card 1: Label "Object F1" in 22pt Bold #003380. Below: "핵심 객체 존재 기반 precision/recall" in 14pt #282945.
Card 2: Label "Caption Similarity" in 22pt Bold #003380. Below: "이미지 캡션 embedding 유사도" in 14pt #282945.
Card 3: Label "SEED" in 22pt Bold #E69F00 (HIGHLIGHTED, accent color). Below: "3개 지표 통합 averaging" in 14pt #282945.

Small caption below cards: "평가 대상 SOTA: MindEye2, NeuroPictor, UniBrain, MindBridge, BrainGuard" in 14pt #5A5A6E.

Lower half (40% of slide height) — Vision-Language Model (시각-언어 모델) + TabLeT block:

2 rounded rectangle panels side by side with SNU Blue (#003380) fill and white text:

Left panel:
- Title in white 22pt Bold: "Vision-Language Model"
- Body white 18pt: "대규모 sMRI · DTI · fMRI semantic 정렬"

Right panel:
- Title: "TabLeT"
- Body: "효율적 토크나이징 + Transformer (장기 시계열 뇌영상)"

Bottom single-line caption in 14pt #5A5A6E: "기존 평가 지표(PixCorr, SSIM, CLIP, EffNet 등)의 인간 판단 불일치 문제 해결 → semantic 정합 평가 확립"

Bottom-right: "8 / 14" in 12pt #5A5A6E.

## Style Rules
- Upper 3 cards light/secondary
- Lower 2 panels dark/primary (inverted contrast)
- SEED third card highlighted with Signal Orange text

## Consistency Lock
snu_neurox theme, consistent card sizing.

## Negative
- no network graph (5+ nodes), no circular evaluation wheel, no photorealistic brain reconstruction images, no stock AI photos

## Fallback Layout
If upper-lower 2-section layout fails:
- Focus on SEED 3 cards only, move Vision-Language/TabLeT to next slide annotation

## Self-Validation
- [x] Single core message: "SEED + Vision-Language로 semantic 평가 체계 확립"
- [x] Word count ≤ 400
- [x] Colors ≤ 5
- [x] Complexity: MED

## Review Status
READY
