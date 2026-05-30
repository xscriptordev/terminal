# Samurai Design System -- Backend Patterns

This documents the FastAPI backend architecture, conventions, and patterns used in Samurai.

---

## 1. API ENTRY POINT

File: `backend/app/main.py`

```python
from fastapi import FastAPI, Depends, WebSocket, WebSocketDisconnect, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

app = FastAPI(title="Samurai API", version="2.5.0")

@app.on_event("startup")
def init_database():
    database.wait_for_db()
    models.Base.metadata.create_all(bind=database.engine)

app.add_middleware(CORSMiddleware, allow_origins=["*"], ...)
```

### Conventions
- Version string: `"2.5.0"` (also in `app.component.html` footer and `ROADMAP.md`)
- CORS: wide open for development
- DB tables auto-created on startup (after waiting for DB availability)
- All routes are defined directly in `main.py`

---

## 2. DATABASE CONNECTION

File: `backend/app/database.py`

```python
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker, declarative_base

DB_USER = os.getenv("DB_USER", "postgres")
DB_PASS = os.getenv("DB_PASS", "postgres")
DB_HOST = os.getenv("DB_HOST", "db")
DB_NAME = os.getenv("DB_NAME", "samurai")

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}/{DB_NAME}"

engine = create_engine(DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def wait_for_db(max_retries=30, retry_delay=1.5):
    # Retries connection until DB is available
```

### Key Points
- `get_db()` is the FastAPI dependency for session injection
- `wait_for_db()` handles Docker startup ordering (DB may start after backend)
- `pool_pre_ping=True` ensures stale connections are detected

---

## 3. ORM MODELS

File: `backend/app/models.py`

See `database-schema.md` for complete schema. Key patterns:
- `Scan` is the root entity with cascade-delete relationships
- `Base` is imported from `database.py` (not directly from SQLAlchemy)
- Default `status` is `"RUNNING"`
- `created_at` uses `datetime.utcnow`
- `poc_payload` is unlimited-length String (formerly had a limit that was removed)

---

## 4. REST ENDPOINT PATTERNS

### Standard CRUD endpoint:
```python
@app.get("/api/resource")
def list_resource(db: Session = Depends(database.get_db)):
    items = db.query(models.Model).order_by(models.Model.id.desc()).all()
    return items

@app.get("/api/resource/{id}")
def get_resource(id: int, db: Session = Depends(database.get_db)):
    item = db.query(models.Model).filter(models.Model.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    return item

@app.delete("/api/resource/{id}")
def delete_resource(id: int, db: Session = Depends(database.get_db)):
    item = db.query(models.Model).filter(models.Model.id == id).first()
    if not item:
        raise HTTPException(status_code=404, detail="Not found")
    db.delete(item)
    db.commit()
    return {"status": "deleted", "id": id}
```

### Eager loading for relationships:
```python
scan = db.query(models.Scan)\
    .options(
        joinedload(models.Scan.findings),
        joinedload(models.Scan.discovered_links)
            .joinedload(models.DiscoveredLink.findings)
    )\
    .filter(models.Scan.id == scan_id)\
    .first()
```

---

## 5. WEBSOCKET ENDPOINT PATTERNS

### Standard WebSocket endpoint:
```python
@app.websocket("/api/endpoint/live")
async def websocket_endpoint(
    websocket: WebSocket,
    target: str,
    param1: str = "default",
    db: Session = Depends(database.get_db)
):
    await websocket.accept()
    try:
        # Create scan record
        scan_record = models.Scan(
            domain_target=target,
            status="RUNNING",
            scan_type="type_identifier"
        )
        db.add(scan_record)
        db.commit()
        db.refresh(scan_record)

        await websocket.send_text(f"[SCAN_META] scan_id={scan_record.id}")

        # Perform the actual work
        await perform_operation(target, websocket, db, ...)

        # Mark complete
        scan_record.status = "COMPLETED"
        db.commit()
        await websocket.send_text("[done] scan completed and saved to history")

    except WebSocketDisconnect:
        if scan_record:
            scan_record.status = "CANCELLED"
            db.commit()
    except Exception as e:
        if scan_record:
            scan_record.status = "ERROR"
            db.commit()
        await websocket.send_text(f"[!] CRITICAL ERROR: {str(e)}")
        await websocket.close()
```

### WebSocket Message Convention
- `[SCAN_META] scan_id={id}` -- First message, identifies the scan record
- `[...]` -- Bracket-prefixed log/status messages
- `[!] ...` -- Error messages
- `[done] ...` -- Completion message

---

## 6. ASYNCHRONOUS SERVICE LAYER

Long-running operations are async functions running in the WebSocket handler:

### Subprocess Execution Pattern
```python
process = await asyncio.create_subprocess_exec(
    "tool-name", *args,
    stdout=asyncio.subprocess.PIPE,
    stderr=asyncio.subprocess.STDOUT
)

async for line in process.stdout:
    decoded = line.decode("utf-8", errors="replace").rstrip()
    await websocket.send_text(decoded)
```

### Sync HTTP in Async Context
Synchronous `requests` calls are wrapped with `asyncio.to_thread()`:
```python
response = await asyncio.to_thread(requests.get, url, timeout=10)
```

### Module Orchestration
The recon system uses a pluggable module pattern:
```python
# Each module is a callable:
async def run_module(target: str, results: dict, logger: ReconStreamLogger):
    ...

# Orchestrator runs them sequentially:
for module_name in requested_modules:
    await run_module(target, all_results, logger)
```

---

## 7. ADDING A NEW ENDPOINT

1. If it's a long operation with streaming output → use WebSocket
2. If it's a quick CRUD operation → use REST
3. Add route in `main.py` following existing conventions
4. Use `db: Session = Depends(database.get_db)` for DB access
5. Follow error handling patterns (HTTPException for REST, try/except for WS)
6. Use the `[SCAN_META]`, `[done]`, `[!]` message conventions

---

## 8. NEW FILE EXPORT (Database Dump)

The database export is a new POST endpoint pattern:

```python
from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
import base64, os, json

@app.get("/api/database/export/raw")
def export_db_raw(db: Session = Depends(database.get_db)):
    # Query all data
    # Return StreamingResponse or FileResponse

@app.post("/api/database/export/encrypted")
def export_db_encrypted(payload: dict, db: Session = Depends(database.get_db)):
    password = payload.get("password", "")
    # Derive key from password
    # Encrypt database dump
    # Return encrypted file
```

---

## 9. ENVIRONMENT VARIABLES (Docker Compose)

```yaml
environment:
  REDIS_URL: redis://redis:6379/0
  DB_HOST: db
  DB_NAME: samurai
  DB_USER: postgres
  DB_PASS: postgres
```

Access in Python with:
```python
os.getenv("DB_HOST", "db")
```
