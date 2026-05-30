# Samurai Design System -- Component Patterns

This documents the actual component patterns used in the Samurai frontend, based on the Nothing Design philosophy.

---

## 1. COMPONENT ARCHITECTURE RULES

### 1.1 Standalone Components (Mandatory)

All components are Angular standalone. No NgModules. Import what you need:

```typescript
@Component({
  selector: 'app-my-component',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './my.component.html',
  styleUrls: ['./my.component.scss']
})
```

### 1.2 Communication Pattern

- **Parent → Child:** `@Input()` bindings
- **Child → Parent:** `@Output()` EventEmitter
- **No global state:** State lives in feature-level components
- **No service injection** in reusable/dumb components

### 1.3 Template Rendering

Use `*ngIf` for conditional rendering. Use `*ngFor` with `trackBy` where possible.

### 1.4 Change Detection for WebSockets

For components receiving WebSocket data streams, inject `ChangeDetectorRef` and call `this.cdr.detectChanges()` after updating properties:

```typescript
constructor(private cdr: ChangeDetectorRef) {}
// After setting data:
this.cdr.detectChanges();
```

---

## 2. SIDEBAR NAVIGATION

### HTML Structure (app.component.html)
```html
<nav class="sidebar">
  <div class="brand">
    <h1 class="t-heading">SAMURAI</h1>
    <span class="t-label">XWA - MODULE</span>
  </div>
  <ul class="nav-links">
    <li><a routerLink="/scanner" routerLinkActive="active" class="t-label">01 // SCANNER</a></li>
    <!-- ... -->
  </ul>
  <div class="sidebar-footer">
    <!-- Theme toggle, social links, version, dot-grid -->
  </div>
</nav>
```

### SCSS Rules
- Width: 250px fixed, border-right: `1px solid var(--border-visible)`
- Background: `var(--surface)`
- Nav links: `padding: var(--space-lg) var(--space-xl)`, border-bottom divider
- Active link: `background-color: var(--black)`, `border-left: 2px solid var(--interactive)`
- Labels: Space Mono, ALL CAPS

### Adding a New Nav Item
1. Add `<li>` with `<a routerLink="/newroute" routerLinkActive="active" class="t-label">05 // NEW</a>` to `app.component.html`
2. Add route to `app.routes.ts` with `loadComponent`
3. Create feature folder under `features/`

---

## 3. SECTION HEADERS

Every feature page starts with a standard header:

```html
<header class="section-header">
  <div>
    <h1 class="t-heading">PAGE_TITLE</h1>
    <span class="t-label">DESCRIPTIVE_SUBTITLE</span>
  </div>
</header>
```

SCSS:
```scss
.section-header {
  border-bottom: 1px solid var(--border);
  padding-bottom: var(--space-md);
  margin-bottom: var(--space-xl);
}
```

---

## 4. BUTTONS

### Export Action Buttons (Most Common Pattern)

```html
<button class="btn-reset export-btn" type="button" (click)="action()" aria-label="Description">
  <svg class="export-icon" xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true" focusable="false">
    <!-- SVG path data -->
  </svg>
  <span>LABEL</span>
</button>
```

SCSS:
```scss
.export-btn {
  display: inline-flex;
  align-items: center;
  gap: 6px;
  border: 1px solid var(--border-visible);
  background-color: transparent;
  color: var(--text-secondary);
  padding: var(--space-sm) var(--space-md);
  font-family: var(--font-data);
  font-size: var(--label);
  min-height: 40px;
  cursor: pointer;
  transition: all 0.2s ease;

  .export-icon {
    width: 16px;
    height: 16px;
    fill: currentColor;
    transition: color 0.2s ease;
    flex-shrink: 0;
  }

  &:hover {
    color: #FFD700;
    border-color: #FFD700;
  }

  &:disabled {
    opacity: 0.4;
    cursor: not-allowed;
  }
}
```

### Destructive/Delete Buttons

```html
<button type="button" class="btn-sm destructive" (click)="deleteAction()">DELETE</button>
```

SCSS:
```scss
.btn-sm {
  background-color: transparent;
  color: var(--text-primary);
  border: 1px solid var(--border-visible);
  font-family: var(--font-data);
  font-size: var(--body-sm);
  cursor: pointer;

  &.destructive:hover {
    background-color: var(--accent);
    color: var(--black);
    border-color: var(--accent);
  }
}
```

### Theme Toggle Button

```html
<button type="button" class="theme-toggle-btn" (click)="toggleTheme()">
  <svg><!-- moon/sun icon --></svg>
  <span>{{ label }}</span>
</button>
```

SCSS:
```scss
.theme-toggle-btn {
  display: inline-flex;
  align-items: center;
  gap: var(--space-sm);
  border: 1px solid var(--border-visible);
  background: var(--surface-raised);
  color: var(--text-primary);
  padding: 0.45rem 0.7rem;
  font-family: var(--font-data);
  font-size: var(--caption);
  letter-spacing: 0.08em;
  text-transform: uppercase;
  cursor: pointer;
  transition: all 0.2s ease;

  &:hover {
    opacity: 1;
    color: var(--success);
    border-color: var(--success);
  }
}
```

---

## 5. PANELS / CARDS

Standard container for feature content sections:

```html
<section class="panel">
  <!-- content -->
</section>
```

SCSS:
```scss
.panel {
  padding: var(--space-lg);
  border: 1px solid var(--border-visible);
  background-color: var(--surface);
  display: flex;
  flex-direction: column;
  gap: var(--space-md);
}
```

---

## 6. INPUTS

### Text Input (Underline Style)

```html
<label class="t-label" for="input-id">LABEL</label>
<input type="text" id="input-id" [(ngModel)]="value" class="input-field">
```

SCSS:
```scss
.input-field {
  background: transparent;
  border: none;
  border-bottom: 1px solid var(--border-visible);
  color: var(--text-primary);
  font-family: var(--font-data);
  font-size: var(--body);
  padding: var(--space-sm) 0;

  &:focus {
    outline: none;
    border-bottom-color: var(--text-primary);
  }
}
```

### Select/Dropdown

```html
<select [(ngModel)]="selected" class="input-field">
  <option *ngFor="let opt of options" [value]="opt.value">{{opt.label}}</option>
</select>
```

---

## 7. STATUS INDICATORS

### Status Text
```html
<span class="t-label badge" [ngClass]="status === 'COMPLETED' ? 'text-success' : 'text-warning'">[STATUS]</span>
```

### Severity Dots
```scss
.severity-dot {
  width: 10px;
  height: 10px;
  border-radius: 50%;
  &.high { background-color: var(--accent); }
  &.medium { background-color: var(--warning); }
  &.low { background-color: var(--success); }
  &.info { background-color: var(--interactive); }
  &.critical { background-color: var(--accent); }
}
```

---

## 8. LOADING STATE

Never use skeleton screens. Use text-based loading:

```html
<div *ngIf="isLoading" class="t-label">Loading database...</div>
<div *ngIf="!isLoading && items.length === 0" class="empty-state t-label">
  [ NO DATA AVAILABLE ]
</div>
```

---

## 9. LAYOUT GRIDS

### Dashboard Grid (2-column with sidebar)
```scss
.dashboard-grid {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: var(--space-xl);

  &.archive-grid {
    grid-template-columns: 350px 1fr;  // For list+detail layouts
  }
}
```

### Export Actions Row
```scss
.export-actions {
  display: flex;
  gap: var(--space-sm);
  justify-content: flex-end;
  flex-wrap: wrap;

  @media (max-width: 900px) {
    justify-content: center;
  }
}
```

---

## 10. ACCORDION (Details/Summary)

```html
<details class="nothing-accordion">
  <summary>
    <span class="t-label">HEADER</span>
  </summary>
  <div class="accordion-content">
    <!-- Content -->
  </div>
</details>
```

```scss
.nothing-accordion {
  border: 1px solid var(--border-visible);
  background-color: var(--black);
  margin-bottom: var(--space-sm);

  summary {
    padding: var(--space-md);
    cursor: pointer;
    display: flex;
    align-items: center;
    gap: var(--space-md);
    list-style: none;

    &:hover { background-color: var(--surface-raised); }
    &::-webkit-details-marker { display: none; }
  }

  .accordion-content {
    border-top: 1px solid var(--border-visible);
    padding: var(--space-md);
  }
}
```

---

## 11. API URL PATTERN

All HTTP requests use the current hostname with port 8000:

```typescript
this.http.get<Type[]>(`http://${window.location.hostname}:8000/api/path`).subscribe({...});
```

WebSocket connections use the same pattern:
```typescript
new WebSocket(`ws://${window.location.hostname}:8000/api/endpoint/live?param=value`);
```
