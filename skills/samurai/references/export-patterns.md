# Samurai Design System -- Export Patterns

This documents the export system architecture, both existing client-side exports and the new database export feature.

---

## 1. CLIENT-SIDE EXPORT (Existing)

### Architecture
All existing exports are **client-side only** -- no backend involved. The browser generates the file and triggers a download via Blob + URL.createObjectURL.

### Export Component Pattern
Each feature has its own `export-actions` component:

```
features/scanner/components/export-actions/     → scanner-export-actions.component.*
features/recon/components/export-actions/        → recon-export-actions.component.*
features/vulnerabilities/.../findings-export-actions/ → findings-export-actions.component.*
```

Each follows the same template:
- 4 buttons: CSV, JSON, PDF, BIN
- Component receives conditions via `@Input()` (e.g., `hasExports`, `findingsCount`)
- Emits events via `@Output()` (e.g., `exportCsv`, `exportJson`, `exportPdf`, `exportBinary`)
- Parent feature component handles the actual export logic

### Button HTML
```html
<button class="btn-reset export-btn" type="button" (click)="exportJson.emit()" aria-label="Export as JSON">
  <svg class="export-icon" width="16" height="16" viewBox="0 0 16 16" aria-hidden="true">
    <!-- JSON icon path -->
  </svg>
  <span>EXPORT JSON</span>
</button>
```

Note: Each format has a distinct SVG icon (different paths).

### Button SCSS (Identical across all export-actions)
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
    flex-shrink: 0;
  }

  &:hover { color: #FFD700; border-color: #FFD700; }
  &:disabled { opacity: 0.4; cursor: not-allowed; }
}
```

### Parent Feature Export Implementation

**JSON Export** (simplest):
```typescript
exportAsJson(payload: any, filename: string): void {
  const json = JSON.stringify(payload, null, 2);
  const blob = new Blob([json], { type: 'application/json' });
  this.downloadBlob(blob, `${filename}.json`);
}
```

**CSV Export:**
```typescript
exportAsCsv(rows: any[], headers: string[], filename: string): void {
  const escape = (v: string) => `"${String(v).replace(/"/g, '""')}"`;
  const csv = [headers.join(','), ...rows.map(r => headers.map(h => escape(r[h])).join(','))].join('\n');
  const blob = new Blob([csv], { type: 'text/csv' });
  this.downloadBlob(blob, `${filename}.csv`);
}
```

**PDF Export** (uses jsPDF + jspdf-autotable):
```typescript
import { jsPDF } from 'jspdf';
import autoTable from 'jspdf-autotable';

exportAsPdf(rows: any[], headers: string[], title: string, filename: string): void {
  const doc = new jsPDF('landscape', 'mm', 'a4');
  doc.setFillColor(0, 0, 0);
  doc.rect(0, 0, 297, 210, 'F');
  doc.setTextColor(255, 255, 255);
  // Title, metadata, table...
  doc.save(`${filename}.pdf`);
}
```

**Binary Export** (uses pako for gzip):
```typescript
import * as pako from 'pako';

exportAsBinary(payload: any, filename: string): void {
  const json = JSON.stringify(payload, null, 2);
  const compressed = pako.gzip(json);
  const blob = new Blob([compressed], { type: 'application/octet-stream' });
  this.downloadBlob(blob, `${filename}.bin`);
}
```

**Universal Download Helper:**
```typescript
private downloadBlob(blob: Blob, filename: string): void {
  const url = URL.createObjectURL(blob);
  const anchor = document.createElement('a');
  anchor.href = url;
  anchor.download = filename;
  anchor.click();
  URL.revokeObjectURL(url);
}
```

---

## 2. DATABASE EXPORT (New Feature)

### Backend Endpoints

**GET `/api/database/export/raw`** -- Returns full database dump as downloadable JSON:
```json
{
  "export_metadata": {
    "exported_at": "2026-05-30T12:00:00Z",
    "samurai_version": "2.5.0",
    "scan_count": 15,
    "finding_count": 142,
    "link_count": 89
  },
  "scans": [
    {
      "id": 1,
      "domain_target": "example.com",
      "status": "COMPLETED",
      "scan_type": "crawler",
      "created_at": "2026-05-29T10:00:00Z",
      "findings": [...],
      "discovered_links": [...]
    }
  ]
}
```

**POST `/api/database/export/encrypted`** -- Returns AES-encrypted JSON:
- Request body: `{ "password": "user-entered-password" }`
- Response: Binary file with AES-encrypted content
- Encryption: AES-256-GCM via PBKDF2 key derivation

### Frontend Feature

New page at `/export` accessible from sidebar `05 // EXPORT DB`.

Two modes:
1. **Direct export**: Single click downloads `samurai-database-export-{timestamp}.json`
2. **Encrypted export**: Enter password → submit → downloads `samurai-database-export-{timestamp}.bin.enc`

UI Layout:
- Left panel: Export mode selection + description
- Right panel: Action area (download button or password form)
- Export buttons follow the gold hover pattern

---

## 3. FILE NAMING CONVENTION

| Export Type | Filename Pattern |
|---|---|
| Scanner JSON | `samurai-scanner-{scanId}.json` |
| Recon JSON | `samurai-recon-{target}.json` |
| Findings JSON | `samurai-findings-scan-{scanId}.json` |
| DB Raw Export | `samurai-database-export-{YYYY-MM-DD}.json` |
| DB Encrypted | `samurai-database-export-{YYYY-MM-DD}.bin.enc` |
