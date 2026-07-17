# Terax Themes — Color Schemes

> Each theme is a complete `.terax-theme` JSON file. The first color listed is the **interface background** (`colors.background`), followed by all UI tokens and the full 16-color terminal ANSI palette.

---

## Dark Themes

### X — Dark & Neon

**Background:** `#0a0a0a` — near-black with vibrant neon accents

```json
{
  "id": "xscriptor",
  "name": "X",
  "author": "xscriptor-terax-themes",
  "description": "Near-black background with vibrant neon accents. High contrast for late-night coding.",
  "editorTheme": { "dark": "atomone" },
  "variants": {
    "dark": {
      "colors": {
        "background": "#0a0a0a",
        "foreground": "#f7f1ff",
        "card": "#121214",
        "cardForeground": "#f7f1ff",
        "popover": "#121214",
        "popoverForeground": "#f7f1ff",
        "primary": "#fc618d",
        "primaryForeground": "#0a0a0a",
        "secondary": "#1a1a1e",
        "secondaryForeground": "#f7f1ff",
        "muted": "#1a1a1e",
        "mutedForeground": "#69676c",
        "accent": "#1a1a1e",
        "accentForeground": "#f7f1ff",
        "destructive": "#fc618d",
        "border": "rgba(247,241,255,0.08)",
        "input": "rgba(247,241,255,0.12)",
        "ring": "#948ae3",
        "sidebar": "#0a0a0a",
        "sidebarForeground": "#f7f1ff",
        "sidebarPrimary": "#fc618d",
        "sidebarPrimaryForeground": "#0a0a0a",
        "sidebarAccent": "#1a1a1e",
        "sidebarAccentForeground": "#f7f1ff",
        "sidebarBorder": "rgba(247,241,255,0.08)",
        "sidebarRing": "#948ae3"
      },
      "terminal": {
        "background": "#0a0a0a",
        "foreground": "#f7f1ff",
        "cursor": "#f7f1ff",
        "cursorAccent": "#0a0a0a",
        "selection": "rgba(252,97,141,0.25)",
        "ansi": [
          "#0a0a0a", "#fc618d", "#7bd88f", "#fce566",
          "#fd9353", "#948ae3", "#5ad4e6", "#f7f1ff",
          "#69676c", "#fc618d", "#7bd88f", "#fce566",
          "#fd9353", "#948ae3", "#5ad4e6", "#f7f1ff"
        ]
      }
    }
  }
}
```

---

### Lahabana — Deep Charcoal & Lime

**Background:** `#363537` — charcoal with bright lime and magenta

```json
{
  "id": "lahabana",
  "name": "Lahabana",
  "author": "xscriptor-terax-themes",
  "description": "Warm charcoal base with electric lime and magenta. Caribbean nights.",
  "editorTheme": { "dark": "atomone" },
  "variants": {
    "dark": {
      "colors": {
        "background": "#363537",
        "foreground": "#f7f1ff",
        "card": "#3e3d40",
        "cardForeground": "#f7f1ff",
        "popover": "#3e3d40",
        "popoverForeground": "#f7f1ff",
        "primary": "#e5ff9d",
        "primaryForeground": "#363537",
        "secondary": "#444346",
        "secondaryForeground": "#f7f1ff",
        "muted": "#444346",
        "mutedForeground": "#69676c",
        "accent": "#444346",
        "accentForeground": "#f7f1ff",
        "destructive": "#fc618d",
        "border": "rgba(247,241,255,0.10)",
        "input": "rgba(247,241,255,0.14)",
        "ring": "#e5ff9d",
        "sidebar": "#2e2d30",
        "sidebarForeground": "#f7f1ff",
        "sidebarPrimary": "#e5ff9d",
        "sidebarPrimaryForeground": "#363537",
        "sidebarAccent": "#444346",
        "sidebarAccentForeground": "#f7f1ff",
        "sidebarBorder": "rgba(247,241,255,0.10)",
        "sidebarRing": "#e5ff9d"
      },
      "terminal": {
        "background": "#363537",
        "foreground": "#f7f1ff",
        "cursor": "#e5ff9d",
        "cursorAccent": "#363537",
        "selection": "rgba(229,255,157,0.22)",
        "ansi": [
          "#363537", "#fc618d", "#7bd88f", "#e5ff9d",
          "#fd9353", "#948ae3", "#5ad4e6", "#f7f1ff",
          "#69676c", "#fc618d", "#7bd88f", "#e5ff9d",
          "#fd9353", "#948ae3", "#5ad4e6", "#f7f1ff"
        ]
      }
    }
  }
}
```

---

### Miami — Black & Neon Synthwave

**Background:** `#000000` — pure black with cyan, magenta and neon green

```json
{
  "id": "miami",
  "name": "Miami",
  "author": "xscriptor-terax-themes",
  "description": "Pure black with synthwave neon — cyan, magenta, and hot pink. Retro-futuristic.",
  "editorTheme": { "dark": "atomone" },
  "variants": {
    "dark": {
      "colors": {
        "background": "#000000",
        "foreground": "#f7f1ff",
        "card": "#0c0c10",
        "cardForeground": "#f7f1ff",
        "popover": "#0c0c10",
        "popoverForeground": "#f7f1ff",
        "primary": "#FF4C8B",
        "primaryForeground": "#ffffff",
        "secondary": "#14141a",
        "secondaryForeground": "#f7f1ff",
        "muted": "#14141a",
        "mutedForeground": "#69676c",
        "accent": "#14141a",
        "accentForeground": "#f7f1ff",
        "destructive": "#FF4C8B",
        "border": "rgba(255,255,255,0.08)",
        "input": "rgba(255,255,255,0.10)",
        "ring": "#47CFFF",
        "sidebar": "#000000",
        "sidebarForeground": "#f7f1ff",
        "sidebarPrimary": "#47CFFF",
        "sidebarPrimaryForeground": "#000000",
        "sidebarAccent": "#14141a",
        "sidebarAccentForeground": "#f7f1ff",
        "sidebarBorder": "rgba(255,255,255,0.08)",
        "sidebarRing": "#47CFFF"
      },
      "terminal": {
        "background": "#000000",
        "foreground": "#f7f1ff",
        "cursor": "#47CFFF",
        "cursorAccent": "#000000",
        "selection": "rgba(71,207,255,0.25)",
        "ansi": [
          "#000000", "#FF4C8B", "#7FFFD4", "#FFD84C",
          "#00FFA8", "#D36CFF", "#47CFFF", "#f7f1ff",
          "#69676c", "#FF4C8B", "#7FFFD4", "#FFD84C",
          "#00FFA8", "#D36CFF", "#47CFFF", "#f7f1ff"
        ]
      }
    }
  }
}
```

---

### Paris — Deep Violet Night

**Background:** `#10081a` — deep violet-black with cyan and lavender

```json
{
  "id": "paris",
  "name": "Paris",
  "author": "xscriptor-terax-themes",
  "description": "Deep violet-black reminiscent of Parisian nights. Cyan and lavender accents.",
  "editorTheme": { "dark": "atomone" },
  "variants": {
    "dark": {
      "colors": {
        "background": "#10081a",
        "foreground": "#f7f1ff",
        "card": "#191024",
        "cardForeground": "#f7f1ff",
        "popover": "#191024",
        "popoverForeground": "#f7f1ff",
        "primary": "#c4bdff",
        "primaryForeground": "#10081a",
        "secondary": "#201530",
        "secondaryForeground": "#f7f1ff",
        "muted": "#201530",
        "mutedForeground": "#525053",
        "accent": "#201530",
        "accentForeground": "#f7f1ff",
        "destructive": "#fc618d",
        "border": "rgba(247,241,255,0.08)",
        "input": "rgba(247,241,255,0.12)",
        "ring": "#a3f3ff",
        "sidebar": "#10081a",
        "sidebarForeground": "#f7f1ff",
        "sidebarPrimary": "#a3f3ff",
        "sidebarPrimaryForeground": "#10081a",
        "sidebarAccent": "#201530",
        "sidebarAccentForeground": "#f7f1ff",
        "sidebarBorder": "rgba(247,241,255,0.08)",
        "sidebarRing": "#a3f3ff"
      },
      "terminal": {
        "background": "#10081a",
        "foreground": "#f7f1ff",
        "cursor": "#a3f3ff",
        "cursorAccent": "#10081a",
        "selection": "rgba(163,243,255,0.22)",
        "ansi": [
          "#10081a", "#fc618d", "#7bd88f", "#fce566",
          "#a3f3ff", "#c4bdff", "#a3f3ff", "#f7f1ff",
          "#525053", "#fc618d", "#7bd88f", "#fce566",
          "#a3f3ff", "#c4bdff", "#a3f3ff", "#f7f1ff"
        ]
      }
    }
  }
}
```

---

### Tokio — Dark Graphite & Orange

**Background:** `#363537` — graphite with warm orange and electric blue

```json
{
  "id": "tokio",
  "name": "Tokio",
  "author": "xscriptor-terax-themes",
  "description": "Dark graphite surfaces with warm orange accents and electric blue. Tokyo nightscape.",
  "editorTheme": { "dark": "tokyo-night" },
  "variants": {
    "dark": {
      "colors": {
        "background": "#363537",
        "foreground": "#f7f1ff",
        "card": "#3e3d40",
        "cardForeground": "#f7f1ff",
        "popover": "#3e3d40",
        "popoverForeground": "#f7f1ff",
        "primary": "#fd9353",
        "primaryForeground": "#1a1a1a",
        "secondary": "#46454a",
        "secondaryForeground": "#f7f1ff",
        "muted": "#46454a",
        "mutedForeground": "#69676c",
        "accent": "#46454a",
        "accentForeground": "#f7f1ff",
        "destructive": "#fc618d",
        "border": "rgba(247,241,255,0.08)",
        "input": "rgba(247,241,255,0.12)",
        "ring": "#fd9353",
        "sidebar": "#2e2d30",
        "sidebarForeground": "#f7f1ff",
        "sidebarPrimary": "#fd9353",
        "sidebarPrimaryForeground": "#1a1a1a",
        "sidebarAccent": "#46454a",
        "sidebarAccentForeground": "#f7f1ff",
        "sidebarBorder": "rgba(247,241,255,0.08)",
        "sidebarRing": "#fd9353"
      },
      "terminal": {
        "background": "#363537",
        "foreground": "#f7f1ff",
        "cursor": "#fd9353",
        "cursorAccent": "#363537",
        "selection": "rgba(253,147,83,0.22)",
        "ansi": [
          "#363537", "#fc618d", "#7bd88f", "#fce566",
          "#fd9353", "#948ae3", "#5ad4e6", "#f7f1ff",
          "#69676c", "#fc618d", "#7bd88f", "#fce566",
          "#fd9353", "#948ae3", "#5ad4e6", "#f7f1ff"
        ]
      }
    }
  }
}
```

---

### Oslo — Arctic Dark

**Background:** `#3f4451` — slate blue with muted teal and lavender

```json
{
  "id": "oslo",
  "name": "Oslo",
  "author": "xscriptor-terax-themes",
  "description": "Slate-blue dark surfaces with muted teal and lavender. Nordic twilight.",
  "editorTheme": { "dark": "nord" },
  "variants": {
    "dark": {
      "colors": {
        "background": "#3f4451",
        "foreground": "#e6e6e6",
        "card": "#4a4f5e",
        "cardForeground": "#e6e6e6",
        "popover": "#4a4f5e",
        "popoverForeground": "#e6e6e6",
        "primary": "#4dc4ff",
        "primaryForeground": "#1a1c24",
        "secondary": "#535969",
        "secondaryForeground": "#e6e6e6",
        "muted": "#535969",
        "mutedForeground": "#4f5666",
        "accent": "#535969",
        "accentForeground": "#e6e6e6",
        "destructive": "#ff616e",
        "border": "rgba(230,230,230,0.08)",
        "input": "rgba(230,230,230,0.12)",
        "ring": "#4dc4ff",
        "sidebar": "#363b46",
        "sidebarForeground": "#e6e6e6",
        "sidebarPrimary": "#4dc4ff",
        "sidebarPrimaryForeground": "#1a1c24",
        "sidebarAccent": "#535969",
        "sidebarAccentForeground": "#e6e6e6",
        "sidebarBorder": "rgba(230,230,230,0.08)",
        "sidebarRing": "#4dc4ff"
      },
      "terminal": {
        "background": "#3f4451",
        "foreground": "#e6e6e6",
        "cursor": "#42b3c2",
        "cursorAccent": "#3f4451",
        "selection": "rgba(77,196,255,0.22)",
        "ansi": [
          "#3f4451", "#e05561", "#8cc265", "#d18f52",
          "#4aa5f0", "#c162de", "#42b3c2", "#e6e6e6",
          "#4f5666", "#ff616e", "#a5e075", "#f0a45d",
          "#4dc4ff", "#de73ff", "#4cd1e0", "#ffffff"
        ]
      }
    }
  }
}
```

---

### Praha — Dracula-inspired

**Background:** `#1A1A1A` — dark with pink, cyan, and purple

```json
{
  "id": "praha",
  "name": "Praha",
  "author": "xscriptor-terax-themes",
  "description": "Dark and dramatic with pink, cyan, and purple. Bohemian night.",
  "editorTheme": { "dark": "atomone" },
  "variants": {
    "dark": {
      "colors": {
        "background": "#1A1A1A",
        "foreground": "#FFFFFF",
        "card": "#242428",
        "cardForeground": "#FFFFFF",
        "popover": "#242428",
        "popoverForeground": "#FFFFFF",
        "primary": "#BD93F9",
        "primaryForeground": "#1A1A1A",
        "secondary": "#2e2e34",
        "secondaryForeground": "#FFFFFF",
        "muted": "#2e2e34",
        "mutedForeground": "#6272A4",
        "accent": "#2e2e34",
        "accentForeground": "#FFFFFF",
        "destructive": "#FF5555",
        "border": "rgba(255,255,255,0.08)",
        "input": "rgba(255,255,255,0.12)",
        "ring": "#BD93F9",
        "sidebar": "#1A1A1A",
        "sidebarForeground": "#FFFFFF",
        "sidebarPrimary": "#BD93F9",
        "sidebarPrimaryForeground": "#1A1A1A",
        "sidebarAccent": "#2e2e34",
        "sidebarAccentForeground": "#FFFFFF",
        "sidebarBorder": "rgba(255,255,255,0.08)",
        "sidebarRing": "#BD93F9"
      },
      "terminal": {
        "background": "#1A1A1A",
        "foreground": "#FFFFFF",
        "cursor": "#8BE9FD",
        "cursorAccent": "#1A1A1A",
        "selection": "rgba(189,147,249,0.22)",
        "ansi": [
          "#1A1A1A", "#FF5555", "#B8E6A0", "#FFE4A3",
          "#BD93F9", "#FF9AA2", "#8BE9FD", "#FFFFFF",
          "#6272A4", "#FF6E6E", "#B8E6A0", "#FFE4A3",
          "#D6ACFF", "#FF9AA2", "#A4FFFF", "#FFFFFF"
        ]
      }
    }
  }
}
```

---

### Bogota — Deep Crimson Black

**Background:** `#140606` — deep red-black with hot pink and cyan

```json
{
  "id": "bogota",
  "name": "Bogota",
  "author": "xscriptor-terax-themes",
  "description": "Deep crimson-black with hot pink and electric cyan. Warm and intense.",
  "editorTheme": { "dark": "atomone" },
  "variants": {
    "dark": {
      "colors": {
        "background": "#140606",
        "foreground": "#f7f1ff",
        "card": "#1e1010",
        "cardForeground": "#f7f1ff",
        "popover": "#1e1010",
        "popoverForeground": "#f7f1ff",
        "primary": "#ff9999",
        "primaryForeground": "#140606",
        "secondary": "#261818",
        "secondaryForeground": "#f7f1ff",
        "muted": "#261818",
        "mutedForeground": "#525053",
        "accent": "#261818",
        "accentForeground": "#f7f1ff",
        "destructive": "#fc618d",
        "border": "rgba(247,241,255,0.10)",
        "input": "rgba(247,241,255,0.14)",
        "ring": "#47e6ff",
        "sidebar": "#140606",
        "sidebarForeground": "#f7f1ff",
        "sidebarPrimary": "#47e6ff",
        "sidebarPrimaryForeground": "#140606",
        "sidebarAccent": "#261818",
        "sidebarAccentForeground": "#f7f1ff",
        "sidebarBorder": "rgba(247,241,255,0.10)",
        "sidebarRing": "#47e6ff"
      },
      "terminal": {
        "background": "#140606",
        "foreground": "#f7f1ff",
        "cursor": "#47e6ff",
        "cursorAccent": "#140606",
        "selection": "rgba(71,230,255,0.22)",
        "ansi": [
          "#140606", "#fc618d", "#7bd88f", "#ffed89",
          "#47e6ff", "#ff9999", "#47e6ff", "#f7f1ff",
          "#525053", "#fc618d", "#7bd88f", "#ffed89",
          "#47e6ff", "#ff9999", "#47e6ff", "#f7f1ff"
        ]
      }
    }
  }
}
```

---

## Light Themes

### Madrid — Clean Ivory

**Background:** `#fafafa` — off-white with deep crimson and teal accents

```json
{
  "id": "madrid",
  "name": "Madrid",
  "author": "xscriptor-terax-themes",
  "description": "Warm ivory background with crimson and teal. Mediterranean sunlight.",
  "editorTheme": { "light": "xcode-light" },
  "variants": {
    "light": {
      "colors": {
        "background": "#fafafa",
        "foreground": "#1a1a1a",
        "card": "#ffffff",
        "cardForeground": "#1a1a1a",
        "popover": "#ffffff",
        "popoverForeground": "#1a1a1a",
        "primary": "#990026",
        "primaryForeground": "#fafafa",
        "secondary": "#f0f0f0",
        "secondaryForeground": "#1a1a1a",
        "muted": "#f0f0f0",
        "mutedForeground": "#4d4d4d",
        "accent": "#f0f0f0",
        "accentForeground": "#1a1a1a",
        "destructive": "#990026",
        "border": "rgba(26,26,26,0.10)",
        "input": "rgba(26,26,26,0.14)",
        "ring": "#007a28",
        "sidebar": "#f5f5f5",
        "sidebarForeground": "#1a1a1a",
        "sidebarPrimary": "#007a9e",
        "sidebarPrimaryForeground": "#ffffff",
        "sidebarAccent": "#e8e8e8",
        "sidebarAccentForeground": "#1a1a1a",
        "sidebarBorder": "rgba(26,26,26,0.10)",
        "sidebarRing": "#007a9e"
      },
      "terminal": {
        "background": "#fafafa",
        "foreground": "#1a1a1a",
        "cursor": "#1a1a1a",
        "cursorAccent": "#fafafa",
        "selection": "rgba(0,122,158,0.18)",
        "ansi": [
          "#fafafa", "#990026", "#007a28", "#8a6408",
          "#007a9e", "#4d2699", "#007a9e", "#1a1a1a",
          "#4d4d4d", "#990026", "#007a28", "#8a6408",
          "#007a9e", "#4d2699", "#007a9e", "#1a1a1a"
        ]
      }
    }
  }
}
```

---

### Helsinki — Frosted Nordic Light

**Background:** `#f8fafe` — cool white-blue with teal, purple, and amber

```json
{
  "id": "helsinki",
  "name": "Helsinki",
  "author": "xscriptor-terax-themes",
  "description": "Cool frosted-white with teal, deep purple, and warm amber. Nordic mornings.",
  "editorTheme": { "light": "xcode-light" },
  "variants": {
    "light": {
      "colors": {
        "background": "#f8fafe",
        "foreground": "#544d40",
        "card": "#ffffff",
        "cardForeground": "#544d40",
        "popover": "#ffffff",
        "popoverForeground": "#544d40",
        "primary": "#1faa9e",
        "primaryForeground": "#ffffff",
        "secondary": "#eef0f8",
        "secondaryForeground": "#544d40",
        "muted": "#eef0f8",
        "mutedForeground": "#b0a999",
        "accent": "#eef0f8",
        "accentForeground": "#544d40",
        "destructive": "#bd4c3d",
        "border": "rgba(84,77,64,0.10)",
        "input": "rgba(84,77,64,0.14)",
        "ring": "#1faa9e",
        "sidebar": "#eff2fa",
        "sidebarForeground": "#544d40",
        "sidebarPrimary": "#733d9a",
        "sidebarPrimaryForeground": "#ffffff",
        "sidebarAccent": "#e4e7f2",
        "sidebarAccentForeground": "#544d40",
        "sidebarBorder": "rgba(84,77,64,0.10)",
        "sidebarRing": "#733d9a"
      },
      "terminal": {
        "background": "#f8fafe",
        "foreground": "#544d40",
        "cursor": "#0f5ba2",
        "cursorAccent": "#f8fafe",
        "selection": "rgba(31,170,158,0.18)",
        "ansi": [
          "#f8fafe", "#1faa9e", "#733d9a", "#2e70ad",
          "#b55a0f", "#3e9d21", "#bd4c3d", "#544d40",
          "#b0a999", "#009e91", "#5a1f8a", "#0f5ba2",
          "#b23b00", "#218c00", "#b32e1f", "#000000"
        ]
      }
    }
  }
}
```

---

### Berlin — Greyscale

**Background:** `#000000` (UI) / **terminal:** `#000000` — monochrome, high contrast

```json
{
  "id": "berlin",
  "name": "Berlin",
  "author": "xscriptor-terax-themes",
  "description": "Greyscale monochrome. Brutalist, minimal, distraction-free.",
  "editorTheme": { "light": "github-light" },
  "variants": {
    "dark": {
      "colors": {
        "background": "#000000",
        "foreground": "#ffffff",
        "card": "#111111",
        "cardForeground": "#ffffff",
        "popover": "#111111",
        "popoverForeground": "#ffffff",
        "primary": "#cccccc",
        "primaryForeground": "#000000",
        "secondary": "#1a1a1a",
        "secondaryForeground": "#ffffff",
        "muted": "#1a1a1a",
        "mutedForeground": "#999999",
        "accent": "#1a1a1a",
        "accentForeground": "#ffffff",
        "destructive": "#999999",
        "border": "rgba(255,255,255,0.12)",
        "input": "rgba(255,255,255,0.16)",
        "ring": "#dddddd",
        "sidebar": "#0a0a0a",
        "sidebarForeground": "#ffffff",
        "sidebarPrimary": "#dddddd",
        "sidebarPrimaryForeground": "#000000",
        "sidebarAccent": "#1a1a1a",
        "sidebarAccentForeground": "#ffffff",
        "sidebarBorder": "rgba(255,255,255,0.12)",
        "sidebarRing": "#dddddd"
      },
      "terminal": {
        "background": "#000000",
        "foreground": "#ffffff",
        "cursor": "#ffffff",
        "cursorAccent": "#000000",
        "selection": "rgba(255,255,255,0.20)",
        "ansi": [
          "#000000", "#999999", "#bbbbbb", "#dddddd",
          "#888888", "#aaaaaa", "#cccccc", "#ffffff",
          "#333333", "#bbbbbb", "#dddddd", "#ffffff",
          "#aaaaaa", "#cccccc", "#eeeeee", "#ffffff"
        ]
      }
    }
  }
}
```

---

### London — Light Greyscale

**Background:** `#ffffff` — pure white with grey scale

```json
{
  "id": "london",
  "name": "London",
  "author": "xscriptor-terax-themes",
  "description": "Clean white with grey gradients. Minimal and bright.",
  "editorTheme": { "light": "github-light" },
  "variants": {
    "light": {
      "colors": {
        "background": "#ffffff",
        "foreground": "#333333",
        "card": "#fafafa",
        "cardForeground": "#333333",
        "popover": "#fafafa",
        "popoverForeground": "#333333",
        "primary": "#555555",
        "primaryForeground": "#ffffff",
        "secondary": "#f0f0f0",
        "secondaryForeground": "#333333",
        "muted": "#f0f0f0",
        "mutedForeground": "#777777",
        "accent": "#f0f0f0",
        "accentForeground": "#333333",
        "destructive": "#888888",
        "border": "rgba(51,51,51,0.10)",
        "input": "rgba(51,51,51,0.14)",
        "ring": "#333333",
        "sidebar": "#f8f8f8",
        "sidebarForeground": "#333333",
        "sidebarPrimary": "#444444",
        "sidebarPrimaryForeground": "#ffffff",
        "sidebarAccent": "#e8e8e8",
        "sidebarAccentForeground": "#333333",
        "sidebarBorder": "rgba(51,51,51,0.10)",
        "sidebarRing": "#333333"
      },
      "terminal": {
        "background": "#ffffff",
        "foreground": "#333333",
        "cursor": "#333333",
        "cursorAccent": "#ffffff",
        "selection": "rgba(51,51,51,0.15)",
        "ansi": [
          "#ffffff", "#333333", "#444444", "#555555",
          "#666666", "#777777", "#888888", "#333333",
          "#333333", "#444444", "#555555", "#666666",
          "#777777", "#888888", "#999999", "#aaaaaa"
        ]
      }
    }
  }
}
```

---

## Installation

### Manual Installation (individual files)

All 12 `.terax-theme` files are in the `themes/` directory of this repo. Copy them to the Terax themes folder:

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

**Windows (CMD):**
```cmd
copy themes\*.terax-theme %APPDATA%\com.terax.app\themes\
```

| Platform | Themes Directory |
|----------|-----------------|
| **Linux** | `~/.config/com.terax.app/themes/` |
| **macOS** | `~/Library/Application Support/com.terax.app/themes/` |
| **Windows** | `%APPDATA%\com.terax.app\themes\` |

After placing the files, restart Terax. The themes will appear under **Settings → Appearance → Theme**.

### One-Line Remote Install

**Linux & macOS:**
```bash
curl -fsSL https://raw.githubusercontent.com/<user>/<repo>/main/install-terax-themes.sh | bash
```

**Windows (PowerShell):**
```powershell
irm https://raw.githubusercontent.com/<user>/<repo>/main/install-terax-themes.ps1 | iex
```

---

## Theme Format Reference

Each `.terax-theme` JSON file follows this schema:

```json
{
  "id": "kebab-case-id",        // required, a-z 0-9 and hyphens
  "name": "Display Name",       // required
  "author": "Author Name",      // optional
  "description": "...",         // optional
  "editorTheme": {              // optional, CodeMirror themes
    "dark": "atomone",
    "light": "xcode-light"
  },
  "variants": {                 // at least one variant required
    "dark": {
      "colors": { /* 25 UI color tokens */ },
      "terminal": {
        "background": "#...",
        "foreground": "#...",
        "cursor": "#...",
        "cursorAccent": "#...",
        "selection": "rgba(...)",
        "ansi": [/* 16 hex colors */]
      }
    },
    "light": { /* same format */ }
  }
}
```

Valid editor theme names: `atomone`, `aura`, `copilot`, `github-dark`, `github-light`, `gruvbox-dark`, `nord`, `tokyo-night`, `xcode-dark`, `xcode-light`.
