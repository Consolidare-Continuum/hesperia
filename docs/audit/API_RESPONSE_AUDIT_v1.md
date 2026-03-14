# API response audit v1

**Status:** Active  
**Purpose:** Every API response must pass through: service façade → projection → public-safe serializer. Responses (including errors) must not leak internal fields.

---

## 1. Normal responses

| Endpoint | Flow | Check |
|----------|------|--------|
| POST /analyze | analysis_service.run_structural_analysis() → already projected → JSON response | Response must contain only public vocabulary (macro_domain_vector, policy_family_counts, L7/L9 as projected). No side_id, hex, topology, area index 10/11, family 240–287. |
| POST /compare | Two run_structural_analysis() → comparison built from projected outputs only | Same; comparison object has no internal coordinates. |
| POST /batch-analyze | run_structural_analysis_batch() → list of projected results | Each item is projected; no internal fields. |
| GET /health | Fixed {"status": "ok"} | No internal data. |

All success responses are JSON-serialized from data that has passed through the projection layer (inside the service). No response path may bypass projection.

---

## 2. Error responses

- **Rate limit (429):** Body must be generic (e.g. "Rate limit exceeded"). No stack trace, no internal module names, no file paths.
- **Validation (422):** FastAPI/Pydantic default; ensure no internal field names or paths in error detail.
- **License / startup failure:** Server must not start; no response body. If a response is ever returned, it must not include internal paths or module names.
- **Unhandled exception:** Use FastAPI exception handler or generic 500 with a safe message. Never return traceback, internal paths, or layer names to the client.

---

## 3. Verification

1. Call each endpoint with valid input; inspect response body for forbidden keys (side_id, hex, topology, area_id 10/11, family 240–287).
2. Trigger 429 (exceed rate limit); confirm body is generic.
3. Trigger 422 (invalid body); confirm no internal paths in detail.
4. Confirm no endpoint returns raw layer objects (L1–L9 as internal structure) or unprojected metrics.

---

## 4. Done condition

**Done when:** Responses cannot leak internal fields even on errors. All responses pass through service façade and projection; public-safe serializer only.
