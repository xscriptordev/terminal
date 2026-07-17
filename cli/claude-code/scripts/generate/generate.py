#!/usr/bin/env python3
"""
Generate Claude Code themes from X Colors palette definitions.

Usage:
  python generate.py                              # read local colors.md
  python generate.py https://example.com/colors.md # download from URL
  python generate.py ./path/to/colors.md           # custom local path
  python generate.py --out ./my-themes             # output directory
"""

import argparse
import json
import os
import re
import sys
import urllib.request
import urllib.error

DEFAULT_COLORS_URL = "https://raw.githubusercontent.com/xscriptor/xassets/main/colors/colors.md"
DEFAULT_OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "themes")


def parse_hex(c):
    c = c.strip().lower()
    if c.startswith("#"):
        c = c[1:]
    if len(c) == 3:
        c = "".join(x * 2 for x in c)
    return c


def hex_to_rgb(h):
    h = parse_hex(h)
    return int(h[0:2], 16), int(h[2:4], 16), int(h[4:6], 16)


def rgb_to_hex(r, g, b):
    return f"#{max(0, min(255, r)):02x}{max(0, min(255, g)):02x}{max(0, min(255, b)):02x}"


def blend(c1, c2, ratio):
    r1, g1, b1 = hex_to_rgb(c1)
    r2, g2, b2 = hex_to_rgb(c2)
    return rgb_to_hex(
        int(r1 * ratio + r2 * (1 - ratio)),
        int(g1 * ratio + g2 * (1 - ratio)),
        int(b1 * ratio + b2 * (1 - ratio)),
    )


def luminance(h):
    r, g, b = hex_to_rgb(h)
    return (r * 299 + g * 587 + b * 114) / 1000


def is_dark(h):
    return luminance(h) < 128


def is_grayscale(palette):
    for i in range(16):
        key = f"color{i}"
        if key in palette:
            r, g, b = hex_to_rgb(palette[key])
            if max(r, g, b) - min(r, g, b) > 20:
                return False
    return True


def fetch_colors(source):
    if source.startswith("http://") or source.startswith("https://"):
        try:
            with urllib.request.urlopen(source, timeout=30) as resp:
                return resp.read().decode("utf-8")
        except Exception as e:
            print(f"Error downloading {source}: {e}", file=sys.stderr)
            sys.exit(1)
    else:
        path = os.path.expanduser(source)
        if not os.path.isfile(path):
            print(f"File not found: {path}", file=sys.stderr)
            sys.exit(1)
        with open(path, "r") as f:
            return f.read()


def parse_palettes(markdown):
    palettes = []
    current_name = None
    in_json = False
    json_lines = []

    for line in markdown.splitlines():
        heading = re.match(r"^##\s+(.+)$", line) or re.match(r'<h2[^>]*>\s*(.+?)\s*</h2>', line)
        if heading:
            if current_name and json_lines:
                try:
                    data = json.loads("\n".join(json_lines))
                    if "background" in data and "foreground" in data:
                        palettes.append((current_name, data))
                except json.JSONDecodeError:
                    pass
            current_name = heading.group(1).strip()
            json_lines = []
            in_json = False
            continue

        if re.match(r"^```json", line):
            in_json = True
            json_lines = []
            continue

        if line.strip() == "```" and in_json:
            in_json = False
            continue

        if in_json:
            json_lines.append(line)

    if current_name and json_lines:
        try:
            data = json.loads("\n".join(json_lines))
            if "background" in data and "foreground" in data:
                palettes.append((current_name, data))
        except json.JSONDecodeError:
            pass

    return palettes


def slugify(name):
    s = name.strip().lower().replace(" ", "-").replace("_", "-")
    return re.sub(r"[^a-z0-9-]", "", s)


def generate_theme(name, palette):
    bg = palette["background"]
    fg = palette["foreground"]
    c = {i: palette.get(f"color{i}", "#000000") for i in range(16)}
    dark = is_dark(bg)
    gray = is_grayscale(palette)

    if gray:
        primary = c[2]
    else:
        primary = c[4]

    def ddiff(color, ratio=0.18):
        return blend(color, bg, ratio)

    def ldiff(color, ratio=0.12):
        return blend(color, bg, ratio)

    if dark:
        return {
            "name": name,
            "base": "dark",
            "overrides": {
                "claude": primary,
                "text": fg,
                "inverseText": bg,
                "inactive": c[8],
                "subtle": c[0],
                "suggestion": c[6],
                "permission": c[5],
                "remember": c[6],
                "success": c[2],
                "error": c[1],
                "warning": c[3],
                "merged": c[5],
                "promptBorder": primary,
                "planMode": c[6],
                "autoAccept": c[2],
                "bashBorder": primary,
                "ide": c[5],
                "fastMode": c[3],
                "diffAdded": ddiff(c[2], 0.18),
                "diffRemoved": ddiff(c[1], 0.18),
                "diffAddedDimmed": ddiff(c[2], 0.08),
                "diffRemovedDimmed": ddiff(c[1], 0.08),
                "diffAddedWord": c[2],
                "diffRemovedWord": c[1],
                "userMessageBackground": c[0],
                "userMessageBackgroundHover": blend(c[8], bg, 0.5) if c[8] != c[0] else rgb_to_hex(*[min(255, x + 8) for x in hex_to_rgb(c[0])]),
                "bashMessageBackgroundColor": c[0],
                "memoryBackgroundColor": c[0],
                "selectionBg": c[6],
                "rate_limit_fill": c[2],
                "rate_limit_empty": c[0],
                "briefLabelYou": c[6],
                "briefLabelClaude": primary,
                "red_FOR_SUBAGENTS_ONLY": c[1],
                "blue_FOR_SUBAGENTS_ONLY": c[6],
                "green_FOR_SUBAGENTS_ONLY": c[2],
                "yellow_FOR_SUBAGENTS_ONLY": c[3],
                "purple_FOR_SUBAGENTS_ONLY": c[5],
                "orange_FOR_SUBAGENTS_ONLY": primary if primary != c[6] else c[4],
                "pink_FOR_SUBAGENTS_ONLY": c[1],
                "cyan_FOR_SUBAGENTS_ONLY": c[6],
            },
        }
    else:
        return {
            "name": name,
            "base": "light",
            "overrides": {
                "claude": primary,
                "text": fg,
                "inverseText": bg,
                "inactive": c[8],
                "subtle": c[0] if c[0] != bg else fg,
                "suggestion": primary,
                "permission": c[5],
                "remember": primary,
                "success": c[2],
                "error": c[1],
                "warning": c[3],
                "merged": c[5],
                "promptBorder": primary,
                "planMode": primary,
                "autoAccept": c[2],
                "bashBorder": primary,
                "ide": c[5],
                "fastMode": c[3],
                "diffAdded": ldiff(c[2], 0.15),
                "diffRemoved": ldiff(c[1], 0.15),
                "diffAddedDimmed": ldiff(c[2], 0.06),
                "diffRemovedDimmed": ldiff(c[1], 0.06),
                "diffAddedWord": c[2],
                "diffRemovedWord": c[1],
                "userMessageBackground": bg,
                "userMessageBackgroundHover": rgb_to_hex(*[max(0, x - 8) for x in hex_to_rgb(bg)]),
                "bashMessageBackgroundColor": bg,
                "memoryBackgroundColor": bg,
                "selectionBg": primary,
                "rate_limit_fill": c[2],
                "rate_limit_empty": rgb_to_hex(*[max(0, x - 10) for x in hex_to_rgb(bg)]),
                "briefLabelYou": primary,
                "briefLabelClaude": primary,
                "red_FOR_SUBAGENTS_ONLY": c[1],
                "blue_FOR_SUBAGENTS_ONLY": primary,
                "green_FOR_SUBAGENTS_ONLY": c[2],
                "yellow_FOR_SUBAGENTS_ONLY": c[3],
                "purple_FOR_SUBAGENTS_ONLY": c[5],
                "orange_FOR_SUBAGENTS_ONLY": primary,
                "pink_FOR_SUBAGENTS_ONLY": c[1],
                "cyan_FOR_SUBAGENTS_ONLY": primary,
            },
        }


def main():
    parser = argparse.ArgumentParser(description="Generate Claude Code themes from X Colors")
    parser.add_argument("source", nargs="?", default=None,
                        help="URL or local path to colors.md (default: download from GitHub)")
    parser.add_argument("--out", "-o", default=DEFAULT_OUTPUT,
                        help=f"Output directory (default: {DEFAULT_OUTPUT})")
    args = parser.parse_args()

    source = args.source or DEFAULT_COLORS_URL
    out_dir = os.path.abspath(args.out)

    print(f"Reading colors from: {source}")
    markdown = fetch_colors(source)
    palettes = parse_palettes(markdown)

    if not palettes:
        print("No palettes found in source.", file=sys.stderr)
        sys.exit(1)

    print(f"Found {len(palettes)} palette(s): {', '.join(n for n, _ in palettes)}")
    os.makedirs(out_dir, exist_ok=True)

    for name, palette in palettes:
        theme = generate_theme(name, palette)
        slug = slugify(name)
        path = os.path.join(out_dir, f"{slug}.json")
        with open(path, "w") as f:
            json.dump(theme, f, indent=2)
            f.write("\n")
        print(f"  {slug}.json")

    print(f"\nDone! {len(palettes)} theme(s) written to {out_dir}")


if __name__ == "__main__":
    main()
