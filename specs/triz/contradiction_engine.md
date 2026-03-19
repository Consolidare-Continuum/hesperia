---
spec_version: "1.0"
system_version: "0.5.0"
status: canonical
id: HES-SPEC-TRIZ-CONTRADICTION
---

# TRIZ contradiction engine — canonical rules

**Code:** `hesperia.extensions.triz.contradiction_engine`, `hesperia.extensions.triz.topology_binding`, `hesperia.extensions.triz.models`.

## 1. Typed relations (binding)

**CONFLICT_TYPES** = `{"conflict", "negation", "opposition"}` (case-normalized).

Only edges whose `relation_type` ∈ **CONFLICT_TYPES** participate in contradiction enumeration.

## 2. Pair score (binding)

For relation **r** from **source** to **target** with weight **w** and type **rt**:

\[
\text{raw\_score} = \min\left(1,\; a_{src} \cdot a_{tgt} \cdot w_{rt} \cdot w\right)
\]

where \(a_{src}, a_{tgt}\) are concept activations in **[0,1]** (normalized from hit counts in ActiveGraph path), and

| rt | \(w_{rt}\) |
|----|------------|
| conflict | 1.0 |
| negation | 1.0 |
| opposition | 0.85 |
| other | 1.0 (if ever allowed — default path uses CONFLICT_TYPES filter only) |

## 3. Enumeration ordering (binding)

Sort pairs by **raw_score** descending, then `(concept_a, concept_b)` lexicographic.

## 4. ContradictionSignal construction

`build_contradiction_signals` binds each scored pair to matrix coordinates via `bind_concepts_to_coordinates`; signals below **min_score** (default **0.15**) are excluded.

## 5. TRIZ pattern label (supplemental)

`classify_triz_pattern(concept_a, concept_b)` returns one of  
`segmentation | counterbalance | parameter_change | dynamic_adaptation`  
using lexical classifier when available, else deterministic hash bucket — **labels do not change** §2 scores.

## 6. Related

- Innovation scalar: [innovation_metrics.md](innovation_metrics.md)  
- Family-field contradiction pressure on **F**: [../dynamics/semantic_field_dynamics.md](../dynamics/semantic_field_dynamics.md) (matrix **C**)  
