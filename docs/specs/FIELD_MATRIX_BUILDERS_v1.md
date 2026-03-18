<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
See LEGAL_NOTICE.md for full terms.
-->

# FIELD_MATRIX_BUILDERS_v1

**Status:** Draft for lock-in  
**Purpose:** Map ontology-level **families**, **relations**, **contradictions**, and **resistance priors** into numerical matrices for the semantic field engine.

**Module:** `hesperia.engine.field_dynamics.matrix_builders`  
**Pipeline:** ontology → builders → `W_F`, `C_F`, `R` vector → `L_F` (via `equations.build_family_laplacian`) → `run_semantic_field` / `run_field_calibration`

**Related:** [SEMANTIC_FIELD_EQUATIONS_v1.md](SEMANTIC_FIELD_EQUATIONS_v1.md) · [HSPR_CALIBRATION_INDEX_v1.md](HSPR_CALIBRATION_INDEX_v1.md)

---

## 1. Flow

```text
ontology (family ids, relations, contradictions, resistance priors)
    → matrix_builders
    → W_F (adjacency weights)
    → C_F (contradiction strengths)
    → R (per-family resistance vector)
    → semantic field engine
```

HESPERIA can **evolve ontology data** without changing dynamics code.

---

## 2. Family index

`build_family_index(family_ids)` returns a deterministic map **family id → column index**:

- Ids are sorted **lexicographically**; index `0` is the smallest id string.

**Important:** `source_family_index` in documents must match this ordering, or use **`source_family_id`** in JSON configs (runners map id → index).

---

## 3. Adjacency `W_F`

`build_family_adjacency_matrix(family_ids, relations)`

- Input: undirected relation pairs `(a, b)`.
- Output: symmetric `W` with `W_ij = 1` if `{i,j}` is a relation (multiple edges idempotent).
- Self-loops and unknown ids are skipped.

`L_F = D - W` is built by `equations.build_family_laplacian(W)`.

---

## 4. Contradiction `C_F`

`build_contradiction_matrix(family_ids, contradictions)`

- Input: triples `(a, b, strength)` with `strength ≥ 0`.
- Output: symmetric non-negative matrix; diagonal zero before use in engine.
- Duplicate pairs: **max** strength wins.

Runners pass the result through `equations.build_contradiction_matrix` for canonical symmetrization / zero diagonal.

---

## 5. Resistance `R`

`build_resistance_vector(family_ids, resistance_priors, default_value=0.1)`

- Per-family diagonal prior; missing ids get `default_value`.

---

## 6. Runtime config (`ontology` block)

When a JSON config includes **`ontology`**, **`run_semantic_field`** and **`run_field_calibration`** build matrices from it and **ignore** `adjacency_matrix`, `adjacency_mode`, `contradiction_matrix`, `contradiction_zero`, and `resistance_vector` for those tensors.

Required:

- `family_ids`: list of strings, length = `family_count`
- `relations`: list of `[id_a, id_b]`
- `contradictions`: optional list of `[id_a, id_b, strength]`
- `resistance_priors`: optional object id → float
- `resistance_default`: optional float (default 0.1)

Documents may use **`source_family_id`** instead of `source_vector` / `source_family_index`.

---

## 7. Example

```json
"ontology": {
  "family_ids": ["A01", "A02", "A03", "A04"],
  "relations": [["A01", "A02"], ["A02", "A03"], ["A03", "A04"]],
  "contradictions": [["A01", "A04", 0.8]],
  "resistance_priors": {"A01": 0.2, "A02": 0.3},
  "resistance_default": 0.1
}
```

---

## 8. Non-claims

- Builders do **not** validate domain truth; they only materialize graph structure from supplied ontology slices.
- Full **288** canonical families should use ids aligned to deployment taxonomy (e.g. `family_001` …); ordering is still **lexicographic** unless runners are extended with explicit order.

---

## 9. Stack position

Document → Dict A/B → family activation → **ontology + matrix builders** → field evolution → observables → HCI → TRIZ / KME.
