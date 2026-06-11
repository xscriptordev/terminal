# Scripts

## Theme Generator

Generate Helix themes from the palettes in `colors.md`.

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
- Output defaults to `dist/themes` to avoid overwriting curated themes.
- Palette mapping uses `color0` as background and `color7` as foreground.
- Generated files are overwritten when the script runs.

## Roadmap Sync

Sync `ROADMAP.md` task status with GitHub Issues (open/close issues, add labels).

Usage:
```bash
python3 .github/scripts/sync_roadmap.py --roadmap ROADMAP.md
```

Requirements:
- Python 3.12+
- `gh` CLI authenticated with a token with `issues:write` scope

This script is also triggered automatically via `.github/workflows/roadmap-sync.yml`.
