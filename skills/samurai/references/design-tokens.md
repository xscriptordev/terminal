# Samurai Design System -- Design Tokens

This documents the exact CSS custom properties used in `/frontend/src/styles.scss`.

---

## 1. TYPOGRAPHY

### Font Stack

| Role | Font | Fallback | CSS |
|------|------|----------|-----|
| **Display** | `"Doto"` | `"Space Mono", monospace` | `--font-display` |
| **Body / UI** | `"Space Grotesk"` | `"DM Sans", system-ui, sans-serif` | `--font-body` |
| **Data / Labels** | `"Space Mono"` | `"JetBrains Mono", "SF Mono", monospace` | `--font-data` |

### Type Scale

| Token | Size | Line Height | Letter Spacing | Use |
|-------|------|-------------|----------------|-----|
| `--display-xl` | 72px | 1.0 | -0.03em | Hero numbers |
| `--display-lg` | 48px | 1.05 | -0.02em | Section heroes |
| `--display-md` | 36px | 1.1 | -0.02em | Page titles |
| `--heading` | 24px | 1.2 | -0.01em | Section headings |
| `--subheading` | 18px | 1.3 | 0 | Subsections |
| `--body` | 16px | 1.5 | 0 | Body text |
| `--body-sm` | 14px | 1.5 | 0.01em | Secondary body |
| `--caption` | 12px | 1.4 | 0.04em | Timestamps, footnotes |
| `--label` | 11px | 1.2 | 0.08em | ALL CAPS monospace labels |

### Typography Utility Classes

| Class | Font | Size | Weight |
|-------|------|------|--------|
| `.t-display-xl` | Doto | 72px | Variable, tight tracking |
| `.t-display-lg` | Doto | 48px | Variable |
| `.t-display-md` | Doto | 36px | Variable |
| `.t-heading` | Space Grotesk | 24px | Regular |
| `.t-label` | Space Mono | 11px | ALL CAPS |
| `.t-data` | Space Mono | inherit | Regular |

### Typographic Rules (Hard Constraints)
- **Doto:** 36px+ only, tight tracking, never for body text
- **Labels:** Always Space Mono, ALL CAPS, 0.08em spacing, 11px
- **Data/Numbers:** Always Space Mono
- **Hierarchy:** display (Doto) > heading (Space Grotesk) > label (Space Mono caps) > body (Space Grotesk)

---

## 2. COLOR SYSTEM

### Primary Palette (Dark Mode -- Default)

| Token | Hex | Role |
|-------|-----|------|
| `--black` | `#000000` | Primary background (OLED) |
| `--surface` | `#111111` | Elevated surfaces, cards |
| `--surface-raised` | `#1A1A1A` | Secondary elevation |
| `--border` | `#222222` | Subtle dividers (decorative only) |
| `--border-visible` | `#333333` | Intentional borders, wireframe lines |
| `--text-disabled` | `#666666` | Disabled text |
| `--text-secondary` | `#999999` | Labels, captions, metadata |
| `--text-primary` | `#E8E8E8` | Body text |
| `--text-display` | `#FFFFFF` | Headlines, hero numbers |

### Light Mode Overrides

| Token | Dark | Light |
|-------|------|-------|
| `--black` | `#000000` | `#F5F5F5` |
| `--surface` | `#111111` | `#FFFFFF` |
| `--surface-raised` | `#1A1A1A` | `#F0F0F0` |
| `--border` | `#222222` | `#E8E8E8` |
| `--border-visible` | `#333333` | `#CCCCCC` |
| `--text-disabled` | `#666666` | `#999999` |
| `--text-secondary` | `#999999` | `#666666` |
| `--text-primary` | `#E8E8E8` | `#1A1A1A` |
| `--text-display` | `#FFFFFF` | `#000000` |
| `--interactive` | `#5B9BF6` | `#007AFF` |

Light mode is activated by adding class `.theme-light` to `<body>`.

### Accent & Status Colors (Identical Across Modes)

| Token | Hex | Usage |
|-------|-----|-------|
| `--accent` | `#D71921` | Destructive, urgent, active states |
| `--accent-subtle` | `rgba(215,25,33,0.15)` | Accent tint backgrounds |
| `--success` | `#4A9E5C` | Completed, connected |
| `--warning` | `#D4A843` | Caution, pending |
| `--error` | `#D71921` | Shares accent red |
| `--interactive` | `#5B9BF6` (dark) / `#007AFF` (light) | Links, picker values |

### Utility Classes for Colors
- `.text-accent` → `color: var(--accent)`
- `.text-success` → `color: var(--success)`
- `.text-warning` → `color: var(--warning)`
- `.bg-surface` → `background-color: var(--surface)`
- `.border-divider` → `border: 1px solid var(--border)`
- `.border-visible` → `border: 1px solid var(--border-visible)`

---

## 3. SPACING

### Spacing Scale (8px base)

| Token | Value | Use |
|-------|-------|-----|
| `--space-2xs` | 2px | Optical adjustments only |
| `--space-xs` | 4px | Icon-to-label gaps, tight padding |
| `--space-sm` | 8px | Component internal spacing |
| `--space-md` | 16px | Standard padding, element gaps |
| `--space-lg` | 24px | Group separation |
| `--space-xl` | 32px | Section margins |
| `--space-2xl` | 48px | Major section breaks |
| `--space-3xl` | 64px | Page-level vertical rhythm |
| `--space-4xl` | 96px | Hero breathing room |

### Spacing as Meaning
```
Tight (4-8px)   = "These belong together"
Medium (16px)   = "Same group, different items"
Wide (32-48px)  = "New group starts here"
Vast (64-96px)  = "This is a new context"
```

---

## 4. MOTION & INTERACTION

- **Duration:** 150-250ms micro, 300-400ms transitions
- **Easing:** `cubic-bezier(0.25, 0.1, 0.25, 1)` -- subtle ease-out. No spring/bounce.
- **Hover:** border/text brightens. No scale, no shadows.
- **Theme transition:** `cubic-bezier(0.16, 1, 0.3, 1)` over 260ms on color properties
- **Route animation:** `fadeInSlideUp` 400ms, opacity + translateY(10px → 0)

---

## 5. DOT-MATRIX MOTIF

Two utility classes for dot-grid backgrounds:

```css
.dot-grid {
  background-image: radial-gradient(circle, var(--border-visible) 1px, transparent 1px);
  background-size: 16px 16px;
}
.dot-grid-subtle {
  background-image: radial-gradient(circle, var(--border) 0.5px, transparent 0.5px);
  background-size: 12px 12px;
}
```

- `dot-grid-subtle` is used on the main content area background
- `dot-grid` is used for decorative surface treatments
- Never use dot-grid as container border or button style

---

## 6. EXPORT BUTTON GOLD

Export buttons use a specific hover color across the entire application:
- Hover text/border: `#FFD700` (gold)
- This is a project-level convention for export/download actions

---

## 7. RESPONSIVE BREAKPOINTS

| Breakpoint | Target |
|-----------|--------|
| 980px | Sidebar collapses to top bar, nav becomes 2-column grid |
| 900px | Export actions center-align |
| 640px | Nav becomes single column, main padding reduces |
