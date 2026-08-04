# ESCAPE_ENERGY_THRESHOLD (L6)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Stability and Control Theory](../categories/Stability-and-Control-Theory.md)  
**Type:** Layer variable  
**Responsible (module):** `core/layers/layer_6.py:70,98`  
**Value / default:** 1.0 (no-perturbation stub)

## In plain words

how much energy would be needed to leave the current structural basin — scaffold threshold, not a live escape simulation today.

## Definition

- **Receives:** *none declared (constant, hub, or external)*
- **Does:** ESCAPE_ENERGY_THRESHOLD — energy needed to leave the current structural basin (stub 1.0, i.e. maximally sticky, without a real potential-field model).
- **Outputs:** `1.0 (no-perturbation stub)` → [FORCE_ANALOG_MAGNITUDE (L6)](../pages/FORCE-ANALOG-MAGNITUDE-L6.md)
- **Exists for:** L6 Group-IV scaffold constant

## Yields (formula)

ESCAPE_ENERGY_THRESHOLD — energy needed to leave the current structural basin (stub 1.0, i.e. maximally sticky, without a real potential-field model).

## Needed by (consumers)

- [FORCE_ANALOG_MAGNITUDE (L6)](../pages/FORCE-ANALOG-MAGNITUDE-L6.md)

## See also

- [FORCE_ANALOG_MAGNITUDE (L6)](../pages/FORCE-ANALOG-MAGNITUDE-L6.md)

## Origin

39_SPEC Layer-6 — Theory Explainer: plain_lang: how much energy would be needed to leave the current structural basin — scaffold threshold, not a live escape simulation today. author: Hesperia wiki (core/layers/layer_6.py:70,98). extent: full. reasoning: L6 Group-IV scaffold constant. application: [FORCE_ANALOG_MAGNITUDE (L6)](../pages/FORCE-ANALOG-MAGNITUDE-L6.md).

## Notes

**HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-CATALOG-L6-GROUP-IV (2026-08-04):** Closes the Coverage-Ledger's named next-wave candidate — Group-IV scaffold constant, same status as the other 21 L6 stubs (`docs/foundations/output_catalog.md` §6: "documented no-perturbation identity constants... a named scaffold reserved for a future perturbation-analysis pass — not an oversight"). Verified against `layer_6.py` directly.

---
[← back to category](../categories/Stability-and-Control-Theory.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
