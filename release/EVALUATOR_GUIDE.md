# HESPERIA Evaluator Guide

Short guide for running and testing the sealed runtime. (~2 pages.)

**Evaluator promise:** Reproducible CLI/API, deterministic outputs, no exposure of internal model mechanics, stable schema. See `docs/governance/EVALUATOR_PROMISE_v1.md`.

---

## What HESPERIA does

HESPERIA is a **structural measurement engine**. You give it text; it returns:

- **Structural emphasis** over macro-domains and policy families (numeric vectors and counts).
- **Evidence** (matched spans, concept labels, confidence).
- **Trust and confidence** (e.g. trust tier, decision status).

It does **not** expose internal geometry, layer count, or construction method. The only visible concept is: *text in → structural measurement → evidence and metrics out*.

---

## How to run the CLI

**Single-text measurement:**
```bash
./hesperia-cli.bin analyze --text "Your policy or statement here."
```
Output: JSON with structural emphasis, evidence summary, and trust/confidence.

**Compare two texts:**
```bash
./hesperia-cli.bin compare --text1 "First statement." --text2 "Second statement."
```
Output: JSON with trust tags and whether the dominant emphasis matches.

**Batch (multiple texts):**
```bash
./hesperia-cli.bin batch-analyze --raw_text texts.json --out results.json
```
`texts.json` can be a list of strings or `{"texts": ["...", "..."]}`. Max 100 texts per batch in API; CLI follows the same limit when using the API.

**Version:**
```bash
./hesperia-cli.bin --version
```
Shows runtime version, commit, and build date.

**Write output to file:**
```bash
./hesperia-cli.bin analyze --text "..." --out summary.json
```

---

## How to run the API

**Load and start the container:**
```bash
docker load -i hesperia-api-image.tar
docker run -p 8080:8000 -e HESPERIA_LICENSE_SKIP=1 hesperia-api:latest
```

**Endpoints:**
- `GET /health` — Liveness. Returns `{"status": "ok"}`.
- `GET /version` — Version, commit, build.
- `POST /analyze` — Body: `{"text": "your text"}`. Returns measurement JSON.
- `POST /compare` — Body: `{"text1": "...", "text2": "..."}`. Returns comparison JSON.
- `POST /batch-analyze` — Body: `{"texts": ["...", "..."]}`. Max 100 texts. Returns list of measurement results.

**Example:**
```bash
curl -X POST http://localhost:8080/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "sample policy text"}'
```

**Rate limiting:** 60 requests per minute by default. Exceeding returns `429` and `"Rate limit exceeded"`.

**Environment variables:** Only supported `HESPERIA_*` variables are honored. See `docs/governance/RUNTIME_ENV_VARS_v1.md` for the full list (e.g. `HESPERIA_LICENSE_SKIP`, `HESPERIA_RATE_LIMIT`, `HESPERIA_SCHEMA_SHA256` for optional integrity check).

---

## What outputs mean

- **macro_domain_vector / policy_family_counts:** Emphasis over macro-domains (10) and policy families (240). Values are non-negative; interpretation is product-specific.
- **L7 / L9:** Trust and decision fields (e.g. `OUTPUT_TRUST_TAG`, `BRAND_WORD_TRUST`). Use for confidence and follow-up actions.
- **usf / interpretation_metrics:** High-level interpretation state and events. No internal coordinates or topology.
- **compare:** `dominant_match` (true/false), `confidence_delta` (same/different), and trust tags for each text.

All outputs are **projected**: no internal geometry, layer count, or propagation details.

---

## What evaluators should test

1. **Correctness:** Run the same text through CLI and API; results should be consistent (same structural emphasis and trust).
2. **Projection:** No forbidden terms in any output (e.g. no sphere, hex, topology, layer, bridge, area11, family240 in keys or values).
3. **Versioning:** `--version` and `GET /version` show version, commit, build for traceability.
4. **Rate limiting:** Send more than 60 requests per minute to the API; expect 429.
5. **Batch size:** Send more than 100 texts in one `batch-analyze` request; expect 400.
6. **Errors:** Trigger an error (e.g. invalid raw_text); response must be generic (e.g. `internal_processing_error`) with no stack trace or internal names.

---

*Sealed evaluator runtime. For support, provide version and build from `--version` or `/version`.*
