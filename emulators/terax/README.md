<h1 align="center">Terax X Themes</h1>

<p align="center">
  Part of the <a href="https://github.com/xscriptor/terminal">xscriptor/terminal</a> theme collection.
</p>

<p align="center">
  <a href="https://github.com/xscriptor/terminal/blob/main/emulators/terax/LICENSE"><img src="https://img.shields.io/badge/license-Apache--2.0-blue?style=flat-square" alt="License: Apache-2.0" /></a>
  <a href="#"><img src="https://img.shields.io/badge/version-1.0.0-informational?style=flat-square" alt="Version 1.0.0" /></a>
  <a href="#"><img src="https://img.shields.io/badge/platform-linux%20%7C%20macos%20%7C%20windows-lightgrey?style=flat-square" alt="Platform: Linux, macOS, Windows" /></a>
</p>

<p align="center">
  X theme collection for
  <a href="https://github.com/crynta/terax-ai">Terax</a>,
  the open-source terminal AI dev workspace built on Tauri 2, Rust, and React.
</p>

---

<h2 align="center">Quick Install</h2>

<p align="center">
  <strong>Linux / macOS</strong>
</p>

```bash
curl -fsSL https://raw.githubusercontent.com/xscriptor/terminal/main/emulators/terax/install-terax-themes.sh | bash
```

<p align="center">
  <strong>Windows (PowerShell)</strong>
</p>

```powershell
irm https://raw.githubusercontent.com/xscriptor/terminal/main/emulators/terax/install-terax-themes.ps1 | iex
```

After installation, restart Terax. Themes appear under **Settings > Appearance > Theme**.

---

<h2 align="center">Manual Install</h2>

Copy all `.terax-theme` files from the `themes/` directory to your Terax themes folder:

| Platform | Themes Directory |
|----------|-----------------|
| Linux | `~/.config/com.terax.app/themes/` |
| macOS | `~/Library/Application Support/com.terax.app/themes/` |
| Windows | `%APPDATA%\com.terax.app\themes\` |

**Linux:**
```bash
cp themes/*.terax-theme ~/.config/com.terax.app/themes/
```

**macOS:**
```bash
cp themes/*.terax-theme ~/Library/Application\ Support/com.terax.app/themes/
```

**Windows (PowerShell):**
```powershell
Copy-Item themes\*.terax-theme $env:APPDATA\com.terax.app\themes\
```

---

<h2 align="center">Themes</h2>

<h3 align="center">Dark Themes</h3>

| Theme | Background | Description |
|-------|-----------|-------------|
| **X** | `#0a0a0a` | Near-black with vibrant neon accents. High contrast for late-night coding. |
| **Lahabana** | `#363537` | Warm charcoal base with electric lime and magenta. Caribbean nights. |
| **Miami** | `#000000` | Pure black with synthwave neon -- cyan, magenta, and hot pink. Retro-futuristic. |
| **Paris** | `#10081a` | Deep violet-black with cyan and lavender. Parisian nights. |
| **Tokio** | `#363537` | Dark graphite with warm orange accents and electric blue. Tokyo nightscape. |
| **Oslo** | `#3f4451` | Slate-blue dark surfaces with muted teal and lavender. Nordic twilight. |
| **Praha** | `#1A1A1A` | Dark and dramatic with pink, cyan, and purple. Bohemian night. |
| **Bogota** | `#140606` | Deep crimson-black with hot pink and electric cyan. Warm and intense. |

<h3 align="center">Light Themes</h3>

| Theme | Background | Description |
|-------|-----------|-------------|
| **Madrid** | `#fafafa` | Warm ivory with crimson and teal. Mediterranean sunlight. |
| **Helsinki** | `#f8fafe` | Cool frosted-white with teal, deep purple, and warm amber. Nordic mornings. |
| **Berlin** | `#000000` | Greyscale monochrome. Brutalist, minimal, distraction-free. |
| **London** | `#ffffff` | Clean white with grey gradients. Minimal and bright. |

---

<h2 align="center">Preview</h2>

| Theme | Type | Background |
|-------|------|------------|
| X | dark | `#0a0a0a` |
| Lahabana | dark | `#363537` |
| Miami | dark | `#000000` |
| Paris | dark | `#10081a` |
| Tokio | dark | `#363537` |
| Oslo | dark | `#3f4451` |
| Praha | dark | `#1A1A1A` |
| Bogota | dark | `#140606` |
| Madrid | light | `#fafafa` |
| Helsinki | light | `#f8fafe` |
| Berlin | dark | `#000000` |
| London | light | `#ffffff` |

For the complete color reference including every UI token and ANSI terminal palette, see [colors.md](colors.md).

Individual theme files are available in the [themes/](themes/) directory.

---

<h2 align="center">Theme Format</h2>

Each `.terax-theme` file is a JSON document with the following structure:

- **`id`** -- unique kebab-case identifier (a-z, 0-9, hyphens)
- **`name`** -- display name shown in the theme picker
- **`author`** -- theme author (optional)
- **`description`** -- short description (optional)
- **`editorTheme`** -- CodeMirror editor theme mapping for dark/light mode (optional)
- **`variants`** -- at least one of `dark` or `light`, each containing:
  - **`colors`** -- 25 UI color tokens (background, foreground, card, popover, primary, secondary, muted, accent, destructive, border, input, ring, and sidebar variants)
  - **`terminal`** -- ANSI 16-color palette plus background, foreground, cursor, and selection colors

Valid editor theme values: `atomone`, `aura`, `copilot`, `github-dark`, `github-light`, `gruvbox-dark`, `nord`, `tokyo-night`, `xcode-dark`, `xcode-light`.
