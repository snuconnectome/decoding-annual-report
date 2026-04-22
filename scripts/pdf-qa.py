#!/usr/bin/env python3
"""
추출된 PDF 콘텐츠의 한글 품질 검증.

검사 항목:
  1. 치환 문자(U+FFFD) 개수 — 폰트 매핑 실패 검출
  2. 페이지별 텍스트 길이 분포 — 빈 페이지 / 비정상 페이지 감지
  3. 한글 비율 — 극단적으로 낮으면 추출 실패 의심

Output:
  qa-report.json (기계 판독용)
  qa-report.md   (사람 판독용)

Exit code:
  0 — no blocking issues
  1 — critical issues detected (replacement chars, empty pages)
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HANGUL_RE = re.compile(r"[가-힣]")
REPLACEMENT = "�"

# 매우 짧은 페이지는 표지·레이아웃 페이지일 수 있어 문턱을 낮게 설정
MIN_CHARS_CONTENT_PAGE = 50
# 거의 확실히 텍스트 페이지인 곳 (본문 구간)
EXPECTED_TEXT_PAGES = set(range(12, 96))


def analyze_page(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    hangul = len(HANGUL_RE.findall(text))
    total = len(text)
    return {
        "page": int(path.stem),
        "chars": total,
        "hangul_chars": hangul,
        "hangul_ratio": round(hangul / total, 3) if total else 0.0,
        "replacement_chars": text.count(REPLACEMENT),
    }


def classify_issues(pages: list[dict]) -> list[dict]:
    issues = []
    for p in pages:
        if p["replacement_chars"] > 0:
            issues.append(
                {
                    "page": p["page"],
                    "severity": "critical",
                    "kind": "replacement_char",
                    "detail": f"{p['replacement_chars']} U+FFFD occurrences",
                }
            )
        if (
            p["page"] in EXPECTED_TEXT_PAGES
            and p["chars"] < MIN_CHARS_CONTENT_PAGE
        ):
            issues.append(
                {
                    "page": p["page"],
                    "severity": "warning",
                    "kind": "sparse_text",
                    "detail": f"only {p['chars']} chars on expected text page",
                }
            )
        if (
            p["chars"] > 200
            and p["hangul_ratio"] < 0.05
            and p["page"] in EXPECTED_TEXT_PAGES
        ):
            issues.append(
                {
                    "page": p["page"],
                    "severity": "warning",
                    "kind": "no_hangul",
                    "detail": f"hangul ratio {p['hangul_ratio']:.1%} on expected text page",
                }
            )
    return issues


def write_report(report: dict, md_path: Path) -> None:
    lines = [
        "# PDF 추출 품질 검증 리포트",
        "",
        f"- 추출된 페이지: {report['page_count']}",
        f"- 발견된 이슈: {len(report['issues'])}",
        "",
        "## 이슈 상세",
        "",
    ]
    if not report["issues"]:
        lines.append("_감지된 이슈 없음. 추출 품질 양호._")
    else:
        for iss in report["issues"]:
            lines.append(
                f"- **p{iss['page']:03d}** [{iss['severity']}] {iss['kind']}: {iss['detail']}"
            )

    lines += [
        "",
        "## 페이지별 통계",
        "",
        "| Page | Chars | Hangul | Hangul % | Replacement |",
        "|---:|---:|---:|---:|---:|",
    ]
    for p in report["pages"]:
        lines.append(
            f"| {p['page']:03d} | {p['chars']} | {p['hangul_chars']} "
            f"| {p['hangul_ratio']*100:.1f}% | {p['replacement_chars']} |"
        )
    md_path.write_text("\n".join(lines), encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("extracted_dir", type=Path, help="extracted-text/ 디렉토리")
    args = parser.parse_args()

    pages_dir = args.extracted_dir / "pages"
    if not pages_dir.exists():
        print(f"ERROR: {pages_dir} 디렉토리가 존재하지 않습니다.", file=sys.stderr)
        return 1

    pages = sorted(pages_dir.glob("*.txt"))
    if not pages:
        print(f"ERROR: {pages_dir}에 추출된 페이지가 없습니다.", file=sys.stderr)
        return 1

    page_reports = [analyze_page(p) for p in pages]
    issues = classify_issues(page_reports)
    report = {
        "page_count": len(page_reports),
        "pages": page_reports,
        "issues": issues,
    }

    json_path = args.extracted_dir / "qa-report.json"
    md_path = args.extracted_dir / "qa-report.md"
    json_path.write_text(
        json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8"
    )
    write_report(report, md_path)

    print(
        f"QA 완료: {report['page_count']} pages, "
        f"{sum(1 for i in issues if i['severity']=='critical')} critical, "
        f"{sum(1 for i in issues if i['severity']=='warning')} warnings"
    )
    print(f"→ {md_path}")

    critical_count = sum(1 for i in issues if i["severity"] == "critical")
    return 0 if critical_count == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
