# R1–R4 Contradiction Pressure (CP) — Part B.5 contract

**Purpose:** Contract for loading the contradiction graph C and computing **contradiction_pressure** per unit. **Owner:** Ethan (task 2). **Spec:** [SPEC__Reading_Scale_Levels_R1_R4_Structural_Audit_v1_0.md](SPEC__Reading_Scale_Levels_R1_R4_Structural_Audit_v1_0.md) §B.5.

---

## 1. Artifact

| Item | Path |
|------|------|
| Contradiction graph C | `sphere_rag/r1_r4_contradiction_graph_v1_0.json` |

**Format:** JSON with:

- `version`: string (e.g. `"1.0"`).
- `pairs`: array of `[i, j]` with **i < j**, family indices in `0..F-1` (F = 288). Symmetric: (i,j) and (j,i) are the same pair; store once. No self-pairs (no `[k,k]`).

**v1.0:** `pairs` is empty `[]` until curated or imported from Dict-B. With empty C, **CP_raw = 0**, so **contradiction_pressure = 0** for all units. Pipeline is wired and deterministic; add pairs when curated.

---

## 2. Formula (Part B.5 Continuous CP)

- **S** = { f | p_f > 0 } (families with positive mass).
- **CP_raw** = Σ_{(i,j) ∈ C, i < j} (p_i · p_j).
- **CP_max** = 0.25 (normalization; one pair at 0.5·0.5 = 0.25).
- **contradiction_pressure** = min(1, CP_raw / CP_max).

**Input:** Unit’s family distribution **p** = (p_0, …, p_{F-1}) from token→family attribution (probabilities or counts normalized). **Output:** scalar in [0, 1].

---

## 3. Pipeline contract

1. **Load C:** Read `r1_r4_contradiction_graph_v1_0.json`; parse `pairs` as list of [i, j] with i, j in 0..F-1, i < j.
2. **Per unit:** Given **p** (length F), compute CP_raw = Σ p[i]*p[j] for each [i,j] in pairs; then contradiction_pressure = min(1, CP_raw / 0.25).
3. **Deterministic:** Same C and same p → same contradiction_pressure. No sampling.
4. **When C is empty:** contradiction_pressure = 0.

**Extending C:** Add curated or Dict-B–derived pairs to the JSON; re-version (e.g. v1.1) if structure changes. Keep symmetric, no self-pairs, i < j in storage.
