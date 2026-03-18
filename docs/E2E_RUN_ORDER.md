<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
See LEGAL_NOTICE.md for full terms.
-->

# E2E run order (single session)

One command runs **all** stages in a fixed sequence:

```bash
python3 -m runtime.pipeline.run_e2e_all [--out-dir DIR] [--text "…"] [--calibration-batch-n N]
```

Default text is shared across stages (unless overridden). Default artifact dir: `assets/artifacts/e2e/`.  
**Calibration batch:** `run_output_e2e_calibration_100_structural.json` + `_summary.json` use **100** sentences by default; set **`HESPERIA_E2E_CALIBRATION_BATCH_N`** or **`--calibration-batch-n`** (max 500).

## Execution order (what runs after what)

| Step | Output file | What runs | Primary modules |
|------|-------------|-----------|-----------------|
| 1 | `run_output_e2e_sentence.json` | Lexicon analyze: 6-key result, extended (dict_b, family vectors truncated), R1–R4 in extended | `runtime.pipeline.analyze` |
| 2 | `run_output_e2e_l1_l9.json` | Sphere **L1–L9** full pipeline (USF, interpretation, prolog, guards, diagnostics) | `runtime.pipeline.run_l1_through_l9` → `sphere.pipeline.pipeline_runner` |
| 3 | `run_output_e2e_r1_r4.json` | **R1–R4** reading-scale pipeline only (units + book_profile) | `runtime.pipeline.r1_r4_pipeline` |
| 4 | `run_output_e2e_sphere_math_values.json` | L1–L9 **numeric layer values** for the same text | `runtime.pipeline.run_sphere_math_values` |
| 5 | `run_output_e2e_sphere_math_100.json` | Sphere math over first **3** calibration sentences (smoke; distinct file from full batch below) | `runtime.pipeline.run_sphere_math_100_sentences` |
| 5b | `run_output_e2e_calibration_100_structural.json` | Structural batch (L1–L9 public projection) per sentence — **N** sentences (default **100**, `tools/calibration/data/calibration_100_sentences.json`) | `run_structural_analysis_batch` |
| 5c | `run_output_e2e_calibration_100_summary.json` | Aggregates: dominant area/family histograms, mean L1 coverage & stability, token stats | derived from 5b |
| 6 | `run_output_e2e_domain_metrics.json` | Structural analysis **with domain metrics**: matched tokens → KME bridge → 6 primitives, 35 derived, 41 fingerprint + hash | `runtime.services.analysis_service` / `sphere.pipeline` + `hesperia.engine.kme` |
| 7 | `run_output_e2e_session_kme.json` | **Session NLP** → clinical ActiveGraph → **KME** (primitives, derived, fingerprint) + **TRIZ** signals | `hesperia.nlp.session_parser` → `hesperia.engine.kme.clinical_bridge.run_session_kme_pipeline` |
| 8 | `run_output_e2e_triz_complete.json` | Same session activation → **TRIZ complete** (contradictions, topology, reports, commercial_intel); `csv_exports` stored as byte lengths only | `hesperia.engine.triz.pipeline.run_triz_analysis_complete` |
| 9 | `run_output_e2e_session_topology.json` | **Clinical session topology**: windowed segments, area transitions, aggression curve, defense timeline (segments capped in JSON). Raw engine shape — not passed through public projection. | `hesperia.clinical.session_topology.run_session_topology` |
| 10 | `run_output_e2e_tfp_smoke.json` | **TFP testing stack (Gena wiring):** batch structural (CLI `batch-analyze` parity) on smoke sessions + `analyze_session` + propagation + **`detect_tfp_stage`** + **`analyze_session_speaker_aware`** on English dialogue. Input: `assets/testing/tfp_kernberg/session_transcripts_smoke_english.json` (inline fallback if missing). | `runtime.services.analysis_service` · `hesperia.nlp.session_parser` · `hesperia.clinical.stage_detection` |
| 11 | `run_output_e2e_capability_matrix.json` | **Gena full-picture sweep:** structural stages, shipping compare, clinical + enhanced NLP, transcript parse, evaluation baselines, TRIZ direct/corpora + **`run_triz_analysis`**, **`propagate_activation`**, product compare, ontology, temporal timeline; **KME** **`run_document`** + **`run_corpus`** (toy `DomainGraph`); **`batch_runner`** (2 dossiers, temp index); **`mvp_acceptance`** (benchmarks under `benchmarks/triz/`); **`experiment_runner`**. Multiscale if `HESPERIA_E2E_MULTISCALE=1`. | `run_e2e_capability_matrix` in `run_e2e_all.py` |
| **12** | `run_output_e2e_field_dynamics.json` | **Optional** (`HESPERIA_FIELD_DYNAMICS=1`). Full stack: **L4+L8+L5+L6**; **`l8_clusters`**, **`PHASE4`**. | `hesperia.engine.field_dynamics` |

## Dependency mental model

```
Steps 1–4 + 5–5c: runtime + sphere; step 5 is 3-sentence smoke, **5b–5c** full calibration batch (default 100 sentences).
Step 6:     sphere structural match → synthetic domain graph → KME fingerprint.
Steps 7–9:  hesperia NLP session parse → engine (KME/TRIZ/clinical) — independent of step order
            among themselves but placed after sphere batch for a clear “runtime first, engine second” story.
```

Steps 7–8 both call `analyze_session` on the same text (duplicate parse acceptable for clarity and isolation). Step 10 exercises TFP collateral without changing the main `--text` session story.

## Machine-readable list

Tuple `E2E_OUTPUTS` mirrors steps 1–11 (includes 5b–5c). Step 12 uses `E2E_OUTPUT_FIELD_DYNAMICS` when the env flag is set.

## Full stack (all dynamics deliverables)

Steps **1–12** (1–11 always; 12 with dynamics) with **L4+L8+L5+L6**, TRIZ → `c_sig`, Ξ proxy, optional multiscale:

```bash
./tools/e2e_full_deliverables.sh
# or see docs/specs/governance/GENA-DYNAMICS-INTEGRATION-ANALYSIS.md §8
```

Writes e.g. `assets/artifacts/e2e_full_deliverables/` (11 JSON incl. TFP smoke + field dynamics + state sidecars as applicable).

## Verify

`test_e2e_run_e2e_all_produces_all_artifacts` enables field dynamics and checks **14** artifacts (13 base + field_dynamics); calibration batch **N=5** in test via env.

```bash
python3 -m runtime.pipeline.run_e2e_all
pytest tests/test_e2e_flows.py tests/nlp/test_role_direction_and_temporal.py::test_detect_tfp_stage -v
```
