#!/usr/bin/env python3
"""
슬라이드 PNG 이미지 → 단일 통합 PDF (Phase 7용 선작성).

Phase 6에서 `infographics` 스킬이 생성한 `slides/images/*.png`를
슬라이드 순서(파일명 숫자 프리픽스)대로 모아 16:9 PDF 한 개로 합친다.

Usage:
    python build-slides.py <images_dir> <output_pdf>

Example:
    python build-slides.py slides/images slides/build/presentation.pdf
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

try:
    import img2pdf
except ImportError:
    print("ERROR: img2pdf 미설치. `pip install img2pdf` 후 재실행.", file=sys.stderr)
    sys.exit(1)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("images_dir", type=Path, help="PNG 파일이 있는 디렉토리")
    parser.add_argument("output_pdf", type=Path, help="출력 PDF 경로")
    args = parser.parse_args()

    if not args.images_dir.exists():
        print(f"ERROR: {args.images_dir} 디렉토리 없음", file=sys.stderr)
        return 1

    pngs = sorted(args.images_dir.glob("*.png"))
    if not pngs:
        print(
            f"정보: {args.images_dir}에 PNG 없음. Phase 6 완료 후 재실행.",
        )
        return 0

    args.output_pdf.parent.mkdir(parents=True, exist_ok=True)

    # 16:9 1920x1080 가정. img2pdf는 이미지 원본 DPI를 존중.
    with args.output_pdf.open("wb") as f:
        f.write(img2pdf.convert([str(p) for p in pngs]))

    print(f"OK: {len(pngs)} 개 슬라이드 → {args.output_pdf}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
