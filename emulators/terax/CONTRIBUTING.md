<h1 align="center">Contributing to Terax Themes</h1>

<p align="center">
  Thank you for your interest in contributing new themes or improvements to the Terax Themes collection.
</p>

---

<h2 align="center">Proposing a New Theme</h2>

To propose a new theme:

1. **Open an issue** describing the theme concept, target audience, and a rough color palette. Include a name and whether it is a dark or light variant.
2. **Wait for feedback** -- theme proposals are discussed before implementation to ensure they fill a gap in the existing collection.

---

<h2 align="center">Theme Format Requirements</h2>

Every theme must follow the Terax `.terax-theme` JSON schema. See [colors.md](colors.md) for the full reference and examples.

Minimum requirements for a new theme:

- **`id`** -- unique kebab-case string (lowercase a-z, digits, hyphens), not already used by any existing theme
- **`name`** -- human-readable display name
- **`author`** -- your name or handle
- **`description`** -- one sentence describing the theme's character
- **`editorTheme`** -- CodeMirror theme for both `"dark"` and `"light"` keys (if the theme provides both variants), or just the matching variant
- **`variants`** -- at least one variant (`"dark"` or `"light"`) with:
  - **`colors`** -- all 25 UI color tokens (see the schema in colors.md)
  - **`terminal`** -- all 16 ANSI colors, plus `background`, `foreground`, `cursor`, `cursorAccent`, and `selection`

Valid editor theme names: `atomone`, `aura`, `copilot`, `github-dark`, `github-light`, `gruvbox-dark`, `nord`, `tokyo-night`, `xcode-dark`, `xcode-light`.

Place the new theme file in the `themes/` directory with the filename `<id>.terax-theme`.

---

<h2 align="center">Pull Request Process</h2>

1. **Fork** the repository and create a feature branch from `main`.
2. **Add** your theme file to the `themes/` directory.
3. **Update** `colors.md` -- add a section for your theme following the existing format (background color summary, full JSON block).
4. **Update** `install-terax-themes.sh` and `install-terax-themes.ps1` -- add your theme to both install scripts so it is included in automated installs.
5. **Update** `README.md` -- add your theme to the themes table and the preview table.
6. **Open a pull request** with a clear description of the theme and a screenshot or color summary.

PRs must pass the following checks:

- JSON is valid and matches the `.terax-theme` schema
- Theme `id` is unique and uses kebab-case
- All 25 UI color tokens and all 16 ANSI terminal colors are present
- Theme is added to both install scripts
- Documentation (`colors.md`, `README.md`) is updated

---

<h2 align="center">Code of Conduct</h2>

<p align="center">
  This project follows the <a href="CODE_OF_CONDUCT.md">Contributor Covenant Code of Conduct</a>.
  By participating, you agree to uphold its terms.
</p>
