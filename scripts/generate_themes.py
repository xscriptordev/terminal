#!/usr/bin/env python3
"""Generate Helix themes from colors.md palettes."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

THEME_TEMPLATE = """\
"ui.background" = "bg"
"ui.text" = "fg"
"ui.cursor" = {{ fg = "bg", bg = "accent" }}
"ui.cursor.primary" = {{ fg = "bg", bg = "accent" }}
"ui.selection" = "selection"
"ui.menu" = {{ fg = "fg", bg = "menu" }}
"ui.menu.selected" = {{ fg = "bg", bg = "accent", modifiers = ["bold"] }}
"ui.linenr" = {{ fg = "muted", bg = "gutter" }}
"ui.linenr.selected" = {{ fg = "fg", bg = "gutter", modifiers = ["bold"] }}
"ui.statusline" = {{ fg = "fg", bg = "status" }}
"ui.statusline.inactive" = {{ fg = "muted", bg = "status" }}
"ui.statusline.separator" = "muted"
"ui.window" = {{ fg = "muted" }}
"ui.popup" = {{ fg = "fg", bg = "menu" }}
"ui.bufferline.active" = {{ fg = "bg", bg = "accent" }}
"ui.bufferline.inactive" = {{ fg = "muted", bg = "gutter" }}
"ui.bufferline.background" = {{ bg = "gutter" }}
"ui.virtual.ruler" = {{ bg = "gutter" }}

"diagnostic.error" = {{ fg = "color1" }}
"diagnostic.warning" = {{ fg = "color2" }}
"diagnostic.info" = {{ fg = "color5" }}
"diagnostic.hint" = {{ fg = "color6" }}
"diagnostic.error.gutter" = {{ fg = "color1" }}
"diagnostic.warning.gutter" = {{ fg = "color2" }}
"diagnostic.info.gutter" = {{ fg = "color5" }}
"diagnostic.hint.gutter" = {{ fg = "color6" }}

"diff.plus" = {{ fg = "color4" }}
"diff.plus.gutter" = {{ fg = "color4" }}
"diff.minus" = {{ fg = "color1" }}
"diff.minus.gutter" = {{ fg = "color1" }}
"diff.delta" = {{ fg = "color2" }}
"diff.delta.gutter" = {{ fg = "color2" }}

keyword = {{ fg = "color6", modifiers = ["bold"] }}
operator = {{ fg = "color6" }}
type = {{ fg = "color6" }}
function = {{ fg = "color5" }}
method = {{ fg = "color5" }}
constructor = {{ fg = "color5" }}
variable = {{ fg = "fg" }}
constant = {{ fg = "color2" }}
builtin = {{ fg = "color6" }}
attribute = {{ fg = "color4" }}
tag = {{ fg = "color1" }}
string = {{ fg = "color3" }}
character = {{ fg = "color3" }}
number = {{ fg = "color2" }}
boolean = {{ fg = "color2" }}
escape = {{ fg = "color3" }}
comment = {{ fg = "muted", modifiers = ["italic"] }}
namespace = {{ fg = "color6" }}
punctuation = {{ fg = "muted" }}
"punctuation.delimiter" = {{ fg = "muted" }}
"punctuation.bracket" = {{ fg = "muted" }}

rainbow = ["color1", "color2", "color3", "color4", "color5", "color6"]

[palette]
{palette}
"""

PALETTE_KEYS = [
    "bg",
    "fg",
    "muted",
    "menu",
    "selection",
    "gutter",
    "status",
    "accent",
    "color1",
    "color2",
    "color3",
    "color4",
    "color5",
    "color6",
]


def parse_colors_markdown(content: str) -> dict[str, dict[str, str]]:
    palettes: dict[str, dict[str, str]] = {}
    pattern = re.compile(r"<h2[^>]*>(.*?)</h2>\s*```json\s*(\{.*?\})\s*```", re.S)
    for title, json_blob in pattern.findall(content):
        name = re.sub(r"\s+", " ", title).strip()
        colors = json.loads(json_blob)
        palettes[name] = {key: str(value) for key, value in colors.items()}
    return palettes


def build_palette(colors: dict[str, str]) -> dict[str, str]:
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


def format_palette(palette: dict[str, str]) -> str:
    return "\n".join(f'{key} = "{palette[key]}"' for key in PALETTE_KEYS)


def slugify(name: str) -> str:
    return re.sub(r"[^a-z0-9]+", "", name.lower())


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Helix themes from colors.md.")
    parser.add_argument(
        "--colors",
        default="colors.md",
        help="Path to colors.md (default: colors.md).",
    )
    parser.add_argument(
        "--out",
        default="dist/themes",
        help="Output directory for .toml themes (default: dist/themes).",
    )
    parser.add_argument(
        "--only",
        action="append",
        default=[],
        help="Limit to a palette name (can be repeated).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned outputs without writing files.",
    )
    args = parser.parse_args()

    colors_path = Path(args.colors)
    out_dir = Path(args.out)
    content = colors_path.read_text(encoding="utf-8")
    palettes = parse_colors_markdown(content)

    only = [name.strip().lower() for name in args.only]
    targets = {
        name: palette for name, palette in palettes.items() if not only or name.lower() in only
    }

    if not targets:
        print("No palettes found.")
        return 1

    for name, colors in targets.items():
        palette = build_palette(colors)
        body = THEME_TEMPLATE.format(palette=format_palette(palette))
        filename = f"{slugify(name)}.toml"
        path = out_dir / filename
        if args.dry_run:
            print(path)
            continue
        out_dir.mkdir(parents=True, exist_ok=True)
        path.write_text(body, encoding="utf-8")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
