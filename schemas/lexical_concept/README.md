<!--
HESPERIA — RAD. JSON Schemas for DLCR-HP (INT-003).
-->

# `schemas/lexical_concept`

JSON Schemas for deterministic lexical-concept resolution artifacts.

| File | Role |
|------|------|
| `dict_a.schema.json` | Dict A rows |
| `dict_b.schema.json` | Dict B concept rows |
| `resolver_output.schema.json` | Per-span resolution trace |
| `run_metadata.schema.json` | Run / version metadata |
| `analyze_lexical_evidence_dlcr.schema.json` | `analyze()` extended **`lexical_evidence_dlcr`** when `HESPERIA_ANALYZE_DLCR_EVIDENCE=1` (PO-02) |
| `definitions.json` | Shared `$defs` for optional `$ref` from sibling schemas |

**Canon:** `specs/canon/lexical_concept/` (master + § fragments).  
**Validators:** `tools/validate_dict_a.py`, `tools/validate_dict_b_dlcr.py` (no args = all pinned `*.jsonl` under `assets/data/engine_dynamics_v060/dict_{a,b}/`).  
**RU TFP pack integrity:** `python3 tools/validate_tfp_ru_pack.py` (stack merge + ≥3 lexical rows per `dict_b_tfp_ru_v060` concept, anchors).  
**Rebuild stack (corpus → RAW → active):** `python3 tools/build_ru_tfp_dictionary_stack.py --write` (see `docs/governance/working/ETHAN-TFP-RU-CODEX-STACK.md`).
