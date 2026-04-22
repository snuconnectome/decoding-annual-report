#!/usr/bin/env python3
"""
PDF → text / tables / images 추출기 (3년차 연차보고서용).

하이브리드 전략:
  - pymupdf (fitz): 페이지 텍스트, 이미지 (bbox 메타 포함)
  - pdfplumber: 표 (레이아웃 인식 우위)

한글 처리:
  - UTF-8 인코딩 고정
  - 유니코드 NFC 정규화 (조합형 → 완성형)
  - 치환 문자(U+FFFD) 검출은 pdf-qa.py에서 수행

Usage:
    python extract-pdf.py <input.pdf> <output_dir>
"""
from __future__ import annotations

import argparse
import csv
import json
import sys
import unicodedata
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import fitz  # pymupdf
import pdfplumber


def nfc(text: str | None) -> str:
    if not text:
        return ""
    return unicodedata.normalize("NFC", text)


def extract_pages_and_images(pdf_path: Path, out_dir: Path) -> dict[str, Any]:
    pages_dir = out_dir / "pages"
    figures_dir = out_dir / "figures"
    pages_dir.mkdir(parents=True, exist_ok=True)
    figures_dir.mkdir(parents=True, exist_ok=True)

    doc = fitz.open(pdf_path)
    figures_manifest: list[dict[str, Any]] = []

    for page_idx, page in enumerate(doc, start=1):
        text = nfc(page.get_text("text"))
        (pages_dir / f"{page_idx:03d}.txt").write_text(text, encoding="utf-8")

        for fig_idx, img_info in enumerate(page.get_images(full=True), start=1):
            xref = img_info[0]
            try:
                pix = fitz.Pixmap(doc, xref)
                if pix.n - pix.alpha >= 4:
                    pix = fitz.Pixmap(fitz.csRGB, pix)
                name = f"{page_idx:03d}_f{fig_idx:02d}.png"
                pix.save(figures_dir / name)
                figures_manifest.append(
                    {
                        "page": page_idx,
                        "index": fig_idx,
                        "file": name,
                        "width": pix.width,
                        "height": pix.height,
                        "xref": xref,
                    }
                )
                pix = None
            except Exception as exc:
                print(f"  WARN: page {page_idx} figure {fig_idx}: {exc}", file=sys.stderr)

    metadata = {
        "pdf_path": str(pdf_path),
        "page_count": doc.page_count,
        "pdf_metadata": {k: nfc(v) for k, v in (doc.metadata or {}).items()},
    }
    doc.close()

    (figures_dir / "figures.json").write_text(
        json.dumps({"figures": figures_manifest}, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )

    return metadata | {"figures_extracted": len(figures_manifest)}


def extract_tables(pdf_path: Path, out_dir: Path) -> int:
    tables_dir = out_dir / "tables"
    tables_dir.mkdir(parents=True, exist_ok=True)
    total = 0
    with pdfplumber.open(pdf_path) as pdf:
        for page_idx, page in enumerate(pdf.pages, start=1):
            try:
                tables = page.extract_tables() or []
            except Exception as exc:
                print(f"  WARN: page {page_idx} table extract: {exc}", file=sys.stderr)
                continue
            for t_idx, tbl in enumerate(tables, start=1):
                if not tbl or all(not any(row) for row in tbl):
                    continue
                path = tables_dir / f"{page_idx:03d}_t{t_idx:02d}.csv"
                with path.open("w", encoding="utf-8", newline="") as f:
                    writer = csv.writer(f)
                    for row in tbl:
                        writer.writerow([nfc(cell) for cell in row])
                total += 1
    return total


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path, help="원본 PDF 경로")
    parser.add_argument("out_dir", type=Path, help="추출 결과 출력 디렉토리")
    args = parser.parse_args()

    if not args.pdf.exists():
        print(f"ERROR: {args.pdf} does not exist", file=sys.stderr)
        return 1

    args.out_dir.mkdir(parents=True, exist_ok=True)

    print(f"[1/2] pymupdf: 페이지 텍스트 + 이미지 추출 ...")
    meta = extract_pages_and_images(args.pdf, args.out_dir)
    print(f"      {meta['page_count']} pages, {meta['figures_extracted']} figures")

    print(f"[2/2] pdfplumber: 표 추출 ...")
    n_tables = extract_tables(args.pdf, args.out_dir)
    print(f"      {n_tables} tables")

    meta["tables_extracted"] = n_tables
    meta["extracted_at"] = datetime.now(timezone.utc).isoformat()
    meta["tools"] = {
        "pymupdf": getattr(fitz, "__doc__", "").split("\n")[0][:40] or "unknown",
        "pdfplumber": getattr(pdfplumber, "__version__", "unknown"),
    }
    (args.out_dir / "metadata.json").write_text(
        json.dumps(meta, indent=2, ensure_ascii=False, default=str),
        encoding="utf-8",
    )

    print(f"완료. metadata.json 저장.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
