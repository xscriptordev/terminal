---
name: samurai-design
description: Design system and architecture documentation for the Samurai cybersecurity platform. Use when building or modifying any UI component, backend endpoint, or feature module in Samurai.
version: 1.0.0
allowed-tools: [Read, Write, Edit, Glob, Grep, Bash]
---

# Samurai Design System & Architecture

Samurai is a cybersecurity analysis platform built with an Angular 21 frontend and FastAPI backend. The design follows the Nothing Design System philosophy: monochromatic, typographically driven, information-dense without clutter.

---

## 1. DESIGN PHILOSOPHY

- **Subtract, don't add.** Every element must earn its pixel. Default to removal.
- **Structure is ornament.** Expose the grid, the data, the hierarchy itself.
- **Monochrome is the canvas.** Color is an event, not a default -- except when encoding data status.
- **Type does the heavy lifting.** Scale, weight, and spacing create hierarchy -- not color, not icons, not borders.
- **Both modes are first-class.** Dark mode: OLED black. Light mode: warm off-white.
- **Industrial warmth.** Technical and precise, but never cold. A human hand should be felt.

---

## 2. FONT DISCIPLINE

Per screen, use maximum:
- **2 font families** (Space Grotesk + Space Mono. Doto only for hero moments.)
- **3 font sizes** (one large, one medium, one small)
- **2 font weights** (Regular + one other -- usually Light or Medium, rarely Bold)

### Font Assignment (Fixed Rules):
| Context | Font | Size | Weight | Letter-Spacing |
|---------|------|------|--------|----------------|
| Hero numbers, display | Doto | 48px–72px | Variable | -0.03em |
| Headings | Space Grotesk | 24px | Regular | -0.01em |
| Body text | Space Grotesk | 16px | Light/Regular | 0 |
| UI Labels | Space Mono | 11px | Regular | 0.08em ALL CAPS |
| Data/Numbers | Space Mono | 14–16px | Regular | 0 |
| Terminal/logs | Space Mono | 13px | Regular | 0 |

---

## 3. FEATURE-DRIVEN ARCHITECTURE

See `references/architecture-overview.md` for the full system architecture.

The frontend follows a strict feature-driven structure:
```
frontend/src/app/
├── app.component.ts        # Root shell: sidebar nav + router-outlet
├── app.routes.ts           # Lazy-loaded routes (4 features)
├── app.config.ts           # HttpClient + Router providers
├── services/
│   └── theme.service.ts    # Dark/Light mode with Angular Signals
└── features/
    ├── scanner/            # Nmap port scanning
    ├── recon/              # Web reconnaissance
    ├── vulnerabilities/    # DAST vulnerability crawling
    └── history/            # Scan history & archive
```

Each feature is self-contained with its own components, models, and services.

---

## 4. COMPONENT PATTERNS

See `references/component-patterns.md` for detailed component specifications.

Key patterns to follow:
1. **All components are standalone** (Angular 21, no NgModules).
2. **Input/Output only** -- no service injection in reusable components. Use `@Input()` for data, `@Output()` EventEmitter for actions.
3. **State lives in parent** -- feature components hold state, child components are pure rendering.
4. **ChangeDetectorRef.detectChanges()** for WebSocket-driven updates.
5. **No global state library** -- state is managed locally per feature.

---

## 5. BACKEND PATTERNS

See `references/backend-patterns.md` for API and service architecture.

- **WebSocket-first:** All long-running operations (scanning, crawling, recon) use WebSockets for real-time streaming.
- **REST for CRUD:** Short-lived operations (list, get, delete) use standard REST.
- **DB Dependency Injection:** All endpoints use `db: Session = Depends(get_db)`.
- **Subprocess Integration:** External tools (Nmap, SQLMap, Nuclei) run as OS subprocesses via `asyncio.create_subprocess_exec`.
- **Module Orchestration:** Recon modules are pluggable async functions conforming to a `ModuleRunner` callable type.

---

## 6. DATABASE SCHEMA

See `references/database-schema.md` for complete schema documentation.

Three tables:
- **scans** -- Scan records (target, status, type, timestamp)
- **discovered_links** -- URLs discovered during crawling (FK → scans)
- **findings** -- Security findings/vulnerabilities (FK → scans, FK → links)

With cascade delete relationships: deleting a scan removes all its links and findings.

---

## 7. EXPORT SYSTEM

See `references/export-patterns.md` for full export architecture.

Exports are implemented client-side using:
- **CSV:** Manual string building with CSV escaping
- **JSON:** `JSON.stringify(payload, null, 2)`
- **PDF:** jsPDF + jspdf-autotable, landscape A4, dark-themed
- **Binary:** pako gzip compression of JSON payload

Each feature has its own export-actions component with 4 buttons: CSV, JSON, PDF, BIN.

---

## 8. ANTI-PATTERNS -- WHAT TO NEVER DO

- No gradients in UI chrome
- No shadows. No blur. Flat surfaces, border separation.
- No skeleton loading screens. Use `[LOADING...]` text.
- No toast popups. Use inline status text: `[SAVED]`, `[ERROR: ...]`
- No sad-face illustrations, cute mascots, or multi-paragraph empty states
- No zebra striping in tables
- No filled icons, multi-color icons, or emoji as UI
- No parallax, scroll-jacking, or gratuitous animation
- No spring/bounce easing. Use subtle ease-out only.
- No border-radius > 16px on cards. Buttons are pill (999px) or technical (4-8px).

---

## 9. REFERENCE FILES

For detailed specifications:

- **`references/architecture-overview.md`** -- System architecture, Docker services, API endpoints, tech stack
- **`references/design-tokens.md`** -- CSS custom properties, type scale, color system (dark + light), spacing, motion
- **`references/component-patterns.md`** -- Component structure, button variants, inputs, tables, navigation, export actions
- **`references/backend-patterns.md`** -- API routes, WebSocket endpoints, service layer, database interaction
- **`references/database-schema.md`** -- ORM models, relationships, cascade rules, query patterns
- **`references/export-patterns.md`** -- Client-side export architecture, format implementations, encryption patterns
