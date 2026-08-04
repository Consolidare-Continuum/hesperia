# PRINCIPAL_COMPONENT_ENERGY_RATIO (L6)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Stability and Control Theory](../categories/Stability-and-Control-Theory.md)  
**Type:** Layer variable  
**Responsible (module):** `core/layers/layer_6.py:51,90`  
**Value / default:** 1.0 (no-perturbation stub)

## In plain words

fraction of hit-vector energy sitting in the leading component — scaffold for future PCA-style analysis.

## Definition

- **Receives:** [HIT_VECTOR_RANK (L6)](../pages/HIT-VECTOR-RANK-L6.md)
- **Does:** PRINCIPAL_COMPONENT_ENERGY_RATIO — fraction of hit-vector energy in the top principal component (stub 1.0, i.e. fully concentrated, without real PCA).
- **Outputs:** `1.0 (no-perturbation stub)` → *no named wiki consumer yet*
- **Exists for:** L6 Group-IV scaffold constant

## Yields (formula)

PRINCIPAL_COMPONENT_ENERGY_RATIO — fraction of hit-vector energy in the top principal component (stub 1.0, i.e. fully concentrated, without real PCA).

## Produced from (inputs)

- [HIT_VECTOR_RANK (L6)](../pages/HIT-VECTOR-RANK-L6.md)

## See also

- [HIT_VECTOR_RANK (L6)](../pages/HIT-VECTOR-RANK-L6.md)

## Origin

39_SPEC Layer-6 — Theory Explainer: plain_lang: fraction of hit-vector energy sitting in the leading component — scaffold for future PCA-style analysis. author: Hesperia wiki (core/layers/layer_6.py:51,90). extent: full. reasoning: L6 Group-IV scaffold constant. application: [HIT_VECTOR_RANK (L6)](../pages/HIT-VECTOR-RANK-L6.md).

## Notes

**HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-CATALOG-L6-GROUP-IV (2026-08-04):** Closes the Coverage-Ledger's named next-wave candidate — Group-IV scaffold constant, same status as the other 21 L6 stubs (`docs/foundations/output_catalog.md` §6: "documented no-perturbation identity constants... a named scaffold reserved for a future perturbation-analysis pass — not an oversight"). Verified against `layer_6.py` directly.

---
[← back to category](../categories/Stability-and-Control-Theory.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
