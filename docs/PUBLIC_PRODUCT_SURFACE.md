# Public product surface (Task 4)

**Engine Dynamics v0.5** — defines what may leave the runtime: a **mandatory projection gate** and a **minimal HTTP/CLI surface**.

## Layers

| Layer | Role |
|--------|------|
| **Internal** | Hex states, full matrices, propagation, calibration params, raw Dict A/B — **never** serialized to public consumers. |
| **Projection** | `hesperia.engine.projection.project_to_public` — single choke point; wraps `core.projection.apply_public_projection` + `enforce_public_schema`. |
| **Public** | Macro-domain vector, family counts (public subset), dominants, scalar metrics, trust tier, sanitized evidence, version/build metadata — only after projection. |

## Code entry points

- **Projection package:** `hesperia/engine/projection/` — `public_projection.py`, `schema_enforcer.py`, `sanitizer.py`.
- **Measurement façade:** `runtime.services.analysis_service.run_structural_analysis` / `run_structural_analysis_batch` — always calls `project_to_public` before returning.
- **Public JSON writes:** `runtime.artifact_writer.write_public_json` — projects, attaches version envelope, validates keys.

## HTTP

| Deployment | Component | Routes |
|------------|-----------|--------|
| **Shipping** / Docker | `runtime.shipping.api_main` | `POST /analyze`, `/compare`, `/batch` (alias `/batch-analyze`), `GET /health`. Optional `GET /version` when `HESPERIA_EXPOSE_VERSION=1` or non-strict dev (`HESPERIA_PRODUCT_SURFACE=0` + `capabilities.yaml`). **No** `/hesperia/*` or `/product/*`. |
| **Dev / GPT Actions** | `runtime.api.main` | `POST /hesperia/analyze`, `/hesperia/compare`, `/hesperia/batch`, `GET /health`, OpenAPI at `/openapi.json`. **T17 (Task 17)** — additional Bearer-protected handlers: `POST /product/llm-audit`, `/product/tfp`, `/product/fingerprint` (`hesperia.product.service.run_product_profile`). These **do not** exist on `api_main`; operators must not assume one uvicorn target serves both prefix styles. |

**TRIZ** routes (dev API only) register when `HESPERIA_EXPOSE_TRIZ=1` and `HESPERIA_PRODUCT_SURFACE=0` (see `hesperia/system/capabilities.yaml`).

## CLI

```bash
pip install -e .   # exposes `hesperia` console script → runtime.shipping.cli_main
hesperia analyze --text "..."
hesperia compare --text1 "..." --text2 "..."
hesperia batch --texts "a" "b"
# batch-analyze is an alias of batch
```

## Capability flags

- File: `hesperia/system/capabilities.yaml`
- Env overrides: `HESPERIA_PRODUCT_SURFACE`, `HESPERIA_EXPOSE_TRIZ`, `HESPERIA_EXPOSE_VERSION`, `HESPERIA_MAX_INPUT_CHARS`, `HESPERIA_RATE_LIMIT`

## E2E split

| Suite | Command | Scope |
|--------|---------|--------|
| **Product** | `python3 -m runtime.pipeline.run_e2e_product` | One projected artifact + schema guard. |
| **Internal (dev)** | `python3 -m runtime.pipeline.run_e2e_all` | Full stack, research collateral, optional TFP smoke, etc. |

## Docker

- **Product image:** `Dockerfile.shipping` — `runtime`, `core`, `hesperia`, `lexicon`, `assets` only (no `research/`, notebooks, or demos in the image context).
- Full-repo images are a **dev** concern; do not ship research/clinical paths in production containers.

## Security notes

- Do not import internal execution_flow modules from API handlers; use `analysis_service` only.
- Responses are validated with `runtime.shipping.schema_guard.validate_against_public_schema` at boundaries where applicable.

See also: `docs/HESPERIA_v0_5_ENGINE_DYNAMICS.md`, `AGENTS.md`.
