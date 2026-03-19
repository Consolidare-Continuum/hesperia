<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# HESPERIA — Repository Features Encoded (Gena Report)

**Generated:** Pre-freeze consolidation view.  
**Scope:** Entire repo; active execution stack and supporting systems.  
**Reference:** AGENTS.md, canonical top-level structure (core, runtime, lexicon, tools, assets, tests, docs, legacy).

---

## 1. Top-level layout

| Root       | Role |
|-----------|------|
| **core/** | Deterministic computation: layers L1–L9, math, attribution, stability, policy, contracts, topology, propagation (shadow, R1–R4 segmenters/units, guards). |
| **runtime/** | Execution pipelines, orchestration, API server, dossier, provenance. |
| **sphere/** | Orchestration and sphere-specific logic: pipeline (L1–L10 + USF), interpretation, propagation, prolog, guards, shadow, dynamism, metrics, geometry, diagnostics, interfaces. |
| **lexicon/** | Dictionary systems (Dict A/B), build, curated, frozen, validation. |
| **tools/** | Developer utilities, calibration data, diagnostics, scripts. |
| **assets/** | Runtime/static artifacts (e.g. `assets/artifacts/e2e/`). |
| **tests/** | Pytest unit and integration suites. |
| **docs/** | Specs, architecture, governance, refactor notes. |
| **legacy/** | Archived code; not part of active execution. |

---

## 2. Core — encoded features

### 2.1 Layers (L1–L9)

- **Registry:** `runtime/pipeline/layer_registry.py` — single ordered list L1→L9; pipeline imports only from here.
- **Contract:** `core/contracts/layer_contract.py` — `LayerInput` (text, tokens, metadata), `LayerOutput` (layer_id, result, diagnostics). Every layer exposes `run(input: LayerInput) -> LayerOutput`.
- **Layer 1:** Coverage, dominance, entropy, Gini, area spread, family hit vector, profile metrics (optional structure profile).
- **Layer 2:** Traversal on stub adjacency (F×A), visited IDs, reach ratio, clustering, cross-area ratio, loop count, geometric stability.
- **Layer 3:** Shadow comparison (baseline vs shadow), deltas (coverage, dominance, entropy, traversal), acceptability gate.
- **Layer 4:** Retrieval (baseline/shadow), evidence metrics, area vector, family→area, adjacency, area sequence.
- **Layer 5:** Anti-region, contradiction pressure, reality gates, trig/geometry residuals.
- **Layer 6:** Dynamism: trajectory, transition matrix, curvature, jump rate, Lyapunov, stability score, coherence.
- **Layer 7:** Consistency gates, trust tier, decision status code, output trust tag.
- **Layer 8:** SI (scale-invariant) metrics, policy mode, interpretation scope, rounding/clamp policies.
- **Layer 9:** Bands, pillars, BRAND_WORD_* (trust, evidence, contradiction, geometry, shadow), actions.

**Defaults / structure profile:** `core/layers/defaults.py`, `structure_profile.py` — F, A, eps, MAX_ALLOWED_DEPTH, TOP_K, etc.; profile load/validate/checksum.

### 2.2 Core math (deterministic primitives)

- **core/math:** Entropy, normalized entropy; stability index, structural tension; curvature, jump rate; transition matrix and probabilities; trajectory build/compress; loopability; vector ops (dominant area/family, family peaks); coverage (family, area); diffusion step; conservation check; normalization (L1), matrix row_normalize.  
- **Rule:** Sphere layers use `core.math` for numerics; no math logic in sphere.

### 2.3 Attribution

- **core/attribution/structural.py:** `normalize`, `tokenize`, `load_dict_a`, `load_dict_b`, `attribute`, `aggregate_dominant`, `build_region_seed`, `run_attribution_pipeline`.
- **core/attribution (v06 / shared):** Attribution pipeline, surface map (Dict A v0.6), text cap, attribute with surface for R1–R4.

### 2.4 Stability (Δ)

- **core/stability/stability_delta.py:** `run_stability(layers)` — reads L1–L6, returns anomaly flags (AREA_COLLISION, FAMILY_DRIFT, CURVATURE_SPIKE, PROPAGATION_LOOP), corrective_bias, confidence_adjustment. Non-destructive; feeds L7.

### 2.5 Policy

- **core/policy/interpretation_policy.py:** `apply_interpretation_policy(state, mode)` — STRUCTURE_ONLY / STRUCTURE_PLUS_CONTEXT; sets policy and interpretation scope for L8.

### 2.6 Contracts

- **core/contracts/layer_contract.py:** LayerInput, LayerOutput (single entry point per layer).

### 2.7 Topology

- **core/topology/invariant_catalog.py:** Coordinate mapping (forward/inverse), validate_coord, validate_side_id (F×A geometry).

### 2.8 Propagation (core)

- **Shadow layer:** ShadowFailureCode, ShadowMetrics, shadow mass/scores, candidate_set_shadow, ShadowLayerState/Input/Output, process_step.
- **R1–R4:** Segmenters (segment_by_sentences, paragraphs, chapters, book; get_text_span), ESM defaults, contradiction graph, unit builder (`build_unit`), theta gate, gamma guard.
- **Guard pipeline:** `run_pipeline` (degraded detection, shadow layer application) — used by analyze path.
- **Safeguard:** TraversalStatus, SafeguardStopPayload, TraversalSafeguard, run_traversal_with_safeguard.
- **Output/invariant:** to_minimal_operational_result, make_error_result; invariant_enforcer (geometry, bijection, output contract, clamp_domain).

---

## 3. Sphere — encoded features

### 3.1 Pipeline

- **sphere/pipeline/pipeline_runner.py:** `run_pipeline(raw_text, config, document_id)` — L1–L9 via registry, stability before L7, interpretation policy before L8; then propagation (topology-driven), shadow correction, structural logic (L9), interpretation (L10), optional prolog, USF generation, guards. Returns document_id, layer_outputs, usf, pipeline_metadata, diagnostics, shadow_metrics, logic_metrics, interpretation_metrics, prolog_logic, guards.
- **Contract validation:** Per-layer required keys; validate_layer_input/output, validate_pipeline_contracts.
- **Isolation validation:** Snapshot layer output, validate no upstream mutation, validate_layer_isolation.

### 3.2 USF (Unit Summary Format)

- **sphere/usf:** generate_usf, build_usf_object, validate_usf_inputs; drift score (compute_drift_score); compare_usf, serialize_usf_to_json, save_usf_json.

### 3.3 Interpretation (L10)

- **sphere/interpretation:** compute_interpretation_metrics; build_interpretation_diagnostics, build_interpretation_flags; event_summarizer (extract_active_events, build_event_summary); state_classifier (classify_structural_state, entropy_state, tension_state, propagation_state).

### 3.4 Propagation (sphere)

- **sphere/propagation:** compute_propagation (engine); diffuse_once, apply_damping, build_propagation_matrix, propagate_area_vector (diffusion); family_projection, project_area_to_families, propagate_family_counts; build_propagation_diagnostics; weighting (edge weight matrix, stability/jump-rate modulation, effective diffusion rate).

### 3.5 Prolog logic

- **sphere/prolog_logic:** compute_prolog_inference (metrics→facts, inference, trace); inference_executor (evaluate_rule, derive_new_facts, infer). Optional in pipeline via `enable_prolog`.

### 3.6 Logic (structural rules)

- **sphere/logic:** compute_logic_metrics; rule_engine, rule_evaluator, rule_registry (dominant_area, entropy_drop, tension_increase, propagation_spread, dominance_transition); build_diagnostic, build_structural_diagnostics, build_logic_diagnostics.

### 3.7 Shadow (sphere)

- **sphere/shadow:** compute_shadow_correction; apply_tail_suppression, stabilize_entropy, apply_dominant_area_reinforcement; build_shadow_diagnostics.

### 3.8 Dynamism

- **sphere/dynamism:** compute_dynamism; build_trajectory, compress_trajectory; transition_matrix, curvature, jump_rate, compute_stability_index.

### 3.9 Metrics (sphere)

- **sphere/metrics:** entropy, coverage (family/area), dominance (detect_dominant_area/family, family_peaks), tension, loopability; aggregate_structural_metrics (for USF raw_metrics).

### 3.10 Geometry

- **sphere/geometry:** validate_topological_boundaries; load_family_geometry, load_area_geometry, build_geometry_index.

### 3.11 Diagnostics

- **sphere/diagnostics:** run_diagnostics; detect_rhetorical_instability, detect_structural_monotony, detect_structural_anomalies.

### 3.12 Guards

- **sphere/guards:** run_all_guards (sigma, gamma, theta); sigma_validator (invariants: path, length, matrix 12×12, symmetric, no_nan, non_negative, closed [0,1], area_id); gamma_validator (validate_gamma_invariants); theta_governance (evaluate_theta_governance, builtin rules).

### 3.13 Interfaces

- **sphere/interfaces:** analyze_text (structural_api); get_usf, serialize_usf, save_usf, compare_usf (usf_api); debug_pipeline (debug_interface); validate_text_input, validate_config, validate_layer_request (interface_validation).

---

## 4. Runtime — encoded features

### 4.1 Pipelines

- **run_l1_through_l9:** Delegates to sphere.pipeline.run_pipeline when no profile; maps to L1..L9 + diagnostics + usf, interpretation_metrics, prolog_logic, guards, pipeline_metadata, shadow_metrics, logic_metrics. Legacy path: profile-based local L1–L9 loop.
- **run_e2e_all:** run_e2e_sentence (analyze), run_e2e_l1_l9, run_e2e_r1_r4, run_e2e_sphere_math_values, run_e2e_sphere_math_100; writes to assets/artifacts/e2e (or --out-dir).
- **run_sphere_math_values:** Core-only L1–L9 values run; writes one JSON (--out, --profile, --text).
- **run_sphere_math_100_sentences:** L1–L9 per sentence over calibration_100_sentences (tools/calibration/data); --sentences, --limit.
- **r1_r4_pipeline:** segment_by_* (R1 sentence, R2 paragraph, R3 chapter, R4 book), L1–L9 per segment, build_unit, aggregate level_averages and scale_deltas; run_r1_pipeline, run_full_pipeline, run_r1_pipeline_to_json, run_full_pipeline_to_json.
- **analyze:** Text → attribution (v06 or shared) → guard_pipeline → 6-key minimal result + extended; optional r1_r4 (units + book_profile).
- **Other runners:** run_reference_pipeline (canonical sphere run_pipeline CLI); run_l1_l2, run_l1_l2_l3; run_r1_r4_pipeline; run_e2e_sentence; batch_runner.

### 4.2 Pipeline state / registry

- **pipeline_state.py:** PipelineState (layers, diagnostics).
- **layer_registry.py:** LAYERS = [(1, layer_1), …, (9, layer_9)].
- **reading_scales.py:** R1–R4 scale definitions.

### 4.3 API

- **runtime/api/main.py:** FastAPI — GET /health, POST /hesperia/analyze (Bearer auth, HESPERIA_API_KEY); OpenAPI 3.x; text-only body; 6-key + extended result.

### 4.4 Dossier / provenance

- **runtime/dossier:** index_manager, compare_dossiers, validate_schema (dossier_schema_v1).
- **runtime/provenance:** run_manifest, provenance_info.

---

## 5. Lexicon — encoded features

- **curated:** A_CORE_STAR_MAP (v1, v0.4.1.x), DICT_A_SURFACE_MAP, B_SURFACE_LEX_FIELD, FAMILY_SPEC_v0.6, FREEZE_RECORD, checksums.
- **frozen:** v06 (dict_a_v06, family_prior_v06, calibration_stats); legacy A/B maps and SHA256.
- **build:** Dict A/B build scripts (definitions v0412/v0413/v0414), preprocess (scowl, oewn, wiktionary), ingest_lexical_to_chroma, generate_families_yaml, build_family_spec_v060, sync_curated_to_assets, ci_lexical.
- **validation:** validate_lexical, validate_dict_a, audit_dict_a_runtime.

---

## 6. Tools

- **tools/calibration/data:** calibration_100_sentences.json (used by run_sphere_math_100_sentences and e2e).
- **tools/diagnostics, tools/scripts:** Developer utilities and operational helpers (structure per AGENTS.md).

---

## 7. Assets

- **assets/artifacts/e2e:** Default output directory for run_e2e_all: run_output_e2e_sentence.json, run_output_e2e_l1_l9.json, run_output_e2e_r1_r4.json, run_output_e2e_sphere_math_values.json, run_output_e2e_sphere_math_100.json.

---

## 8. Tests — encoded coverage

- **test_e2e_flows.py:** analyze, L1–L9, R1–R4, sphere_math_values, sphere_math_100, run_e2e_all artifacts.
- **Pipeline:** test_pipeline_execution (all nine layers, L7/L9 reportable keys), test_prolog_toggle, test_stability_layer, test_interpretation_policy; propagation layer7 integration; pipeline contracts, determinism, isolation.
- **Fingerprint:** golden, drift, determinism.
- **Layers, logic, interpretation, shadow, propagation, topology, geometry, prolog, usf, golden, determinism, attribution, dossier, architecture:** Dedicated test modules under tests/.

---

## 9. Docs — encoded specs and design

- **docs/architecture:** propagation_layer, math_layer, interpretation_layer, logic_layer, shadow_layer, ENGINE_BOUNDARIES, SYSTEM_OVERVIEW.
- **docs/specs:** schema, profiles (TAXONOMY_v1), project (charter, risk, schedule, security, observability, handoff, ARTIFACT-INDEX), governance tasks, history (CONCEPTS, SPECs, REPORTs), releases.
- **legacy/docs/refactor_notes:** propagation_design, prolog_extension, interpretation_usf_consolidation, logic_engine_design, math_reintegration_audit, fingerprint_validation, multistep_propagation, prolog_fact_schema.
- **docs:** R1_R4_BAND_DECISION_CODE_MAPPING, FREEZE_v0_6, DICT-A-SCAFFOLD-NOTE, REPORT math consolidation, etc.

---

## 10. Summary table — feature areas

| Area | Encoded features |
|------|------------------|
| **Layers** | L1–L9 deterministic stack; contract (LayerInput/LayerOutput); registry; structure profile & defaults. |
| **Math** | Entropy, stability, curvature, jump rate, transition matrix, trajectory, loopability, coverage, vector ops, diffusion, conservation (core.math). |
| **Attribution** | Normalize, tokenize, Dict A/B load & attribute, aggregate dominant, R1–R4 surface attribution. |
| **Stability** | Δ stability (anomaly flags, corrective bias) after L6, input to L7. |
| **Policy** | Interpretation policy (structure-only / structure+context) for L8. |
| **Propagation** | Core: shadow layer, R1–R4 segmenters/units/ESM/contradiction/guards; Sphere: diffusion, family projection, weighting, compute_propagation. |
| **USF** | Generate, validate, build, drift, compare, serialize, save. |
| **Interpretation** | L10 metrics, diagnostics, flags, event summary, state classification. |
| **Prolog** | Optional inference from metrics; fact/rule evaluation. |
| **Logic** | Structural rules (dominance, entropy, tension, propagation, transition); diagnostics. |
| **Shadow (sphere)** | Correction, suppression, entropy stabilization, dominance reinforcement. |
| **Dynamism** | Trajectory, transition matrix, curvature, jump rate, stability index; compute_dynamism. |
| **Guards** | Sigma (invariants), Gamma (invariants), Theta (governance); run_all_guards. |
| **Geometry** | Boundary validation; family/area geometry load and index. |
| **Diagnostics** | Instability, monotony, anomaly detection; interpretation/shadow/propagation/logic diagnostics. |
| **Interfaces** | analyze_text, USF get/serialize/save/compare, debug_pipeline, input/config/layer validation. |
| **R1–R4** | Sentence/paragraph/chapter/book segmentation; L1–L9 per segment; unit build; book_profile aggregation. |
| **E2E** | Sentence (analyze), L1–L9 (full sphere + USF/interpretation/prolog/guards), R1–R4, sphere_math_values, sphere_math_100; all persist to assets/artifacts/e2e. |
| **API** | FastAPI /health, POST /hesperia/analyze (Bearer), 6-key + extended. |
| **Lexicon** | Curated/frozen Dict A/B, family spec, build and validation pipelines. |

This report reflects the repository state at report generation; for authoritative layout and scope, see **AGENTS.md**.
