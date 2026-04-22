# S6 Prompt — DB 구축 · 이상아 Lab 중심

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
- Layout: 2 experiment panels with hero metric badge

## Prompt for nanobanana2

16:9 horizontal Korean research-results infographic, #FFFFFF background.

Top-left: "디코딩과제 3년차" 14pt #003380.

Title: "데이터베이스 구축 — 평가항목 #1 (25%)" 32pt Bold #003380.
Subtitle: "이상아 Lab 중심 · 인간 정서-맥락 지각" 22pt #11604B.

Top-right: circular badge "100%" 48pt Bold #E69F00 with small "달성도" label.

Thin horizontal bar under title (#EDF6FC fill): 14pt #5A5A6E "동물 파트 (최형진 Lab): 칼슘 이미징 기반 자연환경 지각·정서 DB 구축".

Main center 60%: 2 equal rounded rectangle panels side by side, #EDF6FC fill, thin #0072B2 outline.

LEFT panel "실험 1" badge (22pt Bold #E69F00):
Title 22pt Bold #003380: "fMRI / EEG 다중양식 감정 연합"
Bullets 18pt #282945 (unified "X: Y → Z" format):
- fMRI: 편도체 · 전두/두정엽 → 지각
- fMRI: DMN · PCC · precuneus → 기억 인출
- EEG: Posterior θ → 맥락 연합 성공 마커
- EEG: Frontal θ → 맥락 갱신 마커

RIGHT panel "실험 2" badge:
Title: "가상공간 탐험 EEG — 랜드마크 공간기억"
Bullets (noun-phrase form):
- 수동적 가상공간 탐험 + EEG 재활성화 분석
- 회전지점 sequential reactivation → 시간 순서 재활성화
- 원거리 랜드마크 재활성화 ↔ 공간기억 성공 연관
- 정서적 가치 → 맥락화 디코딩의 핵심 변인

Bottom caption 18pt #282945: "정서 맥락화 기반 지각 디코딩 모델 개발의 핵심 DB · 분석 프로토콜 구축 완료"

Bottom-right: "6 / 14" 12pt #5A5A6E.

## Style Rules
- 2 equal panels side by side
- Panels use #EDF6FC fill + #0072B2 thin outline
- Hero metric 100% as prominent circular badge (top-right)
- 4 bullets max per panel

## Consistency Lock
snu_neurox theme, same panel card style as Slide 8.

## Negative
- no photorealistic brain images, no 3D neurons, no complex fMRI rendering, no stock medical photos, no circular diagrams, no cluttered bullets

## Fallback Layout
If 2-panel layout fails:
- Stack panels vertically (실험 1 above 실험 2)
- Move 100% badge to top-center

## Self-Validation
- [x] Single core message: "이상아 Lab 2개 실험으로 인간 DB 구축 100%"
- [x] Word count ≤ 400
- [x] Colors ≤ 5 (+ Lab color #11604B as sidebar)
- [x] Complexity: MED

## Review Status
READY
