# Hesperia (`/data/hesperia`): model formulation + structure guide (book-backed)

Date: 2026-03-25  
Role: Ethan  
Scope: Turn **arbitrary pipeline code** into a **named scientific object** with **rebuildable layers**, aligned to Chroma `layer=books` sources where they fit.

---

## 1. Problem statement (your diagnosis)

The repo can be clear and the bundle can run, but **without an explicit model object** the system stays **under-specified**: weights, planes, and rules are hard to defend, compare across versions, or improve under measurement. This document names **one primary formulation** (composite, standard in the literature) and a **directory-aligned structure** so rebuild or migration is not guesswork.

---

## 2. What Hesperia TFP actually is (ground truth from `/data/hesperia/hesperia`)

From `values-tfp-extracted.md` and bundle manifests, the running system is already structurally:

| Mechanism | Role |
|-----------|------|
| **Lexical markers → scores** | Text is tokenized; dictionary hits drive **concept / family / area** activations with damping, caps, normalization. |
| **Hierarchical aggregation** | Scores roll up a **taxonomy** (concept ⊂ family ⊂ area) with optional **graph propagation** (embedding on topology). |
| **Temporal structure** | Windows → segments → curves, transitions, stage labels (`tfp_stage`). |
| **Multiple estimators (“planes”)** | Structural batch, session parser, DLCR, sealed multiscale, `analyze()`, topology, TRIZ, KME — then **cross-plane audit** and **release gate**. |

So the implementation is **not** “one model”; it is a **stack of coupled estimators** over the same underlying clinical text. That is exactly where a **single scientific umbrella** helps.

---

## 3. Best-fitting **primary** formulation (recommended umbrella)

**Name (use this in docs and APIs):**  
**Hierarchical latent-state measurement model with multi-view (multi-plane) readouts, lexical likelihoods, and graph-structured prior on the taxonomy.**

In plain terms:

- **Latent**: “true” session-level and segment-level clinical state (not observed directly).
- **Observed**: token sequence, speaker tags, time windows.
- **Measurement**: each marker hit is a **noisy indicator** of latent concept activation; aggregation rules are **measurement functions** (not ad hoc if you document them as such).
- **Taxonomy**: ontology-backed **is-a / part-of style** structure (your TFP graph + hex/family/area).
- **Multi-view**: each **plane** is an **estimator** of overlapping quantities; **consistency** is a **testable** property (you already approximate this with calibration audit + gate).

This umbrella is the standard way to unify **rules + scores + multiple modules** without pretending everything is a single neural net.

---

## 4. Secondary formulations (explicit roles — do not mix without naming)

Use these as **named sub-models** inside the umbrella:

| Sub-model | What it maps to in Hesperia | Book anchor (Chroma `books`) |
|-----------|----------------------------|------------------------------|
| **Ontology + conceptualization** | TFP topology, `data/topology/*`, DLCR canonical concepts | *Elmasri & Navathe* — ontology as **specification of a conceptualization**; *Silberschatz & Sudarshan* — **hierarchical ontologies**, `is-a`, `part-of`, WordNet-style relations. |
| **Expert system / rule inference** | Stage rules, intervention classifier, thresholds, TRIZ rule blocks | *Siler & Buckley* — **forward/backward chaining**, rule firing, fuzzy expert systems (your pipeline is largely rule + score, not end-to-end learned). |
| **Evidence combination under uncertainty** | Combining marker mass, multi-plane signals, abstention | *Siler & Buckley* — **Dempster–Shafer** belief/plausibility and combination of evidence (useful **conceptually** for “many weak indicators”; implementation may stay simpler). |
| **Graph-structured smoothing / propagation** | Family embedding propagation, adjacency-weighted flows | *ESLII* — **similarity graphs**, **Laplacian**, spectral view of graphs (adjacency → smoothing/partition intuition). |
| **Latent / undirected graphical models** | Hidden nodes, marginalization (future: full probabilistic layer) | *ESLII* — **undirected graphical models**, latent nodes and Gaussian case notes. |
| **Segmented discrete dynamics** | `segments`, `transitions`, `state_sequence` | *Taubes (notes in corpus)* — **Markov-type** dependence across ordered segments (use as **Markov chain / HMM** story for stage sequence, even if you only implement heuristics today). |
| **Consistency / learning-theoretic view** | Cross-plane audit, goldset, gates | *Bach* — **consistency** of structured methods under assumptions (frame “audit score” as **empirical agreement** between estimators under a stated hypothesis class). |

**Pearl / causality** (*Pearl, Causality* in corpus): reserve for **explicit causal claims** (interventions, counterfactuals). Do **not** label the whole lexical pipeline as “causal” without a DAG and assumptions; use **associative / measurement** language by default.

---

## 5. Structure guide: **rebuild or align** the repo to the model

Treat the codebase as **layers**. Each layer must own **types**, **invariants**, and **tests**. Suggested mapping (adjust names to match actual tree under `/data/hesperia/hesperia`):

### Layer A — **Ontology & topology registry** (read-only at runtime)

- **Scientific object:** ontology \(O = (C, R, w)\): concepts, typed relations, optional weights.  
- **Code home:** `data/topology/`, schema packs, any `*_map.json` / embedding registry.  
- **Deliverables:** versioned `ontology_version`, `topology_version`; no silent edits in pipeline runs.

### Layer B — **Lexical measurement kernel**

- **Scientific object:** for token stream \(x\), marker \(m\), concept \(c\): contribution \(h_m(x) \rightarrow \Delta s_c\) with documented negation windows, caps, normalization.  
- **Code home:** `hesperia/nlp/session_parser.py`, lexical pipelines, marker tables.  
- **Deliverables:** single **measurement spec** (YAML/JSON) referenced by code; golden vector tests per marker family.

### Layer C — **Hierarchical sufficient statistics**

- **Scientific object:** maps concept scores → family → area (and hex projection); optional graph propagation as **smoothing on a weighted graph**.  
- **Code home:** `hesperia/engine/lexical_concept/`, `hex_outputs/`, `sealed_multiscale_stack.py`.  
- **Deliverables:** explicit **aggregation DAG** diagram in docs; prove idempotence / bounds where claimed.

### Layer D — **Temporal model**

- **Scientific object:** partition timeline into segments; per-segment latent summaries; **transition** events on discrete labels (areas/stages).  
- **Code home:** `research/clinical_tfp/session_topology.py`, `stage_detection.py`.  
- **Deliverables:** segment definition contract (window size, overlap); transition matrix optional (even if estimated offline later).

### Layer E — **Multi-view readouts (“planes”)**

- **Scientific object:** views \(V_1,\ldots,V_k\) each outputting overlapping random vectors; **agreement** functional \(A(V_i,V_j)\) (your audit).  
- **Code home:** structural batch, DLCR, sealed, analyze, TRIZ, KME — each as `PlaneId` module.  
- **Deliverables:** per-plane **schema + semantic contract** (“this plane estimates X, not Y”).

### Layer F — **Decision / release policy**

- **Scientific object:** hypothesis tests or thresholds on audit + schema + goldset → pass/fail.  
- **Code home:** `tools/tfp_calibration_audit.py`, `hesperia/engine/calibration_release_gate.py`.  
- **Deliverables:** policy as data (`release_policy_vN.yaml`), not buried constants.

### Layer G — **Public API surface**

- **Scientific object:** **observed-output** is a **reporting layer** over latent posteriors/summaries (even if point estimates today).  
- **Code home:** `schemas/public/*`, `analyze()` path.  
- **Deliverables:** explicit **epistemic status** field per output block (`point_estimate` | `heuristic_rule` | `experimental`).

---

## 6. One-page **model card** (mandatory for non-arbitrary operation)

Create `docs/MODEL_CARD.md` (in Hesperia repo, not necessarily cursor) with:

1. **Umbrella formulation** (section 3, one paragraph).  
2. **Latent variables** (session state, segment state — what you pretend exists).  
3. **Observables** (inputs).  
4. **Measurement map** (lexical kernel summary + key hyperparameters).  
5. **Planes** (list + what each estimates).  
6. **Consistency checks** (audit: which pairs must agree, tolerances).  
7. **Known violations** (where rules contradict probabilistic interpretation).  
8. **Version pins** (`ontology_version`, `calibration_registry`, schema hashes).

Until this exists, “beautiful repo” ≠ “defined model.”

---

## 7. Alignment vs rebuild

- **Align (incremental):** keep code; add model card, plane contracts, policy YAML, tests that encode sections 5–6.  
- **Rebuild (structural):** re-root packages under layers A–G; enforce imports only **downward** (G may call F, not vice versa); split “research” vs “sealed product” by **same** layer boundaries.

---

## 8. SIGNED

SIGNED: Engineer (Ethan) | Hesperia model formulation + structure guide | 2026-03-25 | Chroma books + `/data/hesperia/hesperia` ground truth
