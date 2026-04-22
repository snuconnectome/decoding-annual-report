#!/usr/bin/env python3
"""
디코딩과제 3년차 발표 슬라이드 matplotlib 생성기 (Fallback).

Gemini API 의존 없이 `data/*.yaml`에서 14개 슬라이드 PNG를 직접 렌더링.
Apple SD Gothic Neo + snu_neurox 팔레트 + 1920x1080 = 16:9.

Usage:
    python generate-slides-matplotlib.py --data-dir data --output slides/images
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
from matplotlib.patches import FancyBboxPatch, Rectangle, FancyArrowPatch, Circle
from matplotlib import font_manager

try:
    import yaml
except ImportError:
    print("ERROR: pyyaml 필요.", file=sys.stderr); sys.exit(1)

# ---------------------------------------------------------------------------
# 공통 설정
# ---------------------------------------------------------------------------
PAGE_W_PX = 1920
PAGE_H_PX = 1080
DPI = 160  # 12×6.75 inches at 160 DPI = 1920×1080

# Font priority: Korean-first
FONT_KR = "Apple SD Gothic Neo"
FONT_EN = "Helvetica"
plt.rcParams["font.family"] = FONT_KR
plt.rcParams["font.sans-serif"] = [FONT_KR, "AppleGothic", "Nanum Gothic", "DejaVu Sans"]
plt.rcParams["axes.unicode_minus"] = False

# snu_neurox palette
SNU_BLUE = "#003380"
SIGNAL_ORANGE = "#E69F00"
NEURAL_TEAL = "#0072B2"
TEXT_DARK = "#282945"
SNU_ICE = "#EDF6FC"
TEXT_SEC = "#5A5A6E"
COGNITIVE_BLUE = "#56B4E9"
PALETTE_PINK = "#CC79A7"
LAB_TEAL = "#11604B"
LAB_VERMIL = "#D55E00"
LAB_PURPLE = "#584B9F"
BG_PEACH = "#FDECE2"
BG_LAVENDER = "#EFEAF7"
BG_MINT = "#E7F0ED"


# ---------------------------------------------------------------------------
# 유틸리티
# ---------------------------------------------------------------------------
def load_yamls(data_dir: Path) -> dict[str, Any]:
    data = {}
    for p in sorted(data_dir.glob("*.yaml")):
        data[p.stem] = yaml.safe_load(p.read_text(encoding="utf-8"))
    return data


def setup_figure() -> tuple[plt.Figure, plt.Axes]:
    fig, ax = plt.subplots(figsize=(PAGE_W_PX / DPI, PAGE_H_PX / DPI), dpi=DPI)
    ax.set_xlim(0, 1920)
    ax.set_ylim(0, 1080)
    ax.set_aspect("equal")
    ax.invert_yaxis()  # top-down coordinate (0 top, 1080 bottom)
    ax.axis("off")
    fig.patch.set_facecolor("white")
    return fig, ax


def draw_header_footer(ax: plt.Axes, page_num: int, total: int = 14) -> None:
    # Top-left: 디코딩과제 3년차
    ax.text(
        60, 45, "디코딩과제 3년차", fontsize=10, color=SNU_BLUE, weight="bold",
        va="top", ha="left",
    )
    # Bottom-right: page number
    ax.text(
        1860, 1035, f"{page_num} / {total}", fontsize=9, color=TEXT_SEC,
        va="bottom", ha="right",
    )


def rounded_card(
    ax, x, y, w, h, fill=SNU_ICE, edge=NEURAL_TEAL, lw=1.5, pad=0.03,
) -> FancyBboxPatch:
    patch = FancyBboxPatch(
        (x, y), w, h,
        boxstyle=f"round,pad={pad*100:.0f},rounding_size=20",
        linewidth=lw, edgecolor=edge, facecolor=fill,
    )
    ax.add_patch(patch)
    return patch


def save(fig, out_path: Path) -> None:
    out_path.parent.mkdir(parents=True, exist_ok=True)
    fig.savefig(out_path, dpi=DPI, bbox_inches="tight",
                pad_inches=0, facecolor="white")
    plt.close(fig)


def text(ax, x, y, s, **kw):
    kw.setdefault("color", TEXT_DARK)
    kw.setdefault("va", "center")
    kw.setdefault("ha", "center")
    ax.text(x, y, s, **kw)


# ---------------------------------------------------------------------------
# Slide renderers
# ---------------------------------------------------------------------------
def render_slide_01_title(d, out_dir: Path) -> Path:
    fig, ax = setup_figure()
    draw_header_footer(ax, 1)

    pm = d["project-meta"]
    title_ko = pm["project"]["title_ko"]
    title_en = pm["project"]["title_en"]
    pi = pm["principal_investigator"]
    budget_y3 = next(b["total"] for b in pm["budget"]["by_year"] if b["year"] == 3)

    # Main title
    ax.text(
        960, 220, "디코딩과제 3년차 연차보고서", fontsize=34, color=SNU_BLUE,
        weight="bold", ha="center", va="center",
    )
    # Korean subtitle (3 lines for breathing room)
    title_lines = [
        "동물-사람 멀티스케일 신경과학 파운데이션 모델 기반",
        "뇌-외부환경 상호작용 시 정서로 맥락화된",
        "(contextualized) 지각의 디코딩",
    ]
    for i, line in enumerate(title_lines):
        ax.text(960, 310 + i * 48, line, fontsize=18, color=SNU_BLUE, weight="bold", ha="center", va="center")

    # English title
    en_wrap_1 = "Affect-contextualized perception decoding with"
    en_wrap_2 = "cross-species multiscale neuroscience foundation model"
    ax.text(960, 480, en_wrap_1, fontsize=14, color=NEURAL_TEAL, style="italic", ha="center")
    ax.text(960, 510, en_wrap_2, fontsize=14, color=NEURAL_TEAL, style="italic", ha="center")

    # Meta card
    card_x, card_y, card_w, card_h = 260, 640, 1400, 320
    rounded_card(ax, card_x, card_y, card_w, card_h, fill=SNU_ICE, edge=NEURAL_TEAL)

    # Meta rows
    rows = [
        ("연구책임자", f"{pi['name']} ({pi['institution']}, {pi['position']})"),
        ("과제번호", pm["project"]["id"]),
        ("연구기간", f"{pm['period']['overall']['start']} — {pm['period']['overall']['end']} (54개월)"),
        ("해당 연차", f"3차년도 ({pm['period']['by_year'][2]['start'][:4]}) · 예산 {budget_y3:,} 천원"),
        ("주관", "과학기술정보통신부 · 한국연구재단"),
        ("제출일", pm["period"]["submission_date"]),
    ]
    for i, (label, value) in enumerate(rows):
        y = card_y + 45 + i * 43
        ax.text(card_x + 80, y, f"{label}:", fontsize=14, color=SNU_BLUE, weight="bold", ha="left", va="center")
        ax.text(card_x + 280, y, value, fontsize=14, color=TEXT_DARK, ha="left", va="center")

    out = out_dir / "slide_01_title.png"
    save(fig, out)
    return out


def render_slide_02_overview(d, out_dir: Path) -> Path:
    fig, ax = setup_figure()
    draw_header_footer(ax, 2)

    ax.text(960, 110, "본 연구의 핵심 개념", fontsize=32, color=SNU_BLUE, weight="bold", ha="center")
    ax.text(960, 165, "정서에 의해 맥락화된 지각의 디코딩", fontsize=18, color=NEURAL_TEAL, ha="center")

    # 3 cards horizontal
    cards = [
        ("외부환경", "시각 · 청각 · 복합 자극", "1"),
        ("뇌의 능동적 추론", "불완전 감각\n→ 예측 → 표상 갱신", "2"),
        ("정서에 의한 맥락화", "신체 반응 유도", "3"),
    ]
    card_w, card_h = 480, 360
    gap = 30
    total_w = card_w * 3 + gap * 2
    start_x = (1920 - total_w) / 2
    y = 330

    for i, (title, desc, num) in enumerate(cards):
        x = start_x + i * (card_w + gap)
        rounded_card(ax, x, y, card_w, card_h, fill=SNU_ICE, edge=NEURAL_TEAL)
        # Circle with number
        num_color = SIGNAL_ORANGE if i == 2 else NEURAL_TEAL
        circle = Circle((x + card_w/2, y + 95), 38, facecolor=num_color, edgecolor="none")
        ax.add_patch(circle)
        ax.text(x + card_w/2, y + 95, num, fontsize=26, color="white", weight="bold", ha="center", va="center")
        ax.text(x + card_w/2, y + 215, title, fontsize=20, weight="bold", color=SNU_BLUE, ha="center", va="center")
        ax.text(x + card_w/2, y + 290, desc, fontsize=13, color=TEXT_DARK, ha="center", va="center")

        # Arrow to next card (except last)
        if i < 2:
            arrow = FancyArrowPatch(
                (x + card_w + 2, y + card_h/2),
                (x + card_w + gap - 2, y + card_h/2),
                arrowstyle="->", mutation_scale=20, color=SNU_BLUE, lw=2,
            )
            ax.add_patch(arrow)

    # Bottom caption
    ax.text(
        960, 790, "기존 디코딩은 수동적 지각에 국한 → 본 연구는 능동적 추론과 정서 맥락을 반영",
        fontsize=16, color=TEXT_DARK, ha="center",
    )
    ax.text(
        960, 835, "정서 맥락은 지각 디코딩의 핵심 변인",
        fontsize=13, color=TEXT_SEC, style="italic", ha="center",
    )

    out = out_dir / "slide_02_overview.png"
    save(fig, out)
    return out


def render_slide_03_roadmap(d, out_dir: Path) -> Path:
    fig, ax = setup_figure()
    draw_header_footer(ax, 3)

    pm = d["project-meta"]
    years_data = [
        (1, 300000, "빅데이터 자동화 실험환경"),
        (2, 453500, "고정 환경 지각 DB"),
        (3, 453500, "변동 환경 DB + 멀티 모달리티 ML"),
        (4, 600000, "BrainLife 공개 · 종간 사전학습"),
        (5, 600000, "전이학습 검증 · 실험형 전시"),
    ]

    ax.text(960, 110, "5개년 연구개발 로드맵", fontsize=32, color=SNU_BLUE, weight="bold", ha="center")
    ax.text(960, 160, "2023.07 — 2027.12 (54개월)", fontsize=14, color=TEXT_SEC, ha="center")

    # Timeline axis
    axis_y = 400
    axis_left, axis_right = 180, 1740
    ax.plot([axis_left, axis_right], [axis_y, axis_y], color=SNU_BLUE, lw=2)

    # 5 markers with cards
    n = 5
    for i, (year, budget, topic) in enumerate(years_data):
        x = axis_left + (axis_right - axis_left) * i / (n - 1)
        is_current = year == 3
        color = SIGNAL_ORANGE if is_current else NEURAL_TEAL
        size = 30 if is_current else 20
        # diamond marker
        diamond = mpatches.RegularPolygon(
            (x, axis_y), numVertices=4, radius=size, orientation=0,
            facecolor=color, edgecolor="white", linewidth=2,
        )
        ax.add_patch(diamond)

        # "현재" pill for current year
        if is_current:
            pill = FancyBboxPatch(
                (x - 40, axis_y - 95), 80, 28,
                boxstyle="round,pad=5,rounding_size=14",
                facecolor=SIGNAL_ORANGE, edgecolor="none",
            )
            ax.add_patch(pill)
            ax.text(x, axis_y - 81, "현재", fontsize=11, color="white", weight="bold", ha="center", va="center")

        # Year label above
        ax.text(x, axis_y - 35, f"{year}차년도", fontsize=13, color=SNU_BLUE, weight="bold", ha="center", va="bottom")

        # Card below
        card_w, card_h = 230, 150
        card_x = x - card_w/2
        card_y = axis_y + 50
        outline = SIGNAL_ORANGE if is_current else NEURAL_TEAL
        rounded_card(ax, card_x, card_y, card_w, card_h, fill=SNU_ICE, edge=outline, lw=2 if is_current else 1)
        ax.text(card_x + card_w/2, card_y + 35, f"{budget:,}천원", fontsize=14, color=SNU_BLUE, weight="bold", ha="center")
        # wrap topic text
        words = topic.split()
        wrapped = ""
        line_len = 0
        lines = []
        current = ""
        for w in words:
            if len(current) + len(w) > 12:
                lines.append(current.strip())
                current = w + " "
            else:
                current += w + " "
        lines.append(current.strip())
        for li, ln in enumerate(lines):
            ax.text(card_x + card_w/2, card_y + 75 + li * 22, ln, fontsize=11, color=TEXT_DARK, ha="center", va="center")

    out = out_dir / "slide_03_roadmap.png"
    save(fig, out)
    return out


def render_slide_04_year3_goals(d, out_dir: Path) -> Path:
    fig, ax = setup_figure()
    draw_header_footer(ax, 4)

    ax.text(960, 110, "3차년도 평가 구조", fontsize=32, color=SNU_BLUE, weight="bold", ha="center")
    ax.text(960, 165, "4개 평가항목 · 각 25% · 합계 달성도 97.5%", fontsize=18, color=NEURAL_TEAL, ha="center")

    # 2x2 grid
    cards = [
        ("#1", "뇌-환경 상호작용 데이터베이스 구축", "세부목표 1-1, 1-2"),
        ("#2", "기계학습 모델 개발 및 검증", "세부목표 1-3, 1-4"),
        ("#4", "뇌영상-파운데이션 기계학습 모델", "세부목표 2-1, 2-2"),
        ("#5", "다중 모달리티 통합 모델", "세부목표 2-3"),
    ]
    card_w, card_h = 720, 250
    gap = 40
    start_x = (1920 - card_w * 2 - gap) / 2
    start_y = 260
    for i, (num, title, sub) in enumerate(cards):
        row, col = divmod(i, 2)
        x = start_x + col * (card_w + gap)
        y = start_y + row * (card_h + gap)
        rounded_card(ax, x, y, card_w, card_h, fill=SNU_ICE, edge=NEURAL_TEAL)
        # [25%] badge
        badge = Circle((x + 60, y + 60), 40, facecolor=SIGNAL_ORANGE, edgecolor="none")
        ax.add_patch(badge)
        ax.text(x + 60, y + 60, "25%", fontsize=14, color="white", weight="bold", ha="center", va="center")
        # #number label
        ax.text(x + 140, y + 60, f"평가항목 {num}", fontsize=14, color=SNU_BLUE, weight="bold", va="center")
        # Title
        ax.text(x + card_w/2, y + 135, title, fontsize=20, color=SNU_BLUE, weight="bold", ha="center")
        # Subtitle
        ax.text(x + card_w/2, y + 185, sub, fontsize=13, color=TEXT_SEC, ha="center")

    # Bottom annotation
    ax.text(
        260, 910,
        "※ 5개년 기준 6개 평가항목(#1·#2·#3·#4·#5·#6) 중 3차년도 active 4개(#1·#2·#4·#5)에 가중치 100% 재분배",
        fontsize=11, color=TEXT_SEC, ha="left",
    )
    ax.text(
        260, 945,
        "  #3 신경과학 메커니즘(10%)은 4차년도 개시 예정",
        fontsize=11, color=TEXT_SEC, ha="left",
    )

    out = out_dir / "slide_04_year3-goals.png"
    save(fig, out)
    return out


def render_slide_05_strategy(d, out_dir: Path) -> Path:
    fig, ax = setup_figure()
    draw_header_footer(ax, 5)

    ax.text(960, 110, "연구개발 추진전략", fontsize=32, color=SNU_BLUE, weight="bold", ha="center")

    stages = [
        ("01", "데이터 생성", "동물·사람\n신경과학 DB"),
        ("02", "전처리", "정제\n표준화"),
        ("03", "디코더", "맥락화 지각\n디코딩 모델"),
        ("04", "파운데이션", "모델 개발\n검증"),
        ("05", "확장·활용", "질환 예측\n예술 전시"),
    ]
    n = 5
    card_w, card_h = 300, 340
    gap = 45
    total_w = card_w * n + gap * (n - 1)
    start_x = (1920 - total_w) / 2
    y = 250
    for i, (num, title, desc) in enumerate(stages):
        x = start_x + i * (card_w + gap)
        is_last = i == n - 1
        edge = SIGNAL_ORANGE if is_last else NEURAL_TEAL
        rounded_card(ax, x, y, card_w, card_h, fill=SNU_ICE, edge=edge, lw=2 if is_last else 1)
        # Stage number large top-center
        ax.text(x + card_w/2, y + 80, num, fontsize=40, color=NEURAL_TEAL, weight="bold", ha="center", va="center")
        # Divider
        ax.plot([x + 60, x + card_w - 60], [y + 140, y + 140], color=NEURAL_TEAL, lw=1, alpha=0.3)
        ax.text(x + card_w/2, y + 195, title, fontsize=18, color=SNU_BLUE, weight="bold", ha="center", va="center")
        ax.text(x + card_w/2, y + 265, desc, fontsize=12, color=TEXT_DARK, ha="center", va="center")
        if i < n - 1:
            arrow = FancyArrowPatch(
                (x + card_w + 5, y + card_h/2),
                (x + card_w + gap - 5, y + card_h/2),
                arrowstyle="->", mutation_scale=18, color=SNU_BLUE, lw=2,
            )
            ax.add_patch(arrow)

    # Team legend
    teams = [
        (LAB_TEAL, "이상아 Lab", "(인간 기억·정서)"),
        (LAB_VERMIL, "최형진 Lab", "(동물 신경)"),
        (PALETTE_PINK, "차지욱 Lab", "(ML foundation)"),
        (LAB_PURPLE, "문태섭 Lab", "(Vision-Lang · SEED)"),
    ]
    legend_y = 760
    legend_start_x = 180
    legend_item_w = 410
    for i, (color, name, sub) in enumerate(teams):
        x = legend_start_x + i * legend_item_w
        swatch = Rectangle((x, legend_y - 14), 24, 24, facecolor=color, edgecolor="none")
        ax.add_patch(swatch)
        ax.text(x + 36, legend_y - 2, name, fontsize=13, color=SNU_BLUE, weight="bold", ha="left", va="center")
        ax.text(x + 36, legend_y + 22, sub, fontsize=10, color=TEXT_SEC, ha="left", va="center")

    out = out_dir / "slide_05_strategy.png"
    save(fig, out)
    return out


def render_slide_06_db_construction(d, out_dir: Path) -> Path:
    fig, ax = setup_figure()
    draw_header_footer(ax, 6)

    ax.text(80, 110, "데이터베이스 구축 — 평가항목 #1 (25%)", fontsize=28, color=SNU_BLUE, weight="bold", ha="left", va="center")
    ax.text(80, 155, "이상아 Lab 중심 · 인간 정서-맥락 지각", fontsize=16, color=LAB_TEAL, ha="left", va="center")

    # 100% circular badge (top-right)
    badge = Circle((1780, 130), 75, facecolor="white", edgecolor=SIGNAL_ORANGE, linewidth=5)
    ax.add_patch(badge)
    ax.text(1780, 130, "100%", fontsize=24, color=SIGNAL_ORANGE, weight="bold", ha="center", va="center")
    ax.text(1780, 50, "달성도", fontsize=11, color=TEXT_SEC, ha="center")

    # Animal track thin bar
    bar_y = 220
    bar = Rectangle((80, bar_y), 1760, 30, facecolor=SNU_ICE, edgecolor="none")
    ax.add_patch(bar)
    ax.text(
        960, bar_y + 15,
        "동물 파트 (최형진 Lab): 칼슘 이미징 기반 자연환경 지각·정서 DB 구축",
        fontsize=12, color=TEXT_SEC, ha="center", va="center",
    )

    # 2 panels
    panel_w, panel_h = 860, 620
    gap = 40
    start_x = (1920 - panel_w * 2 - gap) / 2
    y = 290
    panels = [
        (
            "실험 1 — fMRI / EEG 감정 연합",
            [
                "fMRI: 편도체 · 전두/두정엽 → 지각",
                "fMRI: DMN · PCC · precuneus → 기억 인출",
                "EEG: Posterior θ → 맥락 연합 성공 마커",
                "EEG: Frontal θ → 맥락 갱신 마커",
            ],
        ),
        (
            "실험 2 — 가상공간 탐험 EEG",
            [
                "수동적 가상공간 탐험 + EEG 재활성화 분석",
                "회전지점 sequential reactivation → 시간 순서 재활성화",
                "원거리 랜드마크 재활성화 ↔ 공간기억 성공 연관",
                "정서적 가치 → 맥락화 디코딩의 핵심 변인",
            ],
        ),
    ]
    for i, (title, bullets) in enumerate(panels):
        x = start_x + i * (panel_w + gap)
        rounded_card(ax, x, y, panel_w, panel_h, fill=SNU_ICE, edge=NEURAL_TEAL)
        # Badge
        exp_pill = FancyBboxPatch(
            (x + 30, y + 30), 110, 36,
            boxstyle="round,pad=3,rounding_size=18",
            facecolor=SIGNAL_ORANGE, edgecolor="none",
        )
        ax.add_patch(exp_pill)
        ax.text(x + 85, y + 48, f"실험 {i+1}", fontsize=14, color="white", weight="bold", ha="center", va="center")
        # Title
        ax.text(x + panel_w/2, y + 130, title, fontsize=20, color=SNU_BLUE, weight="bold", ha="center")
        # Bullets
        for bi, b in enumerate(bullets):
            ax.text(x + 40, y + 220 + bi * 80, f"• {b}", fontsize=14, color=TEXT_DARK, ha="left", va="top")

    ax.text(
        960, 945,
        "정서 맥락화 기반 지각 디코딩 모델 개발의 핵심 DB · 분석 프로토콜 구축 완료",
        fontsize=14, color=TEXT_DARK, ha="center",
    )

    out = out_dir / "slide_06_db-construction.png"
    save(fig, out)
    return out


def render_slide_07_ml_models(d, out_dir: Path) -> Path:
    fig, ax = setup_figure()
    draw_header_footer(ax, 7)

    ax.text(80, 110, "기계학습 모델 — 평가항목 #2 (25%)", fontsize=28, color=SNU_BLUE, weight="bold", ha="left", va="center")
    ax.text(80, 155, "차지욱 Lab 중심 · 4개 모델 벤치마크 대비 성능 향상", fontsize=16, color=NEURAL_TEAL, ha="left")

    badge = Circle((1780, 130), 75, facecolor="white", edgecolor=SIGNAL_ORANGE, linewidth=5)
    ax.add_patch(badge)
    ax.text(1780, 130, "100%", fontsize=24, color=SIGNAL_ORANGE, weight="bold", ha="center", va="center")
    ax.text(1780, 50, "달성도", fontsize=11, color=TEXT_SEC, ha="center")

    models = [
        ("SwiFT-IO", "R² = 0.96", "fMRI 파운데이션 모델 · 정서·언어·인지 예측"),
        ("POYO-SSL", "+12 ~ 13%", "칼슘이미징 Cell-Pattern-Aware SSL · 동적 시각 디코딩"),
        ("Language-Brain Alignment\n(언어-뇌영상 정렬)", "+14.4%", "언어-뇌영상 semantic 정렬 · 정서 예측"),
        ("MBBN", "Top-1", "Frequency-Specific Multi-Band Attention · 대규모 fMRI (SOTA)"),
    ]
    card_w, card_h = 800, 280
    gap = 40
    start_x = (1920 - card_w * 2 - gap) / 2
    start_y = 260
    for i, (name, metric, desc) in enumerate(models):
        row, col = divmod(i, 2)
        x = start_x + col * (card_w + gap)
        y = start_y + row * (card_h + gap)
        rounded_card(ax, x, y, card_w, card_h, fill=SNU_ICE, edge=NEURAL_TEAL)
        ax.text(x + card_w/2, y + 55, name, fontsize=18, color=SNU_BLUE, weight="bold", ha="center", va="center")
        ax.text(x + card_w/2, y + 145, metric, fontsize=42, color=SIGNAL_ORANGE, weight="bold", ha="center", va="center")
        ax.text(x + card_w/2, y + 235, desc, fontsize=12, color=TEXT_DARK, ha="center")

    ax.text(
        80, 910,
        "증빙: 국제 발표 1 · 리뷰 중 2 · 출판 예정 1 · 4개 세부 연구",
        fontsize=12, color=TEXT_SEC, ha="left",
    )

    out = out_dir / "slide_07_ml-models.png"
    save(fig, out)
    return out


def render_slide_08_multimodal_seed(d, out_dir: Path) -> Path:
    fig, ax = setup_figure()
    draw_header_footer(ax, 8)

    ax.text(80, 110, "다중 모달리티 · 시맨틱 평가 — 평가항목 #5 (25%)", fontsize=26, color=SNU_BLUE, weight="bold", ha="left")
    ax.text(80, 155, "문태섭 Lab 중심 · SEED 평가 체계 + Vision-Language Model", fontsize=15, color=LAB_PURPLE, ha="left")

    badge = Circle((1780, 130), 75, facecolor="white", edgecolor=SIGNAL_ORANGE, linewidth=5)
    ax.add_patch(badge)
    ax.text(1780, 130, "100%", fontsize=24, color=SIGNAL_ORANGE, weight="bold", ha="center", va="center")
    ax.text(1780, 50, "달성도", fontsize=11, color=TEXT_SEC, ha="center")

    # Upper SEED block
    ax.text(80, 230, "SEED — Semantic Evaluation for Visual Brain Decoding", fontsize=20, color=SNU_BLUE, weight="bold", ha="left")
    ax.text(80, 270, "22명 × 1K 이미지쌍 = 22K 인간 판단", fontsize=14, color=NEURAL_TEAL, ha="left")

    # 3 SEED metric cards
    seed_cards = [
        ("Object F1", "핵심 객체 존재 기반\nprecision/recall"),
        ("Caption Similarity", "이미지 캡션\nembedding 유사도"),
        ("SEED", "3개 지표 통합\naveraging"),
    ]
    card_w, card_h = 540, 180
    gap = 30
    start_x = (1920 - card_w * 3 - gap * 2) / 2
    y = 330
    for i, (name, desc) in enumerate(seed_cards):
        x = start_x + i * (card_w + gap)
        edge = SIGNAL_ORANGE if i == 2 else COGNITIVE_BLUE
        rounded_card(ax, x, y, card_w, card_h, fill=SNU_ICE, edge=edge, lw=2 if i == 2 else 1)
        color = SIGNAL_ORANGE if i == 2 else SNU_BLUE
        ax.text(x + card_w/2, y + 55, name, fontsize=22, color=color, weight="bold", ha="center", va="center")
        ax.text(x + card_w/2, y + 125, desc, fontsize=13, color=TEXT_DARK, ha="center", va="center")

    ax.text(
        80, 555,
        "평가 대상 SOTA: MindEye2 · NeuroPictor · UniBrain · MindBridge · BrainGuard",
        fontsize=12, color=TEXT_SEC, ha="left",
    )

    # Lower VLM + TabLeT (SNU Blue filled panels)
    vlm_panels = [
        ("Vision-Language Model", "(시각-언어 모델)", "대규모 sMRI · DTI · fMRI\nsemantic 정렬"),
        ("TabLeT", "", "효율적 토크나이징 + Transformer\n(장기 시계열 뇌영상)"),
    ]
    panel_w, panel_h = 780, 230
    panel_gap = 50
    start_x = (1920 - panel_w * 2 - panel_gap) / 2
    y = 620
    for i, (title, sub, body) in enumerate(vlm_panels):
        x = start_x + i * (panel_w + panel_gap)
        patch = FancyBboxPatch(
            (x, y), panel_w, panel_h,
            boxstyle="round,pad=3,rounding_size=18",
            facecolor=SNU_BLUE, edgecolor="none",
        )
        ax.add_patch(patch)
        if sub:
            ax.text(x + panel_w/2, y + 60, title, fontsize=20, color="white", weight="bold", ha="center", va="center")
            ax.text(x + panel_w/2, y + 95, sub, fontsize=13, color="white", ha="center", va="center")
        else:
            ax.text(x + panel_w/2, y + 75, title, fontsize=24, color="white", weight="bold", ha="center", va="center")
        ax.text(x + panel_w/2, y + 165, body, fontsize=13, color="white", ha="center", va="center")

    ax.text(
        80, 900,
        "기존 평가 지표(PixCorr, SSIM, CLIP, EffNet 등)의 인간 판단 불일치 문제 해결 → semantic 정합 평가 확립",
        fontsize=11, color=TEXT_SEC, ha="left",
    )

    out = out_dir / "slide_08_multimodal-seed.png"
    save(fig, out)
    return out


def render_slide_09_cross_species(d, out_dir: Path) -> Path:
    fig, ax = setup_figure()
    draw_header_footer(ax, 9)

    ax.text(80, 110, "뇌영상-파운데이션 모델 — 평가항목 #4 (25%)", fontsize=26, color=SNU_BLUE, weight="bold", ha="left")
    ax.text(80, 155, "동물-사람 종간 파운데이션 모델의 토대 확립", fontsize=16, color=NEURAL_TEAL, ha="left")

    badge = Circle((1780, 130), 75, facecolor="white", edgecolor=SIGNAL_ORANGE, linewidth=5)
    ax.add_patch(badge)
    ax.text(1780, 130, "100%", fontsize=24, color=SIGNAL_ORANGE, weight="bold", ha="center", va="center")
    ax.text(1780, 50, "달성도", fontsize=11, color=TEXT_SEC, ha="center")

    # Hero metric
    ax.text(1500, 225, "5개 세부 연구", fontsize=22, color=SIGNAL_ORANGE, weight="bold", ha="center")

    # 2 upper panels
    panels = [
        (
            LAB_VERMIL, "A", "동물 (Animal)",
            ["대규모 행동 · 신경신호 데이터", "사전학습 → 전이학습 디코딩", "NeuroMamba (CausalMamba 기반)"],
        ),
        (
            NEURAL_TEAL, "H", "사람 (Human)",
            ["대규모 다중 모달리티 (휴지기 / 과제 / 영화 / 자연자극)", "fMRI · sMRI · EEG 통합", "SwiFT · DIVER-1 · TabLeT"],
        ),
    ]
    panel_w, panel_h = 860, 440
    gap = 40
    start_x = (1920 - panel_w * 2 - gap) / 2
    y = 280
    for i, (lab_color, initial, title, bullets) in enumerate(panels):
        x = start_x + i * (panel_w + gap)
        rounded_card(ax, x, y, panel_w, panel_h, fill=SNU_ICE, edge=NEURAL_TEAL)
        # Left-side Lab color bar
        side_bar = Rectangle((x + 2, y + 2), 6, panel_h - 4, facecolor=lab_color, edgecolor="none")
        ax.add_patch(side_bar)
        # Initial badge (circle)
        badge = Circle((x + panel_w/2, y + 80), 35, facecolor=lab_color, edgecolor="none")
        ax.add_patch(badge)
        ax.text(x + panel_w/2, y + 80, initial, fontsize=30, color="white", weight="bold", ha="center", va="center")
        ax.text(x + panel_w/2, y + 155, title, fontsize=22, color=SNU_BLUE, weight="bold", ha="center")
        for bi, b in enumerate(bullets):
            ax.text(x + 50, y + 220 + bi * 60, f"• {b}", fontsize=13, color=TEXT_DARK, ha="left", va="top")

    # Lower unified panel (SNU Blue)
    uy = 750
    uh = 150
    patch = FancyBboxPatch(
        (80, uy), 1760, uh,
        boxstyle="round,pad=3,rounding_size=18",
        facecolor=SNU_BLUE, edgecolor="none",
    )
    ax.add_patch(patch)
    ax.text(960, uy + 50, "공통 표현 학습 기반", fontsize=20, color="white", weight="bold", ha="center", va="center")
    ax.text(960, uy + 100, "구조 · 기능 · 전기생리 신호 통합 → 종간 파운데이션 모델 핵심 토대 확보", fontsize=14, color="white", ha="center", va="center")

    ax.text(80, 950, "증빙: 국제 발표 2 · 투고·리뷰 중 2 · 기술개발 1", fontsize=11, color=TEXT_SEC, ha="left")

    out = out_dir / "slide_09_cross-species.png"
    save(fig, out)
    return out


def render_slide_10_extensions_quantum(d, out_dir: Path) -> Path:
    fig, ax = setup_figure()
    draw_header_footer(ax, 10)

    ax.text(960, 110, "확장적 활용 가능성", fontsize=32, color=SNU_BLUE, weight="bold", ha="center")
    ax.text(960, 160, "개발 모델의 다양한 응용 분야", fontsize=16, color=NEURAL_TEAL, ha="center")

    apps = [
        ("BCI", "BCI 디코더", "비침습적 뇌-컴퓨터\n운동·언어 신경보철"),
        ("Dx", "정신질환 진단", "우울증 · 조현병\n바이오마커 발굴"),
        ("Art", "실험형 전시", "뇌-AI 예술 실험\n전시 기획 응용"),
    ]
    card_w, card_h = 500, 360
    gap = 40
    start_x = (1920 - card_w * 3 - gap * 2) / 2
    y = 250
    for i, (label, title, desc) in enumerate(apps):
        x = start_x + i * (card_w + gap)
        rounded_card(ax, x, y, card_w, card_h, fill=SNU_ICE, edge=NEURAL_TEAL)
        # Label badge
        badge = Circle((x + card_w/2, y + 90), 55, facecolor=NEURAL_TEAL, edgecolor="none")
        ax.add_patch(badge)
        ax.text(x + card_w/2, y + 90, label, fontsize=26, color="white", weight="bold", ha="center", va="center")
        ax.text(x + card_w/2, y + 200, title, fontsize=22, color=SNU_BLUE, weight="bold", ha="center", va="center")
        ax.text(x + card_w/2, y + 280, desc, fontsize=13, color=TEXT_DARK, ha="center", va="center")

    # Quantum ML band
    band_y = 680
    band_h = 200
    band = Rectangle((80, band_y), 1760, band_h, facecolor=COGNITIVE_BLUE, edgecolor="none", alpha=0.25)
    ax.add_patch(band)
    ax.text(110, band_y + 40, "신기술 확장 — Quantum Machine Learning", fontsize=20, color=SNU_BLUE, weight="bold", ha="left", va="center")

    q_items = [
        ("Quantum Mario", "Scalable Quantum RL"),
        ("Quantum Time-series", "fMRI Transformer"),
        ("Hybrid Quantum RL", "Explainable Quantum"),
    ]
    chip_y = band_y + 105
    chip_start = 140
    chip_w = 530
    chip_gap = 30
    for i, (name, sub) in enumerate(q_items):
        chip_x = chip_start + i * (chip_w + chip_gap)
        chip = FancyBboxPatch(
            (chip_x, chip_y), chip_w, 70,
            boxstyle="round,pad=3,rounding_size=14",
            facecolor="white", edgecolor=COGNITIVE_BLUE, linewidth=1.5,
        )
        ax.add_patch(chip)
        ax.text(chip_x + chip_w/2, chip_y + 22, name, fontsize=14, color=SNU_BLUE, weight="bold", ha="center", va="center")
        ax.text(chip_x + chip_w/2, chip_y + 50, sub, fontsize=11, color=TEXT_SEC, ha="center", va="center")

    out = out_dir / "slide_10_extensions-quantum.png"
    save(fig, out)
    return out


def render_slide_11_quantitative(d, out_dir: Path) -> Path:
    fig, ax = setup_figure()
    draw_header_footer(ax, 11)

    ax.text(960, 110, "3차년도 정량 성과", fontsize=32, color=SNU_BLUE, weight="bold", ha="center")
    ax.text(960, 160, "2025-01-01 ~ 2025-12-31 실적", fontsize=14, color=TEXT_SEC, ha="center")

    total_w = 1700
    start_x = (1920 - total_w) / 2
    item_w = total_w / 3
    # Vertical stack: number at y_num, label at y_label, caption at y_cap
    y_num = 430
    y_label = 620
    y_cap = 680

    items = [
        ("97.5%", "", "합계 달성도", "4개 평가항목 × 가중치 100%", 80),
        ("17", "편", "논문", "국제 저널 중심", 100),
        ("4", "건", "학회참석", "국제 학술대회", 100),
    ]
    for i, (num, unit, label, cap, size) in enumerate(items):
        cx = start_x + item_w * (i + 0.5)
        if unit:
            # Number + unit side by side
            ax.text(cx - 35, y_num, num, fontsize=size, color=SIGNAL_ORANGE, weight="black", ha="center", va="center")
            ax.text(cx + 55, y_num + 18, unit, fontsize=32, color=SNU_BLUE, weight="bold", ha="center", va="center")
        else:
            ax.text(cx, y_num, num, fontsize=size, color=SIGNAL_ORANGE, weight="black", ha="center", va="center")
        ax.text(cx, y_label, label, fontsize=22, color=SNU_BLUE, weight="bold", ha="center", va="center")
        ax.text(cx, y_cap, cap, fontsize=12, color=TEXT_SEC, ha="center", va="center")

    # Vertical separators
    for i in [1, 2]:
        sx = start_x + item_w * i
        ax.plot([sx, sx], [y_num - 90, y_cap + 20], color="#D0D0D0", lw=1)

    ax.text(
        80, 900,
        "3차년도 active 평가항목 4개(#1·#2·#4·#5) 전수 달성도 100% · 평가항목 #3(10% 가중치)은 4차년도 개시 예정",
        fontsize=11, color=TEXT_SEC, ha="left",
    )

    out = out_dir / "slide_11_quantitative-results.png"
    save(fig, out)
    return out


def render_slide_12_year4_plan(d, out_dir: Path) -> Path:
    fig, ax = setup_figure()
    draw_header_footer(ax, 12)

    ax.text(960, 110, "4차년도(2026) 연구개발계획", fontsize=32, color=SNU_BLUE, weight="bold", ha="center")
    ax.text(960, 160, "예산 600,000천원 (약 6억원) · 5개 핵심 방향", fontsize=16, color=NEURAL_TEAL, ha="center")

    dirs = [
        ("01", "DB 공개", "자연환경 지각·정서\nBrainLife 오픈"),
        ("02", "ML 모델", "동일종 다중 모달리티\n디코더 검증"),
        ("03", "메커니즘 규명", "two-site 광유전학\n칼슘이미징"),
        ("04", "전이학습", "대규모 사전학습\n+ 전이 성능 검증"),
        ("05", "종간 통합", "동물-사람 파운데이션\n사전학습 진행"),
    ]
    n = 5
    card_w, card_h = 330, 330
    gap = 20
    total_w = card_w * n + gap * (n - 1)
    start_x = (1920 - total_w) / 2
    y = 240
    for i, (num, title, desc) in enumerate(dirs):
        x = start_x + i * (card_w + gap)
        rounded_card(ax, x, y, card_w, card_h, fill=SNU_ICE, edge=NEURAL_TEAL)
        # Large number on top
        ax.text(x + card_w/2, y + 95, num, fontsize=60, color=NEURAL_TEAL, weight="bold", ha="center", va="center")
        # Divider line
        ax.plot([x + 50, x + card_w - 50], [y + 160, y + 160], color=NEURAL_TEAL, lw=1, alpha=0.3)
        ax.text(x + card_w/2, y + 210, title, fontsize=18, color=SNU_BLUE, weight="bold", ha="center", va="center")
        ax.text(x + card_w/2, y + 275, desc, fontsize=11, color=TEXT_DARK, ha="center", va="center")

    # Total above bar
    bar_total_w = 1700
    bar_x = (1920 - bar_total_w) / 2
    ax.text(bar_x + bar_total_w, 625, "합계 600,000천원", fontsize=18, color=SIGNAL_ORANGE, weight="bold", ha="right", va="center")

    # Budget bar
    by = 670
    bh = 60
    direct_ratio = 468750 / 600000
    direct_w = bar_total_w * direct_ratio
    indirect_w = bar_total_w - direct_w
    # Direct (SNU Blue)
    direct_rect = FancyBboxPatch(
        (bar_x, by), direct_w, bh,
        boxstyle="round,pad=0,rounding_size=8",
        facecolor=SNU_BLUE, edgecolor="none",
    )
    ax.add_patch(direct_rect)
    ax.text(bar_x + direct_w/2, by + bh/2, "직접비 468,750천원", fontsize=16, color="white", weight="bold", ha="center", va="center")
    # Indirect (Neural Teal)
    indirect_rect = FancyBboxPatch(
        (bar_x + direct_w, by), indirect_w, bh,
        boxstyle="round,pad=0,rounding_size=8",
        facecolor=NEURAL_TEAL, edgecolor="none",
    )
    ax.add_patch(indirect_rect)
    ax.text(bar_x + direct_w + indirect_w/2, by + bh/2, "간접비 131,250천원", fontsize=14, color="white", weight="bold", ha="center", va="center")

    ax.text(
        960, 780,
        "주요 항목: 인건비 64,896 · 학생인건비 189,520 · 연구활동비 95,081 · 연구수당 51,352 · 장비비 32,000 · 재료비 35,901 (단위: 천원)",
        fontsize=10, color=TEXT_SEC, ha="center",
    )

    out = out_dir / "slide_12_year4-plan.png"
    save(fig, out)
    return out


def render_slide_13_expected_impact(d, out_dir: Path) -> Path:
    fig, ax = setup_figure()
    draw_header_footer(ax, 13)

    ax.text(960, 110, "연구개발 성과의 기대효과", fontsize=32, color=SNU_BLUE, weight="bold", ha="center")
    ax.text(960, 160, "4개 축의 사회적·학문적 파급", fontsize=16, color=NEURAL_TEAL, ha="center")

    quadrants = [
        (SNU_ICE, SNU_BLUE, "학문", "학문적 효과", [
            "BrainLife 공유 · UKB · ABCD급 데이터",
            "정서 디코딩 후속연구",
            "아동 · 성인 뇌노화 궤적 연구 적용",
        ]),
        (BG_PEACH, LAB_VERMIL, "의과학", "의과학 기술 효과", [
            "정신질환 바이오마커 발굴 (재현·일반화)",
            "비침습적 BCI 디코더 원천기술",
            "개인 맞춤형 정신질환 치료",
        ]),
        (BG_MINT, LAB_TEAL, "교육", "교육적 효과", [
            "신경과학·초거대 AI 융합 박사급 인력",
            "윤리·가치 정렬형 인간형 AI",
            "국제 공동연구 · 연구자 교류",
        ]),
        (BG_LAVENDER, LAB_PURPLE, "산업", "사회·산업적 효과", [
            "마케팅 · 엔터테인먼트 선호 예측",
            "소아청소년 정신건강 조기개입",
            "공공 안전 AI 응용 가능성",
        ]),
    ]
    # 2x2
    card_w, card_h = 830, 350
    gap = 40
    start_x = (1920 - card_w * 2 - gap) / 2
    start_y = 230
    for i, (bg, badge_color, tag, title, bullets) in enumerate(quadrants):
        row, col = divmod(i, 2)
        x = start_x + col * (card_w + gap)
        y = start_y + row * (card_h + gap)
        rect = FancyBboxPatch(
            (x, y), card_w, card_h,
            boxstyle="round,pad=3,rounding_size=18",
            facecolor=bg, edgecolor="none",
        )
        ax.add_patch(rect)
        # Tag pill
        tag_pill = FancyBboxPatch(
            (x + 30, y + 35), 90, 40,
            boxstyle="round,pad=3,rounding_size=18",
            facecolor=badge_color, edgecolor="none",
        )
        ax.add_patch(tag_pill)
        ax.text(x + 75, y + 55, tag, fontsize=14, color="white", weight="bold", ha="center", va="center")
        ax.text(x + 150, y + 55, title, fontsize=22, color=SNU_BLUE, weight="bold", ha="left", va="center")
        for bi, b in enumerate(bullets):
            ax.text(x + 50, y + 135 + bi * 55, f"• {b}", fontsize=14, color=TEXT_DARK, ha="left", va="top")

    out = out_dir / "slide_13_expected-impact.png"
    save(fig, out)
    return out


def render_slide_14_wrap_up(d, out_dir: Path) -> Path:
    fig, ax = setup_figure()
    draw_header_footer(ax, 14)

    ax.text(960, 130, "Summary", fontsize=48, color=SNU_BLUE, weight="bold", ha="center")
    ax.text(960, 190, "3차년도 핵심 성과 요약", fontsize=16, color=NEURAL_TEAL, ha="center")

    takeaways = [
        ("97.5%", "합계 달성도", "4개 평가항목 100% 달성"),
        ("5개", "멀티스케일 파운데이션", "SwiFT · DIVER-1 ·\nNeuroMamba · TabLeT 등"),
        ("6억원", "4차년도 예산", "종간 사전학습 진행\n(600,000천원)"),
    ]
    card_w, card_h = 500, 330
    gap = 40
    start_x = (1920 - card_w * 3 - gap * 2) / 2
    y = 260
    for i, (big, label, desc) in enumerate(takeaways):
        x = start_x + i * (card_w + gap)
        rounded_card(ax, x, y, card_w, card_h, fill=SNU_ICE, edge=NEURAL_TEAL)
        ax.text(x + card_w/2, y + 105, big, fontsize=54, color=SIGNAL_ORANGE, weight="black", ha="center", va="center")
        ax.text(x + card_w/2, y + 195, label, fontsize=20, color=SNU_BLUE, weight="bold", ha="center", va="center")
        ax.text(x + card_w/2, y + 265, desc, fontsize=12, color=TEXT_DARK, ha="center", va="center")

    # Closing (generous vertical space)
    ax.text(960, 680, "감사합니다", fontsize=44, color=SNU_BLUE, weight="bold", ha="center", va="center")
    ax.text(960, 800, "질의응답 (Q&A)", fontsize=26, color=SIGNAL_ORANGE, weight="bold", ha="center", va="center")
    ax.text(960, 900, "서울대학교 · snu.ac.kr", fontsize=12, color=TEXT_SEC, ha="center", va="center")

    out = out_dir / "slide_14_wrap-up.png"
    save(fig, out)
    return out


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
RENDERERS = [
    render_slide_01_title,
    render_slide_02_overview,
    render_slide_03_roadmap,
    render_slide_04_year3_goals,
    render_slide_05_strategy,
    render_slide_06_db_construction,
    render_slide_07_ml_models,
    render_slide_08_multimodal_seed,
    render_slide_09_cross_species,
    render_slide_10_extensions_quantum,
    render_slide_11_quantitative,
    render_slide_12_year4_plan,
    render_slide_13_expected_impact,
    render_slide_14_wrap_up,
]


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--data-dir", type=Path, default=Path("data"))
    ap.add_argument("--output", type=Path, default=Path("slides/images"))
    args = ap.parse_args()

    if not args.data_dir.exists():
        print(f"ERROR: data dir not found: {args.data_dir}", file=sys.stderr)
        return 1
    args.output.mkdir(parents=True, exist_ok=True)

    print(f"Loading YAMLs from {args.data_dir}...")
    data = load_yamls(args.data_dir)
    print(f"  Loaded: {', '.join(data.keys())}")

    print(f"\nRendering {len(RENDERERS)} slides to {args.output}...")
    for i, renderer in enumerate(RENDERERS, 1):
        try:
            out_path = renderer(data, args.output)
            size_kb = out_path.stat().st_size / 1024
            print(f"  [{i:2d}/14] {out_path.name} ({size_kb:.0f} KB)")
        except Exception as exc:
            print(f"  [{i:2d}/14] FAIL: {renderer.__name__}: {exc}", file=sys.stderr)
            return 1

    print(f"\nDone. {len(RENDERERS)} PNG files generated.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
