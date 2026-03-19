<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
See LEGAL_NOTICE.md for full terms.
-->

# HESPERIA — runtime dependency graph (testing & change impact)

This is **not** a directory tree. It is the **runtime dependency graph**: what feeds what, what to treat as frozen during testing, and where failures propagate.

**Companion:** [HESPERIA_REPOSITORY_MAP.md](HESPERIA_REPOSITORY_MAP.md) (what lives where). **Signals:** [HESPERIA_VARIABLE_CATALOG.md](HESPERIA_VARIABLE_CATALOG.md). **Product lines:** [HESPERIA_PRODUCT_LINES.md](HESPERIA_PRODUCT_LINES.md). **Product stack:** [HESPERIA_PRODUCT_STACK_MAP.md](HESPERIA_PRODUCT_STACK_MAP.md). **Field dynamics (L0–L10 wire, H0–H9 + Part B hex):** [specs/ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md](../specs/dynamics/ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md). **Geometry truth:** [TOPOLOGY_INVARIANTS.md](TOPOLOGY_INVARIANTS.md).

---

## 13. System capability summary

The current repository provides:

| Capability | Primary locus |
|------------|----------------|
| **Semantic parsing** | `hesperia/nlp`, `lexicon`, Dict A/B |
| **Structured knowledge graph** | `hesperia/graph`, KME `ActiveGraph`, Dict-B relations |
| **Topology-based propagation** | `sphere/topology`, `sphere/propagation`, L1–L9 pipeline |
| **Domain metrics** | `hesperia/engine/kme`, structural bridge → fingerprint |
| **Contradiction analysis** | `hesperia/extensions/triz` |
| **Clinical ontology projection** | `hesperia/clinical`, session topology |
| **Product-ready analytics** | `hesperia/product`, `runtime/api`, reports |

**Next depth:** this document is the **structural dependency map** (~core modules). For a finer import-level graph, generate from static analysis (e.g. `pydeps`, `importlab`) on `hesperia/`, `sphere/`, `runtime/`.

### Dynamics pipeline vs dependency layers (crosswalk)

**Two views:** Layers **0–11** here are **code / change-impact**. **[Ethan spec](../specs/dynamics/ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md) Part A L0–L10** is the **temporal** discrete-time field pipeline. Approximate mapping:

| L (Ethan) | Dependency-layer focus |
|-----------|-------------------------|
| L0 | Input text, session envelope |
| L1–L2 | NLP, lexicon (Dict A/B) |
| L3 | Activation & weights |
| L4 | Matrix / family–area, graph construction |
| L5 | Sphere topology & propagation (L1–L9 numeric pipeline) |
| L6 | KME / fingerprint |
| L7 | TRIZ |
| L8 | Domain projections (e.g. clinical) |
| L9–L10 | Reports, API, product surfaces |

Authoritative L-layer list: Ethan §A.

---

## 1. Global dependency chain

Everything flows in this **direction** (runtime orchestrator composes these stages):

```text
TEXT INPUT
   → NLP
   → Dict A / markers
   → Dict B / concepts
   → Activation & weights
   → Matrix / family–area placement
   → Graph construction
   → Sphere topology & propagation
   → Metrics (KME)
   → Reasoning (TRIZ)
   → Domain projections (clinical)
   → Reports / products / API
```

Failures **downstream** of a broken layer are unreliable until that layer is fixed.

---

## 2. Layered dependency diagram

### Layer 0 — Core primitives

| Modules | `core/*` |
|---------|----------|
| **Role** | Deterministic JSON, hashing, serialization, numeric helpers, schema utilities, projection |
| **Deps** | Python stdlib + minimal third-party (as per stack) |
| **Status** | **SAFE + FROZEN for RAD** — changes ripple everywhere |

`tools/*` is **not** layer-0: many scripts depend on `hesperia/`, `sphere/`, or `runtime/`.

---

### Layer 1 — Structural definitions

| Modules | `data/`, `specs/canon/`, `sphere/topology/` |
|---------|--------------------------------------|
| **Role** | Area adjacency, icosahedron structure, family geometry, embedding constants |
| **Invariant** | See [TOPOLOGY_INVARIANTS.md](TOPOLOGY_INVARIANTS.md): **12 areas**, **288 families**, **72 000 hexes** (10+2 areas / 240+48 families / 60k+12k hexes for public vs reserved) |
| **Status** | **FROZEN** — do not change during ad-hoc testing |

---

### Layer 2 — Ontology and lexicon

| Modules | `hesperia/ontology/`, `hesperia/config/`, `lexicon/` |
|---------|-----------------------------------------------------|
| **Role** | Dict A, Dict B, `ontology_registry.yaml` — marker → concept → coordinate rules |
| **Depends on** | `core`, layer-1 data/spec |
| **Feeds** | NLP, activation, pipeline matching |
| **Status** | **TUNABLE** — most lexical calibration happens here |

---

### Layer 3 — NLP

| Modules | `hesperia/nlp/` |
|---------|-----------------|
| **Role** | Segmentation, tokenization, marker detection, concept extraction (`analyze_session`, etc.) |
| **Depends on** | `lexicon`, Dict A, ontology loaders |
| **Feeds** | Activation payloads, clinical graph builders |
| **Status** | **TUNABLE** — recall/latency sensitive |

---

### Layer 4 — Activation system (code mapping)

There is **no** separate `hesperia/engine/activation` or `hesperia/engine/relations` package. **Functionally:**

| Concern | Real modules |
|---------|--------------|
| Session activation | `hesperia/nlp/session_parser.py`, related NLP modules |
| Hits / relations for KME | `hesperia/engine/kme/clinical_bridge.py` (`activation_to_hits_and_relations`, `build_clinical_active_graph`) |
| Lexicon-side matching | `runtime.pipeline.analyze`, sphere pipeline matched tokens |

**Depends on:** NLP, Dict B, ontology. **Feeds:** semantic graph, KME `ActiveGraph`, TRIZ inputs. **Status:** **TUNABLE**.

---

### Layer 5 — Alignment / placement

Concept placement in **area × family × hex** space (matrix-style **M[area][family][hex]** conceptually).

| **Depends on** | ontology, activation outputs |
| **Feeds** | graph layer, sphere attribution |
| **Status** | **FROZEN STRUCTURE** — coordinate system fixed; **content** (which concept maps where) via ontology |

---

### Layer 6 — Graph engine

| Modules | `hesperia/graph/` |
|---------|-------------------|
| **Role** | Graph store, nodes, relations, traversal |
| **Depends on** | activation path, placement |
| **Feeds** | sphere pipeline inputs, KME domain graph loaders |
| **Status** | **MOSTLY STABLE** — tuning usually in relations/ontology, not store shape |

---

### Layer 7 — Sphere topology

| Modules | `sphere/topology/` (incl. embedding loaders), `sphere/propagation/`, `sphere/metrics/`, `sphere/pipeline/` |
|---------|-------------------------------------------------------------------------------------------------------------|
| **Role** | Adjacency, propagation, L1–L9 metrics, distance-style behavior |
| **Depends on** | topology data, attributed input from graph/lexicon path |
| **Feeds** | pipeline diagnostics, USF, domain_metrics bridge |
| **Status** | **FROZEN** for geometry — breaks calibration if changed casually |

---

### Layer 8 — KME metrics engine

| Modules | `hesperia/engine/kme/` (`active_graph`, `primitives`, `derived`, `fingerprint`, `pipeline`, `clinical_bridge`) |
|---------|---------------------------------------------------------------------------------------------------------------|
| **Depends on** | `ActiveGraph` / domain graph, constants; TRIZ reads same graph + topology hints |
| **Feeds** | reports, TRIZ, `domain_metrics` E2E artifact, session KME artifact |
| **Status** | **CALIBRATION LAYER** — normalization tunable |

---

### Layer 9 — TRIZ reasoning engine

| Modules | `hesperia/extensions/triz/` |
|---------|-------------------------|
| **Role** | Contradictions, propagation narrative, innovation signals |
| **Depends on** | KME-style graph, topology maps from activation trace / coordinates |
| **Feeds** | API `/analysis/triz`, product packagers |
| **Status** | **EVOLVING** — thresholds and report shape may change |

---

### Layer 10 — Domain projection

| Modules | `research/clinical_tfp/` |
|---------|---------------------|
| **Role** | TFP-oriented signals, session topology, defenses, transference, etc. |
| **Depends on** | NLP activation, graph/session structures |
| **Feeds** | session topology E2E artifact, clinical reports |
| **Status** | **TUNABLE** — domain knowledge |

---

### Layer 11 — Runtime orchestrator

| Modules | `runtime/pipeline/`, `runtime/services/`, `runtime/artifact_writer/`, `runtime/api/` |
|---------|--------------------------------------------------------------------------------------|
| **Role** | Run pipelines, write artifacts, HTTP API, dossier/shipping |
| **Depends on** | all engine layers above |
| **Outputs** | E2E artifacts, API JSON, dossiers |
| **Status** | **STABLE** — change only with contract/version bumps |

---

## 14. Artifact layer

| Location | `assets/artifacts/` (e.g. `e2e/`) |
|----------|-----------------------------------|
| **Typical outputs** | Full `run_e2e_all`: **19** baseline JSON (+ optional field dynamics) — [E2E_RUN_ORDER.md](E2E_RUN_ORDER.md), [E2E_OUTPUTS.md](../assets/artifacts/e2e/E2E_OUTPUTS.md) |

---

## 15. Testing layer

| Modules | `tests/` |
|---------|----------|
| **Key E2E** | `tests/test_e2e_flows.py` |
| **Ensures** | pipelines run, imports resolve, artifacts exist |

---

## 16. Module dependency graph (condensed)

```text
core
  → spec + data
  → lexicon + ontology (+ config)
  → NLP
  → activation / hits / relations (clinical_bridge + session parse)
  → alignment / placement (ontology + topology)
  → semantic graph (graph store + KME graph)
  → sphere topology & pipeline
  → KME metrics
  → TRIZ reasoning
  → domain projection (clinical)
  → runtime pipeline / API
  → artifacts
```

---

## 17. Safe vs risky modules

| **Must stay frozen (RAD)** | `core` (contract math), `sphere/topology` geometry, `specs/canon/` + frozen `data/`, alignment **structure** |
| **Calibration-heavy** | Dict A/B, NLP tuning, relation weights, KME normalization, TRIZ thresholds |
| **Domain extend** | `hesperia/clinical`, corpus loaders, domain configs, `hesperia/product` |

---

## 18. Practical testing strategy

Verify **in order** (failure at layer *N* invalidates checks below):

1. **NLP** → marker / concept detection  
2. **Activation** → concept placement and weights  
3. **Graph** → relation integrity  
4. **Sphere** → propagation / L1–L9 validity  
5. **KME** → metric stability & fingerprint  
6. **TRIZ** → contradiction / signal sanity  
7. **Clinical projection** → session topology mapping  

**Rule:** if layer *N* fails, treat **all downstream** results as suspect until *N* is green.

---

*Last aligned with repository layout and TOPOLOGY_INVARIANTS; update when architecture boundaries move.*
