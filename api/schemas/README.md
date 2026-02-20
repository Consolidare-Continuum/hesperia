# JSON Schemas — Hesperia Analyze API

Draft 2020-12 JSON Schema files for the `/hesperia/analyze` contract (OpenAI GPT actions, docs, validation).

| File | Use |
|------|-----|
| `HesperiaAnalyzeRequest.json` | Request body: `text` (required), optional `options`. |
| `HesperiaAnalyzeResponse.json` | Response body: dominant_area/family, loopability, governance, metrics, etc. |

Python types live in `api/schemas.py` (Pydantic); OpenAPI/JSON Schema also at `GET /openapi.json` when the API is running.
