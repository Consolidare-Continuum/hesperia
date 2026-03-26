<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
See LEGAL_NOTICE.md for full terms.
-->

# HESPERIA — product stack map

End-to-end stack from **raw raw_text** to **commercial analytics**. Variable names mix **product vocabulary** and **engine keys**; canonical KME derived codes are `KDI`…`KVI` ([HESPERIA_VARIABLE_CATALOG.md](HESPERIA_VARIABLE_CATALOG.md)). Geometry: [TOPOLOGY_INVARIANTS.md](TOPOLOGY_INVARIANTS.md).

**Related:** [HESPERIA_PRODUCT_LINES.md](HESPERIA_PRODUCT_LINES.md) · [E2E_RUN_ORDER.md](E2E_RUN_ORDER.md)

---

## 1. Raw raw_text layer

**Sources ingested:** documents, laws, policy programs, research papers, corporate strategies, news corpora, psychological transcripts.

**Execution Flow entry (lexicon / attribution path):** `runtime.execution_flow.analyze`  
**Full multi-artifact E2E:** `python3 -m runtime.execution_flow.run_e2e_all`

**Primary outputs (text-layer variables):**

`token_count`, `sentence_count`, `lexical_diversity`, `token_entropy`, `repetition_index`, `frequency_skew`

→ Linguistic structure of the raw_text. Many are **derived** from tokenizer output / `extended` payload.

---

## 2. Detection layer — Dict A

**Purpose:** Detect semantic markers.

```text
text → marker detection → marker signals
```

**Variables**

| Detection | Weights | Structural patterns |
|-----------|---------|----------------------|
| `marker_hits` | `marker_weight_sum` | `marker_cluster_count` |
| `marker_unique_count` | `marker_weight_mean` | `marker_cluster_mean_size` |
| `marker_density` | `marker_weight_variance` | `marker_overlap_count` |
| `marker_entropy` | `marker_weight_max` | |
| `marker_coverage` | | |

→ **Semantic trigger density** in text.

---

## 3. Interpretation layer — Dict B

Markers → conceptual meaning.

```text
markers → concept mapping → concept activations
```

**Variables:** `concept_hits`, `concept_unique_count`, `concept_density`, `concept_entropy`, `concept_weight_sum`, `concept_weight_variance`; patterns: `concept_cluster_count`, `concept_cluster_mean_size`, `concept_overlap`.

→ **Semantic meaning extraction.**

---

## 4. Alignment layer — semantic matrix

Concepts placed in HESPERIA coordinate space **(A_i, F_j, H_k)** — Area / Family / Hex.

**Capacity (full grid):** **12 areas**, **288 families**, **72 000 hex** positions (public vs reserved split: 10+2 areas, 240+48 families, 60k+12k hexes — see topology doc). Sparse activation weights.

**Variables**

| Activation distribution | Spatial | Cross-domain |
|-------------------------|---------|--------------|
| `activated_area_count` | `activation_radius` | `area_transition_count` |
| `activated_family_count` | `activation_compactness` | `cross_area_activation_ratio` |
| `activated_hex_count` | `activation_dispersion` | `cross_family_activation_ratio` |
| `activation_density` | | |

→ **Text → semantic topology.**

---

## 5. Semantic graph layer

Activated coordinates → **graph** (concept nodes, semantic relations).

**Nodes:** `node_count`, `active_node_count`, `node_degree_mean`, `node_degree_entropy`  
**Edges:** `edge_count`, `edge_density`, `edge_weight_mean`  
**Structure:** `cluster_count`, `component_count`, `graph_modularity`, `graph_entropy`

→ **Structural model of the document.**

---

## 6. Sphere topology layer

Graph signals propagate over **icosahedral** area topology (12 nodes, degree 5).

**Propagation:** `propagation_speed`, `propagation_radius`, `propagation_decay`, `signal_retention`, `propagation_resistance`  
**Area influence:** `area_centrality`, `area_flux`, `area_gravity`, `area_influence`

→ **How ideas travel across topology.**

---

## 7. Reading scale layer (R1–R4)

| Scale | Interpretation |
|-------|----------------|
| R1 | Lexical |
| R2 | Conceptual |
| R3 | Structural |
| R4 | Narrative |

**Variables:** `R1_activation` … `R4_activation`, `scale_amplification`, `scale_decay`, `scale_transition_rate`

→ **Multi-scale interpretation of meaning.** Artifact: `run_output_e2e_r1_r4.json`.

---

## 8. Metric engine — KME

**Primitives**

| Code | Name |
|------|------|
| LD | link_density |
| COH | cohesion |
| NC | node_centralization |
| PR | propagation_rate |
| PV | propagation_variance |
| CI | concept_intensity |

**Derived (~35)** — JSON keys `KDI`…`KVI`; **product labels** include:

- **Structural:** semantic_density, domain_compactness, cluster_stability, graph_rigidity  
- **Propagation:** propagation_velocity, signal_persistence, propagation_diffusion  
- **Concept distribution:** concept_dispersion, topic_compactness, semantic_temperature  
- **Complexity:** graph_complexity, argument_complexity, concept_connectivity  
- **Conflict:** contradiction_pressure, conflict_density, tension_index  
- **Narrative:** narrative_concentration, theme_stability, topic_dominance  

→ **Primary analytical outputs** from KME. Artifacts: domain_metrics, session_kme E2E JSON.

---

## 9. TRIZ contradiction engine

**Conflict detection:** `contradiction_count`, `contradiction_density`, `contradiction_entropy`, `contradiction_clusters`, `contradiction_severity`  
**TRIZ classification:** `triz_principle_distribution` (engine: **`triz_class_distribution`**), `triz_solution_pattern_count`, `triz_solution_entropy`  
**Innovation:** `innovation_index`, `innovation_density`

→ **Innovation potential and internal conflicts.** Artifact: `run_output_e2e_triz_complete.json`.

---

## 10. Fingerprint layer

`fingerprint_vector` (`metricValues`, 41 floats), `fingerprint_norm`, `fingerprint_entropy`, `fingerprint_similarity`, `vector_hash`

→ **Corpus indexing, similarity, document clustering.**

---

## 11. Semantic physics layer

**Aggregates:** `semantic_energy`, `semantic_mass`, `semantic_temperature`, `semantic_pressure`, `semantic_gravity`, `semantic_inertia`, `semantic_velocity`

→ **Global semantic dynamics** (composites across layers).

---

## 12. Product signal layer

From **~176** variables, a **small set** becomes commercial outputs.

**10 primary marketable indicators:**

semantic_density · structural_coherence · topic_dominance · propagation_velocity · signal_persistence · contradiction_pressure · innovation_index · fingerprint_similarity · domain_compactness · argument_complexity

---

## 13. Final product outputs

Signals power:

- Policy measurement  
- Program comparison  
- Narrative spread tracking  
- Innovation detection  
- Knowledge mapping  
- Semantic similarity search  
- Argument structure measurement  
- Contradiction detection  

Product packaging: [HESPERIA_PRODUCT_LINES.md](HESPERIA_PRODUCT_LINES.md).

---

## 14. Full stack overview

**Future dynamics step (Ethan):** **Concept→Hex→Family→Area** time evolution on hex lattice + area graph — [ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md](../specs/dynamics/ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md) (Phases A–D; active hex subgraph before full grid).

```text
TEXT
  → LEXICAL VARIABLES
  → DICT A MARKERS
  → DICT B CONCEPTS
  → ALIGNMENT MATRIX (A, F, H)
  → SEMANTIC GRAPH
  → SPHERE PROPAGATION
  → READING SCALES (R1–R4)
  → KME METRICS
  → TRIZ CONTRADICTIONS
  → FINGERPRINT
  → SEMANTIC PHYSICS
  → PRODUCT SIGNALS
  → COMMERCIAL ANALYTICS
```

---

*Update when execution_flow stages or E2E contracts change.*
