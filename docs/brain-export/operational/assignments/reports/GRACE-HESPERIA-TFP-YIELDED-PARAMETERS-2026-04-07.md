# Grace — Parameters Hesperia yields (outputs) when TFP runs

**Root table (Ethan):** `HESPERIA-TFP-YIELDED-PARAMETERS-TABLE.md` (repo root).  
**Date:** 2026-04-07  
**Companion:** `GRACE-HESPERIA-TFP-RUNTIME-VARIABLES-2026-04-07.md` (inputs / env).  
**Scope:** Fields the engine and modules **write into context** or **return** on a run that includes the TFP module, plus which of those are **calibratable** via assets (dict packs, JSON calibration, matrices, anchors) vs fixed in code.

---

## Clinical / process lens on yielded data (one sentence each)

- **Iteration:** Yielded **per-request** scores and tags reflect **one analyzed slice** (or duplicated slice for default loop detection), not a stored multi-turn **iteration index** in the public TFP bundle unless the integration layer passes a richer `signals` timeline into a different code path.
- **Session:** **`input.signals`** and any attached **DLCR / dialog bundles** are the only session-shaped inputs echoed or merged into context; the sealed **`tfp_vector` / `tfp_profile` / `tfp_conflicts`** triple does not embed a full session transcript by itself.
- **Client iterations perspective:** All lexical-derived scores ultimately trace to **one `input.text`** (after optional clinical role stripping), so yielded **family/area/concept** structure is **client-utterance-centric** unless upstream supplies pre-merged dialog in signals.
- **Therapist iterations perspective:** Default **`tfp_profile`** and **`tfp_conflicts`** do **not** include therapist-turn labels; **`classify_intervention`** outputs exist only on code paths that supply **`therapist_utterances`** to loop detection, which **`TFPModule.project`** does not do today.
- **Interference / answer across client–therapist iterations:** Surfaced mainly as **`interaction_loop`** entries in **`tfp_conflicts`** and, on full loop APIs, structured loop records with **intervention_type** / **projective_identification_signal** when a real timeline plus therapist lines are provided.
- **Shift (client → therapist → client):** **Not** emitted as a dedicated field; detecting shift requires **comparing multiple run outputs** or a higher layer that builds a timeline and calls extended math, not a single **`tfp_profile.stage`** string alone.

---

## General — aggregated and cross-module yields

After `HesperiaEngine.run` completes the **project** phase for all modules, **`aggregate_modules`** runs and updates top-level context (see `hesperia/engine/aggregation.py`, `hesperia/engine/core.py`).

- **`areas`** — Normalized merged map of **area id → weight** combining each module payload’s **`area_scores`** according to **`aggregation_strategy`** and per-module **weight** / **priority**.
- **`families`** — Same for **`family_scores`** payloads (keys often **`A#_F#`** style composite family slots).
- **`metrics`** — Flat merge of **`metrics`** dicts from module payloads (later keys overlay earlier where both define the same name).
- **`signals.tfp_conflicts`** — Sorted deduplicated list of strings taken from every module payload’s **`tfp_conflicts`** (TFP module is the primary contributor when loaded).
- **`modules.<module_name>`** — Opaque per-module output bags (e.g. lexical **`concept_hits`**, NLP **`tokens`**, dict **scores**); shape is contract-defined per module, not rewritten by aggregation.
- **`input`** — Carries **`text`** and validated **`signals`** as provided to **`build_context`**.
- **`meta.trace`** — Ordered list of module phase executions with **errors**, **outputs** key lists, and hashes per phase for reproducibility auditing.
- **`meta.execution_graph`** — Which modules ran in **preprocess / project / postprocess** order.
- **`meta.hash_<phase>`** / **`meta.hash_aggregated`** — Fingerprints of frozen context after phases for determinism checks.

**Invariant activation bundle** (when **`build_invariant_tfp_activation`** / **`build_invariant_activation`** is used on a marker path, not the minimal **`compute_tfp_bundle`** alone): yields **`concepts`**, **`families`**, **`areas`** (probability vector over **`AREA_IDS`**), **`areas_raw`**, **`areas_inhibited`**, **`areas_final`**, pre/post-hex family and concept weight maps, **`hex_*`** activations, **`hex_feedback_delta`**, **`invariant_activation`** metadata block, and optionally **`propagation_trace`** / **`families_propagated`** / **`areas_propagated`** when sphere embedding propagation succeeds (`hesperia/nlp/tfp_activation.py`).

---

## TFP module — `tfp.v1` yields (`hesperia/modules/tfp/v1.py` → `compute_tfp_bundle`)

- **`modules["tfp.v1"]["tfp_vector"]`** — Dict mapping **configured labels** (default **control, aggression, identity, trust**) to **non-negative weights** summing to **1** after normalizing folded **family_scores** into label buckets by round-robin over sorted family keys.
- **`modules["tfp.v1"]["tfp_profile"]["dominant"]`** — The label key with maximum mass in **`tfp_vector`**, or **null** if empty.
- **`modules["tfp.v1"]["tfp_profile"]["confidence"]`** — Scalar **max** mass across **`tfp_vector`** (dominance strength, not statistical confidence).
- **`modules["tfp.v1"]["tfp_profile"]["stage"]`** — One of **`chaotic`**, **`defense_clarification`**, **`interpretation`**, **`integration`** from **`detect_tfp_stage(area_scores, family_scores)`** using **fixed numeric thresholds** on **A2/A3/A4/A7** (`hesperia/engine/tfp_math.py`).
- **`modules["tfp.v1"]["tfp_profile"]["affect_intensity"]`** — **0–1** scalar from **`estimate_affect_intensity(text, tokens)`** (regex + token heuristics, **not** from calibration JSON).
- **`modules["tfp.v1"]["tfp_profile"]["confidence_scores"]`** — Nested structure with **per-area / per-family / per-concept** rounded masses plus **dominant_*_confidence** and **level_confidence** entropy-style summaries (`compute_confidence_scores`).
- **`modules["tfp.v1"]["tfp_conflicts"]`** — List of **label names** whose **`tfp_vector`** mass **exceeds 0.4**, plus one **`interaction_loop`** string per loop record from **`detect_interaction_loops`** on the **synthetic two-step** timeline (default call passes **no** therapist utterances).

---

## Calibratable vs fixed (governance-relevant)

**Calibratable** (change assets or module config, then validate / pin per **`VERSION.yaml`** and **`HESPERIA_CALIB_DICT_VERSION`**):

- **Dict pack under `assets/calibration/dicts/<version>/`** — **Dict A/B** rows (concept ids, **family_ids**, **area_ids**, confidence, negative patterns) directly change **`concept_hits`** and upstream **family_scores** / **area_scores**, hence everything downstream including **`tfp_vector`** and **`stage`**.
- **`signal_calibration_v2.json`** (mainline under **`assets/data/engine_dynamics_v060/semantic_dynamics/`**, legacy **`.../tfp/tfp_signal_calibration_v2.json`**) — Drives **invariant activation** path: **concept_cap**, **log_normalization_enabled**, **segment_length_normalization**, **hex_decay**, **hex_smoothing_alpha**, **area_softmax_temperature**, **temporal_momentum**, **session_topology_defaults**, curve and negation fields consumed via **`get_default_session_topology_run_params`** (`hesperia/engine/tfp_signal_calibration.py`, `hesperia/engine/engine_signal_calibration.py`).
- **Area inhibition matrix JSON** (name from calibration’s **`inhibition_matrix_file`**, e.g. **`area_inhibition_matrix_main_v1.json`**) — **12×12** off-diagonal weights applied before softmax in invariant path.
- **Hex anchors** — **`concept_hex_anchors_tfp.json`** (fallback **`concept_hex_anchors.json`**) maps concepts to hex cells for **hex feedback** scaling in invariant activation.
- **`TFPModule.configure({"labels": [...]})`** — Changes **`tfp_vector`** keys and folding semantics (YAML **`module_config`** for **`tfp.v1`**).

**Mostly fixed in code** (calibrate only by **code change** or future extract-to-config work):

- **`detect_tfp_stage`** thresholds and **`estimate_affect_intensity`** lexicon/patterns.
- **`detect_interaction_loops`** escalation / accusation thresholds and **`classify_intervention`** regex sets.
- **`tfp_vector`** **0.4** conflict cutoff and **round-robin** label assignment from families.
- **`compute_confidence_scores`** entropy formula.

**Mixed:** Upstream **normalization** of empty area scores (**uniform fill**) in **`normalize_area_scores`** is code-default; **which areas exist** in invariant path is pinned by calibration **`area_ids`**.

---

## Cross-references

- **Runtime variables table (repo root):** `HESPERIA-TFP-RUNTIME-VARIABLES-TABLE.md`.  
- Input env narrative: `operational/assignments/reports/GRACE-HESPERIA-TFP-RUNTIME-VARIABLES-2026-04-07.md`.  
- Dict resolution: `hesperia/docs/HESPERIA_TFP_MODULE_DICTS.md`, `hesperia/docs/governance/TFP_RESOLUTION_CONTRACT.md`.  
- TFP env allowlist: `hesperia/docs/governance/TFP_ENV_FLAGS_V1.md`.

`SIGNED: Grace (triage) | Hesperia TFP yielded outputs | 2026-04-07 | GRACE-HESPERIA-TFP-YIELDED-PARAMETERS`
