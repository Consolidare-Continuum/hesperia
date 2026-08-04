# entropy_threshold (monotony)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Activation and Diagnostic Thresholds](../categories/Activation-and-Diagnostic-Thresholds.md)  
**Type:** Parameter (constant)  
**Responsible (module):** `assets/specs/canon/diagnostic_rules.yaml`  
**Value / default:** 0.35

## In plain words

if family entropy falls below this, label the discourse structurally narrow (monotony regime).

## Definition

- **Receives:** [compute_entropy (Shannon)](../pages/compute-entropy-Shannon.md)
- **Does:** structural_monotony label — entropy below this = structurally narrow discourse.
- **Outputs:** `0.35` → *no named wiki consumer yet*
- **Exists for:** pairs with coverage_threshold for monotony

## Yields (formula)

structural_monotony label — entropy below this = structurally narrow discourse.

## Produced from (inputs)

- [compute_entropy (Shannon)](../pages/compute-entropy-Shannon.md)

## See also

- [compute_entropy (Shannon)](../pages/compute-entropy-Shannon.md)
- [Gini concentration](../pages/Gini-concentration.md)

## Origin

Shannon (1948) — Theory Explainer: plain_lang: if family entropy falls below this, label the discourse structurally narrow (monotony regime). author: Hesperia wiki (assets/specs/canon/diagnostic_rules.yaml). extent: full. reasoning: pairs with coverage_threshold for monotony. application: [compute_entropy (Shannon)](../pages/compute-entropy-Shannon.md).

## Notes

**HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04.

---
[← back to category](../categories/Activation-and-Diagnostic-Thresholds.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
