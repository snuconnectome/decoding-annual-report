#!/usr/bin/env python3
"""
Phase 7 — 15장 슬라이드 Gemini nanobanana2 생성기.

Usage:
    GEMINI_API_KEY=xxx python scripts/generate-slides-gemini.py \
        slides/prompts slides/images

- 각 prompt 파일에서 "## Prompt for nanobanana[2]" 섹션의 body 를 추출
- gemini-3.1-flash-image-preview (nanobanana2) 호출
- PNG 를 slide_<base>.png 로 저장
- 실패 시 재시도 3회, 최종 실패는 manifest 기록
"""
from __future__ import annotations

import os
import re
import sys
import json
import time
import argparse
from pathlib import Path
from datetime import datetime

from google import genai
from google.genai import types


PROMPT_HEADER_RE = re.compile(r"^##\s+Prompt for nanobanana2?\s*$", re.MULTILINE)
NEXT_HEADER_RE = re.compile(r"^##\s+", re.MULTILINE)


def extract_prompt(md_text: str) -> str:
    m = PROMPT_HEADER_RE.search(md_text)
    if not m:
        raise ValueError("No '## Prompt for nanobanana[2]' header found")
    start = m.end()
    tail = md_text[start:]
    nm = NEXT_HEADER_RE.search(tail)
    end = nm.start() if nm else len(tail)
    return tail[:end].strip()


def prompt_filename_to_output(prompt_path: Path) -> str:
    # slides/prompts/slide_07a_cha-fmri.md -> slide_07a_cha-fmri.png
    return prompt_path.stem + ".png"


def generate_one(client, prompt_text: str, out_path: Path, retries: int = 3) -> tuple[bool, str]:
    last_err = ""
    for attempt in range(1, retries + 1):
        try:
            resp = client.models.generate_content(
                model="gemini-3.1-flash-image-preview",
                contents=[prompt_text],
            )
            for cand in resp.candidates or []:
                for part in cand.content.parts or []:
                    if part.inline_data is not None:
                        out_path.parent.mkdir(parents=True, exist_ok=True)
                        with out_path.open("wb") as f:
                            f.write(part.inline_data.data)
                        return True, f"attempt {attempt}: {len(part.inline_data.data)} bytes"
            last_err = f"attempt {attempt}: no inline_data in response"
        except Exception as e:
            last_err = f"attempt {attempt}: {type(e).__name__}: {e}"
        time.sleep(1.5 * attempt)
    return False, last_err


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("prompts_dir", type=Path)
    parser.add_argument("output_dir", type=Path)
    parser.add_argument("--only", help="comma-separated base names to generate (e.g. slide_07a_cha-fmri)", default="")
    args = parser.parse_args()

    api_key = os.environ.get("GEMINI_API_KEY") or os.environ.get("GOOGLE_API_KEY")
    if not api_key:
        print("ERROR: GEMINI_API_KEY not set", file=sys.stderr)
        return 1
    os.environ["GEMINI_API_KEY"] = api_key

    client = genai.Client()

    prompt_files = sorted(args.prompts_dir.glob("slide_*.md"))
    if args.only:
        allowed = set(args.only.split(","))
        prompt_files = [p for p in prompt_files if p.stem in allowed]

    manifest = {
        "started": datetime.utcnow().isoformat() + "Z",
        "model": "gemini-3.1-flash-image-preview",
        "aspect_ratio": "16:9",
        "generated": [],
        "failed": [],
    }

    args.output_dir.mkdir(parents=True, exist_ok=True)

    for pp in prompt_files:
        out = args.output_dir / prompt_filename_to_output(pp)
        try:
            prompt_text = extract_prompt(pp.read_text(encoding="utf-8"))
        except Exception as e:
            print(f"[SKIP] {pp.name}: {e}", file=sys.stderr)
            manifest["failed"].append({"source": pp.name, "error": f"extract: {e}", "timestamp": datetime.utcnow().isoformat() + "Z"})
            continue

        print(f"[GEN] {pp.name} -> {out.name} ({len(prompt_text)} chars)", flush=True)
        t0 = time.time()
        ok, detail = generate_one(client, prompt_text, out)
        dt = time.time() - t0
        if ok:
            manifest["generated"].append({"source": pp.name, "output": out.name, "detail": detail, "seconds": round(dt, 1), "timestamp": datetime.utcnow().isoformat() + "Z"})
            print(f"  OK ({dt:.1f}s · {detail})")
        else:
            manifest["failed"].append({"source": pp.name, "error": detail, "seconds": round(dt, 1), "timestamp": datetime.utcnow().isoformat() + "Z"})
            print(f"  FAIL ({dt:.1f}s · {detail})", file=sys.stderr)

    manifest["completed"] = datetime.utcnow().isoformat() + "Z"
    mf = args.output_dir / "generation_manifest.json"
    mf.write_text(json.dumps(manifest, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"\nManifest: {mf}")
    print(f"Generated: {len(manifest['generated'])}/{len(prompt_files)}")
    return 0 if not manifest["failed"] else 2


if __name__ == "__main__":
    sys.exit(main())
