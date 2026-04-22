# Plan: Phase 6 — 슬라이드 이미지 생성

## Hypothesis
14개 프롬프트를 Gemini nanobanana2로 실제 PNG 이미지로 변환. API key 문제 발생 시 matplotlib fallback으로 보장된 완성도 확보.

## Risks
- Gemini API key expired/unavailable → fallback 필요
- 한글 폰트 렌더링 실패 → Apple SD Gothic Neo 확인 필수
- Layout overflow → 반복 시각 검수 필요
