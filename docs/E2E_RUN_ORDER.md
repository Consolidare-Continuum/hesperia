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

**Product-only E2E (Task 4):** minimal sealed proof — one text → `run_structural_analysis` (projection inside service) → schema guard → `run_output_e2e_product_surface.json`:

```bash
python3 -m runtime.pipeline.run_e2e_product
```

See `docs/PUBLIC_PRODUCT_SURFACE.md`.

## Execution order (what runs after what)

| Step | Output file | What runs | Primary modules |
|------|-------------|-----------|-----------------|
| 1 | `run_output_e2e_sentence.json` | Lexicon analyze: 6-key result, extended (dict_b, family vectors truncated), R1–R4 in extended | `runtime.pipeline.analyze` |
| 2 | `run_output_e2e_l1_l9.json` | Sphere **L1–L9** full pipeline (USF, interpretation, prolog, guards, diagnostics) + **`narrative_microstructure_e2e`** (hex product maps + Option A + TFP slice) | `run_l1_through_l9` → `sphere.pipeline` · **`hex_outputs.e2e_integration`** |
| 3 | `run_output_e2e_r1_r4.json` | **R1–R4** reading-scale pipeline only (units + book_profile) | `runtime.pipeline.r1_r4_pipeline` |
| 4 | `run_output_e2e_sphere_math_values.json` | L1–L9 **numeric layer values** for the same text | `runtime.pipeline.run_sphere_math_values` |
| 5 | `run_output_e2e_sphere_math_100.json` | Sphere math over first **3** calibration sentences (smoke; distinct file from full batch below) | `runtime.pipeline.run_sphere_math_100_sentences` |
| 5b | `run_output_e2e_calibration_100_structural.json` | Structural batch (L1–L9 public projection) per sentence — **N** sentences (default **100**, `tools/calibration/data/calibration_100_sentences.json`) | `run_structural_analysis_batch` |
| 5c | `run_output_e2e_calibration_100_summary.json` | Aggregates: dominant area/family histograms, mean L1 coverage & stability, token stats | derived from 5b |
| 6 | `run_output_e2e_domain_metrics.json` | Structural analysis **with domain metrics**: matched tokens → KME bridge → 6 primitives, 35 derived, 41 fingerprint + hash | `runtime.services.analysis_service` / `sphere.pipeline` + `hesperia.engine.kme` |
| 7 | `run_output_e2e_session_kme.json` | **Session NLP** → clinical ActiveGraph → **KME** (primitives, derived, fingerprint) + **TRIZ** signals | `hesperia.nlp.session_parser` → `hesperia.engine.kme.clinical_bridge.run_session_kme_pipeline` |
| 8 | `run_output_e2e_triz_complete.json` | Same session activation → **TRIZ complete** (contradictions, topology, reports, commercial_intel); `csv_exports` stored as byte lengths only | `hesperia.extensions.triz.pipeline.run_triz_analysis_complete` |
| 9 | `run_output_e2e_session_topology.json` | **Clinical session topology**: windowed segments, area transitions, aggression curve, defense timeline (segments capped in JSON). Raw engine shape — not passed through public projection. | `research.clinical_tfp.session_topology.run_session_topology` |
| 10 | `run_output_e2e_tfp_smoke.json` | **TFP testing stack (Gena wiring):** batch structural (CLI `batch-analyze` parity) on smoke sessions + `analyze_session` + propagation + **`detect_tfp_stage`** + **`analyze_session_speaker_aware`** + **`session_hex_microstructure_tfp`** (per-session hex analytics + Option A + TFP provenance). | `runtime.services.analysis_service` · `hesperia.nlp.session_parser` · `research.clinical_tfp.stage_detection` · **`hesperia.engine.hex_outputs.e2e_integration`** |
| 10b | `run_output_e2e_hex_microstructure_tfp.json` | **Full hex microstructure artifact:** primary E2E text + every TFP smoke session — microstructure maps, **Option A** hex-primary closure summary, **TFP** embedding / families_structure provenance. | **`hex_microstructure_bundle_for_text`** |
| 10c | `run_output_e2e_sealed_multiscale.json` | **Sealed stack:** hex activation → **local microphysics** → **hex_family_bridge** → family/area vectors → **product_signals** → **hspr_index** (`hesperia.engine.sealed_multiscale_stack`). Optional TRIZ contradiction: `HESPERIA_SEALED_E2E_TRIZ=1`. | **`run_sealed_multiscale_stack`** |
| **10d** | `run_output_e2e_dlcr.json` | **Optional** (`HESPERIA_E2E_DLCR=1`). Full **`run_dlcr_pipeline`** bundle for the primary E2E text (L0→L6 + segment trajectory). | `hesperia.engine.lexical_concept.pipeline` |
| 11 | `run_output_e2e_capability_matrix.json` | **Gena full-picture sweep** + **`semantic_field_and_hci`** (ontology semantic field smoke + HCI scalar); structural stages, shipping compare, clinical + enhanced NLP, transcript parse, evaluation baselines, TRIZ, **KME** **`run_document`** + **`run_corpus`**; **`batch_runner`**, **`mvp_acceptance`**, **`experiment_runner`**. Multiscale if `HESPERIA_E2E_MULTISCALE=1`. Includes **`dlcr_pipeline`** block. | `run_e2e_capability_matrix` |
| 11a | `run_output_e2e_semantic_field.json` | **Semantic field engine:** ontology → `matrix_builders` → `equations` → convergence; `runtime/configs/semantic_field_ontology_example.json` (timeline truncated in artifact). | `runtime.semantic_field.run_semantic_field` |
| 11b | `run_output_e2e_field_calibration.json` | **HCI grid calibration** (mini 2×2×… grid, ontology matrices). | `runtime.semantic_field.run_field_calibration` |
| 11c | `run_output_e2e_field_calibration_best.json` | Best candidate + `area_field_final`. | same |
| 11d | `run_output_e2e_field_calibration_topk.json` | Top-k ranked rows. | same |
| **12** | `run_output_e2e_field_dynamics.json` | **Optional** (`HESPERIA_FIELD_DYNAMICS=1`). Ethan phases + **`semantic_field_v1`** bundle (`HESPERIA_SEMANTIC_FIELD_EQUATIONS_V1` set during run). | `hesperia.extensions.dynamics` |

## Dependency mental model

```
Steps 1–4 + 5–5c: runtime + sphere; step 5 is 3-sentence smoke, **5b–5c** full calibration batch (default 100 sentences).
Step 6:     sphere structural match → synthetic domain graph → KME fingerprint.
Steps 7–9:  hesperia NLP session parse → engine (KME/TRIZ/clinical).
Steps 11a–11d: semantic field stack (ontology matrices, HCI) — always on.
Step 12:    optional Ethan field dynamics + v1 semantic field equation artifact.
```

## Machine-readable list

Tuple **`E2E_OUTPUTS`** mirrors steps 1–11d (**19** files incl. hex microstructure TFP + **sealed multiscale**). Step 12 uses **`E2E_OUTPUT_FIELD_DYNAMICS`** when the env flag is set → **20** files with dynamics. **Optional step 10d:** **`E2E_OUTPUT_DLCR`** when `HESPERIA_E2E_DLCR=1` adds one more file → **20** total without field_dynamics (**19+dlcr**), **21** with field_dynamics (**19+field_dynamics+dlcr**).

## Full encompassing pipe (all E2E artifacts + product + physics + system seal)

Single orchestrator — **same directory** for every JSON + **manifest** with SHA256 index:

```bash
python3 -m runtime.pipeline.run_e2e_full_stack [--out-dir DIR] [--text "..."] [--calibration-batch-n N]
#   [--no-dynamics] [--skip-physics] [--skip-seal]
```

- Runs **`run_e2e_all`** (with dynamics + multiscale env by default — Ethan field bundle when applicable).
- Writes **`run_output_e2e_full_product_surface.json`** (`run_structural_analysis` + schema guard).
- Runs **`python3 -m tests.physics_validation.run_all`** then **`run_system_seal_gate`** (skips duplicate physics pytest if validation already passed).
- Emits **`run_output_e2e_full_stack_manifest.json`** (`artifacts[]` with `path`, `bytes`, `sha256`, plus `system_seal`, `steps`, `ok`).

Shell wrapper (same defaults; fast mode skips physics/seal/dynamics env):

```bash
./tools/e2e_full_deliverables.sh
# HESPERIA_E2E_FULL_DELIVERABLES_FAST=1 ./tools/e2e_full_deliverables.sh   # smaller / no seal
```

Writes e.g. `assets/artifacts/e2e_full_deliverables/` (all `run_output_e2e_*.json` from `run_e2e_all` + product + manifest; **20+** files when field dynamics on).

## Verify

`test_e2e_run_e2e_all_produces_all_artifacts` enables field dynamics and checks **20** artifacts (19 base + field_dynamics); `test_e2e_run_e2e_all_optional_dlcr_artifact` adds **`HESPERIA_E2E_DLCR=1`** → **21** files. Calibration batch **N=5** in tests via env.

**TFP smoke:** `HESPERIA_TFP_DLCR=1` adds **`session_dlcr_bundles`** to `run_output_e2e_tfp_smoke.json`.

```bash
python3 -m runtime.pipeline.run_e2e_all
pytest tests/test_e2e_flows.py tests/nlp/test_role_direction_and_temporal.py::test_detect_tfp_stage -v
```
