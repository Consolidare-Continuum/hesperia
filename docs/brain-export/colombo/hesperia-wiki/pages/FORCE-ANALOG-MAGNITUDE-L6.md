# FORCE_ANALOG_MAGNITUDE (L6)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Stability and Control Theory](../categories/Stability-and-Control-Theory.md)  
**Type:** Layer variable  
**Responsible (module):** `core/layers/layer_6.py:71,99`  
**Value / default:** 0.0 (no-perturbation stub)

## In plain words

force-like magnitude from the potential-field scaffold (usually stubbed 0 until perturbation analysis is live).

## Definition

- **Receives:** [ESCAPE_ENERGY_THRESHOLD (L6)](../pages/ESCAPE-ENERGY-THRESHOLD-L6.md)
- **Does:** FORCE_ANALOG_MAGNITUDE — force-like quantity analog from the potential-field scaffold (stub 0.0, i.e. no net force, without real dynamics).
- **Outputs:** `0.0 (no-perturbation stub)` → *no named wiki consumer yet*
- **Exists for:** L6 Group-IV scaffold constant

## Yields (formula)

FORCE_ANALOG_MAGNITUDE — force-like quantity analog from the potential-field scaffold (stub 0.0, i.e. no net force, without real dynamics).

## Produced from (inputs)

- [ESCAPE_ENERGY_THRESHOLD (L6)](../pages/ESCAPE-ENERGY-THRESHOLD-L6.md)

## See also

- [ESCAPE_ENERGY_THRESHOLD (L6)](../pages/ESCAPE-ENERGY-THRESHOLD-L6.md)

## Origin

39_SPEC Layer-6 — Theory Explainer: plain_lang: force-like magnitude from the potential-field scaffold (usually stubbed 0 until perturbation analysis is live). author: Hesperia wiki (core/layers/layer_6.py:71,99). extent: full. reasoning: L6 Group-IV scaffold constant. application: [ESCAPE_ENERGY_THRESHOLD (L6)](../pages/ESCAPE-ENERGY-THRESHOLD-L6.md).

## Notes

**HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-CATALOG-L6-GROUP-IV (2026-08-04):** Closes the Coverage-Ledger's named next-wave candidate — Group-IV scaffold constant, same status as the other 21 L6 stubs (`docs/foundations/output_catalog.md` §6: "documented no-perturbation identity constants... a named scaffold reserved for a future perturbation-analysis pass — not an oversight"). Verified against `layer_6.py` directly.

---
[← back to category](../categories/Stability-and-Control-Theory.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
