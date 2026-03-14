# Runtime environment variables v1

**Status:** Locked  
**Purpose:** Only supported variables control behavior. Reject or ignore unknown `HESPERIA_*` in sealed runtime.

---

## Supported variables

| Variable | Purpose | Default |
|---------|---------|---------|
| **HESPERIA_LICENSE_SKIP** | Skip license check (e.g. evaluator run) | unset → check applies if required |
| **HESPERIA_LICENSE_REQUIRED** | If set, startup fails without valid license | unset |
| **HESPERIA_LICENSE_TOKEN** | License token (env or file) | — |
| **HESPERIA_LICENSE_EXPIRY** | Optional expiry date | — |
| **HESPERIA_RATE_LIMIT** | Max requests per minute (API) | 60 |
| **HESPERIA_MACHINE_BINDING** | Enable optional machine binding | unset / off |
| **HESPERIA_MACHINE_ID** | Override machine id for binding check | — |
| **HESPERIA_ASSETS_ROOT** | Override repo root for assets | — |
| **HESPERIA_API_HOST** | API bind host | 0.0.0.0 |
| **HESPERIA_API_PORT** | API bind port | 8000 |
| **HESPERIA_RUNTIME_MODE** | public_runtime \| internal_review \| internal_debug | public_runtime |
| **HESPERIA_SCHEMA_SHA256** | Optional: expected SHA256 of public_output_schema.json (integrity check) | unset → no check |

No other `HESPERIA_*` variables are supported. Unknown variables are ignored (or, in strict mode, can cause a warning at startup).

---

## Reject unknown (optional)

In sealed evaluator runtime, at startup the process can:

1. List all `os.environ` keys starting with `HESPERIA_`.
2. Compare against the allowed set above.
3. If any unknown key is present: log a warning and continue, or (strict) exit with a clear message.

This prevents accidental behavior change from typos or unsupported flags.

---

*See license_check.py, api_main.py, and EVALUATOR_GUIDE.md for usage.*
