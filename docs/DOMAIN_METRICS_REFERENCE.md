# HESPERIA Domain Metrics — Reference Definitions

**Single reference for what was shipped in Tasks 1–7.**  
**Canonical component:** `hesperia.engine.kme` (KME — Knowledge Metrics Engine). Legacy: `core.domain` re-exports from KME. Use this document everywhere (code comments, specs, onboarding) so definitions are not lost in math and code.

---

## 1. What We Shipped (Tasks 1–7)

| Task | Name | What it does | Where it lives |
|------|------|--------------|----------------|
| **1** | Domain Constants Extractor | From reference domain graph, computes and freezes **domain_node_count**, **domain_degree_p95**, **domain_distance_p95**. | `hesperia/engine/kme/extractor.py`, `hesperia/engine/kme/loader.py`; constants → `assets/data/domain_constants.json` |
| **2** | Active Graph Canonicalizer | From concept hits + relation candidates + domain graph, builds **ActiveGraph** A=(V_A,E_A) with V_A⊆V_R, E_A⊆E_R. Deterministic. | `hesperia/engine/kme/active_graph.py`, `hesperia/engine/kme/models.py` |
| **3** | Primitive Metric Calculator | From ActiveGraph + DomainConstants, computes **6 primitives** (LD, COH, NC, PR, PV, CI), all in [0,1]. | `hesperia/engine/kme/primitives/`; `compute_primitives(graph, constants)` |
| **4** | Derived Metric Engine | From PrimitiveMetrics only, computes **35 derived metrics**, all in [0,1]. Strict clamp01 + safeDiv. | `hesperia/engine/kme/derived/`; `compute_derived_metrics(p)` |
| **5** | Validation & Toy-Graph Test Suite | Verifies primitives and derived: determinism, range [0,1], division safety, propagation, structural scenarios. | `tests/domain/test_validation_toy_graphs.py` |
| **6** | Domain Fingerprint Engine | From PrimitiveMetrics + DerivedMetrics, produces **DomainFingerprint**: 41-value vector (round6), metadata, **vectorHash** (SHA-256). Same metrics → same bytes. Comparison: same_fingerprint, euclidean, manhattan, cosine. | `hesperia/engine/kme/fingerprint/`; `build_fingerprint(p, d, domain_release, source_id)` |
| **7** | Domain Profile Layer | Aggregates N document fingerprints into one **DomainProfile**: mean, std, median, p90 per dimension (41), **profileHash**. Domain comparison, classification, drift detection. | `hesperia/engine/kme/profiling/`; `build_profile(domain_id, fingerprints)`, `domain_distance`, `classify_document`. See `docs/DOMAIN_PROFILE.md`. |

**Execution Flow (end-to-end):**  
Domain Graph → Domain Constants (Task 1) → Active Graph (Task 2) → Primitive Metrics (Task 3) → Derived Metrics (Task 4) → Fingerprint (Task 6). Task 5 validates the chain.

**E2E Integration:** Single entry point and batch runner: `run_document` / `run_pipeline` / `run_corpus` in `hesperia/engine/kme/execution_flow.py`. Export: `metric_report_to_dict`, `export_metric_report_json`. See `docs/DOMAIN_E2E_PIPELINE.md`.

**Domain Profile:** After document fingerprints exist (e.g. from `run_corpus`), use `build_profile(domain_id, fingerprints)` to get one corpus-level profile; `domain_distance` and `classify_document` for comparison and classification. See `docs/DOMAIN_PROFILE.md`.

---

## 2. Primitive Metrics (6)

All primitives are in **[0, 1]**. Inputs: **ActiveGraph** (nodes, edges) + **DomainConstants** (N, Deg95, Dist95). Implemented in `core/domain/primitive_metrics.py`.

| Code | Name | Definition (what it means) | Formula / implementation note |
|------|------|----------------------------|--------------------------------|
| **LD** | Logical Density | Measures how many conceptual relations exist relative to the number of active concepts; indicates **structural tightness**. | avgActiveDegree / Deg95, where avgActiveDegree = 2m/n. 0 if n=0. |
| **COH** | Coherence | Measures the **structural integrity** of the concept network by combining connectivity and local clustering. | 0.6×Conn + 0.4×Trans. Conn = |largest component|/n. Trans = 3×triangles / connected triplets. 0 if n<3 (tiny-graph rule). |
| **NC** | Node Coverage | Represents the **proportion of the domain’s concept space** activated by the analyzed text. | n / N (clamped). n = |V_A|, N = domain_node_count. |
| **PR** | Propagation Radius | Indicates **how far ideas travel** through the concept graph; reflects conceptual reach. | Mean distance from non-anchor nodes to nearest anchor, divided by Dist95. Anchors = top k by mass, k = max(1, ⌈0.10×n⌉). |
| **PV** | Propagation Volume | Measures the **total conceptual space influenced** by the text’s idea propagation. | Sum over V_prop of (d*(v,S)+1), divided by N×(Dist95+1). d* = 0 on anchors, distance on reachable nodes. |
| **CI** | Concentration Index | Measures how **unevenly conceptual attention** is distributed across nodes; indicates specialization. | Normalized HHI: (HHI − 1/n)/(1 − 1/n), where HHI = Σ p_i², p_i = hitCount_i / F. 0 if n≤1 or F≤0. |

**Canonical order (serialization / fingerprint):** LD, COH, NC, PR, PV, CI.

---

## 3. Derived Metrics (35)

All derived metrics are in **[0, 1]**. Inputs: **PrimitiveMetrics** only (LD, COH, NC, PR, PV, CI). Every formula uses **clamp01** on output and **safeDiv** for divisions. Implemented in `core/domain/derived_metrics.py`.

**Canonical order (serialization / fingerprint):**  
KDI, CSI, SPI, TDS, SSS, KCI, CCI, SPS, DCI, CSI2, KEF, ASS, CDR, KCR, TCI, PEI, KE, SCS, CRI, KNS, CII, TEP, KSI, CDD, SSR, TER, CPC, KBS, TRI, IDE, KPS, TBI, KDI2, CDI, KVI.

### Core knowledge structure (1–15)

| Code | Name | Definition (what it means) | Formula |
|------|------|----------------------------|---------|
| **KDI** | Knowledge Density Index | Structurally dense and coherent knowledge representation. | LD × COH |
| **CSI** | Concept Spread Index | How widely domain concepts are activated and propagated. | NC × PR |
| **SPI** | Specialization Index | Degree to which the text concentrates on a narrow conceptual region. | CI |
| **TDS** | Theory Depth Score | How deeply the text develops ideas through conceptual propagation. | PR × LD |
| **SSS** | Structural Stability Score | Whether conceptual structure holds together relative to propagation size. | safeDiv(COH, PV) |
| **KCI** | Knowledge Compactness Index | How concentrated logical structure is within the propagation radius. | safeDiv(LD, PR) |
| **CCI** | Concept Connectivity Index | How well activated concepts are interconnected in the domain. | COH × NC |
| **SPS** | Semantic Propagation Strength | Strength of idea propagation supported by structural coherence. | PR × COH |
| **DCI** | Domain Complexity Index | How much structural logic is expressed relative to concept breadth. | LD × NC |
| **CSI₂** | Concept Saturation Index | How densely the activated conceptual region is internally structured. | CI × LD |
| **KEF** | Knowledge Expansion Factor | How much conceptual space the text influences relative to concepts used. | safeDiv(PV, NC) |
| **ASS** | Argument Stability Score | How stable argumentative structure remains under conceptual expansion. | safeDiv(COH×LD, PV) |
| **CDR** | Concept Diffusion Rate | How quickly ideas spread across the activated concept space. | safeDiv(PR, NC) |
| **KCR** | Knowledge Compression Ratio | How efficiently logical structure is expressed per concept. | safeDiv(LD, NC) |
| **TCI** | Theory Cohesion Index | How tightly theoretical structure binds concentration and coherence. | COH × LD × CI |

### Structural efficiency (16–23)

| Code | Name | Definition (what it means) | Formula |
|------|------|----------------------------|---------|
| **PEI** | Propagation Efficiency Index | How efficiently propagation distance translates into total conceptual reach. | safeDiv(PR, PV) |
| **KE** | Knowledge Elasticity | How easily conceptual propagation expands relative to structural density. | safeDiv(PR, LD) |
| **SCS** | Structural Compression Score | How effectively logical structure and coherence are compressed into the concept set. | safeDiv(LD×COH, NC) |
| **CRI** | Conceptual Rigidity Index | How strongly conceptual concentration aligns with structural coherence. | CI × COH |
| **KNS** | Knowledge Network Strength | Overall structural strength of the concept network activated by the text. | NC × COH × LD |
| **CII** | Concept Isolation Index | How fragmented the concept network becomes relative to propagation radius. | safeDiv(NC, PR) |
| **TEP** | Theory Expansion Pressure | Pressure for conceptual expansion generated by structural density. | PV × LD |
| **KSI** | Knowledge Stability Index | How stable structural knowledge remains as propagation distance increases. | safeDiv(COH×LD, PR) |

### Concept distribution (24–29)

| Code | Name | Definition (what it means) | Formula |
|------|------|----------------------------|---------|
| **CDD** | Concept Distribution Density | How densely concepts populate the conceptual space reached by propagation. | safeDiv(NC, PV) |
| **SSR** | Semantic Spread Ratio | How far propagation extends relative to the conceptual area covered. | safeDiv(PR, PV) |
| **TER** | Terminology Efficiency Ratio | How effectively conceptual concentration translates into structural density. | safeDiv(CI, LD) |
| **CPC** | Concept Propagation Coefficient | How effectively concept coverage supports propagation across conceptual space. | safeDiv(PR×NC, PV) |
| **KBS** | Knowledge Balance Score | Balance between concept coverage and structural coherence. | safeDiv(COH×NC, PV) |
| **TRI** | Theory Rigidity Index | How tightly conceptual concentration restricts propagation. | safeDiv(CI×LD, PR) |

### Knowledge dynamics (30–35)

| Code | Name | Definition (what it means) | Formula |
|------|------|----------------------------|---------|
| **IDE** | Idea Diffusion Efficiency | How effectively coherent structure enables idea diffusion across concepts. | safeDiv(PR×COH, NC) |
| **KPS** | Knowledge Propagation Stability | How stable coherence remains as propagation radius grows. | safeDiv(COH, PR) |
| **TBI** | Theory Breadth Index | Overall conceptual breadth achieved through propagation volume and coverage. | NC × PV |
| **KDI₂** | Knowledge Development Index | How strongly density, propagation, and coherence jointly drive knowledge growth. | LD × PR × COH |
| **CDI** | Concept Dependency Index | How dependent conceptual structure is on concentrated conceptual regions. | CI × NC |
| **KVI** | Knowledge Vitality Index | Overall vitality of the knowledge system (density, coherence, propagation, expansion). | safeDiv(LD×COH×PR, PV) |

---

## 4. Marketable Derived Metrics (14 of 35)

All **35** derived metrics are computed and available. For **dashboards, reports, and external users**, a subset of **14** is designated **market-facing** based on:

- **Interpretability** — non-technical users understand it quickly.
- **Non-redundancy** — avoid obvious algebraic duplicates.
- **Business meaning** — useful for comparing texts, theories, or domains.
- **Dashboard clarity** — each metric answers a distinct question.

The remaining 21 are engineering diagnostics: useful internally, not required for external storytelling.

### Summary by category

| Category | Metrics | Count |
|----------|---------|-------|
| **Knowledge Structure** | KDI, KNS, KCR, KBS | 4 |
| **Concept Spread & Coverage** | CSI, TBI, CDD | 3 |
| **Theory Quality** | TDS, TCI, SSS | 3 |
| **Knowledge Dynamics** | IDE, SPS | 2 |
| **Domain Character** | SPI, DCI | 2 |
| **Total market-facing** | | **14** |

### The 14 market-facing metrics (definitions)

**Knowledge Structure**

| Code | Name | Definition |
|------|------|------------|
| **KDI** | Knowledge Density Index | How structurally dense and coherent the knowledge representation is. |
| **KNS** | Knowledge Network Strength | Overall structural strength of the concept network activated by the text. |
| **KCR** | Knowledge Compression Ratio | How efficiently logical structure is expressed per concept used. |
| **KBS** | Knowledge Balance Score | Whether conceptual breadth and structural coherence are balanced. |

**Concept Spread & Coverage**

| Code | Name | Definition |
|------|------|------------|
| **CSI** | Concept Spread Index | How widely the text activates concepts across the domain. |
| **TBI** | Theory Breadth Index | Overall conceptual breadth achieved through propagation. |
| **CDD** | Concept Distribution Density | How densely concepts populate the conceptual space reached by propagation. |

**Theory Quality**

| Code | Name | Definition |
|------|------|------------|
| **TDS** | Theory Depth Score | How deeply ideas are developed through conceptual propagation. |
| **TCI** | Theory Cohesion Index | How tightly conceptual concentration and coherence bind the theory together. |
| **SSS** | Structural Stability Score | Whether the conceptual structure holds together under expansion. |

**Knowledge Dynamics**

| Code | Name | Definition |
|------|------|------------|
| **IDE** | Idea Diffusion Efficiency | How effectively ideas propagate through the concept network. |
| **SPS** | Semantic Propagation Strength | How strongly coherence supports idea propagation. |

**Domain Character**

| Code | Name | Definition |
|------|------|------------|
| **SPI** | Specialization Index | How specialized the text is within a conceptual region. |
| **DCI** | Domain Complexity Index | How structurally complex the conceptual system expressed in the text is. |

**Code constant:** `core/domain/fingerprint.py` → `MARKETABLE_DERIVED_ORDER`. Use for dashboards, APIs, and any UI that shows “key metrics” instead of all 35. Full list: `docs/DOMAIN_MARKETABLE_METRICS.md`.

---

## 5. Fingerprint and Comparison (Task 6)

- **Fingerprint:** 41 values = 6 primitives + 35 derived, in fixed order. Each value is **round6** (6 decimal places) for stable hashing and serialization. **vectorHash** = SHA-256 of `fingerprintVersion|domainRelease|sourceId|v1,v2,...,v41` (each v formatted as `%.6f`).
- **Comparison:**  
  - **same_fingerprint(a, b)** — equality by vectorHash.  
  - **euclidean_distance(a_values, b_values)** — L2.  
  - **manhattan_distance(a_values, b_values)** — L1.  
  - **cosine_similarity(a_values, b_values)** — in [−1, 1]; for nonnegative vectors, [0, 1].

All comparison uses **round6** on values for stability.

---

## 6. Where to Point in Code and Specs

- **Primitive formulas:** `core/domain/primitive_metrics.py` (compute_nc, compute_ci, compute_ld, compute_coh, compute_pr, compute_pv).
- **Derived formulas:** `core/domain/derived_metrics.py` (compute_derived_metrics; each metric in build block).
- **Order constants:** `core/domain/fingerprint.py` (PRIMITIVE_ORDER, DERIVED_ORDER, FULL_ORDER).
- **Marketable subset (14):** `core/domain/fingerprint.py` (MARKETABLE_DERIVED_ORDER); full narrative: `docs/DOMAIN_MARKETABLE_METRICS.md`.
- **This definitions reference:** `docs/DOMAIN_METRICS_REFERENCE.md` — **do not lose this file**; reference it wherever primitives or derived metrics are documented or coded.
