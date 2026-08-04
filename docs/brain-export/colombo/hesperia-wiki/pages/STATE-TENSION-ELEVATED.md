# STATE_TENSION_ELEVATED

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Evidence and Trust](../categories/Evidence-and-Trust.md)  
**Type:** Parameter (constant)  
**Responsible (module):** `sphere/fpf_bridge/constants.py`  
**Value / default:** "tension_elevated"

## In plain words

Contradiction/tension signals are high enough to flag — same risk tier as UNSTABLE_TRANSITION but a distinct cause (opposition, not instability).

## Definition

- **Receives:** [fpf_bridge structural states](../pages/fpf-bridge-structural-states.md)
- **Does:** Risk level: high
- **Outputs:** `"tension_elevated"` → *no named wiki consumer yet*
- **Exists for:** one of five structural states the LLM actually sees — not the raw L1–L9 dict

## Yields (formula)

Risk level: high

## Produced from (inputs)

- [fpf_bridge structural states](../pages/fpf-bridge-structural-states.md)

## See also

- [fpf_bridge structural states](../pages/fpf-bridge-structural-states.md)
- [STATE_FOCUSED_DOMINANT](../pages/STATE-FOCUSED-DOMINANT.md)
- [STATE_DISTRIBUTED_BALANCED](../pages/STATE-DISTRIBUTED-BALANCED.md)
- [STATE_UNSTABLE_TRANSITION](../pages/STATE-UNSTABLE-TRANSITION.md)
- [STATE_DIFFUSE_SPREAD](../pages/STATE-DIFFUSE-SPREAD.md)

## Origin

Hesperia-native fpf_bridge design — no Java prototype ancestor — Theory Explainer: plain_lang: Contradiction/tension signals are high enough to flag — same risk tier as UNSTABLE_TRANSITION but a distinct cause (opposition, not instability).. author: Hesperia fpf_bridge (output_catalog §12). extent: full. reasoning: one of five structural states the LLM actually sees — not the raw L1–L9 dict. application: [fpf_bridge structural states](../pages/fpf-bridge-structural-states.md).

## Notes

**HWIKI-CATALOG-BRIDGE / HWIKI-PLAIN:** Contradiction/tension signals are high enough to flag — same risk tier as UNSTABLE_TRANSITION but a distinct cause (opposition, not instability). One of exactly 5 structural states in `ALL_STATES`. Source: `docs/foundations/output_catalog.md` §12.

---
[← back to category](../categories/Evidence-and-Trust.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
