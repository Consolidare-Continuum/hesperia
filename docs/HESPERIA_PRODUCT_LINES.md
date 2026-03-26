<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
See LEGAL_NOTICE.md for full terms.
-->

# HESPERIA — product lines (as of now)

Commercial **product lines** mapped to engine signals. Variable names are **product vocabulary** where applicable; canonical keys: [HESPERIA_VARIABLE_CATALOG.md](HESPERIA_VARIABLE_CATALOG.md). **Layered stack (text → product signals):** [HESPERIA_PRODUCT_STACK_MAP.md](HESPERIA_PRODUCT_STACK_MAP.md). **Placement engine & boundaries:** [HESPERIA_SYSTEM_AWARENESS.md](HESPERIA_SYSTEM_AWARENESS.md). TRIZ commercial bundles: [COMMERCIAL_TRIZ_PRODUCTS.md](COMMERCIAL_TRIZ_PRODUCTS.md). Implementation surface: `hesperia/product/`, `runtime/api/`.

---

## Product Line A — Semantic structural measurement

**What it measures:** Structure of arguments and ideas.

**Key variables**

| Variable | Role |
|----------|------|
| semantic_density | Mass of meaning per structural unit |
| structural_coherence | Internal consistency of graph / KME |
| graph_complexity | Size + connectivity of semantic graph |
| argument_complexity | Relational depth of claims |
| cluster_interaction | Cross-cluster linkage |
| topic_compactness | Concentration on few topics |
| concept_connectivity | Edge density among concepts |

**Engine sources:** semantic graph metrics, **KME primitives** (LD, COH, NC, PR, PV, CI), **KME derived** (35 codes — map via glossary).

**Product examples**

1. **Document structure analyzer**  
   - **Outputs:** argument complexity score, semantic density, coherence score, topic dominance.  
   - **Customers:** research institutes, media, think tanks, academia.

2. **Policy / program analyzer**  
   - **Example:** Party A program vs Party B program.  
   - **Outputs:** policy similarity (e.g. %), economic cluster strength, energy policy contradictions, narrative concentration.  
   - **Market:** political analysts, NGOs, journalists.

---

## Product Line B — Narrative propagation measurement

**What it measures:** How ideas move across **semantic topology** (Sphere + reading scales).

**Key variables**

| Variable | Role |
|----------|------|
| propagation_speed | Rate of signal spread |
| propagation_radius | Reach in topology steps |
| signal_retention | What survives multi-step propagation |
| propagation_resistance | Friction in area/family graph |
| propagation_entropy | Dispersion vs concentration |
| scale_amplification | Growth R1→R4 |
| scale_decay | Attenuation across scales |

**Engine sources:** `sphere/` propagation + layer metrics, **R1–R4** (`run_output_e2e_r1_r4.json`), TRIZ narrative metrics where overlapped.

**Product example: Narrative spread index**

- **Example phrase:** “security threat”.  
- **Illustrative path:** security area → migration → economy → foreign policy.  
- **Outputs:** narrative penetration score, propagation velocity, domain influence.  
- **Uses:** media measurement, geopolitical measurement, corporate narrative tracking.

---

## Product Line C — Contradiction intelligence

**What it measures:** Incompatible concepts and strategic tension.

**Key variables**

| Variable | Role |
|----------|------|
| contradiction_pressure | Composite tension |
| conflict_density | Conflicts per unit activation |
| tension_index | Scalar stress (see also `policy_tension_index` in TRIZ commercial) |
| contradiction_clusters | Grouped conflicts |
| innovation_index | TRIZ-side innovation score |

**Engine sources:** **TRIZ** layer (`run_triz_analysis_complete`), `atomic_metrics`, contradiction rows, [commercial_intelligence](COMMERCIAL_TRIZ_PRODUCTS.md).

**Product examples**

1. **Policy contradiction detector**  
   - **Raw_text:** policy documents, government / corporate strategies.  
   - **Outputs:** internal contradictions, policy conflict clusters, implementation risk indicators.  
   - **Customers:** governments, NGOs, policy research.

2. **Strategic conflict analyzer**  
   - **Example:** corporate strategy vs execution.  
   - **Outputs:** strategy contradictions, organizational tension, execution mismatch.

---

## Product Line D — Idea novelty / innovation radar

**What it measures:** Novelty and solution-pattern structure (TRIZ).

**Key variables**

| Variable | Role |
|----------|------|
| innovation_index | e.g. `innovation_score`, cluster peaks |
| innovation_density | Conflicts × activation mass–style composites |
| triz_principle_distribution | Engine: **`triz_class_distribution`** |
| contradiction_entropy | Spread of conflict types |

**Engine sources:** TRIZ `innovation_clusters`, `commercial_intelligence.innovation_intelligence_products`.

**Product example: Innovation potential scoring**

- **Raw_text:** startup pitch, research paper, technology roadmap.  
- **Outputs:** innovation score, novelty index, contradiction potential, solution pattern classification.  
- **Customers:** venture capital, R&D, innovation labs.

---

## Product Line E — Semantic fingerprint & similarity

**What it measures:** Document-to-document semantic distance in **41-signal** space.

**Key variables**

| Variable | Role |
|----------|------|
| fingerprint_vector | `metricValues` (6 primitives + 35 derived) |
| fingerprint_similarity | Cosine / hash match vs corpus |
| vector_hash | Deterministic doc ID (`vectorHash`) |

**Engine sources:** KME fingerprint component — `run_output_e2e_domain_metrics.json`, `run_output_e2e_session_kme.json`.

**Product: Document similarity engine**

- **Examples:** law vs law, research vs research, policy vs policy.  
- **Outputs:** semantic similarity, topic overlap, cluster similarity.  
- **Markets:** legal measurement, academic search, knowledge management.

---

## Product Line F — Domain topology intelligence

**What it measures:** How **domains** activate and evolve over segments (session / corpus).

**Key variables**

| Variable | Role |
|----------|------|
| domain_area_activation | Mass per area over corpus/segments |
| domain_pattern_count | Distinct recurring patterns |
| domain_cluster_interaction | Cross-cluster coupling |
| domain_transition_rate | Rate of area/state change |

**Engine sources:** `run_output_e2e_session_topology.json` (`segments`, `transitions`, …) — **domain_\*** names are product views on those structures.

**Product: Knowledge domain mapping**

- **Example:** research corpus.  
- **Outputs:** topic clusters, domain dominance, knowledge fragmentation, topic evolution.  
- **Markets:** research analytics, patent measurement, technology intelligence.

---

## Product Line G — Semantic physics dashboard

**What it measures:** Highest-level **aggregates** across layers (“idea dynamics”).

**Key variables**

| Variable | Role |
|----------|------|
| semantic_energy | Combined activation + tension |
| semantic_mass | Concept + graph weight mass |
| semantic_temperature | Entropy / dispersion metaphor |
| semantic_pressure | TRIZ `semantic_pressure` + composites |
| semantic_gravity | Topic / area pull |
| semantic_velocity | Propagation speed metaphor |

**Engine sources:** composites from KME, TRIZ, graph, sphere (see [HESPERIA_VARIABLE_CATALOG.md](HESPERIA_VARIABLE_CATALOG.md) §13).

**Product: Global semantic diagnostics**

- **Example outputs:** argument pressure, narrative heat, semantic inertia, contradiction pressure.  
- **Positioning:** dashboard of **idea dynamics** — executive / monitoring view on top of Lines A–F.

---

## Cross-line map (quick reference)

| Line | Primary engine buckets |
|------|-------------------------|
| A | Graph + KME |
| B | Sphere + R1–R4 + narrative TRIZ |
| C | TRIZ contradictions + commercial_intelligence |
| D | TRIZ innovation clusters + classes |
| E | KME fingerprint |
| F | Session / domain topology |
| G | Aggregates (semantic physics) |

---

*Update when product contracts or TRIZ/KME envelopes change.*
