<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
See LEGAL_NOTICE.md for full terms.
-->

# E2E run order (single session)

One command runs **all** stages in a fixed sequence:

```bash
python3 -m runtime.pipeline.run_e2e_all [--out-dir DIR] [--text "…"]
```

Default text is shared across stages (unless overridden). Default artifact dir: `assets/artifacts/e2e/`.

## Execution order (what runs after what)

| Step | Output file | What runs | Primary modules |
|------|-------------|-----------|-----------------|
| 1 | `run_output_e2e_sentence.json` | Lexicon analyze: 6-key result, extended (dict_b, family vectors truncated), R1–R4 in extended | `runtime.pipeline.analyze` |
| 2 | `run_output_e2e_l1_l9.json` | Sphere **L1–L9** full pipeline (USF, interpretation, prolog, guards, diagnostics) | `runtime.pipeline.run_l1_through_l9` → `sphere.pipeline.pipeline_runner` |
| 3 | `run_output_e2e_r1_r4.json` | **R1–R4** reading-scale pipeline only (units + book_profile) | `runtime.pipeline.r1_r4_pipeline` |
| 4 | `run_output_e2e_sphere_math_values.json` | L1–L9 **numeric layer values** for the same text | `runtime.pipeline.run_sphere_math_values` |
| 5 | `run_output_e2e_sphere_math_100.json` | Sphere math over first *N* calibration sentences (default limit 3) | `runtime.pipeline.run_sphere_math_100_sentences` |
| 6 | `run_output_e2e_domain_metrics.json` | Structural analysis **with domain metrics**: matched tokens → KME bridge → 6 primitives, 35 derived, 41 fingerprint + hash | `runtime.services.analysis_service` / `sphere.pipeline` + `hesperia.engine.kme` |
| 7 | `run_output_e2e_session_kme.json` | **Session NLP** → clinical ActiveGraph → **KME** (primitives, derived, fingerprint) + **TRIZ** signals | `hesperia.nlp.session_parser` → `hesperia.engine.kme.clinical_bridge.run_session_kme_pipeline` |
| 8 | `run_output_e2e_triz_complete.json` | Same session activation → **TRIZ complete** (contradictions, topology, reports, commercial_intel); `csv_exports` stored as byte lengths only | `hesperia.engine.triz.pipeline.run_triz_analysis_complete` |
| 9 | `run_output_e2e_session_topology.json` | **Clinical session topology**: windowed segments, area transitions, aggression curve, defense timeline (segments capped in JSON). Raw engine shape — not passed through public projection. | `hesperia.clinical.session_topology.run_session_topology` |

## Dependency mental model

```
Steps 1–5: runtime + sphere layers (mostly independent reads of the same text).
Step 6:     sphere structural match → synthetic domain graph → KME fingerprint.
Steps 7–9:  hesperia NLP session parse → engine (KME/TRIZ/clinical) — independent of step order
            among themselves but placed after sphere batch for a clear “runtime first, engine second” story.
```

Steps 7–8 both call `analyze_session` on the same text (duplicate parse acceptable for clarity and isolation).

## Machine-readable list

Tuple `E2E_OUTPUTS` in `runtime/pipeline/run_e2e_all.py` mirrors this table.

## Verify

```bash
python3 -m runtime.pipeline.run_e2e_all
pytest tests/test_e2e_flows.py -v
```
