# Do: Phase 1 — 실행 로그

## 타임라인

### 2026-04-22 23:04 KST — Phase 0 승계
Phase 0 스캐폴드·초기 커밋·public repo (`snuconnectome/decoding-annual-report`) 완료 상태에서 Phase 1 개시.

### 2026-04-22 23:13 KST — PDF 복사 및 gitignore 검증
- `cp` 명령으로 원본 PDF를 `source/original-3year-report.pdf`에 복사 (27MB)
- 검증: `git status --short`에서 **`source/` 경로가 나타나지 않음** 확인
- 검증: `git ls-files source/` → 0개 (gitignore 정상 동작)
- **결과**: Redaction 2차 방어선(파일시스템 차단) 정상 작동

### 2026-04-22 23:13 KST — venv 및 의존성 설치 (background)
- `python3 -m venv .venv` (Python 3.10.12)
- `.venv/bin/pip install pymupdf pdfplumber pyyaml img2pdf Pillow pypdf`
- 결과: 모든 패키지 설치 성공
  - PyMuPDF 1.27.2.2
  - pdfplumber 0.11.9
  - PyYAML 6.0.3
  - img2pdf 0.6.3
  - Pillow 12.2.0
  - pypdf 6.10.2

### 2026-04-22 23:14–23:15 KST — 스크립트 4종 작성
venv 설치 대기 중 병렬 진행:
- `scripts/extract-pdf.py` (pymupdf + pdfplumber 하이브리드 추출)
- `scripts/pdf-qa.py` (한글 품질 검증, 치환 문자 감지)
- `scripts/redact-check.py` (Phase 8 선작성, 개인정보 패턴 스캐너)
- `scripts/build-slides.py` (Phase 7 선작성, PNG → PDF)

모두 `chmod +x`로 실행 권한 부여.

### 2026-04-22 23:15 KST — section-map.yaml 작성
98페이지를 7개 섹션(+ subsection)으로 매핑. TOC 페이지가 아닌 **실제 콘텐츠 기반** 매핑 채택. 예상 표 위치와 예상 그림 위치도 함께 정의하여 추출 결과 검증 기준 마련.

### 2026-04-22 23:16 KST — 추출 실행

```
[1/2] pymupdf: 페이지 텍스트 + 이미지 추출 ...
      98 pages, 74 figures
[2/2] pdfplumber: 표 추출 ...
      45 tables
```

**발견된 경고 1**: `Could not get FontBBox from font descriptor because None cannot be parsed as 4 floats`

- **조사**: pdfplumber GitHub Issues 다수 보고된 알려진 경고. 특정 폰트 디스크립터 블록에서 FontBBox 메타가 비정상일 때 발생. **텍스트 추출 정확도에 영향 없음**.
- **영향**: 없음 (추출 결과 98 pages 온전, 한글 치환 문자 0개).
- **조치**: 경고 허용, do.md에 기록.

### 2026-04-22 23:16 KST — QA 실행

```
QA 완료: 98 pages, 0 critical, 4 warnings
```

**발견된 중대 사실**: 페이지 1-9, 86, 90, 91이 **이미지 기반 렌더링** (텍스트 4-28자만 추출).

#### 조사 과정 (Root Cause Analysis)

1. **증상**: QA 리포트에서 페이지 83, 86, 90, 91이 sparse_text 경고. 추가로 p1-9도 텍스트 매우 적음 (4-15자).

2. **가설**: 해당 페이지들이 이미지로 렌더링되었을 것.

3. **검증**: `fitz.Page.get_images(full=True)`로 페이지별 이미지 수 확인:
   ```
   p001: text=4   chars, images=1
   p005: text=9   chars, images=1
   p086: text=28  chars, images=1
   p090: text=24  chars, images=1
   p091: text=29  chars, images=1
   ```

4. **추가 증거**: `metadata.json`의 `pdf_metadata.producer` = **"Skia/PDF m149 Google Docs Renderer"**
   - Google Docs에서 복잡한 표·폼·다이어그램을 포함한 PDF를 내보낼 때, 서식 보존을 위해 일부 페이지를 이미지로 변환하는 패턴이 확인됨.
   - 한국 R&D 제안서 시스템의 전형적 출력 포맷.

5. **결론**: 이미지 기반 렌더링은 원본 PDF의 특성. 추출 도구 결함이 아님.

#### 영향 평가

이 발견은 프로젝트에 **긍정적** 영향:

- **Redaction 1차 방어선 강화**: 표지 2페이지(전화번호·연구자번호·전자서명)가 이미지 형태이므로 자동 텍스트 추출로는 노출되지 않음. 개인정보 유출 경로가 자연스럽게 차단됨.
- **Phase 3 작업 방향**: `report/00_cover.md`는 이미 맥락에 있는 PDF 내용(Phase 0 이전 Plan mode에서 Read tool로 전체 PDF 읽음)을 기반으로 redact된 버전을 수기로 작성하면 충분.
- **Track B 시각 자료**: p86, p90, p91의 일정·전략 다이어그램 이미지는 `figures/`에 추출되어 있으므로 Phase 5 스토리보드에서 레퍼런스로 활용 가능.

**의사결정**: OCR 파이프라인 추가 **불필요**. 복잡도 증가 대비 실익이 낮음 (내용은 이미 확보, 개인정보는 자연스럽게 보호됨).

### 2026-04-22 23:18 KST — make verify + scripts 로드 검증

```
---MAKE-VERIFY---
스캔 대상 파일 없음 (경로: report). 통과.
---SCRIPTS-LOAD---
OK: extract-pdf.py
OK: build-slides.py
OK: pdf-qa.py
OK: redact-check.py
```

**발견된 경고 2**: `FutureWarning: Possible set symmetric difference at position 12` in redact-check.py

#### 조사

- **위치**: `scripts/redact-check.py:48`의 `re.compile(r"20\d{2}\s*[-~~–]\s*20\d{2}")`
- **원인**: 문자 클래스 `[-~~–]` 내 `~~` 중복. Python 3.13+ 또는 `re` 모듈은 문자 클래스 내 연속된 같은 문자를 set symmetric difference 연산자로 해석할 가능성을 경고. 단순 오타.
- **의도**: 연도 범위 구분자(하이픈·틸드·en-dash·em-dash) 허용
- **수정**: `[-~–—]` 로 중복 제거 + em-dash 추가
- **검증**: 재실행 시 경고 없음 확인

**교훈**: "Warnings = Future technical debt". 즉시 수정하지 않으면 향후 Python 버전 업그레이드에서 에러로 승격될 수 있음.

## 주요 수치 결과

| 지표 | 목표 | 실제 | 상태 |
|---|---|---|---|
| 추출 페이지 | 98 | 98 | ✅ |
| 치환 문자 | 0 | 0 | ✅ |
| 추출 표 | ≥5 | **45** | ✅ 초과 |
| 추출 그림 | ≥3 | **74** | ✅ 초과 |
| 섹션 매핑 | 7 | 7 (+ subsections) | ✅ |
| git 보호 | source/*.pdf 추적 0 | 0 | ✅ |
| 스크립트 로드 | 4/4 | 4/4 | ✅ |
| 총 실행 시간 | ≤ 90분 | ~18분 | ✅ 우수 |

## 학습 사항 (Phase 2 이후 적용)

1. **Korean Government R&D PDF 특성**: Google Docs Renderer 기반 PDF는 복잡한 페이지를 이미지화함. 텍스트 기반 workflow는 본문 페이지(p11+)에 집중, 표지·요약문은 수기 작성 또는 OCR 고려.

2. **pdfplumber 표 추출의 강점**: 테이블 추출이 pymupdf보다 명확히 우수함. 45개 표 추출 중 CSV 구조 온전성이 높음 (e.g., `097_t01.csv`의 레퍼런스 목록).

3. **Redaction을 추출 단계에서도 검증**: 원본 복사 직후 `git status` + `git ls-files`로 이중 확인이 중요. 이 습관은 향후 Phase마다 반복 적용.

4. **Warning zero tolerance**: FutureWarning을 무시하지 않고 즉시 조사·수정하여 장기적 기술부채 방지.

5. **Meta-data is evidence**: `metadata.json`에 도구 버전·추출 시각·producer 기록이 향후 재현성(reproducibility)의 핵심.
