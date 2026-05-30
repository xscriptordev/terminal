# Samurai Design System -- Architecture Overview

This documents the complete system architecture of the Samurai cybersecurity platform.

---

## 1. SYSTEM DIAGRAM

```
┌─────────────────────────────────────────────────────────────────┐
│                       DOCKER COMPOSE                            │
│  ┌───────────────┐  ┌───────────────┐  ┌───────┐  ┌─────────┐  │
│  │   FRONTEND    │  │    BACKEND    │  │ REDIS │  │   DB    │  │
│  │  Angular 21   │  │   FastAPI     │  │alpine │  │ PG 15   │  │
│  │   :4200       │──│   :8000       │  │:6379  │  │ :5432   │  │
│  │   ng serve    │  │   uvicorn     │──│        │──│         │  │
│  │   (HMR)       │  │   (reload)    │  │        │  │         │  │
│  └───────────────┘  └───────────────┘  └───────┘  └─────────┘  │
│         │                    │                                   │
│         └──── WebSocket ────┘ (3 WS endpoints)                  │
│              + REST API (5 HTTP endpoints)                       │
└─────────────────────────────────────────────────────────────────┘
```

---

## 2. TECH STACK

### Frontend
| Technology | Version | Purpose |
|---|---|---|
| Angular (standalone) | 21.2.8 | SPA framework |
| TypeScript | 5.9.3 | Language |
| SCSS | - | Styling |
| RxJS | 7.8.1 | Reactive streams |
| jsPDF + jspdf-autotable | 4.2.1 / 5.0.7 | PDF export generation |
| pako | 2.1.0 | gzip for binary exports |

### Backend
| Technology | Version | Purpose |
|---|---|---|
| FastAPI | 0.105.0 | REST + WebSocket API framework |
| Uvicorn | 0.24.0 | ASGI server |
| SQLAlchemy | 2.0.23 | ORM + session management |
| PostgreSQL | 15-alpine | Primary database |
| cryptography | 42.0.2 | AES encryption (available) |
| Playwright | 1.52.0 | Headless browser analysis |
| httpx | 0.25.2 | Async HTTP client |
| requests | 2.31.0 | Sync HTTP for probes |
| BeautifulSoup4 | 4.12.2 | HTML parsing |
| dnspython | 2.5.0 | DNS resolution |

### Infrastructure
| Component | Technology |
|---|---|
| Containerization | Docker Compose (4 services) |
| Dev mode | ng serve + HMR, uvicorn --reload |
| External tools | Nmap, SQLMap, Nuclei (in container) |

---

## 3. API ENDPOINTS

### REST Endpoints

| Method | Path | Description |
|---|---|---|
| `GET` | `/` | Health check |
| `GET` | `/api/scans` | List all scans (ordered by ID desc) |
| `GET` | `/api/scans/{scan_id}` | Get scan with findings + links (eager loaded) |
| `DELETE` | `/api/scans/{scan_id}` | Delete scan + cascade |
| `POST` | `/api/scan/cancel/{scan_id}` | Cancel running scan |
| `GET` | `/api/database/export/raw` | Download full database as JSON |
| `POST` | `/api/database/export/encrypted` | Download encrypted database dump |

### WebSocket Endpoints

| Path | Parameters | Engine |
|---|---|---|
| `/api/scan/live` | target, profile, timeout, web_scan, collect_contacts, scan_unsanitized, max_pages | `scanner.py` - Nmap + web surface scan |
| `/api/vuln/live` | target, modules, auth_mode, auth_bearer, auth_user, auth_pass, auth_cookie | `crawler.py` - DAST vulnerability crawler |
| `/api/recon/live` | target, recon_types, timeout | `recon/orchestrator.py` - Web recon modules |

---

## 4. FRONTEND ROUTES

| Path | Component | Description |
|---|---|---|
| `/scanner` | ScannerComponent | Nmap port scanning dashboard |
| `/recon` | ReconComponent | Web reconnaissance dashboard |
| `/vulnerabilities` | VulnerabilitiesComponent | DAST vulnerability crawler |
| `/history` | HistoryComponent | Scan history archive |
| `/export` | ExportDatabaseComponent | Full database export |
| `/` | Redirect → `/scanner` | Default route |

All routes use lazy loading via `loadComponent`.

---

## 5. DIRECTORY STRUCTURE

```
samurai/
├── docs/                              # Documentation
│   ├── manual.md                      # Dev & production setup
│   ├── python-libraries.md            # Backend dependency inventory
│   ├── ui-architecture.md             # UI architecture philosophy
│   ├── uses/                          # Use case docs
│   │   └── dast.md
│   └── skills/                        # AI-consumable design docs (THIS)
│       ├── SKILL.md
│       └── references/
│           ├── design-tokens.md
│           ├── component-patterns.md
│           ├── backend-patterns.md
│           ├── database-schema.md
│           ├── export-patterns.md
│           └── architecture-overview.md
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── app/
│       ├── main.py                    # FastAPI app + all routes
│       ├── database.py                # SQLAlchemy engine + session
│       ├── models.py                  # ORM models
│       ├── scanner.py                 # Nmap + web surface scan engine
│       ├── crawler.py                 # DAST vulnerability crawler
│       ├── db_exporter.py             # Database export engine (NEW)
│       └── recon/                     # Web recon subsystem
│           ├── orchestrator.py
│           ├── target.py
│           ├── logger.py
│           ├── types.py
│           └── modules/
├── frontend/
│   ├── Dockerfile
│   ├── nginx.conf
│   ├── angular.json
│   ├── package.json
│   └── src/
│       ├── main.ts
│       ├── index.html
│       ├── styles.scss                # Nothing Design tokens
│       └── app/
│           ├── app.component.ts/html/scss
│           ├── app.config.ts
│           ├── app.routes.ts
│           ├── services/
│           │   └── theme.service.ts
│           └── features/
│               ├── scanner/
│               ├── recon/
│               ├── vulnerabilities/
│               ├── history/
│               └── export-database/   # (NEW)
└── docker-compose.yml
```

---

## 6. DATA FLOW

### Scanning Flow (WebSocket)
1. User enters target + config → clicks "Start Scan"
2. Frontend opens WebSocket to `/api/{type}/live?target=...`
3. Backend creates `Scan` record → sends `[SCAN_META] scan_id={id}`
4. Backend runs tool/analysis → streams stdout + findings over WebSocket
5. Findings stored as `Finding` records linked to the `Scan`
6. On completion: scan status = COMPLETED, `[done]` message sent

### History/Replay Flow
1. User navigates to `/history`
2. Frontend GETs `/api/scans` → lists all scans
3. Clicking a scan navigates to appropriate feature with `scanId` query param
4. Feature page detects `scanId` → GETs `/api/scans/{id}` → rehydrates UI from DB

### Export Flow (Current)
1. Feature component collects all scan data into a payload object
2. User clicks export button → feature calls format function
3. JS creates Blob → creates download URL → triggers browser download
4. All export logic is client-side, no backend involved

### Database Export Flow (NEW)
1. User navigates to `/export`
2. Chooses direct export → backend queries all scans+findings+links → returns JSON file
3. OR chooses encrypted export → enters password → backend encrypts with AES → returns .bin file
