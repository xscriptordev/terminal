"""Verify themes match colors.md palettes."""

from __future__ import annotations

import json
import re
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
COLORS_MD = ROOT / "colors.md"
THEMES_DIR = ROOT / "themes"


def parse_colors_md(content: str) -> dict[str, dict[str, str]]:
    palettes: dict[str, dict[str, str]] = {}
    pattern = re.compile(r"<h2[^>]*>(.*?)</h2>\s*```json\s*(\{.*?\})\s*```", re.S)
    for title, json_blob in pattern.findall(content):
        name = re.sub(r"\s+", " ", title).strip()
        colors = json.loads(json_blob)
        palettes[name] = {str(k): str(v) for k, v in colors.items()}
    return palettes


def expected_palette(colors: dict[str, str]) -> dict[str, str]:
    return {
        "bg": colors["color0"],
        "fg": colors["color7"],
        "muted": colors["color8"],
        "menu": colors["color0"],
        "selection": colors["color8"],
        "gutter": colors["color0"],
        "status": colors["color0"],
        "accent": colors["color5"],
        "color1": colors["color1"],
        "color2": colors["color2"],
        "color3": colors["color3"],
        "color4": colors["color4"],
        "color5": colors["color5"],
        "color6": colors["color6"],
    }


def parse_theme_palette(path: Path) -> dict[str, str]:
    lines = path.read_text().splitlines()
    in_palette = False
    palette: dict[str, str] = {}
    for line in lines:
        stripped = line.strip()
        if stripped == "[palette]":
            in_palette = True
            continue
        if in_palette:
            if stripped.startswith("[") and not stripped.startswith("[palette"):
                break
            if "=" in stripped:
                key, _, val = stripped.partition("=")
                key = key.strip().strip('"')
                val = val.strip().strip('"')
                palette[key] = val
    return palette


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", name.lower())


def get_theme_files() -> list[Path]:
    return sorted(THEMES_DIR.glob("*.toml"))


@pytest.mark.parametrize("theme_path", get_theme_files(), ids=lambda p: p.stem)
def test_theme_matches_colors_md(theme_path: Path) -> None:
    content = COLORS_MD.read_text(encoding="utf-8")
    palettes = parse_colors_md(content)

    theme_name = theme_path.stem.capitalize()
    # Handle special names
    for name in palettes:
        if slugify(name) == theme_path.stem:
            theme_name = name
            break

    assert theme_name in palettes, (
        f"No palette found in colors.md for theme '{theme_name}' "
        f"(file: {theme_path.name})"
    )

    expected = expected_palette(palettes[theme_name])
    actual = parse_theme_palette(theme_path)

    for key, expected_value in expected.items():
        assert key in actual, (
            f"Missing key '{key}' in {theme_path.name} palette"
        )
        assert actual[key].lower() == expected_value.lower(), (
            f"{theme_path.name}: palette '{key}' "
            f"expected {expected_value}, got {actual[key]}"
        )
