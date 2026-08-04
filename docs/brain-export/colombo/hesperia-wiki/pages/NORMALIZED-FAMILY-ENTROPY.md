# NORMALIZED_FAMILY_ENTROPY

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Entropy and Information Theory](../categories/Entropy-and-Information-Theory.md)  
**Type:** Derived variable  
**Responsible (module):** `core/layers/layer_1.py::compute_L1 -> result["NORMALIZED_FAMILY_ENTROPY"]`  
**Value / default:** float [0,1]

## In plain words

FAMILY_ENTROPY rescaled to [0,1] — the form every downstream consumer ([STRUCTURAL_STABILITY_INDEX](../pages/STRUCTURAL-STABILITY-INDEX.md), L7 SYSTEM_CONFIDENCE_SCORE) actually uses.

## Definition

- **Receives:** [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md)
- **Does:** min(1.0, [FAMILY_ENTROPY](../pages/FAMILY-ENTROPY.md) / ln(F))
- **Outputs:** `float [0,1]` → *no named wiki consumer yet*
- **Exists for:** L1 census field — first pipeline layer every later layer reads

## Yields (formula)

min(1.0, [FAMILY_ENTROPY](../pages/FAMILY-ENTROPY.md) / ln(F))

## Produced from (inputs)

- [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md)

## See also

- [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md)
- [FAMILY_ENTROPY](../pages/FAMILY-ENTROPY.md)

## Origin

Hesperia-native `34_SPEC` L1 instrumentation — no Java prototype ancestor for the L1-L9 layer pipeline as a whole — Theory Explainer: plain_lang: FAMILY_ENTROPY rescaled to [0,1] — the form every downstream consumer ([STRUCTURAL_STABILITY_INDEX](../pages/STRUCTURAL-STABILITY-INDEX.md), L7 SYSTEM_CONFIDENCE_SCORE) actually uses.. author: Hesperia L1 (34_SPEC / output_catalog §1). extent: full. reasoning: L1 census field — first pipeline layer every later layer reads. application: [L1 — Structural Activation Census](../pages/L1-Structural-Activation-Census.md), L2–L9.

## Notes

**HWIKI-CATALOG-L1 / HWIKI-PLAIN:** FAMILY_ENTROPY rescaled to [0,1] — the form every downstream consumer ([STRUCTURAL_STABILITY_INDEX](../pages/STRUCTURAL-STABILITY-INDEX.md), L7 SYSTEM_CONFIDENCE_SCORE) actually uses. Source: `docs/foundations/output_catalog.md` §1, re-verified against `compute_L1` 2026-08-04.

---
[← back to category](../categories/Entropy-and-Information-Theory.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
