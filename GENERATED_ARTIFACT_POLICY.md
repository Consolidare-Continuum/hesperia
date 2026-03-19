# Generated artifact policy

## Default location

All **machine-generated** JSON/CSV/Markdown runs (E2E, smoke, benchmarks, ad-hoc reports) should write under:

```
outputs/
  e2e/
  smoke/
  benchmarks/
  reports/
```

Paths are **gitignored** by default (see `.gitignore`).

## What may be committed

| Class | Typical path | Rule |
|-------|----------------|------|
| **Frozen regression exemplars** | `assets/artifacts/e2e/*.json` (explicit list in docs) | Commit only after review; document in `docs/E2E_RUN_ORDER.md` |
| **Shipping checksums** | `release/*` | Release process only |
| **Calibration registries** | `assets/calibration/*` | Human-governed YAML/JSON |
| **Public schema** | `schemas/public/public_output_schema.json` | Canonical; `assets/public/public_output_schema.json` is a **symlink** for legacy paths |

## Forbidden

- Dumping unbounded run output next to source modules (e.g. under `hesperia/` or `runtime/`).
- Committing local-only `outputs/**` without an explicit freeze decision.

## Demo outputs

TRIZ demo artifacts live under **`examples/extensions/triz_demo/triz/outputs/`** (committed small samples). Full reruns should go to `outputs/reports/` locally.
