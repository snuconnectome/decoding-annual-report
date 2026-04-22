# 디코딩과제 3년차 연차보고서 (정리본 & 평가단 발표 슬라이드)

> RS-2023-00265406 · 과학기술정보통신부 바이오·의료기술개발(R&D) · 뇌과학선도융합기술개발
>
> **과제명**: 동물-사람 멀티스케일 신경과학 파운데이션 모델 기반 뇌-외부환경 상호작용시의 정서에 의해 맥락화된(contextualized) 지각의 디코딩
>
> **연구책임자**: 차지욱 (서울대학교)
> **과제기간**: 2023-07-01 ~ 2027-12-31 (54개월)
> **해당 연차**: 3차년도 (2025-01-01 ~ 2025-12-31) / 제출일 2025-12-08

---

## 프로젝트 목적

본 저장소는 **이미 제출된 3년차 연차보고서의 공개 가능 아카이브본**과 **과기부/연구재단 평가단용 요약 인포그래픽 슬라이드**를 생산·관리한다.

### 두 개의 산출물 트랙

| Track | 산출물 | 포맷 |
|---|---|---|
| **A** | 3년차 최종 아카이브본 | Markdown 7개 섹션 + KoPub 한글 PDF |
| **B** | 평가단 발표용 인포그래픽 슬라이드 | PNG (개별) + 통합 PDF (12–15장) |

## 디렉토리 구조

```
.
├── source/               # 원본 PDF (gitignore, local-only)
├── data/                 # 구조화된 YAML 데이터 (메타·성과·평가항목)
├── report/               # Track A: 보고서 Markdown 7섹션
├── slides/               # Track B: 스토리보드·프롬프트·이미지
├── scripts/              # PDF 추출·빌드·redaction 자동화
└── docs/                 # 정책 문서·PDCA 로그
```

## 빌드 방법

```bash
# 의존성 설치 (최초 1회)
make setup

# 보고서 PDF 빌드
make report
# → report/build/final.pdf

# 슬라이드 PDF 빌드
make slides
# → slides/build/presentation.pdf

# 전체 빌드 + redaction 검증
make all
```

## 공개 정책 (중요)

본 저장소는 **public**으로 공개되며, 다음 redaction 정책을 엄격히 준수한다.

- **제거**: 전화번호, 국가연구자번호, 사업자·법인등록번호, 전자서명, 공동연구자 개인 연락처
- **유지**: 과제번호(IRIS 공시), 책임자 이름·소속, 연차별 예산, 학술 성과, 기술 결과
- 세부 정책: [`docs/redaction-policy.md`](docs/redaction-policy.md)

원본 PDF는 `source/` 디렉토리에 배치되며 `.gitignore`로 저장소에 포함되지 않는다.

## 재사용 자원

본 프로젝트는 아래 Claude Code 스킬·자원을 조합해 구축된다.

- `infographics` — Gemini Flash Image Preview (nanobanana2) 기반 한국어 인포그래픽 슬라이드 생성
- `doc-format` — KoPub 한글 폰트 기반 camera-ready PDF 빌드
- `cross-check` — OpenRouter 다중 LLM 품질 교차 검증

## 라이센스

- **코드/스크립트**: MIT License
- **문서/보고서 콘텐츠**: CC BY 4.0 (저작자 표시 조건)

## 인용

```bibtex
@techreport{cha2025decoding_y3,
  title  = {동물-사람 멀티스케일 신경과학 파운데이션 모델 기반 뇌-외부환경 상호작용시의 정서에 의해 맥락화된 지각의 디코딩: 3차년도 연차보고서},
  author = {차지욱},
  year   = {2025},
  institution = {서울대학교},
  number = {RS-2023-00265406},
  note   = {과학기술정보통신부 뇌과학선도융합기술개발, 제출일 2025-12-08}
}
```

## 연락

- 연구책임자: 차지욱 (서울대학교)
- 이 저장소 관련 이슈: [GitHub Issues](../../issues)
