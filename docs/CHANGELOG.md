# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

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
