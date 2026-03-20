<!--
Ethan — operator runbook for DLCR v0.6.0 integration (INT-020).
-->

# DLCR integration runbook (v0.6.0)

Quick commands for **validators**, **regression**, **E2E**, and **TFP smoke** with DLCR flags. Default product path stays unchanged unless capabilities + env allow structural DLCR.

## Env matrix

| Variable | Effect |
|----------|--------|
| `HESPERIA_DLCR_STRUCTURAL` | Merge DLCR summary into public `lexical_resolution` after projection (strict caps; see `structural_dlcr_allowed()`) |
| `HESPERIA_E2E_DLCR` | `run_e2e_all` writes **`run_output_e2e_dlcr.json`** (21st file alongside baseline + optional field dynamics) |
| `HESPERIA_TFP_DLCR` | `run_e2e_tfp_smoke` adds **`session_dlcr_bundles`** |
| `HESPERIA_FIELD_DYNAMICS_DLCR` | Blend DLCR `family_hits_288` into field-dynamics injection (`e2e_bridge`) |
| `HESPERIA_SEALED_DLCR_SIDECAR` | Attach DLCR rollup to sealed multiscale sidecar (research path) |
| `HESPERIA_DLCR_DOMAIN_PACK` | Active pack from `assets/data/engine_dynamics_v060/domain_packs.yaml` (PO-30) |
| `HESPERIA_DICT_A_MAX_ACCEPTED` | Override Dict A accepted-hit cap (PO-04) |
| `HESPERIA_API_INSTRUMENTATION` | `1` → enables `POST /hesperia/internal/dlcr_trace` (PO-26) |
| `HESPERIA_CLINICAL_STRIP_ROLES` | With clinical/speech policy, fold `patient:` / `therapist:` line prefixes (PO-14) |
| `HESPERIA_ANALYZE_DLCR_EVIDENCE` | `1` → `runtime.pipeline.analyze` extended **`lexical_evidence_dlcr`** (PO-02): counts, `resource_versions`, **`evidence_spans`** (≤24 rows, same keys as `resolver_output.schema.json`, no `audit`) |
| `HESPERIA_CONCEPT_EVIDENCE_GUARD` | `observe` \| `strict` — semantic evidence + optional ban on Dict-A direct family path in multiscale L1; **strict** still applies **Dict B (b0) fallback** per token when the token exists in the merged B map (PO-11/12). Trace rows include **`effective_landing_source`** (`observe`/`strict`): e.g. **`B0_fallback`** when raw landing was **A** but b0 was used. |

## Commands

```bash
# Dict A / B validators (no args = all pinned *.jsonl under engine_dynamics_v060/dict_{a,b}/)
python3 tools/validate_dict_a.py
python3 tools/validate_dict_b_dlcr.py
# Or explicit file: python3 tools/validate_dict_a.py assets/data/engine_dynamics_v060/dict_a/dict_a_seed.jsonl

# Multi-corpus regression (EN seed + TFP RU gold)
python3 tools/check_dlcr_regression.py

# Trace tooling (different roles — not duplicates):
# - Full pipeline JSON: python3 tools/dump_dlcr_trace.py "your text"
# - Human-readable gold corpus outline → outputs/dlcr_trace_report.md:
python3 tools/dlcr_trace_report.py

# Lexical_concept unit tests
pytest tests/lexical_concept/ -q

# Full E2E (optional DLCR artifact)
HESPERIA_E2E_DLCR=1 HESPERIA_FIELD_DYNAMICS=1 HESPERIA_E2E_CALIBRATION_BATCH_N=5 \
  python3 -m runtime.pipeline.run_e2e_all --out-dir /tmp/e2e_dlcr

# TFP smoke with per-session DLCR bundles
HESPERIA_TFP_DLCR=1 python3 -c "
from pathlib import Path
import tempfile
from runtime.pipeline.run_e2e_all import run_e2e_tfp_smoke
with tempfile.TemporaryDirectory() as d:
    p = Path(d) / 'tfp.json'
    run_e2e_tfp_smoke(p)
    print(p.read_text()[:500])
"

# Experimental benchmark DLCR checks
pytest tests/experimental/clinical_tfp/test_dlcr_benchmark_sessions.py -q

# Full internal DLCR JSON (PO-10)
python3 tools/dump_dlcr_trace.py "justice fairness order" --out /tmp/dlcr.json
```

## References

- **TFP runnable — which dictionaries to wire (frozen vs DLCR vs ontology):** [ETHAN-TFP-RUNNABLE-DICT-WIRING.md](ETHAN-TFP-RUNNABLE-DICT-WIRING.md)
- **TFP Russian DLCR pack (4× Dict A + `TFP_*` Dict B, corpus, validation):** [ETHAN-TFP-RU-DICT-12TASKS.md](ETHAN-TFP-RU-DICT-12TASKS.md)
- **Codex-style corpus → RAW → promoted stack (deterministic):** [ETHAN-TFP-RU-CODEX-STACK.md](ETHAN-TFP-RU-CODEX-STACK.md) · `python3 tools/build_ru_tfp_dictionary_stack.py --write`
- **Post-options (30 tasks, in progress):** [ETHAN-DLCR-POST-OPTIONS-TASKS-30.md](ETHAN-DLCR-POST-OPTIONS-TASKS-30.md)
- **Instrumentation template (PO-27):** [ETHAN-DLCR-INSTRUMENTATION-TEMPLATE.md](ETHAN-DLCR-INSTRUMENTATION-TEMPLATE.md)
- **20-task board (closed):** [ETHAN-DLCR-INTEGRATION-20-v0_6_0.md](ETHAN-DLCR-INTEGRATION-20-v0_6_0.md)
- **Canon:** `specs/canon/lexical_concept/README.md`
- **72k phased scale:** `specs/canon/lexical_concept/SPEC__72k_Phased_Scale_v0_6_0.md`
- **Registry:** `assets/version_registry.yaml` → `dlcr` / `paths.dlcr_engine_dynamics_v060`
- **E2E order:** `docs/E2E_RUN_ORDER.md`, `assets/artifacts/e2e/E2E_OUTPUTS.md`
