# shadow_step

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Core Math Contract](../categories/Core-Math-Contract.md)  
**Type:** Formula / function  
**Responsible (module):** `core/math/core_math.py`  
**Value / default:** —

## In plain words

push energy through a separate shadow transition matrix to estimate correction cost without rewriting the main field.

## Definition

- **Receives:** *E (energy vector)*
- **Does:** E_shadow = E · Ws — propagation through a separate shadow transition matrix Ws.
- **Outputs:** `—` → [P_shadow (shadow-hop penalty)](../pages/P-shadow-shadow-hop-penalty.md), *check_shadow_non_creation*, [Energy conservation epsilon](../pages/Energy-conservation-epsilon.md)
- **Exists for:** shadow propagation for fallback costing

## Yields (formula)

E_shadow = E · Ws — propagation through a separate shadow transition matrix Ws.

## Produced from (inputs)

- *E (energy vector)*

## Needed by (consumers)

- [P_shadow (shadow-hop penalty)](../pages/P-shadow-shadow-hop-penalty.md)
- *check_shadow_non_creation*
- [Energy conservation epsilon](../pages/Energy-conservation-epsilon.md)

## See also

- [P_shadow (shadow-hop penalty)](../pages/P-shadow-shadow-hop-penalty.md)
- [Energy conservation epsilon](../pages/Energy-conservation-epsilon.md)

## Origin

22_SPEC §6 — Theory Explainer: plain_lang: push energy through a separate shadow transition matrix to estimate correction cost without rewriting the main field. author: Hesperia wiki (core/math/core_math.py). extent: full. reasoning: shadow propagation for fallback costing. application: [P_shadow (shadow-hop penalty)](../pages/P-shadow-shadow-hop-penalty.md), *check_shadow_non_creation*.

## Notes

**HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. Shadow field for fallback / correction cost.

---
[← back to category](../categories/Core-Math-Contract.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
