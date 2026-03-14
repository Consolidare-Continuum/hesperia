# Clean machine dry run v1

**Status:** Active  
**Purpose:** On a clean Linux machine (no repo, only the evaluator bundle), run CLI, run API, send analyze request, verify projected outputs, verify no extra artifacts. Bundle must work without repo and without leaking internals.

---

## 1. Prerequisites

- Clean machine or container (no HESPERIA repo).
- Only the evaluator bundle: CLI binary, API image tar, examples, quickstart, manifest, checksums (no source tree).

---

## 2. Steps

| Step | Action | Expected |
|------|--------|----------|
| 1 | Copy bundle to machine. Unpack if zip/tarball. | No errors. |
| 2 | **Run CLI:** `./hesperia-cli.bin analyze --text "justice fairness"` (or from dist/hesperia-cli/ if standalone). | Exit 0. JSON on stdout. No internal terms (sphere, hex, side_id, topology) in output. |
| 3 | **Run API:** `docker load -i hesperia-api-image.tar`, then `docker run -p 8000:8000 -e HESPERIA_LICENSE_SKIP=1 hesperia-api:latest`. | Container starts. GET /health returns {"status":"ok"}. |
| 4 | **Send analyze request:** `curl -X POST http://localhost:8000/analyze -H "Content-Type: application/json" -d '{"text":"justice fairness"}'`. | 200. Response is JSON with projected shape (e.g. run, text_preview, L7, L9; no side_id, no 12-area vector, no family 240–287). |
| 5 | **Verify projected outputs:** Grep response for forbidden terms. Check that macro_domain_vector length is 10 if present, policy_family counts 240. No area index 10 or 11. | No forbidden terms; public counts only. |
| 6 | **Verify no extra artifacts:** No files written to disk except by explicit --out or API response. No layer dumps, no trace files, no debug output in container logs that reveals internal structure. | No extra artifacts; logs product-shaped only. |

---

## 3. Done condition

**Done when:** Bundle works without repo and without leaking internals. CLI runs, API runs, analyze returns projected output, no extra artifacts appear.
