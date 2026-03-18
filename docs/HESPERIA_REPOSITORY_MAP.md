<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
See LEGAL_NOTICE.md for full terms.
-->

# HESPERIA — repository map (canonical description)

**End-to-end awareness (product + integration):** [HESPERIA_SYSTEM_AWARENESS.md](HESPERIA_SYSTEM_AWARENESS.md) · [research/HESPERIA_RAD_DEEP_RESEARCH_2026-03-18.md](research/HESPERIA_RAD_DEEP_RESEARCH_2026-03-18.md)

**Purpose:** Single document describing what the archive is, how top-level directories map to layers, and how execution flows. Use this as the **long-form repo description** (GitHub’s short “Description” field is ~350 characters — link here or paste a one-line summary).

**Suggested GitHub short description (paste into repo Settings → Description):**  
*Deterministic semantic engine: Sphere topology, KME metrics, TRIZ reasoning, clinical NLP — orchestrated via `runtime.pipeline.run_e2e_all` (9 E2E artifacts). RAD reference architecture.*

**Scale:** The archive contains on the order of **~1100–1600+ files** under a single repository root (exact count varies with lexicon, benchmarks, and demos). Treat the tree below as **`<repo-root>/`** (e.g. `hesperia-main/` if distributed as a tarball).

---

## Top-level modules

| Directory | Role |
|-----------|------|
| `assets/` | Generated artifacts, E2E outputs |
| `benchmarks/` | Algorithm / corpus benchmarks (e.g. TRIZ) |
| `core/` | Deterministic computation, shared primitives |
| `data/` | Frozen structural inputs (topology, constants) |
| `demo/` | Demonstrations (e.g. TRIZ demo reports) |
| `deploy/` | Docker, compose, deployment (e.g. TRIZ MVP) |
| `docs/` | Specs, architecture, governance |
| `examples/` | Sample outputs / README |
| `hesperia/` | Semantic engine (NLP, ontology, KME, TRIZ, clinical, product) |
| `lexicon/` | Lexical resources, Dict A/B tooling |
| `runtime/` | Execution: API, pipelines, services, shipping |
| `spec/` | Structural specifications (YAML / invariants) |
| `sphere/` | Topology-backed pipeline (L1–L9, propagation, USF) |
| `tests/` | Pytest unit, integration, E2E |
| `tools/` | Utilities, calibration, TRIZ CLI helpers |

---

## Functional map: infrastructure → engine → analysis → outputs

### 1. System architecture overview

HESPERIA is organized into **six operational layers**:

```text
Infrastructure
    ↓
Runtime execution
    ↓
Topology (Sphere)
    ↓
Semantic engine
    ↓
Analytical engines
    ↓
Products / outputs
```

The directories above map directly to these layers.

---

### 2. Infrastructure layer

#### `core/`

Foundational utilities and shared infrastructure.

**Typical roles:** serialization, hashing, deterministic IO, schema utilities, graph primitives, numeric helpers.

**Purpose:** deterministic artifacts; shared data structures; isolate primitives from domain code. **No domain logic** in the sense of clinical/TRIZ product rules.

#### `data/`

Static datasets used by the engine: topology matrices, area adjacency, family geometry, frozen constants, domain graphs. **Frozen structural inputs.**

#### `lexicon/`

Lexical resources: marker lists, synonyms, normalization, stopword rules. Feeds **Dict A** detection and lexicon build/validation.

---

### 3. Runtime execution layer — `runtime/`

Execution environment for the system.

| Path | Role |
|------|------|
| `runtime/api/` | HTTP API (analysis, metrics, TRIZ, etc.) |
| `runtime/pipeline/` | **Main orchestration** — E2E commands (e.g. `run_e2e_all.py`), analyze, L1–L9 entrypoints |
| `runtime/runners/` | Reference / CLI runners |
| `runtime/services/` | Reusable services (e.g. structural analysis, config) |
| `runtime/artifact_writer/` | Deterministic writing of outputs → **`assets/artifacts/`** |
| `runtime/provenance/` | Reproducibility: hashes, run metadata, build signatures |
| `runtime/public_reports/` | Readable reports from artifacts |
| `runtime/dossier/` | Structured dossiers (policy, domain, document summaries) |
| `runtime/shipping/` | Sealed builds: Docker, manifests, checksums |

**E2E:** `python3 -m runtime.pipeline.run_e2e_all` produces **9** analysis artifacts (see `docs/E2E_RUN_ORDER.md`, default under `assets/artifacts/e2e/`).

---

### 4. Sphere topology layer — `sphere/`

Mathematical backbone: **icosahedral surface graph** (12 areas / nodes, 30 edges, degree 5), propagation, L1–L9 pipeline.

**Representative layout:**

| Area | Role |
|------|------|
| `sphere/topology/` | Graph, embedding, family/area structure, export |
| `sphere/propagation/` | Signal movement across topology |
| `sphere/pipeline/` | Canonical **L1–L9** runner, layer registry, contracts |
| `sphere/metrics/`, `sphere/diagnostics/`, … | Layer and tension metrics |
| `sphere/usf/`, `sphere/shadow/`, `sphere/interpretation/` | Fingerprint, shadow, interpretation |
| `sphere/logic/`, `sphere/prolog_logic/` | Rule layers, explanation |
| `sphere/runtime/` | Topology guards at startup |

---

### 5. Semantic engine — `hesperia/`

Core knowledge and text processing stack.

| Submodule | Role |
|-----------|------|
| `hesperia/nlp/` | Text → tokens, markers, concepts, session parsing |
| `hesperia/ontology/` | Dict A/B, registry (`ontology_registry.yaml`), relations |
| `hesperia/config/` | System / clinical / pipeline parameters |
| `hesperia/corpus/` | Corpus ingestion, session corpus helpers |
| `hesperia/graph/` | Semantic graph store |
| `hesperia/engine/` | **KME**, **TRIZ**, explainability, calibration |
| `hesperia/clinical/` | TFP-oriented clinical signals, session topology, defenses |
| `hesperia/product/` | Commercial outputs, API contracts, release gates |
| `hesperia/evaluation/` | Baselines, TRIZ evaluation |
| `hesperia/experiments/` | Experiment runner |
| `hesperia/logging/` | Session logging |
| `hesperia/visualization/` | Graph / session visualizations |

#### 5.1 NLP — `hesperia/nlp/`

Tokenization, segmentation, marker detection, concept extraction → feeds Dict A / session pipelines.

#### 5.2 Ontology — `hesperia/ontology/`

Governance of Dict A/B, relations, families, areas — consistent ontology versions.

#### 5.3 Engine — `hesperia/engine/`

| Path | Role |
|------|------|
| `hesperia/engine/kme/` | **KME:** active graph, primitives, derived, fingerprint, clinical bridge, `run_session_kme_pipeline` |
| `hesperia/engine/triz/` | **TRIZ:** contradictions, propagation, reports, `run_triz_analysis_complete` |
| `hesperia/engine/explainability.py` | Activation trace → topology hints for TRIZ/KME |
| `hesperia/engine/calibration/` | Activation calibration |

*Logical pipeline:* activations and **Dict-B-style relations** feed **KME** `ActiveGraph`; **TRIZ** consumes graph + topology.

#### 5.4 Clinical — `hesperia/clinical/`

TFP-oriented domains (affects, defenses, transference, session topology, etc.) for clinical projections.

#### 5.5 Product — `hesperia/product/`

Policy/innovation/narrative packaging, investor demo, MVP acceptance, tenant context.

---

### 6. Specifications — `spec/`

Structural specs: areas, families, embedding rules, topology invariants (see also `docs/TOPOLOGY_INVARIANTS.md`).

---

### 7. Benchmarks, demos, examples

| Path | Use |
|------|-----|
| `benchmarks/` | Corpus fixtures, TRIZ benchmarks |
| `demo/` | Scripted demos (e.g. TRIZ reports) |
| `examples/` | Sample JSON outputs |

---

### 8. Deployment — `deploy/`

Dockerfiles, compose, env examples (e.g. `deploy/triz_mvp/`).

---

### 9. Assets — `assets/`

Generated outputs; **E2E:** `assets/artifacts/e2e/` (9 files from `run_e2e_all`).

---

### 10. Testing — `tests/`

Unit, integration, domain, product, TRIZ suites. **E2E:** `tests/test_e2e_flows.py`.

---

### 11. Tools — `tools/`

Calibration data, diagnostics, **TRIZ** CLIs under `tools/triz/`.

---

### 12. Full pipeline execution (conceptual)

```text
Text
  → NLP parsing
  → Dict A marker detection
  → Dict B concept mapping
  → Matrix / family coordinate placement
  → Semantic graph construction
  → Sphere topology propagation (L1–L9 path)
  → KME metrics (domain + session paths)
  → TRIZ contradiction / innovation analysis
  → Domain / clinical topology projection
  → Product & report generation
```

**Single orchestrated E2E entrypoint:** `runtime.pipeline.run_e2e_all` → **9** artifacts (`docs/E2E_RUN_ORDER.md`).

---

## 13. System capability summary & dependency graph

**Capabilities + runtime dependency layers (what feeds what, frozen vs tunable, testing order):**  
[HESPERIA_DEPENDENCY_GRAPH.md](HESPERIA_DEPENDENCY_GRAPH.md)

**NLP → KME → TRIZ variable / signal catalog:**  
[HESPERIA_VARIABLE_CATALOG.md](HESPERIA_VARIABLE_CATALOG.md)

**Commercial product lines (A–G):**  
[HESPERIA_PRODUCT_LINES.md](HESPERIA_PRODUCT_LINES.md)

**Product stack map (layers 1–14):**  
[HESPERIA_PRODUCT_STACK_MAP.md](HESPERIA_PRODUCT_STACK_MAP.md)

---

*This file is the canonical “repository description as of now”; update it when top-level layout or E2E contract changes.*
