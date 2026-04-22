# 디코딩과제 3년차 연차보고서 빌드 자동화
#
# Usage:
#   make setup   — Python 가상환경 + 의존성 설치
#   make extract — 원본 PDF에서 텍스트·표 추출 (source/*.pdf 필요)
#   make report  — report/*.md → KoPub 한글 PDF
#   make slides  — slides/images/*.png → 통합 PDF
#   make verify  — redaction 자동 스캔
#   make all     — extract + report + slides + verify
#   make clean   — build 산출물 정리

.PHONY: help setup extract report slides verify all clean

PY ?= python3
VENV := .venv
VENV_BIN := $(VENV)/bin

help:
	@echo "Available targets:"
	@echo "  setup    - Install Python dependencies in .venv"
	@echo "  extract  - Extract text/tables from source PDF"
	@echo "  report   - Build report PDF (requires doc-format skill)"
	@echo "  slides   - Build slides PDF (combines images/*.png)"
	@echo "  verify   - Run redaction scan on report/"
	@echo "  all      - extract + report + slides + verify"
	@echo "  clean    - Remove build artifacts"

$(VENV)/bin/activate:
	$(PY) -m venv $(VENV)
	$(VENV_BIN)/pip install --upgrade pip

setup: $(VENV)/bin/activate
	$(VENV_BIN)/pip install pymupdf pdfplumber pyyaml jinja2 img2pdf Pillow pypdf

extract: setup
	@test -f source/original-3year-report.pdf || (echo "ERROR: Place original PDF at source/original-3year-report.pdf" && exit 1)
	$(VENV_BIN)/python scripts/extract-pdf.py source/original-3year-report.pdf source/extracted-text/

report:
	@echo "[TODO] Invoke doc-format skill on merged report/*.md"
	@echo "       Target: report/build/final.pdf"

slides:
	@echo "[TODO] Combine slides/images/*.png -> slides/build/presentation.pdf"
	$(VENV_BIN)/python scripts/build-slides.py slides/images slides/build/presentation.pdf

verify:
	$(VENV_BIN)/python scripts/redact-check.py report/

all: extract report slides verify

clean:
	rm -rf report/build/* slides/build/*
	find . -type d -name __pycache__ -exec rm -rf {} +
	@echo "Cleaned build artifacts."
