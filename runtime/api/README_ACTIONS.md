<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Hesperia API — Wire into GPT Builder (Actions)

**Base URL**: `https://hesperia.prichindel.com`  
**Operational spec**: [OPERATIONAL_SPEC__HESPERIA_ACTION_v0_4_0.md](OPERATIONAL_SPEC__HESPERIA_ACTION_v0_4_0.md)  
**Verification**: `./verify_operational_v040.sh` (requires `API_KEY`)

---

## 1. Schema URL

In GPT Builder → **Actions** → **Import from URL**:

```
https://hesperia.prichindel.com/openapi.json
```

No auth is required for this URL.

---

## 2. Auth in GPT Builder

- **Authentication**: **API Key**
- **Key type**: **Bearer**
- **Key**: paste the value of `HESPERIA_API_KEY` (same as in `/etc/hesperia/hesperia-api.env` on the server).

GPT will send `Authorization: Bearer <key>` on every request. Do not rely on custom headers.

---

## 3. Key rotation (dual-key)

The server accepts either `HESPERIA_API_KEY` or `HESPERIA_API_KEY_NEXT`. To rotate without downtime:

1. On the server: add `HESPERIA_API_KEY_NEXT=<new-secret>` to `/etc/hesperia/hesperia-api.env`. Restart: `sudo systemctl restart hesperia-api`.
2. In GPT Builder: update the Action’s API Key to the **new** secret.
3. On the server: set `HESPERIA_API_KEY=<new-secret>`, remove `HESPERIA_API_KEY_NEXT`. Restart API.

Variables reference: [CLIENTS/hesperia/VARIABLES.md](../VARIABLES.md) §1 (runtime).

---

## 4. What to paste / test

- **Health** (no auth): `GET https://hesperia.prichindel.com/health` → `{"ok":true,"service":"hesperia","version":"0.4.0"}`
- **Analyze** (with Bearer):  
  `POST https://hesperia.prichindel.com/hesperia/analyze`  
  Headers: `Authorization: Bearer <your-key>`, `Content-Type: application/json`  
  Body: `{"text": "your sentence"}`  
  - 200 → result with `dominant_area`, `dominant_family`, etc.  
  - 400 → ask user for different wording.

Add to GPT instructions: *Use the Hesperia action for semantic attribution. If the API returns 400, ask the user for different wording.*

---

**Full setup and server-side details**: [GPT-ACTIONS-SETUP.md](GPT-ACTIONS-SETUP.md)
