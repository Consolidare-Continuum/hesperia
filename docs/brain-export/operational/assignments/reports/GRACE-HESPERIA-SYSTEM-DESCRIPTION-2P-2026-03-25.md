# Hesperia at `/data/hesperia` — two-page system description (documentation)

**Status:** Canonical brief for documentation and onboarding.  
**Sources:** Ethan reports dated 2026-03-25 (`ETHAN-HESPERIA-*` under `operational/assignments/reports/`).  
**SIGNED:** Triage (Grace) | documentation pack | 2026-03-25 | Hesperia `/data/hesperia`

---

## Page 1 — What the system is and how it is organized

### Location and scope

- **Host path:** `/data/hesperia/` holds the Hesperia workspace; the **engine repository** is **`/data/hesperia/hesperia`** (canonical code, schemas, assets, pipelines).
- **Role:** Hesperia is a **deterministic, multi-stage engine** that ingests **text** (e.g. clinical session transcripts), runs it through **versioned lexical and topological resources**, and produces **structured JSON artifacts**, **public-facing projections** (where applicable), and **governance outputs** (schema validation, calibration audit, release gate).

### One-sentence scientific description

Hesperia is a **deterministic hierarchical measurement-and-inference system**: it resolves text into **concept-level evidence** with traceable rules, **projects** that evidence through an **ontology-backed hierarchy** (concept → family → area), optionally **evolves or regularizes** signal on a **graph/field substrate** (hex layer and topology), derives **indices and product signals**, compares **multiple estimator “planes”** for agreement, and **accepts or blocks** further use via **reliability-style gates**.

This is **not** a single end-to-end learned model. It is a **stack of coupled estimators** (planes) over the same input, with explicit contracts (schemas, registries, versioning).

### Functional flow (operator view)

Typical analysis flows (exact flags vary by pipeline):

1. **Ingestion** — load session text (and optional speaker structure).
2. **Lexical measurement** — tokenize, normalize, match markers; apply damping, caps, normalization; produce **concept / family / area** activations.
3. **Structural / Sphere plane** — deterministic structural analysis under fixed topology resources (L1–L9 style structural batch).
4. **DLCR / resolver plane** — span-level resolution to concept IDs with **candidate lists, scores, winner, reason codes** (auditable “instrument”).
5. **Hex microstructure** — bridge sparse lexical hits into **hex-scale** representations for microphysics-style observables.
6. **Sealed multiscale stack** — markers → concept mass → **hex field** \(H\); optional local microphysics step \(H_0 \rightarrow H_1\); **aggregate** to family/area for interpretation; compute **product signals** and **HSPR** under the **hex-causal rule**: core KPI formulas consume the **hex field**, not pre-aggregated family vectors as formula inputs.
7. **Extensions** — optional **KME**, **TRIZ**, **session topology** (segmentation, curves, transitions).
8. **Governance** — **calibration audit** (cross-plane consistency score, alarms, suspect fields) and **release gate** (pass/fail policy over schema, anomalies, consistency floor, optional goldset).

### Repository shape (where to look)

| Area | Role |
|------|------|
| `hesperia/` | Engine package: NLP, ontology, engines, extensions |
| `sphere/` | Topology-backed pipeline, propagation, USF / fingerprint |
| `runtime/` | API, orchestration, shipping, provenance |
| `schemas/` | JSON Schema contracts (public, bundle, lexical) |
| `assets/` | Versioned calibration, maps, frozen exemplars |
| `data/` | Frozen topology inputs |
| `research/` | Experimental stacks (e.g. clinical TFP) — not baseline product by default |
| `outputs/` | Generated runs (typically gitignored) |

**Version truth:** `VERSION.yaml` (`system_version`, component pins, schema ids, calibration profile bundle).

---

## Page 2 — Scientific definitions, alignment to literature, and proper use

### Primary scientific umbrella (documentation name)

**Hierarchical latent-state measurement model with multi-view (multi-plane) readouts and graph-structured ontology.**

- **Observed:** text tokens, spans, optional speaker tags, segment windows.  
- **Latent (operational sense):** concept/family/area summaries — **inferred**, not directly observed clinical truth.  
- **Measurement:** marker hits are **indicators**; resolver output is the **instrument trace**.  
- **Multi-view:** structural batch, session parser, DLCR, sealed stack, `analyze()`, topology, TRIZ, KME are **different estimators**; the **calibration audit** scores **empirical agreement** between them under fixed resources.  
- **Release gate:** **reliability governance** — block shipping when measurement validity is out of spec (schemas, anomalies, consistency thresholds, optional goldset).

### Alignment to rediscovered book concepts (Chroma `books`)

Use this table when writing external-facing science text; it keeps language honest.

| Hesperia idea | Scientific anchor (literature family) | Use in documentation |
|---------------|----------------------------------------|----------------------|
| Concept/family/area activations | Latent variables + measurement / factor-style models | “Indicator-derived latent summaries,” not ground truth |
| Topology / registry | Ontology as conceptualization; `is-a` / `part-of` hierarchies | Formal vocabulary + typed projection |
| Stages, thresholds, classifiers | Rule-based expert systems (chaining, firing) | Explicit deterministic rules |
| Cross-plane combination | Evidence fusion frameworks (e.g. D-S as *concept*) | Say “fusion” unless full formalism is implemented |
| Hex / propagation | Graph adjacency, Laplacian, spectral graph intuition | Neighborhood-structured field transforms |
| Segment transitions | Markov chains / discrete dynamics | “Markov-like” unless a full HMM is fit |
| Entropy-like scalars | Information-theoretic summaries | Distribution concentration / uncertainty index |
| Retrieval / ranking quality | IR evaluation (precision, recall, AP, rank metrics) | Evaluate evidence/retrieval modules properly |
| Audit consistency | Estimator agreement under assumptions | Diagnostic, not proof of correctness |
| Release gate | Software reliability testing discipline | Operational dependability policy |

### Metrics: what they are scientifically

- **Declared semantics** live in **`assets/config/output_metric_registry_v1.json`** (`semantic_type`, ranges, null policy, comparability across runs).
- **Sealed product signals** (contradiction pressure, propagation strength, narrative density, spatial entropy on hex, innovation potential, etc.) are **deterministic indices** of the **hex field** and coupling matrices — useful engineering summaries, **not** standalone clinical constructs unless separately validated.
- **Public output** (`schemas/public/public_output_schema.json`) is a **projection** that **must not** leak internal geometry; treat it as a **reporting layer** over internal state.

### Guardrails (non-negotiable for sound docs)

- Do **not** label the pipeline “causal” without an explicit causal model and assumptions.  
- Do **not** call stage logic “HMM inference” unless transition/emission models are estimated and scored.  
- Do **not** claim “Dempster–Shafer” unless belief/plausibility outputs and combination rules are implemented and tested.  
- Default public stance: **deterministic measurement system** + **governed multi-plane estimators** + **reliability gates**.

### Intended use

- **Engineering:** versioned rebuilds, regression bundles, schema-sealed releases.  
- **Research:** experimental planes under `research/` with explicit non-product scope.  
- **Product / API:** public schema and vocabulary only; traceability via `system_version`, `build_id`, `calibration_profile`, schemas.

### Deep references (Ethan, same date)

- Model formulation + structure layers A–G: `ETHAN-HESPERIA-MODEL-FORMULATION-STRUCTURE-GUIDE-2026-03-25.md`  
- Component / plane / metric definitions: `ETHAN-HESPERIA-SCIENTIFIC-DEFINITIONS-COMPONENTS-LAYERS-METRICS-2026-03-25.md`  
- Books alignment + terminology guardrails: `ETHAN-HESPERIA-SCIENTIFIC-ALIGNMENT-BOOKS-REDISCOVERY-2026-03-25.md`  
- Yield / evaluation proposals (separate thread): `ETHAN-HESPERIA-ENHANCEMENTS-FROM-CHROMA-BOOKS-2026-03-25.md`

---

*End — target length ~two printed pages at normal body font; expand only by linking to specs in `/data/hesperia/hesperia/specs/` and `schemas/`.*
