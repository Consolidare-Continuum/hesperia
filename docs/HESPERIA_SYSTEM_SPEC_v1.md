<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# HESPERIA System Specification v1

Canonical architecture spec for the HESPERIA engine. Single authoritative reference for layers, attribution, topology, propagation, dynamism, shadow, logic, interpretation, guards, USF fingerprint, and pipeline flow.

---

## 1. System overview

HESPERIA is a deterministic structural analysis engine: raw text → attribution → L1–L9 core layers → topology-driven propagation → shadow correction → structural logic → interpretation (L10) → USF and guards. No learning; all behavior is config-driven and reproducible. Active stack: **core/** (layers, math, attribution, stability, policy, contracts, topology, propagation), **runtime/** (pipelines, API), **sphere/** (pipeline orchestration, USF, interpretation, propagation, prolog, guards, shadow, dynamism, metrics, geometry, diagnostics, interfaces), **lexicon/** (Dict A/B, build, validation).

---

## 2. Architecture layers L1–L10

- **L1** Coverage, dominance, entropy, Gini, area spread, family hit vector; optional structure profile.
- **L2** Traversal on 12×12 area adjacency (stub or topology); visited IDs, reach ratio, clustering, cross-area ratio, loop count, geometric stability.
- **L3** Shadow comparison (baseline vs shadow); deltas (coverage, dominance, entropy, traversal); acceptability gate.
- **L4** Retrieval (baseline/shadow), evidence metrics, area vector, family→area, adjacency, area sequence.
- **L5** Anti-region, contradiction pressure, reality gates, trig/geometry residuals.
- **L6** Dynamism: trajectory, transition matrix, curvature, jump rate, Lyapunov, stability score, coherence.
- **L7** Consistency gates, trust tier, decision status code, output trust tag; consumes Δ stability (anomaly flags, corrective bias).
- **L8** Scale-invariant (SI) metrics, policy mode, interpretation scope, rounding/clamp policies.
- **L9** Bands, pillars, BRAND_WORD_* (trust, evidence, contradiction, geometry, shadow), actions.
- **L10** Structured interpretation: consumes L7/L8/L9; produces structural_state, entropy_state, tension_state, propagation_state, active_events, interpretation_flags, event_summary (used by USF and fingerprint).

Contract: every layer takes `LayerInput` (text, tokens, metadata) and returns `LayerOutput` (layer_id, result, diagnostics). Registry: `sphere.pipeline.layer_registry.LAYERS` (L1→L9). Validation: `sphere.pipeline.contract_validation`, `isolation_validation`.

---

## 3. Attribution system

- **Normalize / tokenize:** `core.attribution.structural` (normalize, tokenize).
- **Dict A / Dict B:** load_dict_a(assets_root), load_dict_b(); attribute(tokens, dict_a, dict_b) → matched (family, altitude), diagnostics.
- **Aggregation:** aggregate_dominant, build_region_seed; optional run_attribution_pipeline. v0.6/surface: attribution_shared, attribute_with_surface for R1–R4.
- **Output:** hits (288), matched, adjacency (from core.layers.build_canonical_stub_adjacency). Lexicon: curated/frozen Dict A/B, family spec; build and validation under lexicon/.

---

## 4. Topology model

- **Area adjacency:** 12×12 binary, symmetric, diagonal 0; loaded from `data/topology/area_adjacency_matrix.json` (or topology_data_root). No isolated nodes; graph connected.
- **Family→area:** 288 families → area index 0–11; `data/topology/family_to_area_map.json`. Canonical order family_001..family_288.
- **Graph:** build_topology_graph() → neighbors per area; used by propagation and Layer-4.

---

## 5. Propagation mechanics

- **Single step:** (1−α)v + α(vW); W row-stochastic from adjacency (and optional edge weights). core.math.diffusion.diffuse_step; sphere.propagation.diffusion (diffuse_once, apply_damping, build_propagation_matrix, propagate_area_vector).
- **Multi-step:** config `propagation_steps` (num_steps); engine loops steps then projects area→family. Optional: sphere.propagation.multi_step_diffusion (propagate_k_steps v W^k, iterative_diffusion, propagation_depth_metric).
- **Engine:** compute_propagation(area_vector, family_counts, adjacency, family_to_area; base_alpha, num_steps, …) → propagated_area_vector, propagated_family_counts, propagation_diagnostics. Effective diffusion rate can be modulated by stability_index, jump_rate.

---

## 6. Dynamism

- **Trajectory / transition matrix / curvature / jump rate / stability index:** core.math (sequence_utils, transition_matrix, curvature_metrics, stability_metrics); sphere.dynamism (compute_dynamism, build_trajectory, compress_trajectory, transition_matrix, curvature, jump_rate, stability_index).
- **Layer 6:** consumes L1/L2; produces trajectory, transition matrix, curvature, jump rate, Lyapunov estimate, global stability score, conceptual coherence. Used by propagation (alpha modulation) and interpretation.

---

## 7. Shadow correction

- **Purpose:** Filter propagation noise, reinforce dominance after propagation.
- **sphere.shadow:** compute_shadow_correction(propagated_area_vector, propagated_family_counts, propagation_diagnostics; family_to_area) → corrected_area_vector, corrected_family_counts, shadow_diagnostics. Uses suppression, entropy correction, dominance filter.
- **Core shadow (L3):** core.propagation.shadow_layer (ShadowMetrics, process_step, candidate_set_shadow); L3 compares baseline vs shadow and produces deltas and acceptability gate.

---

## 8. Structural logic

- **Rules:** sphere.logic (compute_logic_metrics; rule_registry: dominant_area, entropy_drop, tension_increase, propagation_spread, dominance_transition). Evaluates rules on shadow + propagation + dynamism state.
- **Output:** triggered_rules, structural_diagnostics, rule_trigger_registry; feeds interpretation and USF logic_outputs.

---

## 9. Interpretation

- **L10:** sphere.interpretation.compute_interpretation_metrics(layer_7, layer_8, layer_9, propagation_metrics, logic_metrics, …) → structural_state, entropy_state, tension_state, propagation_state, active_events, interpretation_flags, event_summary, interpretation_diagnostics.
- **Policy:** core.policy.apply_interpretation_policy(state, mode) before L8; mode e.g. STRUCTURE_PLUS_CONTEXT. Interpretation scope and POLICY_MODE appear in L8.

---

## 10. Guards Σ Γ Θ

- **Runtime:** sphere.guards.run_all_guards(result, layer_outputs, runtime_meta, config) → sigma, gamma, theta.
- **Sigma:** Invariants on USF/pipeline (path, length, 12×12 matrix, symmetry, no_nan, non_negative, [0,1], area_id). sphere.guards.sigma_validator.
- **Gamma:** validate_gamma_invariants; builtin gamma invariants.
- **Theta:** evaluate_theta_governance; governance facts and builtin theta rules; approved/quarantined, violations, warnings.

---

## 11. USF fingerprint

- **USF:** sphere.usf.generate_usf(document_id, source_metadata, raw_metrics, dynamism_metrics, propagation_metrics, logic_outputs, provenance; interpretation_metrics, …) → canonical USF with schema_version, structural_state, dominant_area_id, fingerprint (structural_state, dominant_area_id, active_events, interpretation_flags), raw_metrics, dynamism_metrics, propagation_metrics, logic_outputs, provenance.
- **Fingerprint:** Subset of USF used for drift: structural_state, dominant_area_id, entropy_state, tension_state, propagation_state, active_events. Drift score: (state_delta*0.6 + event_delta*0.4); thresholds MINOR 0.15, MAJOR 0.40. sphere.usf.drift.compute_drift_score; sphere.usf.fingerprint_diff (compare_structural_fingerprint, fingerprint_distance, classify_drift).

---

## 12. Pipeline flow

1. Validate config (pipeline_version, deterministic=True).
2. Attribution: normalize → tokenize → attribute → hits, adjacency.
3. L1–L9 in order (registry); before L7 inject run_stability(L1–L6); before L8 apply_interpretation_policy.
4. Build layer_outputs, dynamism_metrics, area_sequence.
5. compute_propagation(area_vector, family_counts, adjacency, family_to_area; num_steps=config.propagation_steps).
6. compute_shadow_correction(propagated_area_vector, propagated_family_counts).
7. compute_logic_metrics (structural rules).
8. compute_interpretation_metrics (L10).
9. Optional: compute_prolog_inference (if enable_prolog).
10. generate_usf(…).
11. run_all_guards(result, …).
12. Return document_id, layer_outputs, usf, pipeline_metadata, diagnostics, shadow_metrics, logic_metrics, interpretation_metrics, prolog_logic, guards.

**Entrypoints:** sphere.pipeline.run_pipeline (canonical); runtime.pipeline.run_l1_through_l9 (delegates to sphere, maps to L1..L9 + USF/interpretation/guards); runtime.runners.run_reference_pipeline (CLI); runtime.pipeline.run_e2e_all (sentence, L1–L9, R1–R4, sphere_math, domain_metrics, session KME, TRIZ complete, session topology — see docs/E2E_RUN_ORDER.md).

---

*End of HESPERIA System Specification v1.*
