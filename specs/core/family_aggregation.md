---
spec_version: "1.0"
system_version: "0.5.0"
status: canonical
id: HES-SPEC-CORE-FAMILY-AGG
---


# Family aggregation (hex → family) — canonical

**Code:** `hesperia.engine.hex_family_bridge` · data `data/topology/hex_family_weights.json`  
**Related:** [hex_microphysics_canon.md](hex_microphysics_canon.md) · [area_aggregation.md](area_aggregation.md) · `core/topology/invariant_catalog.py`.

---

## Equation

For hex activations **A_h** and family activations **F_j**:

**F_j = Σ_h w_{hj} A_h**

---

## Constraints on **w_{hj}**

1. **w_{hj} ∈ [0, 1]**
2. **Σ_j w_{hj} = 1** for each hex **h**
3. **Sparse:** typically one primary family per hex; optional soft split across ≤ few families
4. **Deterministic:** weights fixed by topology + optional overrides (no stochastic draw)

---

## Default (singleton) mapping

Canonical grid: **Nf = 288**, **250** hexes per family. Linear hex index **u = m · 250 + k** belongs to family **m** with **w_{m,u} = 1**, all other **w_{j,u} = 0**.

This matches **F = P_HF A** with binary **P_HF**.

---

## Overrides

File **`data/topology/hex_family_weights.json`** may list **exemplar** or production overrides:

- **hex_id** string, e.g. `A3_F12_H05` → area (1-based A index), family-in-area (F12), hex-in-family (H05)
- **family_weights**: map **global family index** (string, 0-based) → weight, summing to 1

Engine merges overrides into aggregation column-wise.

---

## Determinism

Same **A_hex**, same weight table → same **F**. **Area** aggregation is defined only in [area_aggregation.md](area_aggregation.md).
