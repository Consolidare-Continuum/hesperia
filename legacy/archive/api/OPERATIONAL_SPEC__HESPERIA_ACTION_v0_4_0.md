<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# HESPERIA Action v0.4.0 — Operational Spec

**Version**: 0.4.0  
**Base URL**: `https://hesperia.prichindel.com`  
**Verification**: `CLIENTS/hesperia/api/verify_operational_v040.sh`

---

## 1. Endpoints

| Method | Path | Auth | Response |
|--------|------|------|----------|
| GET | /health | None | 200 JSON `{ok, service, version}` |
| GET | /openapi.json | None | 200 JSON (OpenAPI 3.x) |
| POST | /hesperia/analyze | Bearer required | 200/400/401/413/415/422/429/500/503 JSON |

No other endpoints are exposed. All responses are JSON; no HTML.

---

## 2. Auth

- **POST /hesperia/analyze** requires `Authorization: Bearer <token>`.
- **Missing or invalid Bearer** → 401 JSON `{error:true, message, code:401}`.
- **Dual-key rotation**: Server accepts either `HESPERIA_API_KEY` or `HESPERIA_API_KEY_NEXT` (env from `/etc/hesperia/hesperia-api.env`). See VARIABLES.md and README_ACTIONS.md for rotation procedure.
- **GET /health** and **GET /openapi.json** require no auth.

---

## 3. Nginx edge (invariants)

- **Wrong Host** → 444 (connection closed). `server_name hesperia.prichindel.com`; `if ($host != "hesperia.prichindel.com") { return 444; }`.
- **Wrong method** (e.g. POST /health, GET /hesperia/analyze) → 403 (limit_except).
- **OPTIONS** → handled at nginx: 204 with `Allow` and `X-Request-ID`. No CORS headers.
- **POST /hesperia/* with Content-Type not matching `application/json`** (e.g. prefix) → 415 JSON `{error, message, code:415}`.
- **Upstream down or timeout** → 503 JSON (no HTML). `proxy_intercept_errors on`; `error_page 502 503 504 = @json_5xx`.
- **Rate limit exceeded** → 429 JSON (no HTML). `limit_req_status 429`; `error_page 429 = @json_429`.
- **X-Content-Type-Options: nosniff** present on all responses (server-level and named error locations).
- **/docs, /redoc, /swagger** → 404.
- **/, /.env, /.git, /robots.txt, /favicon.ico** → 404 (no directory index, no leakage).

Config: `cluster/hesperia.prichindel.com.conf`. Deploy: `sudo cp ... /etc/nginx/conf.d/`; `sudo nginx -t && sudo systemctl reload nginx`.

---

## 4. Error contract (app)

- All error responses: JSON `{error:true, message:string, code:number}`.
- **422**: Stable messages only — `"Invalid request body"` or `"Invalid request body: extra fields not permitted"`. No stack traces, no Pydantic internals, no user input echoed.
- **500**: Generic `"Internal error"` only.

---

## 5. Logging (nginx)

- **Must not log** `Authorization` (or any secret). Log format does not include `$http_authorization`.
- **Access log** includes: `$request_id`, `$request_time`, `$upstream_status`, `$upstream_response_time`. Format: `hesperia`; file: `/var/log/nginx/hesperia.access.log`.

---

## 6. Verification checklist

Run: `API_KEY=<secret> ./verify_operational_v040.sh` (optionally `BASE_URL=...`).

| # | Check | Expected |
|---|-------|----------|
| 1 | GET /health | 200, JSON with `"ok":true` |
| 2 | GET /openapi.json | 200, JSON contains `bearerAuth` |
| 3 | POST /hesperia/analyze no auth | 401 JSON, code=401 |
| 4 | POST /hesperia/analyze wrong auth | 401 JSON, code=401 |
| 5 | POST /hesperia/analyze + Content-Type text/plain | 415 JSON, code=415 |
| 6 | POST /hesperia/analyze + JSON extra field | 422 JSON, code=422, stable message |
| 7 | POST /hesperia/analyze + valid JSON + auth | 200 or 400, JSON |
| 8 | OPTIONS /hesperia/analyze | 204, Allow header present |
| 9 | GET /docs | 404 |
| 10 | GET / | 404 |
| 11 | GET /health response | Header X-Content-Type-Options: nosniff |
| 12 | Wrong Host | Connection close / non-200 (best-effort) |

---

**Spec file**: `CLIENTS/hesperia/api/OPERATIONAL_SPEC__HESPERIA_ACTION_v0_4_0.md`  
**Harness**: `CLIENTS/hesperia/api/verify_operational_v040.sh`  
**GPT Builder wiring**: `CLIENTS/hesperia/api/README_ACTIONS.md`
