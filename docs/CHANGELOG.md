# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
