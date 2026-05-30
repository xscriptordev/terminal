# Samurai Design System -- Database Schema

This documents the PostgreSQL database schema used by Samurai.

---

## 1. ENTITY-RELATIONSHIP DIAGRAM

```
┌──────────┐          ┌──────────────────┐          ┌──────────┐
│  scans   │ 1───────*│ discovered_links  │ 1───────*│ findings │
│          │          │                  │          │          │
│ id (PK)  │          │ id (PK)          │          │ id (PK)  │
│ target   │          │ scan_id (FK)     │          │ scan_id  │
│ status   │          │ url              │          │ link_id  │
│ type     │          │ status_code      │          │ severity │
│ created  │          │ content_type     │          │ type     │
└──────────┘          └──────────────────┘          │ desc     │
      │                                              │ poc      │
      │ 1───────* (direct findings, link_id=NULL)   │ cvss     │
      └─────────────────────────────────────────────│          │
                                                     └──────────┘
```

A `Scan` can have:
- Direct `findings` (where `link_id` is NULL) -- e.g., open ports, global recon results
- `discovered_links` which each can have their own `findings` -- e.g., SQLi on a specific page

---

## 2. TABLE DEFINITIONS

### 2.1 `scans`

```python
class Scan(Base):
    __tablename__ = "scans"
    id = Column(Integer, primary_key=True, index=True)
    domain_target = Column(String, index=True)
    status = Column(String, default="RUNNING")
    created_at = Column(DateTime, default=datetime.utcnow)
    scan_type = Column(String, default="port_scan")
```

| Column | Type | Constraints | Notes |
|--------|------|------------|-------|
| `id` | Integer | PK, auto-increment, indexed | Scan identifier |
| `domain_target` | String(255) | Indexed | Target hostname/IP |
| `status` | String | Default: `RUNNING` | One of: RUNNING, COMPLETED, ERROR, CANCELLED |
| `created_at` | DateTime | Default: utcnow | Scan creation timestamp |
| `scan_type` | String | Default: `port_scan` | Type identifier: `port_scan:{profile}`, `crawler`, `web_recon` |

### 2.2 `discovered_links`

```python
class DiscoveredLink(Base):
    __tablename__ = "discovered_links"
    id = Column(Integer, primary_key=True, index=True)
    scan_id = Column(Integer, ForeignKey("scans.id", ondelete="CASCADE"))
    url = Column(String)
    status_code = Column(Integer, nullable=True)
    content_type = Column(String, nullable=True)
```

| Column | Type | Constraints | Notes |
|--------|------|------------|-------|
| `id` | Integer | PK, indexed | Link identifier |
| `scan_id` | Integer | FK → scans.id, CASCADE | Parent scan |
| `url` | String | Required | Full URL discovered |
| `status_code` | Integer | Nullable | HTTP response code |
| `content_type` | String | Nullable | HTTP Content-Type header |

### 2.3 `findings`

```python
class Finding(Base):
    __tablename__ = "findings"
    id = Column(Integer, primary_key=True, index=True)
    scan_id = Column(Integer, ForeignKey("scans.id", ondelete="CASCADE"))
    link_id = Column(Integer, ForeignKey("discovered_links.id", ondelete="CASCADE"), nullable=True)
    severity = Column(String)
    finding_type = Column(String)
    description = Column(String)
    poc_payload = Column(String, nullable=True)  # Unlimited text (JSON/proof)
    cvss_score = Column(String, nullable=True)
```

| Column | Type | Constraints | Notes |
|--------|------|------------|-------|
| `id` | Integer | PK, indexed | Finding identifier |
| `scan_id` | Integer | FK → scans.id, CASCADE | Parent scan |
| `link_id` | Integer | FK → discovered_links.id, CASCADE, Nullable | NULL = global/direct finding |
| `severity` | String | Required | `info`, `low`, `medium`, `high`, `critical` |
| `finding_type` | String | Required | Type code: `OPEN_PORT`, `SQL_INJECTION`, `REFLECTED_XSS`, etc. |
| `description` | String | Required | Human-readable description |
| `poc_payload` | String | Nullable, unlimited length | Proof-of-concept or serialized JSON |
| `cvss_score` | String | Nullable | CVSS score string |

---

## 3. RELATIONSHIPS & CASCADE RULES

```python
# Scan has many Findings (direct)
findings = relationship("Finding", back_populates="scan",
    cascade="all, delete-orphan")

# Scan has many DiscoveredLinks
discovered_links = relationship("DiscoveredLink", back_populates="scan",
    cascade="all, delete-orphan")

# DiscoveredLink has many Findings
findings = relationship("Finding", back_populates="link",
    cascade="all, delete-orphan")
```

### Cascade Behavior
- Deleting a `Scan` → deletes all its `discovered_links` and `findings`
- Deleting a `DiscoveredLink` → deletes all its child `findings`
- These cascades are enforced at both ORM level (`cascade="all, delete-orphan"`) and DB level (`ondelete="CASCADE"`)

---

## 4. QUERY PATTERNS

### List all scans (latest first):
```python
scans = db.query(Scan).order_by(Scan.id.desc()).all()
```

### Get scan with all relationships (eager loaded):
```python
scan = db.query(Scan)\
    .options(
        joinedload(Scan.findings),
        joinedload(Scan.discovered_links)
            .joinedload(DiscoveredLink.findings)
    )\
    .filter(Scan.id == scan_id)\
    .first()
```

### Export all data (full dump):
```python
all_scans = db.query(Scan)\
    .options(
        joinedload(Scan.findings),
        joinedload(Scan.discovered_links)
            .joinedload(DiscoveredLink.findings)
    )\
    .order_by(Scan.id.desc())\
    .all()
```

### Create new scan with findings:
```python
scan = Scan(domain_target="example.com", status="RUNNING", scan_type="crawler")
db.add(scan)
db.commit()
db.refresh(scan)

finding = Finding(
    scan_id=scan.id,
    severity="high",
    finding_type="SQL_INJECTION",
    description="SQL injection in login form",
    cvss_score="8.5"
)
db.add(finding)
db.commit()
```

---

## 5. FINDING TYPES REFERENCE

Common `finding_type` values used across engines:

| finding_type | Engine | Description |
|---|---|---|
| `OPEN_PORT` | scanner | Nmap-discovered open port |
| `CONTACT_INFO_DISCLOSURE` | scanner | Email/phone found on web surface |
| `UNSANITIZED_INPUT_CANDIDATE` | scanner | Form input without sanitization |
| `REFLECTED_INPUT_ECHO` | scanner | Probe value reflected in response |
| `web_recon_results` | recon | Full recon results as JSON blob in poc_payload |
| `SQL_INJECTION` | crawler | SQLMap or manual payload confirmation |
| `REFLECTED_XSS` | crawler | XSS payload reflected in response |
| `MISSING_SECURITY_HEADER` | crawler | Missing HSTS/CSP/etc. |
| `INSECURE_COOKIE` | crawler | Missing Secure/HttpOnly flags |
| `EXPOSED_CONFIG` | crawler | .env/.git/config accessible |
| `OPEN_CORS` | crawler | Overly permissive CORS |
| `LFI_VULNERABILITY` | crawler | Directory traversal |
| `INSECURE_LOGIN_FORM` | crawler | Password over HTTP |
| `JS_SECRET_EXPOSURE` | crawler | API keys/tokens in JS |
| `API_DISCOVERY` | crawler | API docs/schema publicly exposed |
| `RISKY_HTTP_METHOD` | crawler | PUT/DELETE allowed publicly |
| `SSL_TLS_ISSUE` | crawler | SSL/TLS protocol vulnerabilities |
