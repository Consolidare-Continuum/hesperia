<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
See LEGAL_NOTICE.md for full terms.
-->

# HESPERIA — repository map (canonical description)

**Hesperia Engine Dynamics v0.5 (canonical release, closed):** [HESPERIA_v0_5_ENGINE_DYNAMICS.md](HESPERIA_v0_5_ENGINE_DYNAMICS.md) · [release narrative](../specs/release/HESPERIA_v0_5_ENGINE_DYNAMICS_RELEASE.md) · [CHANGELOG.md](../CHANGELOG.md) · [canonical naming](ENGINE_DYNAMICS_CANONICAL_NAMING_v0.5.md)  
**Awareness + research archive:** [HESPERIA_SYSTEM_AWARENESS.md](HESPERIA_SYSTEM_AWARENESS.md) · [research/reports/HESPERIA_RAD_DEEP_RESEARCH_2026-03-18.md](../research/reports/HESPERIA_RAD_DEEP_RESEARCH_2026-03-18.md)

**Purpose:** Single document describing what the archive is, how top-level directories map to layers, and how execution flows. Use this as the **long-form repo description** (GitHub’s short “Description” field is ~350 characters — link here or paste a one-line summary).

**Suggested GitHub short description (paste into repo Settings → Description):**  
*Hesperia Engine Dynamics: deterministic multiscale semantic physics (concept→hex→family→area→signals→HSPR); L1–L9 sphere execution_flow, KME, TRIZ; `run_e2e_all` → 19 E2E JSON artifacts (+ optional field dynamics). RAD reference architecture.*

**Scale:** The archive contains on the order of **~1100–1600+ files** under a single repository root (exact count varies with lexicon, benchmarks, and demos). Treat the tree below as **`<repo-root>/`** (e.g. `hesperia-main/` if distributed as a tarball).

---

## Top-level modules

| Directory | Role |
|-----------|------|
| `assets/` | Versioned calibration + public maps; **frozen** E2E exemplars under `assets/artifacts/` (not casual run dumps) |
| `benchmarks/` | Algorithm / corpus benchmarks (e.g. TRIZ) |
| `core/` | Deterministic computation, shared primitives |
| `data/` | Frozen structural inputs (topology, constants) |
| `examples/` | Runnable demos (e.g. **`examples/extensions/triz_demo/`** TRIZ report scripts) |
| `deploy/` | Docker, compose, deployment (e.g. TRIZ MVP) |
| `docs/` | Explanatory docs, governance, maps (**binding specs → `specs/`**) |
| `hesperia/` | Engine package: KME, hex stack, `extensions/` (dynamics, TRIZ), ontology, NLP, product helpers |
| `legacy/` | **Quarantine:** deprecated code, frozen data dumps (`legacy/assets/data/`), historical specs (`legacy/docs/specs_history/`), refactor notes |
| `lexicon/` | Lexical resources, Dict A/B tooling |
| `outputs/` | **Generated** run artifacts (default gitignored); see `GENERATED_ARTIFACT_POLICY.md` |
| `research/` | **Experimental** material — e.g. **`research/clinical_tfp/`** (TFP/clinical; non-product) |
| `runtime/` | Execution: API, pipelines, services, shipping |
| `schemas/` | Canonical JSON Schema (`schemas/public/…`); legacy symlink under `assets/public/` |
| `specs/` | **Binding** specifications: `canon/`, `dynamics/`, `release/`, `schemas/`, `calibration/` |
| `spec/` | Symlink → **`specs/canon/`** (compat for code paths expecting `spec/*.yaml`) |
| `sphere/` | Topology-backed execution_flow (L1–L9, propagation, USF) |
| `tests/` | Pytest unit, integration, E2E |
| `tools/` | Utilities, calibration, TRIZ CLI helpers |
| `requirements/` | Python deps (`runtime.txt`, `api.txt`, `surface.txt`, …); root `requirements.txt` includes `runtime.txt` |

---

## Functional map: infrastructure → engine → measurement → outputs

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
| `runtime/api/` | HTTP API (measurement, metrics, TRIZ, etc.) |
| `runtime/execution_flow/` | **Main orchestration** — E2E commands (e.g. `run_e2e_all.py`), analyze, L1–L9 entrypoints |
| `runtime/runners/` | Reference / CLI runners |
| `runtime/services/` | Reusable services (e.g. structural measurement, config) |
| `runtime/artifact_writer/` | Deterministic writing of outputs → **`assets/artifacts/`** |
| `runtime/provenance/` | Reproducibility: hashes, run metadata, build signatures |
| `runtime/public_reports/` | Readable reports from artifacts |
| `runtime/dossier/` | Structured dossiers (policy, domain, document summaries) |
| `runtime/shipping/` | Sealed builds: Docker, manifests, checksums |
| `runtime/configs/` | Example JSON for semantic field + field calibration |

**E2E:** `python3 -m runtime.execution_flow.run_e2e_all` produces **19** baseline JSON artifacts (+ **20th** with `HESPERIA_FIELD_DYNAMICS=1`); see `docs/E2E_RUN_ORDER.md`, manifest `assets/artifacts/e2e/E2E_OUTPUTS.md`, default under `assets/artifacts/e2e/`.

---

### 4. Sphere topology layer — `sphere/`

Mathematical backbone: **icosahedral surface graph** (12 areas / nodes, 30 edges, degree 5), propagation, L1–L9 execution_flow.

**Representative layout:**

| Area | Role |
|------|------|
| `sphere/topology/` | Graph, embedding, family/area structure, export |
| `sphere/propagation/` | Signal movement across topology |
| `sphere/execution_flow/` | Canonical **L1–L9** runner, layer registry, contracts |
| `sphere/metrics/`, `sphere/diagnostics/`, … | Layer and tension metrics |
| `sphere/usf/`, `sphere/shadow/`, `sphere/interpretation/` | Fingerprint, shadow, interpretation |
| `sphere/logic/`, `sphere/prolog_logic/` | Rule layers, explanation |
| `sphere/runtime/` | Topology guards at startup |

---

### 5. Semantic engine — `hesperia/`

Core knowledge and text compute stack.

| Submodule | Role |
|-----------|------|
| `hesperia/nlp/` | Text → tokens, markers, concepts, session parsing |
| `hesperia/ontology/` | Dict A/B, registry (`ontology_registry.yaml`), relations |
| `hesperia/config/` | System / clinical / execution_flow parameters |
| `hesperia/corpus/` | Corpus ingestion, session corpus helpers |
| `hesperia/graph/` | Semantic graph store |
| `hesperia/engine/` | **KME**, hex stack, explainability, calibration (core path) |
| `hesperia/extensions/` | **`dynamics`**, **`triz`** — optional extensions (see `EXTENSION_STATUS.yaml`) |
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
| `hesperia/extensions/triz/` | **TRIZ:** contradictions, propagation, reports, `run_triz_analysis_complete` |
| `hesperia/engine/hex_dynamics.py`, `hex_family_bridge.py`, `hex_matrix_builders.py`, `hex_outputs/` | **Engine Dynamics v0.5:** hex microphysics, bridge, E2E integration |
| `hesperia/engine/sealed_multiscale_stack.py` | **Sealed stack:** hex → family/area → product_signals → **HSPR** |
| `hesperia/engine/product_signals.py`, `observables.py`, `hspr_index.py` | Product observables + system HSPR index |
| `hesperia/extensions/dynamics/` | Ethan phases + semantic field v1 (optional E2E) |
| `hesperia/engine/explainability.py` | Activation trace → topology hints for TRIZ/KME |
| `hesperia/engine/calibration/` | Activation + field calibration (`hspr_field`, …) |

*Logical execution_flow:* attributions feed **hex** and **family** layers; **KME** / **TRIZ** consume graph + topology; **v0.5** adds deterministic **sealed multiscale** outputs for product signals.

#### 5.4 Clinical / TFP (experimental) — `research/clinical_tfp/`

TFP-oriented domains (affects, defenses, transference, session topology, etc.). **Not** baseline product engine — see `research/clinical_tfp/README.md`.

#### 5.5 Product — `hesperia/product/`

Policy/innovation/narrative packaging, investor demo, MVP acceptance, tenant context.

---

### 6. Specifications — `specs/` (binding) vs `docs/` (explanatory)

**Tier-1 index (Task 3):** [`specs/CANONICAL_INDEX.md`](../specs/CANONICAL_INDEX.md) · inventory [`specs/INVENTORY.md`](../specs/INVENTORY.md).  
**Core execution_flow (binding):** `specs/core/*.md`. **Family-field dynamics (single file):** `specs/dynamics/semantic_field_dynamics.md`. **`spec/canon` YAML** via `spec/` symlink; markdown there is mostly **redirect** to `core/`.  
**Master narrative index:** [HESPERIA_v0_5_ENGINE_DYNAMICS.md](HESPERIA_v0_5_ENGINE_DYNAMICS.md). Long-form **Tier-2** dynamics / calibration: `specs/dynamics/` (Ethan, equation index). Release notes: `specs/release/`. Workflow / triage: `docs/specs/`; governance task memos: `docs/governance/working/`, `docs/governance/project/`. Geometry lock: `docs/TOPOLOGY_INVARIANTS.md`.

---

### 7. Benchmarks, examples

| Path | Use |
|------|-----|
| `benchmarks/extensions/triz/` | TRIZ corpus fixtures (optional extension) |
| `examples/extensions/triz_demo/` | Scripted TRIZ demo reports (`triz/make_demo_reports.py`) |
| `examples/` | Other sample I/O as added |

---

### 8. Deployment — `deploy/`

Dockerfiles, compose, env examples (e.g. `deploy/extensions/triz_mvp/`).

---

### 9. Assets — `assets/`

Versioned registries + **reviewed frozen** E2E exemplars: `assets/artifacts/e2e/` (**19** baseline JSON + optional field dynamics — `E2E_OUTPUTS.md`). Casual run dumps → **`outputs/`** (gitignored).

---

### 10. Testing — `tests/`

Unit, integration, domain, product, TRIZ suites; **experimental** clinical/TFP under `tests/experimental/clinical_tfp/`. **E2E:** `tests/test_e2e_flows.py`.

---

### 11. Tools — `tools/`

Calibration data, diagnostics, **TRIZ** CLIs under `tools/triz/`.

---

### 12. Full execution_flow execution (conceptual)

```text
Text
  → NLP parsing
  → Dict A marker detection
  → Dict B concept mapping
  → Matrix / family coordinate placement
  → Semantic graph construction
  → Sphere topology propagation (L1–L9 path)
  → KME metrics (domain + session paths)
  → TRIZ contradiction / innovation measurement
  → Domain / clinical topology projection
  → Product & report generation
```

**Single orchestrated E2E entrypoint:** `runtime.execution_flow.run_e2e_all` → **19** artifacts, optional **20th** (`docs/E2E_RUN_ORDER.md`).

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

*Canonical repository description — **Engine Dynamics v0.5**; update when layout or E2E contract changes.*
