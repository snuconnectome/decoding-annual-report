# Plan: Phase 1 — PDF 원본 추출 및 구조 분석

## Hypothesis (가설)

3년차 연차보고서 원본 PDF(98페이지, 27MB)는 한글 본문·구조화된 표·그림·레퍼런스 리스트가 복합된 형태이다. 이를 **재사용 가능한 원자 단위**(페이지별 텍스트 / 표 / 이미지 / 섹션 매핑)로 분해하여 저장하면, 이후 Phase 2(YAML 구조화) 및 Phase 3(Markdown 보고서 작성)가 단일 진실(raw 추출본)을 참조하는 파이프라인으로 작동한다.

**핵심 가정**: 원본 PDF는 폰트가 내장되어 있으며, pymupdf + pdfplumber 하이브리드로 >95% 페이지에서 한글 깨짐 없이 추출 가능하다.

## Goals (정량 목표)

| 지표 | 목표 | 측정 방법 |
|---|---|---|
| 페이지 추출 성공 | 98/98 pages | `metadata.json`의 `page_count` |
| 한글 깨짐 | 0 replacement chars (`�`) | `pdf-qa.py` 결과 |
| 주요 표 추출 | ≥ 5개 (요약문·평가기준·성과표·레퍼런스) | pdfplumber 출력 |
| 주요 그림 추출 | ≥ 3개 (p86 일정·p90 전략·p91 일정) | pymupdf 이미지 목록 |
| 섹션 매핑 | 7개 섹션 공식 정의 | `data/section-map.yaml` |
| git 보호 | `source/*.pdf` 추적 파일 0개 | `git ls-files source/` 결과 |
| 시간 | ≤ 90분 (스크립트 실행 ≤ 5분) | 실측 |

## Design (설계)

### 도구 선택 rationale

| 기능 | 선택 도구 | 대안 | 선택 이유 |
|---|---|---|---|
| 페이지 텍스트 | pymupdf (fitz) | pypdf, pdftotext | 한글 폰트 내장 PDF에 안정적, 속도 우수 |
| 표 추출 | pdfplumber | pymupdf 표기능 | 레이아웃 인식 정확도 우위 |
| 이미지 추출 | pymupdf | pdfimages CLI | bbox 정보와 함께 Python 네이티브 |
| 한글 정규화 | unicodedata.NFC | NFD | 조합형 → 완성형 변환 표준 |

**하이브리드 이유**: 단일 도구 실패 시 대안 제공. 한국 R&D 보고서 PDF는 표·그림·한글이 복잡하게 얽혀 있으므로 각 요소에 특화된 도구를 조합한다.

### 데이터 플로우

```
source/original-3year-report.pdf  (gitignored)
    │
    ├── pymupdf → pages/*.txt        (NFC normalized)
    │          → figures/*.png       (CMYK→RGB 변환)
    │          → figures.json        (bbox metadata)
    │
    └── pdfplumber → tables/*.csv    (UTF-8)

    │
    ▼
source/extracted-text/              (gitignored)
├── metadata.json                   (추출 메타, 도구 버전)
├── pages/001.txt ~ 098.txt
├── tables/NNN_tNN.csv
├── figures/NNN_fNN.png
├── figures.json
└── qa-report.{json,md}             (품질 검증 결과)

data/section-map.yaml               (tracked - 구조 정보만)
```

### 섹션 매핑 전략

TOC 페이지(p10)의 페이지 번호는 실제 콘텐츠 위치와 약간 어긋날 가능성이 있으므로, **실제 콘텐츠 기반 수동 매핑**을 채택한다. 이후 검증은 매핑된 페이지에서 해당 섹션 헤더가 실제로 발견되는지 자동 확인.

### 스크립트 구조

| 파일 | 역할 | 종속성 |
|---|---|---|
| `scripts/extract-pdf.py` | 텍스트·표·이미지 일괄 추출 | pymupdf, pdfplumber |
| `scripts/pdf-qa.py` | 추출 결과 한글 품질 검증 | (stdlib only) |
| `scripts/redact-check.py` | 보고서 개인정보 스캔 (Phase 8용 선작성) | (stdlib only) |
| `scripts/build-slides.py` | 슬라이드 PNG → PDF (Phase 7용 선작성) | img2pdf |

`redact-check.py`와 `build-slides.py`는 Phase 8/7에 사용될 것이지만 Makefile이 이미 참조하므로 스텁(또는 실행 가능한 MVP)을 지금 작성해 `make verify`와 `make slides`가 실패하지 않게 한다.

## Risks & Mitigation (위험 · 대응)

| 위험 | 확률 | 영향 | 대응 |
|---|---|---|---|
| 한글 추출 깨짐 | 낮 | 높 | `pdf-qa.py`로 `�` 카운트 즉시 검출. 깨짐 시 `pdftotext -layout` 대체 검토 |
| 표 구조 손실 | 중 | 중 | pdfplumber 기본 파라미터 실패 시 `table_settings={"vertical_strategy": "lines"}` 재시도. 최종적으로 수동 CSV 보정 허용 |
| 원본 PDF 실수 commit | 낮 | 치명 | 복사 직후 `git status`로 추적 여부 확인. `.gitignore` 정상 동작 검증 통과해야 다음 단계 진행 |
| pyenv/shims Python 문제 | 낮 | 낮 | `.venv` 격리로 시스템 Python 영향 차단. `python3 -m venv` 성공 확인 |
| pymupdf 라이센스 (AGPL v3) | 0 | 0 | 본 repo MIT이나 pymupdf는 런타임 의존성만이며 소스 수정 없음. 주의: 임베딩 배포 시 라이센스 고려 |

## Dependencies (의존성)

Python 패키지 (`.venv`에 설치):
- `pymupdf >= 1.23` (fitz)
- `pdfplumber >= 0.10`
- `pyyaml >= 6.0`
- `img2pdf >= 0.5` (Phase 7 선작성용)
- `Pillow >= 10.0` (img2pdf 보조)
- `pypdf >= 4.0` (북마크 추가용, Phase 7)

시스템 도구:
- Python 3.10+ (확인됨: 3.10.12)
- `git` (확인됨)

## Acceptance Criteria (수락 기준)

Phase 1 종료 조건 (모두 충족):

1. `source/original-3year-report.pdf` 존재, `git ls-files`에서 **발견되지 않음**
2. `source/extracted-text/metadata.json` 생성, `page_count == 98` 확인
3. `source/extracted-text/pages/001.txt ~ 098.txt` 모두 생성
4. `source/extracted-text/qa-report.md`에서 replacement char 0개 또는 문서화된 예외
5. `source/extracted-text/tables/` 최소 5개 CSV 파일 (p5, p13, p87, p97 포함)
6. `source/extracted-text/figures/` 최소 3개 PNG (p86, p90, p91 예상)
7. `data/section-map.yaml` 7 섹션 정의 완료
8. `make verify` smoke test 통과 (redact-check.py가 report/ 빈 디렉토리에서 OK 리턴)
9. `scripts/` 4개 스크립트 모두 `python -c "import <module>"` 로드 성공
10. `docs/pdca/phase-1/do.md`, `check.md` 작성 완료

## Exit → Phase 2 전환 조건

- 위 10개 기준 모두 충족
- `git push origin main` 성공 (scripts + data + docs만, source/ 제외)
- PR 생성 불필요 (main 직접 작업)
