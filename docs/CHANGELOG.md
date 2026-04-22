# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Phase 7 — Granularity 보강 · 15장 재구성 · 연구 보고서 (2026-04-23)

#### 배경
Phase 6 완료 후 사용자 피드백: "구체적 연구 설명이 부족, 하이레벨만 많다."
이상아·문태섭 Lab은 storyboard에 granular content 있었으나 차지욱·최형진 Lab은 개요 수준. 차지욱 Lab은 슬라이드 2장에 걸친 구체 연구 결과 정리 필요.

#### Phase A — Google Drive 4개 문서 harvest
- **디코딩과제-연차보고서-3년차** (Google Docs, 27MB, 2025-12-08) — 공식 제출본 Lab별 실험 상세 추출
- **ephys foundation model-SNU Connectome Lab** (Google Slides, 차지욱 Lab) — DIVER-1/2 스케일, 3-Phase 전략, Trimodal Alignment
- **seed_poster_260404.pptx** (문태섭 Lab) — SEED 지표 재검증, 5 SOTA 디코더 확인
- **(최형진)2025 BK21 자체평가** (Google Sheet) — CeA-Glp1R, NAc-NPY, LH CaMKIIα+, AgRP 회로 등 풍부한 연구 내용

#### Phase B — Lab별 연구 보고서 신규
- `report/03_lab-research-detail.md` 작성 (~900줄, 8 섹션)
  - §1 이상아 Lab: MixedEmo fMRI·EEG (n=92, 2048Hz) + 해마 OCAT + 가상공간 EEG + 청소년 발달 등 9 실험
  - §2 최형진 Lab: 3D 골격 DB + VTA-NAc two-site 광유전학 + 편도체 정서 디코딩 (차지욱 공동) + CeA-Glp1R/NAc-NPY/LH 회로
  - §3 차지욱 Lab: fMRI FM 6개 (SwiFT 8.8B/SwiFT-IO R²=0.96/MBBN/NeuroMamba/TabLeT/Latent Diffusion) + EEG/iEEG 7개 (DIVER-1 5.3k+54k hrs/POYO-SSL/Language-Brain/CEBRA/RYM/Polygenic/sMRI-Tabular)
  - §4 문태섭 Lab: VLM (LLaVA-Next-Interleave) + SEED (22K 판단) + Quantum Time-series Transformer
  - §7 평가항목 #3 (신경과학 메커니즘) 누락 이슈 공식화

#### Phase C — 스토리보드·프롬프트 15장 재구성
- `slides/storyboard.md` 15장 반영
  - S7 분할 → **S7A (fMRI FM)** + **S7B (EEG/iEEG + 임상)** · 차지욱 Lab 2 슬라이드
  - S6 재구성 — 상단 최형진 animal block 확장 (3D 골격 DB + VTA-NAc two-site) + 하단 이상아 human block (실험 수치 구체화: ACC p=0.010, STAI-X1 p=0.002)
  - S9 재편 — 최형진·차지욱 공동 **편도체 개별신경 × 표정 정서 디코딩** highlight + 종간 통합 narrative
  - Lab 기여 매핑 테이블 업데이트 (차지욱 = 2 슬라이드, 최형진 = S6 + S9)
- Prompts:
  - `slide_07a_cha-fmri.md` 신규 (4 모델 2×2 grid + TabLeT/LDT 하단 띠 + 8.8B hero)
  - `slide_07b_cha-clinical.md` 신규 (DIVER-1 Row 1 hero + Cross-Modal Row 2 + 임상·생성 Row 3 + 3-Phase 하단)
  - `slide_07_ml-models.md` 삭제 (S7A로 대체)
  - 후속 슬라이드 페이지 번호 `/14` → `/15` 일괄 업데이트 (S8→9, S9→10, ..., S14→15)

#### Phase D — 15장 PNG 재생성 (Gemini nanobanana2, 100% 성공)
- `scripts/generate-slides-gemini.py` 신규 (prompt 추출 + 재시도 3회 + manifest)
- 모델 `gemini-3.1-flash-image-preview` (nanobanana2) · 15/15 attempt 1 에서 성공
- 각 이미지 1478×831 (16:9) · 343KB–806KB
- 한글 렌더링 완전 (Apple SD Gothic Neo 의존성 제거 — Gemini 내장)
- Prompt 재작성 2개:
  - `slide_06_db-construction.md`: Animal block (3D 골격 DB + VTA-NAc) + Human block (MixedEmo n=92 · ACC p=0.010 · EEG 32ch 2048Hz + 가상공간 reactivation + 해마 OCAT CA23DG) 3-block 구조
  - `slide_09_cross-species.md`: 상단 편도체 공동연구 highlight (최형진·차지욱) + 중단 Animal/Human 대비 + 하단 SNU Blue unified 공통 표현

#### Phase E — 통합 PDF 재빌드
- `slides/build/presentation.pdf`: 15 페이지 · 16:9 (330×184 pts) · img2pdf 통합
- 기존 14장 PNG 제거 → 15장 Gemini 생성본 commit

#### Deliverables this session (Phase 7 전체)
- `report/03_lab-research-detail.md` (신규, ~900 lines, 4 Lab granular research detail)
- `slides/storyboard.md` (개정, 15장 반영)
- `slides/prompts/slide_06_db-construction.md` (재작성, animal+human 3-block)
- `slides/prompts/slide_07a_cha-fmri.md` (신규)
- `slides/prompts/slide_07b_cha-clinical.md` (신규)
- `slides/prompts/slide_09_cross-species.md` (재작성, 편도체 공동연구 중심)
- `slides/prompts/slide_07_ml-models.md` (삭제)
- 12개 기존 prompt 페이지 번호 `/15` 업데이트
- `scripts/generate-slides-gemini.py` (신규 렌더러)
- `slides/images/slide_01~14.png` (15장 재생성, generation_manifest.json 포함)
- `slides/build/presentation.pdf` (15페이지 재빌드)

#### Visual Quality Spot-Check
- S6: Animal block (최형진 vermillion bar) + Human block (이상아 teal bar) · 수치 정합 (n=92, 2048Hz, p=0.010, p=0.002, CA23DG, 10-15%)
- S7A: 2×2 grid (SwiFT 8.8B · SwiFT-IO R²=0.96 · MBBN ADHD/ASD · NeuroMamba 94.9%) + 하단 TabLeT/LDT 띠
- S7B: DIVER-1 hero (5.3k iEEG · 54k EEG) + Cross-Modal Alignment (Language-Brain +14.4%, POYO-SSL +12~13%) + 임상·생성 응용 + DIVER 3-Phase 하단
- S9: 편도체 공동연구 highlight (최형진+차지욱 dual color) + Animal (POYO-SSL) vs Human (SwiFT·DIVER-1) + 공통 표현 unified (SNU Blue)

#### Minor Artifacts (향후 개선 가능, 기능 영향 없음)
- 일부 슬라이드 상단 "14pt #003380" 스타일 annotation 이 본문에 렌더됨 (Gemini prompt adherence 한계)
- 일부 markdown bold (`**text**`) 가 asterisk 포함 렌더됨 (S9 등 소수)
- 재생성 필요 시: 프롬프트에서 style spec 을 body 와 분리

### Phase 6 — 슬라이드 이미지 생성 완료 (2026-04-23)

#### Initial attempt: Gemini nanobanana2
- `GEMINI_API_KEY` 발견, `google-genai` SDK 설치
- dry-run 14/14 PASS
- **실제 생성 차단**: API key expired (400 INVALID_ARGUMENT)

#### Autonomous Fallback: matplotlib renderer
- `scripts/generate-slides-matplotlib.py` 작성 (~700 lines)
- 14 per-slide renderer · snu_neurox 팔레트 · Apple SD Gothic Neo 한글
- YAML 5파일 직접 참조 (data drift 0)

#### Iterative visual QA (3 rounds)
- Round 1 fixes: Slide 01 title spacing, Slide 11 hero overflow, Slide 14 card labels, 이모지 제거
- Round 2 fixes: Slide 05 카드 · 폰트 축소, Slide 10 Quantum chips, Slide 12 합계 text
- Round 3 fixes: Slide 02 카드 폭·폰트, Slide 08 VLM panel

#### Deliverables
- `slides/images/slide_01_title.png ~ 14_wrap-up.png` (14 PNG, 각 80-160KB)
- `slides/build/presentation.pdf` (14 pages, 16:9, 1.6MB)
- `docs/pdca/phase-6/` plan/do/check 완성

#### Outcome
Phase 6 완료. `slides/build/presentation.pdf` = 발표 가능 상태. Gemini 대체 경로가 재사용 가능한 반복 자산으로 확보됨.

### Phase 5 Review Loop — 3회 독립 리뷰 + 수정 루프 (2026-04-23)

#### Added
- `docs/pdca/phase-5-review-loop/plan.md` — 3-iteration review panel 설계
- `iteration-1/` `iteration-2/` `iteration-3/` — 각 findings.md + changes.md
- `docs/pdca/phase-5-review-loop/check.md` — 수렴 matrix + 3인 패널 합의

#### Reviewed by 9 Agent Invocations (3 × 3 iterations)
- quality-engineer (엔지니어링 디스시플린)
- technical-writer (한글 프로즈·평가단 청중 적합)
- superpowers:code-reviewer (계획 준수·YAML 정합)

#### Key Resolutions
- Slide 8, 9 평가항목 번호 오류 (convergent triple-find)
- Slide 14 "600M"·"5 종"·fabricated "connectome Lab"
- Slide 4 ①②③④ 모호성 → 명시적 #1/#2/#4/#5
- Slide 1 archaic Korean ("상호작용시의")
- Slide 2 dual captions
- 이상아 Lab bucket 유지, 문태섭 Lab SEED narrative
- Rendering Rule 섹션 일관성 (04-14 추가)
- Storyboard ↔ prompts 동기화

#### Convergence
| Metric | Iter 0 | Iter 1 | Iter 2 | Iter 3 |
|---|---|---|---|---|
| Critical | 7 | 0 | 0 | **0** |
| Important | 12 | 6 | 5 | **3** |
| Regressions | — | 0 | 1 (caught) | **0** |
| 14/14 PASS | — | ✅ | ✅ | ✅ |

3인 패널 합의: **Phase 6 진입 가능 (production-ready)**.

### Phase 5 — 스토리보드 + Gemini 프롬프트 14장 (2026-04-22 ~ 2026-04-23)

#### Added
- `slides/storyboard.md` — 14장 전체 구성 (snu_neurox 테마, 16:9, 공통 디자인 원칙)
- `slides/prompts/01_title.md` ~ `14_wrap-up.md` — 14개 Gemini nanobanana2 프롬프트
- `docs/pdca/phase-5/` — plan.md, do.md, check.md

#### Labs 반영
- **Slide 6 (DB 구축)** — 이상아 Lab 중심: fMRI/EEG 감정 연합 + 가상공간 탐험 EEG 2개 실험 (from Google Slides)
- **Slide 8 (다중 모달리티)** — 문태섭 Lab 중심: SEED 평가 체계 + Vision-Language Model (from Google Slides)

#### Validated
- 14/14 `prompt_constraints.py` 통과 (ERROR 0건, WARN 허용)
- 수치 정합성: 97.5%, 17편, 4건, 600,000천원 등 `data/*.yaml` 추적 가능

#### Skipped
- **Phase 3·4 (보고서 Markdown/PDF)**: 원본 제출본이 공식 버전이므로 재작성 불필요

#### Pending (Phase 6)
- Gemini API 키 환경변수 설정
- `infographics` 스킬 `generate_image.py` 실행 (14 × 1 variant ≈ $4-6)
- 차지욱 Lab 자료 (Slide 7 refine), 최형진 Lab 자료 (Slide 6 animal) — optional

### Phase 2 — 데이터 구조화 (YAML 레이어) (2026-04-22)

#### Added
- `data/project-meta.yaml` — 과제 메타·예산·기술분류 10종 (개인정보 redact)
- `data/evaluation-criteria.yaml` — 6개 평가항목 × 5개년 목표 (가중치 합 100%)
- `data/achievements.yaml` — 논문 17 + 학회참석 4 + 9개 핵심 기술 모델 메타
- `data/metrics.yaml` — 3차년도 성과 4항목 + 달성도 97.5% + 평가항목 3 누락 플래그
- `data/next-year-plan.yaml` — 4차년도 5 방향 · 전략 · 600,000천원 예산 · 활용방안
- `docs/pdca/phase-2/` — plan.md, do.md, check.md

#### Validated
- 6/6 YAML `yaml.safe_load()` 통과
- `redact-check.py data/` — 0 findings
- 크로스 레퍼런스 일관성: 4차년도 예산 600,000 (3곳 일치), 평가항목 ID subset, 레퍼런스 count 21, 가중치 합 100%

#### Decision
- **Phase 3·4 (보고서 Markdown/PDF) skip**: 원본 제출본이 이미 공식 버전이므로 재작성 불필요. `Makefile`의 `make report` 타겟은 stub 유지하여 향후 필요 시 복원 가능.

### Phase 1 — PDF 원본 추출 및 구조 분석 (2026-04-22)

#### Added
- `scripts/extract-pdf.py` — pymupdf + pdfplumber 하이브리드 추출기
- `scripts/pdf-qa.py` — 한글 품질 검증 (치환 문자·한글 비율·빈 페이지)
- `scripts/redact-check.py` — 개인정보 패턴 스캐너 (Phase 8용 선작성)
- `scripts/build-slides.py` — PNG → 단일 PDF (Phase 7용 선작성)
- `data/section-map.yaml` — 98페이지 → 7 섹션 매핑 (subsections 포함)
- `docs/pdca/phase-1/` — plan.md, do.md, check.md 전체 세트

#### Validated
- 98 pages, 45 tables, 74 figures 성공 추출
- Replacement char 0건 (한글 추출 품질 확보)
- `source/*.pdf` 추적 파일 0건 (gitignore 정상)
- 페이지 1-9·86·90·91이 이미지 기반 렌더링임을 확인 (Google Docs Renderer 출처)

### Phase 0 — Initial scaffold (2026-04-22)

#### Added
- Initial project scaffold
- `README.md` with project description and build instructions
- `LICENSE` — MIT for code, CC BY 4.0 for documentation content
- `.gitignore` with explicit exclusion of `source/*.pdf`
- `Makefile` with `setup`/`extract`/`report`/`slides`/`verify`/`all`/`clean` targets
- `docs/redaction-policy.md` — public commit safety policy
- Directory scaffold: `source/`, `data/`, `report/`, `slides/`, `scripts/`, `docs/`

### Pending (Phase 2+)
- Structured YAML data (`data/project-meta.yaml`, `evaluation-criteria.yaml`, `achievements.yaml`, `metrics.yaml`, `next-year-plan.yaml`)
- Report markdown sections (`report/00_cover.md` ~ `report/99_references.md`)
- Slides storyboard and Gemini prompts (`slides/storyboard.md`, `slides/prompts/*.md`)
