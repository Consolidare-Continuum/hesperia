<!--
HESPERIA — Hesperia Engine Dynamics
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. See LEGAL_NOTICE.md.
-->

# Vocabulary: metric cascade, tiers, field phases, and Hesperia structure

**Problem:** Reusing **“layer”** and **“L*n*”** for unrelated ladders guarantees confusion. This page gives **separate names and number spaces** for each ladder.

**Policy:** In **new** docs and specs, do **not** introduce bare **L*n*** for these systems. Use the names below. **Legacy** code and JSON may still say `layer_id`, `L1`, etc.; migration is phased (see governance plan).

---

## 1. Metric cascade **R1–R10** (Sphere numeric execution_flow; legacy “L1–L10”)

**Term:** **Metric cascade** or **registry metric stages** — **not** “layers” in new prose.

**Codes:** **R1** through **R9**, then **R10** (interpretation / structured state after R9).

| Code | Role (short) |
|------|----------------|
| **R1** | Semantic / coverage metrics from hits |
| **R2** | Dict activation / traversal |
| **R3** | Structural shadow compare |
| **R4** | Topology / evidence / area vector |
| **R5** | Reality / contradiction / geometry gates |
| **R6** | Dynamism / stability / Lyapunov |
| **R7** | Consistency / trust / decision |
| **R8** | Scale-invariant reporting |
| **R9** | Logic bands / pillars / brand words |
| **R10** | Interpretation state (USF), after R9 |

**Why R:** Ties to the **ordered registry** of metric transforms (`sphere.execution_flow`); **R** is not used for Ethan or dependency numbering elsewhere.

**Legacy map:** **R*k* ≈ former Sphere L*k*** (same ordering, different **name**).

**Canonical detail:** [LAYER_PIPELINE_ORDER.md](LAYER_PIPELINE_ORDER.md) (replace mentally L→R until that doc is retitled).

**Code locus (today):** `sphere.execution_flow` registry, `LayerInput` / `LayerOutput` — identifiers may still read `L1`; rename in code is a later phase.

---

## 2. Dependency **Tier 0–Tier 11** (change-impact graph; legacy “Layer 0–11”)

**Term:** **Tier** — freeze / coupling band for **repository modules**, not a metric step and not Ethan time.

**Codes:** **Tier 0** … **Tier 11** (spell **Tier** in prose; optional shorthand **T0–T11** in tables only if legend is present).

**Legacy map:** **Tier *k* = former “Dependency Layer *k*”** in [HESPERIA_DEPENDENCY_GRAPH.md](HESPERIA_DEPENDENCY_GRAPH.md).

**What it is not:** R1–R10, F0–F10, or multiscale chain.

---

## 3. Field phases **F0–F10** (Ethan Part A timeline; legacy “L0–L10”)

**Term:** **Field phase** — one **discrete-time step** in the semantic-field dynamics orchestration (Ethan spec Part A).

**Codes:** **F0** through **F10**.

**Critical:** **F*k* is not R*k*.** Example: **F5** may **call into** the block that runs **R1–R9**; the integers are **not** aligned 1:1.

**Legacy map:** **F*k* ≈ former Ethan Part A step L*k*** (same ordering in the spec, different **symbol**).

**Canonical doc:** [specs/dynamics/ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md](../specs/dynamics/ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md).

---

## 4. Attribution surface (no numeric ladder)

**Term:** **Attribution** (or **lexical front**) — text → normalize → tokenize → Dict A / Dict B evidence.

**Do not** call this “L1” or “R1”; **R1** starts **after** hits exist.

**Rough placement:** lives under **Tier 2–3** (lexicon, NLP) in the dependency graph; sits **inside** early **field phases** (e.g. before placement) in Ethan — see spec wiring, not index equality.

**Code locus:** `hesperia/nlp/`, `lexicon/`, attribution in `core` / execution_flow entrypoints.

---

## 5. Hesperia structure — **multiscale chain** (geometry of meaning)

**Term:** **Multiscale chain** — **not** “layers.”

**Steps (names only, fixed order):**  
**concept → hex → family → area → product signals → HSPR**

**Canonical doc:** [ENGINE_DYNAMICS_CANONICAL_NAMING_v0.5.md](ENGINE_DYNAMICS_CANONICAL_NAMING_v0.5.md), [TOPOLOGY_INVARIANTS.md](TOPOLOGY_INVARIANTS.md).

**Contrast:**

| Term | Meaning |
|------|--------|
| **Multiscale chain** | *Where* meaning is anchored and aggregated |
| **Tier *k*** | *Which code packages* depend on which |
| **R*k*** | *Which metric transform* runs in the sphere registry |
| **F*k*** | *Which orchestration phase* in Ethan time |

---

## 6. Cheat sheet

| You mean… | Say… | Legacy (retire in prose) |
|-----------|------|---------------------------|
| Coverage through bands math | **R1–R9**, **R10** | Sphere L1–L9, L10 |
| Repo freeze / impact bands | **Tier 0–11** | Dependency “Layer 0–11” |
| Ethan time-line steps | **F0–F10** | Ethan “L0–L10” |
| Text → dict hits | **Attribution** | (informal “word layers”) |
| concept→…→HSPR | **Multiscale chain** | — |

---

## 7. Governance

Refactor sequencing and code renames: [docs/governance/working/ETHAN-LAYER-VOCABULARY-AND-REPO-STRUCTURE-PLAN.md](governance/working/ETHAN-LAYER-VOCABULARY-AND-REPO-STRUCTURE-PLAN.md).

---

*Hesperia Engine Dynamics — distinct names for each ladder.*
