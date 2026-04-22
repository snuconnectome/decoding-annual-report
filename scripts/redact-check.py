#!/usr/bin/env python3
"""
Redaction 안전 스캐너 (Phase 8 공개 전 필수 검증).

report/**/*.md, data/**/*.yaml 등 공개 대상 파일에서
개인정보·민감정보 패턴을 탐지하여 매칭이 발견되면 빌드를 실패시킨다.

docs/redaction-policy.md의 정책에 기반.

Usage:
    python redact-check.py <path>
    python redact-check.py report/
    python redact-check.py data/project-meta.yaml

Exit code:
  0 — 매칭 없음 (안전)
  1 — 매칭 발견 (공개 불가)
  2 — 입력 오류
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

# ---------------------------------------------------------------------------
# 탐지 패턴
# ---------------------------------------------------------------------------
PATTERNS: dict[str, re.Pattern[str]] = {
    "kr_mobile": re.compile(r"01[0-9][-\s]?\d{3,4}[-\s]?\d{4}"),
    "kr_landline": re.compile(r"\b0\d{1,2}[-\s]?\d{3,4}[-\s]?\d{4}\b"),
    "kr_resident": re.compile(r"\b\d{6}[-\s]?[1-4]\d{6}\b"),
    "long_digit_run": re.compile(r"(?<!\d)\d{8,13}(?!\d)"),
    "signature_image": re.compile(r"(?:sign|signature|서명)\.(?:png|jpg|jpeg|gif)", re.I),
    "personal_email_hint": re.compile(
        r"[a-zA-Z0-9._%+-]+@(?!snu\.ac\.kr|gmail\.com)[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"
    ),
}

# ---------------------------------------------------------------------------
# 화이트리스트 (공개 가능한 패턴을 포함하는 컨텍스트)
# ---------------------------------------------------------------------------
WHITELIST_CONTEXTS: list[re.Pattern[str]] = [
    # 과제번호 RS-YYYY-NNNNNNNN 내부의 8자리 숫자
    re.compile(r"RS-\d{4}-\d{8}"),
    # 연도 범위 표기 (2023-2027 등, 하이픈·틸드·en-dash·em-dash 허용)
    re.compile(r"20\d{2}\s*[-~–—]\s*20\d{2}"),
    # ISBN/DOI 등 공개 식별자는 추후 필요시 추가
]

# 스캔 대상 확장자
DEFAULT_EXTENSIONS = {".md", ".yaml", ".yml", ".txt", ".json"}


def iter_files(path: Path) -> list[Path]:
    if path.is_file():
        return [path]
    files: list[Path] = []
    for ext in DEFAULT_EXTENSIONS:
        files.extend(path.rglob(f"*{ext}"))
    return sorted(files)


def scan_content(content: str, path: Path) -> list[dict]:
    findings: list[dict] = []
    for label, pattern in PATTERNS.items():
        for match in pattern.finditer(content):
            matched_text = match.group()
            ctx_start = max(0, match.start() - 15)
            ctx_end = min(len(content), match.end() + 15)
            context = content[ctx_start:ctx_end]
            if any(wl.search(context) for wl in WHITELIST_CONTEXTS):
                continue
            line_no = content[: match.start()].count("\n") + 1
            findings.append(
                {
                    "file": str(path),
                    "line": line_no,
                    "kind": label,
                    "match": matched_text,
                    "context": context.replace("\n", " "),
                }
            )
    return findings


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("path", type=Path, help="디렉토리 또는 파일")
    args = parser.parse_args()

    if not args.path.exists():
        print(f"ERROR: {args.path} 경로 없음", file=sys.stderr)
        return 2

    files = iter_files(args.path)
    if not files:
        print(f"스캔 대상 파일 없음 (경로: {args.path}). 통과.")
        return 0

    all_findings: list[dict] = []
    for f in files:
        try:
            content = f.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError) as exc:
            print(f"WARN: {f} 읽기 실패: {exc}", file=sys.stderr)
            continue
        all_findings.extend(scan_content(content, f))

    if not all_findings:
        print(f"OK: {len(files)} 개 파일에서 redaction 패턴 매칭 없음.")
        return 0

    print(f"FAIL: {len(all_findings)} 건의 잠재적 개인정보 노출 발견:")
    for f in all_findings:
        print(f"  {f['file']}:{f['line']} [{f['kind']}] «{f['match']}» | {f['context']}")
    print()
    print("처리 방법:")
    print("  1. 해당 위치의 개인정보를 마스킹하거나 삭제하십시오.")
    print("  2. 공개 가능한 경우 docs/redaction-policy.md의 WHITELIST에 추가하십시오.")
    return 1


if __name__ == "__main__":
    sys.exit(main())
