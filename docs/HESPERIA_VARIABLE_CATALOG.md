<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
See LEGAL_NOTICE.md for full terms.
-->

# HESPERIA — variable & signal catalog

Catalog of **signal families** across the pipeline. Many names are **semantic / product labels**; **canonical JSON keys** differ (especially KME derived: **35 codes** `KDI`…`KVI`, not English names). Coordinate grid: [TOPOLOGY_INVARIANTS.md](TOPOLOGY_INVARIANTS.md) (10+2 areas, 240+48 families, 60k+12k hexes).

**Producers:** `runtime.pipeline.analyze`, sphere math, R1–R4, KME, TRIZ, session topology. **E2E index:** [E2E_RUN_ORDER.md](E2E_RUN_ORDER.md). **Stack view (raw input → commercial):** [HESPERIA_PRODUCT_STACK_MAP.md](HESPERIA_PRODUCT_STACK_MAP.md). **System & product awareness:** [HESPERIA_SYSTEM_AWARENESS.md](HESPERIA_SYSTEM_AWARENESS.md).

**Legend:** **E2E** = in named artifact JSON · **Engine** = stable engine keys · **Derived** = computable from payloads · **Product** = dashboard / commercial label.

---

## 1. Text / lexical base variables

**Produced during:** `runtime.pipeline.analyze` → `run_output_e2e_sentence.json` (`result`, `extended`).

**Document structure**

| Signal | Tag |
|--------|-----|
| `char_count` | Derived |
| `token_count` | Derived / E2E fragments |
| `sentence_count` | Derived |
| `paragraph_count` | Derived |
| `avg_sentence_length` | Derived |
| `sentence_length_variance` | Derived |
| `avg_token_length` | Derived |
| `punctuation_count` | Derived |
| `punctuation_density` | Derived |

**Lexical richness:** `unique_token_count`, `lexical_diversity`, `type_token_ratio`, `hapax_ratio`, `rare_token_ratio`.

**Distribution:** `token_entropy`, `frequency_skew`, `repetition_index`.

*Most lexical-base scalars are **Derived** from tokenizer + histograms; flatten in product layer if needed.*

---

## 2. Marker variables (Dict A)

**Produced during:** marker detection (lexicon / attribution).

**Detection counts:** `marker_hits`, `marker_unique_count`, `marker_density`, `marker_coverage`, `marker_entropy`.

**Marker weights:** `marker_weight_sum`, `marker_weight_mean`, `marker_weight_variance`, `marker_weight_max`, `marker_weight_min`.

**Marker clustering:** `marker_cluster_count`, `marker_cluster_mean_size`, `marker_cluster_max_size`, `marker_overlap_count`, `marker_span_overlap`.

**Tag:** **E2E/Engine** where reflected in `extended`; clustering/overlap often **Derived**.

---

## 3. Concept variables (Dict B)

**Produced after:** marker → concept mapping.

**Concept activations:** `concept_hits`, `concept_unique_count`, `concept_density`, `concept_entropy`, `concept_weight_sum`, `concept_weight_mean`, `concept_weight_variance`.

**Concept reinforcement:** `concept_repetition_index`, `concept_cluster_count`, `concept_cluster_mean_size`, `concept_cluster_max_size`, `concept_overlap`.

**Tag:** **Engine** on KME `ActiveGraph` / session path; **analyze** path via dict_b surfaces in `extended`.

---

## 4. Alignment matrix variables

**Produced during:** coordinate placement **(A_i, F_j, H_k)**.

**Activation distribution:** `activated_area_count`, `activated_family_count`, `activated_hex_count`, `activation_density`, `activation_weight_sum`, `activation_weight_mean`, `activation_weight_variance`.

**Spatial spread:** `area_entropy`, `family_entropy`, `hex_entropy`, `activation_compactness`, `activation_dispersion`, `activation_radius`.

**Cross-area relations:** `area_transition_count`, `area_transition_entropy`, `cross_area_activation_ratio`, `cross_family_activation_ratio`.

**Tag:** **Derived** from `family_vector`, `matched`, session `concept_to_area` / `concept_to_family`; session E2E adds transitions.

---

## 5. Semantic graph variables

**Produced during:** graph construction (`ActiveGraph`, `hesperia/graph`).

**Node metrics:** `node_count`, `active_node_count`, `node_degree_mean`, `node_degree_max`, `node_degree_variance`, `node_degree_entropy`.

**Edge metrics:** `edge_count`, `edge_density`, `edge_weight_mean`, `edge_weight_variance`, `edge_weight_max`.

**Structural metrics:** `cluster_count`, `cluster_mean_size`, `cluster_max_size`, `component_count`, `largest_component_size`, `graph_entropy`, `graph_modularity`.

**Tag:** node/edge core **Engine**; modularity / some clusters **Derived**.

---

## 6. Sphere topology variables

**Produced in:** `run_output_e2e_sphere_math_values.json`, `run_output_e2e_sphere_math_100.json`; also L1–L9 diagnostics (`run_output_e2e_l1_l9.json`).

**Geometric:** `area_distance_mean`, `area_distance_variance`, `area_distance_max`, `geodesic_distance_mean`, `geodesic_distance_max`, `embedding_error`.

**Propagation:** `propagation_steps`, `propagation_radius`, `propagation_speed`, `propagation_decay`, `signal_retention`, `signal_loss`, `propagation_resistance`, `propagation_entropy`.

**Topology influence:** `area_centrality`, `area_influence`, `area_flux`, `area_resistance`, `area_gravity`.

**Tag:** **Engine** + **E2E** layer bundles; exact key names vary by export.

---

## 7. Reading scale variables

**Produced in:** `run_output_e2e_r1_r4.json` (`units`, `book_profile`).

**Scale activation:** `R1_activation`, `R2_activation`, `R3_activation`, `R4_activation`.

**Cross-scale propagation:** `scale_amplification`, `scale_decay`, `scale_entropy`, `scale_transition_rate`, `scale_stability`, `scale_persistence`.

**Tag:** per-level activations **E2E** inside units/profile; cross-scale metrics **Derived** across units.

---

## 8. KME primitive variables

**Core engine metrics** — `run_output_e2e_domain_metrics.json`, `run_output_e2e_session_kme.json` → `primitives`.

| Code | Name |
|------|------|
| **LD** | link_density |
| **COH** | cohesion |
| **NC** | node_centralization |
| **PR** | propagation_rate |
| **PV** | propagation_variance |
| **CI** | concept_intensity |

**Tag:** **Engine** — exact keys `LD`, `COH`, `NC`, `PR`, `PV`, `CI`.

---

## 9. KME derived variables

**≈35 metrics** — algebra over primitives only (`hesperia.engine.kme.derived`). **Canonical JSON keys** (frozen order):

`KDI`, `CSI`, `SPI`, `TDS`, `SSS`, `KCI`, `CCI`, `SPS`, `DCI`, `CSI2`, `KEF`, `ASS`, `CDR`, `KCR`, `TCI`, `PEI`, `KE`, `SCS`, `CRI`, `KNS`, `CII`, `TEP`, `KSI`, `CDD`, `SSR`, `TER`, `CPC`, `KBS`, `TRI`, `IDE`, `KPS`, `TBI`, `KDI2`, `CDI`, `KVI`

**Product vocabulary** (map via glossary — illustrative, not API names):

| Theme | Example labels |
|-------|------------------|
| Structural density | semantic_density, cluster_density, activation_density, domain_compactness |
| Structural stability | structural_coherence, cluster_stability, graph_rigidity, structural_entropy |
| Propagation | propagation_stability, propagation_velocity, signal_persistence, propagation_diffusion |
| Concept distribution | concept_dispersion, concept_concentration, topic_compactness, semantic_temperature |
| Structural complexity | graph_complexity, argument_complexity, concept_connectivity, cluster_interaction |
| Contradiction | contradiction_pressure, conflict_density, tension_index |
| Narrative | narrative_concentration, theme_stability, topic_dominance |

---

## 10. Domain fingerprint variables

**Produced by:** KME fingerprint module.

| Signal | Notes |
|--------|-------|
| `fingerprint_vector` | **Engine:** `fingerprint.metricValues` (41 floats) |
| `fingerprint_norm` | **Derived** |
| `fingerprint_entropy` | **Derived** |
| `fingerprint_similarity` | **Product/Derived** (cosine vs reference) |
| `vector_hash` | **Engine:** `vectorHash` |

**Uses:** document similarity, domain indexing.

---

## 11. TRIZ contradiction variables

**Produced in:** `run_output_e2e_triz_complete.json` → `triz_complete`.

**Contradiction structure:** `contradiction_count`, `contradiction_density`, `contradiction_entropy`, `contradiction_clusters`, `contradiction_severity`.

**Conflict topology:** `conflicting_concept_pairs`, `conflicting_area_pairs`, `conflicting_family_pairs`.

**TRIZ classification:** `triz_principle_distribution` (engine: **`triz_class_distribution`**), `triz_solution_pattern_count`, `triz_solution_entropy`, `innovation_index` (engine: **`innovation_score`** / composites), `innovation_density`.

Also: `innovation_pressure`, `propagation_velocity`, `narrative_stability`, `semantic_pressure`, `activation_energy`, `concept_mass` — see `TRIZDirectMetrics`.

---

## 12. Domain topology variables

**Produced in:** `run_output_e2e_session_topology.json` → `session_topology`.

**Domain activation (aggregates over segments):** `domain_area_activation`, `domain_family_activation`, `domain_cluster_density`, `domain_concept_distribution`.

**Domain patterns:** `domain_pattern_count`, `domain_pattern_entropy`, `domain_cluster_interaction`, `domain_transition_rate`.

**Raw E2E keys** include `segments`, `transitions`, `area_curves` (after per-segment **share** or **softmax** competition + adjacent smooth; see `curve_projection_meta`), `area_curves_session_relative` (mean-centered per curve over the session), `aggression_curve` (alias of `area_curves.aggression`), `curve_projection_meta` (`segment_dominance_confidence`, `lexical_controls` including **`evidence_volume_normalize`** (`1/sqrt(tokens)` on marker weights before rollup), calibration bands), `state_sequence`, `defense_timeline`. Residual roadmap: [CLINICAL_SIGNAL_PIPELINE_GAPS_v0_1.md](../governance/working/CLINICAL_SIGNAL_PIPELINE_GAPS_v0_1.md).

---

### Dynamics layer (Phase 1 wired behind flag)

Discrete-time semantic field: **Concept → Hex → Family → Area**. **H0–H9** compact wire (Part A) plus **Part B extended** IDs (hex resolution, gradients, cluster gravity) including **hex activation** \(x_h\), **hex contradiction pressure** \(p_h\), hex diffusion on \(H_{hk}\), family from hex aggregate \(\hat{X}_f\), gradients/fronts/turbulence, **hex cluster gravity**. Implement on **active hex subgraph** first (Phase C), not full 72k cells. See [specs/ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md](../specs/dynamics/ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md).

**Phase 1 runtime (opt-in):**

| Symbol / key | Role |
|----------------|------|
| `HESPERIA_E2E_CALIBRATION_BATCH_N` | E2E artifacts **5b–5c**: sentence count for calibration structural + summary (default **100**, max 500; pytest uses 5) |
| `HESPERIA_FIELD_DYNAMICS` | Enable E2E step + state persistence |
| `HESPERIA_FIELD_DYNAMICS_PHASE2` | `1`: **Phase 2** L5 + L6 blend |
| `HESPERIA_FIELD_DYNAMICS_PHASE3` | `1`: **Phase 3** L4 — sparse **hex_x** / **hex_p** (family-proxy active subgraph, not full 72k) |
| `HESPERIA_FIELD_DYNAMICS_HEX_CAP` | Max active L4 cells (default 128, max 288) |
| `HESPERIA_FIELD_DYNAMICS_PHASE4` | `1`: **L8** narrative cluster gravity + injection bias + `l8_clusters` artifact |
| `HESPERIA_FIELD_DYNAMICS_TRIZ` | `1` (default): TRIZ → **contradiction_signal_12** / family pressure; `0` skips |
| `HESPERIA_FIELD_DYNAMICS_XI` | `1` (default): **Ξ proxy** — boost `c_sig` from TRIZ row topology (`xi_proxy_global` in artifact meta); `0` disables |
| `HESPERIA_FIELD_DYNAMICS_XI_SCALE` | Max boost scale per area (default **0.14**, clamped [0, 0.5]); registry **xi_scale** |
| `HESPERIA_FIELD_DYNAMICS_STATE_PATH` | Optional override for `field_dynamics_state.json` |
| `HESPERIA_SEMANTIC_FIELD_EQUATIONS_V1` | When `1`/`true`, E2E field-dynamics artifact includes **SEMANTIC_FIELD_EQUATIONS_v1** bundle (`semantic_field_v1` JSON). Binding spec: [specs/dynamics/semantic_field_dynamics.md](../specs/dynamics/semantic_field_dynamics.md). |
| `HESPERIA_SEMANTIC_FIELD_V1_STEPS` | Optional multi-step count for the v1 semantic field integrator in E2E (default `1`). |
| `area_a` (state) | 12-vector L6 area mass (internal icosahedron indices) |
| `p_a` | 12-vector area contradiction pressure |
| `stab` | Compact **H9**-style stability vs prior `area_a` |
| `concept_mass` | L2 scalar stub |
| **Θ Phase 1** | `Phase1Theta`: area L6–L9 knobs |
| **Θ Phase 2** | `Phase2Theta` — **H4/H5** |
| **Θ Phase 3** | `Phase3Theta` |
| **Θ Phase 4** | `Phase4Theta` — `gravity_epsilon`, `tau_front`, `ephemeral_cap` |
| **L8 state** | `l8_cluster_mass_prev` — prior-step cluster masses for velocity |
| **Registry** | [assets/calibration/dynamics_parameter_registry.yaml](../assets/calibration/dynamics_parameter_registry.yaml) |
| **TRIZ bridge** | `contradiction_signal_12` drives `p_a` via `δ_a`; meta: `triz_contradiction_meta` on E2E artifact |

---

## 13. Global semantic physics variables

Aggregate signals combining multiple layers (**Product** composites; sources indicative):

| Signal | Typical sources |
|--------|-----------------|
| `semantic_energy` | CI, `activation_energy`, graph weights |
| `semantic_mass` | `concept_mass`, edge/node weight sums |
| `semantic_temperature` | KME derived / entropy proxies |
| `semantic_pressure` | TRIZ `semantic_pressure`, marker density |
| `activation_pressure` | KME CI + marker/concept density |
| `propagation_energy` | PR, PV, sphere propagation |
| `propagation_pressure` | TRIZ spillover / propagation rows |
| `contradiction_pressure` | TRIZ density + tension derived |
| `innovation_pressure` | TRIZ `innovation_pressure` |
| `semantic_gravity` | area influence, topic dominance |
| `semantic_inertia` | signal_persistence, narrative_stability |
| `semantic_velocity` | TRIZ `propagation_velocity`, PR |

---

## 14. Total variable inventory

Approximate **measurable** slots (scalars / well-defined vectors); not all exported as flat keys.

| Layer | Variables |
|-------|-----------|
| Text / lexical | 15 |
| Markers (Dict A) | 14 |
| Concepts (Dict B) | 12 |
| Alignment matrix | 15 |
| Semantic graph | 15 |
| Sphere topology | 15 |
| Reading scales | 10 |
| KME primitives | 6 |
| KME derived | 35 |
| Fingerprint | 5 |
| TRIZ | 12 |
| Domain topology | 10 |
| Semantic physics | 12 |

**Total: ~176** variables (order of magnitude) — **derivable** within current architecture from analyze + E2E + engine payloads.

---

## 15. Variables that drive analytical products

Primary **commercial / dashboard** metrics (map from §1–13):

| Signal | Typical source layer |
|--------|----------------------|
| semantic_density | KME derived + graph |
| structural_coherence | COH, KDI, SSS |
| topic_dominance | Sphere + alignment entropy |
| propagation_velocity | TRIZ, PR |
| signal_persistence | TRIZ narrative, KME derived |
| contradiction_pressure | TRIZ + tension proxies |
| innovation_index | TRIZ innovation_score / clusters |
| fingerprint_similarity | §10 vs corpus reference |
| domain_compactness | KME + alignment |
| argument_complexity | graph + NC, LD |

These anchor **product outputs** (`hesperia/product`, reports, API envelopes). Full **product line** mapping (A–G): [HESPERIA_PRODUCT_LINES.md](HESPERIA_PRODUCT_LINES.md).

---

## See also

- [HESPERIA_DEPENDENCY_GRAPH.md](HESPERIA_DEPENDENCY_GRAPH.md)  
- [HESPERIA_REPOSITORY_MAP.md](HESPERIA_REPOSITORY_MAP.md)  
- [DOMAIN_E2E_PIPELINE.md](DOMAIN_E2E_PIPELINE.md)  
- `hesperia/product/triz_metric_catalog.py`  
- [HESPERIA_PRODUCT_LINES.md](HESPERIA_PRODUCT_LINES.md) — product lines A–G  

---

*Update when E2E or KME/TRIZ contracts change.*
