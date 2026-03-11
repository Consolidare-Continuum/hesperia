# Historical reference (pre-refactor)

# HESPERIA v0.6 — Operational index (frozen)

**Single active path:** Dict A v0.6 → Dict B v0.6 → 6-key + extended. No v0.4/v0.5 in use.

## Entry points

| What | Path |
|------|------|
| Operational spec | [docs/OPERATIONAL_SPEC_v0_6.md](docs/OPERATIONAL_SPEC_v0_6.md) |
| Core math contract | [22_SPEC__V0_3_Core_Math_Contract_v1_0.md](22_SPEC__V0_3_Core_Math_Contract_v1_0.md) |
| Guard config | [guard_config_v1.json](guard_config_v1.json) |
| Layer defaults | [LAYER_1_9_PREDEFINED_DEFAULTS_v1_0.txt](LAYER_1_9_PREDEFINED_DEFAULTS_v1_0.txt), [layer_1_9_predefined_defaults_v1_0.json](layer_1_9_predefined_defaults_v1_0.json) |
| Layer specs (L1–L9) | [34_SPEC…42_SPEC](docs/) (38–42 in repo root) |

## Scripts (from `CLIENTS/hesperia`)

| Script | Purpose |
|--------|--------|
| `scripts/run_calibration_v06.py` | Full spec run 100 sentences → docs/hesperia_runtime_output/calibration_v06_* |
| `scripts/verify_v06_operational.py` | Operational checks |
| `scripts/calibration_metrics_v06.py` | Per-domain metrics + entropy |
| `sphere_rag/build_dict_a.py` | Build Dict A |
| `sphere_rag/validate_dict_a.py` | Validate artifact |
| `sphere_rag/audit_dict_a_runtime.py` | Runtime audit |

## Analyze

- **`sphere_rag/analyze.py`** — `analyze(text, ...)` → (minimal_6key, extended).

## API

- [api/main.py](api/main.py) — FastAPI 0.6.0; POST /hesperia/analyze.

## Artifacts

- `assets/v06/` — dict_a_v06.jsonl, family_prior_v06.json, sha256
- `hesperia_lex/frozen/DICT_A_SURFACE_MAP_v0_4_1_3.json` — surface→lemma
- `hesperia_lex/curated/FAMILY_SPEC_v0_6.json` — 288-family spec

## Math layers (code + specs)

- `sphere_rag/layers/layer_1.py` … `layer_9.py`, `defaults.py` — implementation
- Specs 34–42 (Layer1–Layer9) — see DOC_INDEX.md for paths

## Deprecated / archived

- [archive/ARCHIVE_MANIFEST.md](archive/ARCHIVE_MANIFEST.md) — what was moved and why
