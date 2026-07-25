# area_entropy (tool-local)

**Status:** 🟡 PARTIAL — present in a narrow slice/tool, not the full contract  
**Category:** [Entropy and Information Theory](../categories/Entropy-and-Information-Theory.md)  
**Type:** Formula / function (duplicate)  
**Responsible (module):** `tools/tfp_calibration_audit.py:245-247`  
**Value / default:** —

## Yields (formula)

Local `_entropy()` helper computing the same Shannon formula inline, not calling the canonical function.

## Origin

Java 21_MATH `areaEntropy`

## Notes

Cosmetic gap, not a feature gap: [compute_entropy (Shannon)](../pages/compute-entropy-Shannon.md) already exists and is used elsewhere. This is a dedup candidate, not new work — see *Coverage Ledger*.

---
[← back to category](../categories/Entropy-and-Information-Theory.md) · [wiki home](../index.md)
