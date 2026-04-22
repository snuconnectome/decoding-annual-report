# S14 Prompt — Wrap-up / Q&A

## API Configuration
- model: gemini-3.1-flash-image-preview
- resolution: 4K (3840x2160)
- aspect_ratio: 16:9
- thinking_mode: high
- language: ko

## MASTER THEME (snu_neurox)
- Layout: 3 takeaway cards + closing thanks

## Prompt for nanobanana2

Create a 16:9 horizontal Korean closing-summary infographic on #FFFFFF background.

Top-left header: "디코딩과제 3년차" in 14pt #003380.

Main title (large, centered in upper 20%): "Summary" in 48pt Bold #003380.
Korean subtitle below: "3차년도 핵심 성과 요약" in 22pt #0072B2.

Main area (middle 50% of slide height): 3 equal-sized rounded rectangle cards horizontally arranged, with #EDF6FC fill and thin #0072B2 outline, each 28px padding.

Card 1 (Takeaway 1):
- Big number on top: "97.5%" in 48pt Black Bold #E69F00
- Label below number: "합계 달성도" in 22pt Bold #003380
- Description: "4개 평가항목 · 전부 100% 달성" in 14pt #282945

Card 2 (Takeaway 2):
- Big text on top: "5 종" in 48pt Black Bold #E69F00
- Label: "멀티스케일 파운데이션 모델" in 22pt Bold #003380
- Description: "SwiFT · DIVER · POYO · MBBN · TabLeT" in 14pt #282945

Card 3 (Takeaway 3):
- Big number on top: "600M" in 48pt Black Bold #E69F00
- Label: "4차년도 예산 (단위: 천원)" in 22pt Bold #003380
- Description: "종간 파운데이션 사전학습 진행" in 14pt #282945

Bottom area (lower 25% of slide height):
- Centered large text: "감사합니다 · Thank you" in 40pt Bold #003380
- Below: "Q & A" in 32pt Bold #E69F00 centered
- Very small caption at bottom 14pt #5A5A6E: "서울대학교 · connectome Lab · @snu.ac.kr"

Bottom-right: "14 / 14" in 12pt #5A5A6E.

## Style Rules
- 3 summary cards matching the storyboard takeaways
- Closing "감사합니다 · Q & A" visually prominent
- No personal contact info beyond the institutional domain

## Consistency Lock
snu_neurox theme, Signal Orange for hero numbers.

## Negative
- no personal phone/email in body text (only institutional domain in caption)
- no photorealistic handshake or Thank-you image
- no confetti, no gradients, no 3D "Thank You"
- no complex contact card

## Fallback Layout
If 3-card + closing fails:
- Simplify to closing text only: "97.5% · 17편 · 600M" one-line + "감사합니다 Q&A"

## Self-Validation
- [x] Single core message: "3 core takeaways + thanks"
- [x] 3 cards + closing
- [x] Word count ≤ 400
- [x] Colors ≤ 5
- [x] Complexity: LOW
- [x] No personal identifiers (redaction compliance)

## Review Status
READY
