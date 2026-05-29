# Scripts

## Theme Generator

Generate Helix themes from the palettes in colors.md.

Requirements:
- Python 3.11+

Usage:
```bash
python3 scripts/generate_themes.py
```

Options:
```bash
python3 scripts/generate_themes.py --dry-run
python3 scripts/generate_themes.py --only Madrid --only X
python3 scripts/generate_themes.py --out dist/themes
python3 scripts/generate_themes.py --colors colors.md
```

Notes:
- Output defaults to dist/themes to avoid overwriting curated themes.
- Palette mapping uses color0 as background and color7 as foreground.
- Generated files are overwritten when the script runs.
