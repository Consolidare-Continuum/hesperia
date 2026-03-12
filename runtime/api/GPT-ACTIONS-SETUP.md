<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# GPT Actions — Hesperia API setup

**Endpoint**: `https://hesperia.prichindel.com`  
**Auth**: API Key → Bearer (single shared key or dual-key rotation). Set in GPT Action config.

**Operational spec and verification**: See [OPERATIONAL_SPEC__HESPERIA_ACTION_v0_4_0.md](OPERATIONAL_SPEC__HESPERIA_ACTION_v0_4_0.md) for invariants and checklist. Run `./verify_operational_v040.sh` (with `API_KEY` set) to verify all checks. Short wiring guide: [README_ACTIONS.md](README_ACTIONS.md).

---

## 1. Authentication (GPT Builder)

- **Authentication**: API Key
- **Key type**: Bearer
- **Key**: your `HESPERIA_API_KEY` value (same as in `/etc/hesperia/hesperia-api.env` on the server).
  GPT will send `Authorization: Bearer <key>` on every request. Do not use custom headers; GPT Actions does not send them reliably.

---

## 2. OpenAPI schema for the GPT

**Option A — Import from URL**
In the GPT Action: **Import from URL**
`https://hesperia.prichindel.com/openapi.json`

**Option B — Paste schema**
Use the trimmed schema below (or export from `/openapi.json` and trim).
In the GPT Action: **Import** → paste the JSON.

**Required in schema** (FastAPI already provides):

- `servers`: `[{ "url": "https://hesperia.prichindel.com" }]`
- `POST /hesperia/analyze` with:
  - `requestBody`: `application/json` → `{ "text": "string" }`
  - `responses`: 200 (6-key result), 400, 401, 413, 500 (all with `error`, `message`, `code`)

---

## 3. Test call

1. **Health** (no auth): `GET https://hesperia.prichindel.com/health` → `{"ok":true,"service":"hesperia","version":"0.4.0"}`
2. **Analyze** (with Bearer):
   `POST https://hesperia.prichindel.com/hesperia/analyze`
   Headers: `Authorization: Bearer <your-key>`, `Content-Type: application/json`
   Body: `{"text": "your sentence that might match Dict A/B"}`
   - 200 → 6 keys: `dominant_area`, `dominant_family`, `governance`, `loopability`, `tension_energy`, `obstacle_score`
   - 400 → e.g. "No tokens matched any dictionary" (ask user for different wording)

---

## 4. GPT instruction line

Add to the GPT instructions:

> Use the Hesperia action for semantic attribution. If the API returns 400, ask the user for different wording.

---

## 5. Server-side (Abelard)

- **API key**: Store in `/etc/hesperia/hesperia-api.env` as `HESPERIA_API_KEY=<secret>`, chmod 600, read by `hesperia-api.service`.
- **Nginx**: Deploy `cluster/hesperia.prichindel.com.conf`. limit_except returns **403** (not 405). OPTIONS: Allow + X-Request-ID only (no CORS). Log format includes `$upstream_status` and `$upstream_response_time`; never log Authorization. 429 and 503 return JSON.
- **No debug**: 500 responses do not leak stack traces; version pinned in response.
- **Logging**: Nginx uses `hesperia` log format (request_id, status, request_time); never log Authorization. Uvicorn/FastAPI do not log request headers by default.

## 6. Key rotation (zero-downtime)

1. Add `HESPERIA_API_KEY_NEXT=<new-secret>` to `/etc/hesperia/hesperia-api.env`. Reload: `sudo systemctl restart hesperia-api`.
2. Update the GPT Action’s API Key in the builder to the new secret.
3. In env: set `HESPERIA_API_KEY=<new-secret>`, remove `HESPERIA_API_KEY_NEXT`. Restart API.
4. Old key stops working; GPT already uses the new key.
