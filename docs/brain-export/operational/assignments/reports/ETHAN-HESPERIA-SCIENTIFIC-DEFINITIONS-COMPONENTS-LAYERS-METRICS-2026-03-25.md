# Hesperia (`/data/hesperia/hesperia`): scientific definitions for components, layers, metrics (alignment-to-science)

Date: 2026-03-25  
Scope: Provide a **sound scientific definition** for each major component/layer/metric in `/data/hesperia/hesperia`, plus a **general scientific description** of “what is going on”.  
Ground truth inputs: `values-tfp-extracted.md`, `docs/HESPERIA_REPOSITORY_MAP.md`, internal schemas under `schemas/`, metric semantics in `assets/config/output_metric_registry_v1.json`, signal formulas in `hesperia/engine/product_signals.py`, sealed stack contract in `hesperia/engine/sealed_multiscale_stack.py`, gating schemas `schemas/tfp_bundle/*`.

---

## 0. The one-sentence scientific description (umbrella)

Hesperia is a **deterministic, multi-stage measurement system** that maps text into a **hierarchical latent-state representation** (concept → family → area), optionally evolves it on a **graph/field substrate** (hex microphysics + topology propagation), derives **signals/indices** (product signals + HSPR), and enforces **multi-view consistency** through audit + release gates.

This is the correct scientific framing because the system is not “one model”; it is a **stack of estimators** with governed interfaces and comparability rules.

---

## 1. Scientific vocabulary: what counts as a “component/layer/metric” here

- **Component**: a governed module with a stable contract (schemas, versioning, tests) that computes an output artifact.
- **Layer**: a *mathematical object* (vector/field/graph/timeline) that can be measured, transformed, and compared under a fixed version.
- **Metric**: a scalar or structured summary with a declared **semantic type** (probability, normalized activation, count, energy, index, etc.) and a comparability policy.

Metric semantics are explicitly intended to live in `assets/config/output_metric_registry_v1.json` (semantic_type, ranges, null policy, and whether comparable across runs).

---

## 2. Layer model (what the system “is”, formally)

### 2.1 Inputs (observables)

- **Text** \(x\): raw session text, possibly with speaker tags.
- **Resources** \(R\): versioned lexicons, ontology, topology matrices, calibration profiles, schemas.

### 2.2 Latent objects (what we infer, not directly observe)

Hesperia implicitly defines latent state at multiple scales:

- **Concept evidence state** \(c\): sparse activations over a controlled concept inventory (deterministically inferred from lexical markers + resolver rules).
- **Family state** \(f\): aggregation/projection of concept evidence into governed families.
- **Area state** \(a\): aggregation of families into governed areas.
- **Hex field state** \(H\): a 2-D field \(n_{families} \times n_{hex-per-family}\) used as the *causal substrate* for product signals (sealed stack).
- **Temporal state** \(s_t\): segment-level states and transitions induced by windowing.

### 2.3 Derived readouts (what we ship / compare)

- **Signals/indices**: deterministic functions of \(H\) (sealed product signals + HSPR).
- **Projected public outputs**: remapped representations that intentionally hide internal geometry (public schema).

---

## 3. Components / planes (definitions + scientific role)

The system is multi-plane. Each plane is an estimator of overlapping quantities; the audit/gate treat agreement as a quality proxy.

### 3.1 Lexical detection + resolver (DLCR “span resolution”)

- **Primary artifact type**: *Span-level determinations* (schemas in `schemas/lexical_concept/*`).
- **Scientific role**: a deterministic **measurement model** from text spans → concept IDs with an audit trail.
- **Output contract**: `resolver_output.schema.json` requires span boundaries, candidate concepts + scores, winner, and reason codes.

Interpretation: this is the *instrument*; everything upstream depends on its stability and versioning.

### 3.2 Session parsing / activation (“areas, families, concepts”)

- **Primary computation**: tokenize + normalize + marker matching; damping/caps/normalization; aggregate into `concepts/families/areas`.
- **Scientific role**: deterministic mapping \(x \mapsto (c,f,a)\) under fixed resources \(R\).
- **Key assumption**: “marker hits are indicators of latent concept evidence” (measurement, not ground truth).

### 3.3 Structural batch (Sphere L1–L9 / structural plane)

- **Role**: deterministic structural analysis over sessions; provides a baseline “structural state” and metrics like coverage and attributed tokens (see registry entries under `structural_batch.L1`).
- **Scientific role**: a stable estimator of structural emphasis under a fixed topology + lexicon.
- **Comparability**: intended to be comparable across runs when version + registry are stable.

### 3.4 Hex microstructure (microphysics-ready representation)

- **Role**: compute microstructure analytics and “Option A observables” from lexical evidence projected into hex substrate.
- **Scientific role**: a representation layer bridging sparse lexical evidence into a dense field where local operations are meaningful.

### 3.5 Sealed multiscale stack (product-causal path)

Defined explicitly in `hesperia/engine/sealed_multiscale_stack.py`:

- **Scientific role**: a deterministic **field evolution** step:
  1) markers → concept activation  
  2) concept → hex field \(H_0\) (via P_CH / PCH)  
  3) local microphysics step \(H_0 \to H_1\) (optionally)  
  4) aggregate \(H_1 \to f \to a\) (for projection/interpretation)  
  5) compute **product signals** strictly from \(H\) (hex-causal requirement)  
  6) compute **HSPR index** from field-state summary

**Non-negotiable scientific claim of the sealed stack:** product signals are functions of the hex field only; family/area are *aggregates*, not causal inputs to the formulas.

### 3.6 Product signals + HSPR

Signals are defined in `hesperia/engine/product_signals.py` as deterministic functions of hex fields:

- **`contradiction_pressure`**: quadratic form using family coupling lift \(C_F\):  
  \[
  P = \sum_{ij} C_F[i,j]\,(H[i,\cdot]\cdot H[j,\cdot])
  \]
- **`propagation_strength`**: mean absolute change per step: \(\mathbb{E}[|H_{t+1}-H_t|]/dt\)
- **`narrative_density`**: mass per active cell: \(\sum H / \#\{H>\theta\}\)
- **`spatial_entropy_hex`**: normalized Shannon entropy of flattened mass (0 peaky → 1 uniform-ish)
- **`innovation_potential`**: contradiction_density × spatial_entropy (clipped)
- **`narrative_hotspot_mean`**: ring-neighborhood hotspot average (local adjacency within family row)

**Scientific role**: these are **derived indices** intended to be stable summaries of a governed field, not “psychological truths”.

### 3.7 TRIZ / KME / topology extensions

From repo map:

- **KME**: builds/uses an “active graph” and produces derived primitives + reports. Scientific role: **graph-based feature extraction + interpretation**.
- **TRIZ**: contradiction and innovation blocks from active graph/topology. Scientific role: **structured contradiction detection** + derived metrics.
- **Session topology**: segmentation, curves, transitions. Scientific role: **time-series summarization** over segment states.

Important: these are explicit **planes**; they must declare what they estimate and how it compares to other planes.

### 3.8 Cross-plane calibration audit (10)

Schema: `schemas/tfp_bundle/10_calibration_audit.schema.json`

- **Scientific role**: a **multi-view consistency test** across plane outputs.
- Key outputs:
  - **`consistency_score`**: scalar agreement score (must be defined in spec + registry).
  - **`plane_reliability_ranking`**: ranking of which plane appears most reliable in this run context.
  - **`suspect_fields`**, **`alarms`**, **`likely_breakpoint_stage`**: structured diagnostics.

### 3.9 Calibration release gate (11)

Schema: `schemas/tfp_bundle/11_calibration_release_gate.schema.json`, spec: `docs/specs/calibration_release_gate_v1.md`

- **Scientific role**: a **decision procedure** that blocks shipping when the measurement system is out of spec.
- Inputs: schema validation, anomaly severity, `consistency_score` floor, optional goldset pass rate.
- Output: `pass: boolean` + checks[] + rollback advice.

This is not “model output”; it is **governance over measurement validity**.

### 3.10 Public projection (public schema)

Schema: `schemas/public/public_output_schema.json`, with explicit “do not reveal geometry” rules (`docs/governance/SCHEMA_SEALING_AUDIT_v1.md`).

- **Scientific role**: a **reporting transform** that maps internal state into a public vocabulary (macro-domain vector length 10, policy family counts length 240) while preserving comparability and preventing reverse-engineering.
- Key requirement: public schemas cannot reveal internal 12/288 geometry; they must expose only public counts + scalars + bounded evidence strings.

---

## 4. Metric definitions (what they mean, how to validate them)

Below are the minimal scientific definitions aligned to the existing contracts. When a metric’s exact formula is not in the inspected snippets, the definition is constrained to what is already contractually true (type/range/role); the formula must be linked from the owning module/spec.

### 4.1 Coverage and attribution (structural plane)

From metric registry `structural_batch.L1`:

- **`ATTRIBUTED_TOKENS` (count)**: number of tokens for which the system produced attributable evidence under the current lexicon/resources.
  - **Zero meaning**: `no_signal_or_fallback_pending` (registry).
  - **Validation**: monotonic in text length under stable tokenizer; stable under fixed version.

- **`COVERAGE_RATIO` (probability [0,1])**: proportion of tokens attributable (operationally: attributed / total, or equivalent).
  - **Validation**: bounded in [0,1]; should correlate with lexical marker mass and with evidence span count.

### 4.2 Marker mass and fallback flags (calibration status)

From metric registry `structural_batch.diagnostics.calibration_status` and sealed stack outputs:

- **`marker_concept_mass` (normalized_mass, \(\ge0\))**: total mass of concept evidence from markers.
  - **Scientific meaning**: instrument excitation; near-zero implies the measurement model has no support in the lexicon for this input.

- **`uniform_concept_prior_fallback_used` (boolean)**: the system substituted a uniform concept prior because marker mass was non-positive.
  - **Scientific meaning**: run is not evidence-driven; treat downstream outputs as degraded.

### 4.3 Hex/field metrics (sealed/product plane)

From `hesperia/engine/product_signals.py`:

- **`contradiction_pressure` (energy-like scalar)**: quadratic coupling energy on field state.
- **`propagation_strength` (rate)**: mean absolute step change per \(dt\).
- **`narrative_density` (density)**: mass per active cell.
- **`spatial_entropy_hex` (unitless index in [0,1])**: normalized Shannon entropy over field mass.
- **`innovation_potential` (index, clipped)**: contradiction_density × entropy; a synthetic indicator, not a physical constant.
- **`narrative_hotspot_mean` (local adjacency statistic)**: mean hotspot value under ring neighborhood.

Validation (scientific):

- **Invariance under permutation** (where applicable): entropy should be permutation-invariant across cells; hotspot depends on local adjacency definition (ring).
- **Sensitivity tests**: scaling field mass should scale pressure and density in predictable ways; entropy should remain stable under uniform scaling.
- **Null behavior**: when field mass is ~0, entropy is defined as 0.0 (per code).

### 4.4 HSPR index

HSPR is computed from a field-state summary (`field_state_from_hex_stack` → `compute_hspr_index`). Scientific status:

- Treat as a **bounded index** (intended [0,1] per registry guidance in calibration contract).
- Validation requirement: must be monotonic with its governed components and stable under versioned calibration profiles.

### 4.5 Public structural metrics (projected)

From `schemas/public/public_output_schema.json`:

- **`macro_domain_vector`**: length-10 vector in [0,1] representing projected structural emphasis over public macro-domains.
- **`policy_family_counts`**: length-240 non-negative counts over public policy families.
- **`entropy`, `coverage`, `tension`, `loopability`, `confidence`**: scalars (scientific role: indices); exact formulas must be traced to the internal pipeline modules that produce them.
- **`trust_tier`**: categorical bucket describing confidence/trust regime (policy, not science).
- **`evidence[]`**: bounded evidence entries; scientific role: explainability trace for auditability, not a complete proof of correctness.

Validation: public projection must be a **deterministic function** of internal state under fixed versions, and must not reveal internal geometry (per schema sealing audit).

### 4.6 Cross-plane consistency metrics

From calibration audit schema:

- **`consistency_score`**: scalar agreement score across planes.
  - Scientific meaning: empirical agreement between estimators of overlapping quantities.
  - Validation: must be stable under rerun; should decrease under injected perturbations that break one plane.

---

## 5. Scientific alignment checklist (what “sound definition” requires)

For each component/layer/metric, the definition is “sound” only if these are true:

- **Versioned resources**: the definition binds to resource versions (lexicon, ontology, matrices, calibration profile, schema version).
- **Semantic type**: probability vs count vs index vs energy is declared (registry), with range and null policy.
- **Identifiability**: the component states what it estimates (and what it does not).
- **Validation plan**: at least one of:
  - goldset regression (expected outputs),
  - invariance tests (permutation/scale/bounds),
  - multi-view consistency checks (audit),
  - schema + gate pass policy (release gate).

---

## 6. Immediate next action (to finish the alignment)

Create a single canonical doc inside Hesperia (recommended path: `docs/SCIENTIFIC_DEFINITIONS.md`) that:

1) enumerates all shipped artifacts/planes (A–G),  
2) links each metric to **its formula location** (module + function),  
3) enumerates each metric’s entry in `output_metric_registry_v1.json`,  
4) states comparability rules (what can be compared across runs/versions),  
5) binds consistency_score and public indices (tension/loopability/confidence) to their exact derivations.\n+
This report already provides the **definitions and roles** consistent with current contracts; the remaining work is to attach the missing formula links for the few public scalars whose computation wasn’t read here.\n+
SIGNED: Engineer (Ethan) | Hesperia scientific alignment definitions | 2026-03-25 | components/layers/metrics

