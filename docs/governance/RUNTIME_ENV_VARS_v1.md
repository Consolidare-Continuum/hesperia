# Runtime environment variables v1

**Status:** Locked  
**Purpose:** Document `HESPERIA_*` variables and align with `runtime/shipping/env_guard.py`. Unknown keys still trigger a stderr warning (or `ValueError` in strict mode) at shipping API startup when `check_hesperia_env` runs.

---

## Source of truth

- **Machine-readable allowlist:** `ALLOWED_HESPERIA_ENV` in `runtime/shipping/env_guard.py` (103 names as of 2026-03-28).  
- **Regenerate** after adding new env readers: `python3 tools/list_hesperia_env_for_guard.py` (paste output into that frozenset).

---

## Tier A — Shipping API (`runtime.shipping.api_main`)

Most operators touch these when running the sealed / product-facing API:

| Variable | Purpose | Default / notes |
|----------|---------|-----------------|
| **HESPERIA_LICENSE_SKIP** | Skip license check (e.g. evaluator) | unset → check applies if required |
| **HESPERIA_LICENSE_REQUIRED** | Startup fails without valid license if set | unset |
| **HESPERIA_LICENSE_TOKEN** | License token (env or file) | — |
| **HESPERIA_LICENSE_FILE** | Path to license file | — |
| **HESPERIA_LICENSE_EXPIRY** | Optional expiry | — |
| **HESPERIA_RATE_LIMIT** | Max requests per minute | 60 |
| **HESPERIA_MAX_INPUT_CHARS** | Cap request body size | see `api_main.py` |
| **HESPERIA_MACHINE_BINDING** / **HESPERIA_MACHINE_ID** | Optional machine binding | — |
| **HESPERIA_ASSETS_ROOT** | Override repo root for assets | — |
| **HESPERIA_API_HOST** / **HESPERIA_API_PORT** | Bind address | 0.0.0.0 / 8000 |
| **HESPERIA_SCHEMA_SHA256** | Expected SHA256 of public output schema | unset → no check |
| **HESPERIA_REQUIRE_SYSTEM_SEAL** | Enforce system seal when set | see shipping code |
| **HESPERIA_PUBLIC_SCHEMA_STRICT_KEYS** | Stricter public JSON keys (schema guard) | — |
| **HESPERIA_RUNTIME_MODE** | `public_runtime` \| `internal_review` \| `internal_debug` | `public_runtime` |
| **HESPERIA_PRODUCT_SURFACE** | Strict product surface (hides optional HTTP routes) | default true in capabilities |
| **HESPERIA_EXPOSE_TRIZ** / **HESPERIA_EXPOSE_VERSION** | Dev-only route exposure | see `hesperia/system/capabilities.py` |
| **HESPERIA_DLCR_STRUCTURAL** | Structural DLCR attachment (with capabilities) | — |

---

## Tier B — Dev API and tooling (`runtime.api.main`, tests, CI)

Used mainly for local/dev servers and automation (also on the allowlist so mixed environments do not warn spuriously):

| Variable | Purpose |
|----------|---------|
| **HESPERIA_API_KEY** / **HESPERIA_API_KEY_NEXT** | Bearer auth for dev API |
| **HESPERIA_API_INSTRUMENTATION** | Optional request logging / metrics hooks |

---

## Tier C — Research, calibration, E2E, field dynamics, CD, core math

The allowlist includes every `HESPERIA_*` name read anywhere in the repo: calibration (`HESPERIA_CALIB_*`, `HESPERIA_DICT_*`), concept dictionary (`HESPERIA_CD_*`), DLCR (`HESPERIA_DLCR_*`), field dynamics (`HESPERIA_FIELD_DYNAMICS_*`), E2E (`HESPERIA_E2E_*`, `HESPERIA_PRODUCT_E2E_*`), sealed sidecars, semantic field flags, TFP paths, build provenance (`HESPERIA_BUILD_*`, `HESPERIA_GIT_COMMIT`, `HESPERIA_VERSION`), and core math tuning (`HESPERIA_ALPHA`, `HESPERIA_ETA`, `HESPERIA_LAMBDA`, …). See the code path that reads each name for semantics.

---

## Reject unknown (optional)

At shipping startup:

1. Enumerate `os.environ` keys starting with `HESPERIA_`.
2. Compare to `ALLOWED_HESPERIA_ENV`.
3. Unknown keys: stderr warning (default) or `ValueError` if `strict=True`.

---

*See `license_check.py`, `api_main.py`, `schema_guard.py`, `EVALUATOR_GUIDE.md`, and `env_guard.py`.*
