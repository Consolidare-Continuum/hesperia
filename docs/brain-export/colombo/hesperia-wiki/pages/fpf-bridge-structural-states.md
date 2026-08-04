# fpf_bridge structural states

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Evidence and Trust](../categories/Evidence-and-Trust.md)  
**Type:** Hub / concept  
**Responsible (module):** `sphere/fpf_bridge/constants.py`  
**Value / default:** 5 states

## In plain words

The state machine the LLM actually sees — bridge_to_llm_prompt()'s envelope is a projection (one active state + legal next transitions + evidence requirements + pre-evaluated guard verdicts), never L1-L9's ~190 raw variables directly.

## Definition

- **Receives:** [L9 — Pillars, Brand Labels, Action Triggers](../pages/L9-Pillars-Brand-Labels-Action-Triggers.md)
- **Does:** The state machine the LLM actually sees — bridge_to_llm_prompt()'s envelope is a projection (one active state + legal next transitions + evidence requirements + pre-evaluated guard verdicts), never L1-L9's ~190 raw variables directly.
- **Outputs:** `5 states` → [STATE_FOCUSED_DOMINANT](../pages/STATE-FOCUSED-DOMINANT.md), [STATE_DISTRIBUTED_BALANCED](../pages/STATE-DISTRIBUTED-BALANCED.md), [STATE_UNSTABLE_TRANSITION](../pages/STATE-UNSTABLE-TRANSITION.md), [STATE_TENSION_ELEVATED](../pages/STATE-TENSION-ELEVATED.md), [STATE_DIFFUSE_SPREAD](../pages/STATE-DIFFUSE-SPREAD.md)
- **Exists for:** **HWIKI-CATALOG-BRIDGE:** Source: `docs/foundations/output_catalog.md` §12, re-verified against `sphere/fpf_bridge/constants.py` 2026-08-04

## Yields (formula)

The state machine the LLM actually sees — bridge_to_llm_prompt()'s envelope is a projection (one active state + legal next transitions + evidence requirements + pre-evaluated guard verdicts), never L1-L9's ~190 raw variables directly.

## Produced from (inputs)

- [L9 — Pillars, Brand Labels, Action Triggers](../pages/L9-Pillars-Brand-Labels-Action-Triggers.md)

## Needed by (consumers)

- [STATE_FOCUSED_DOMINANT](../pages/STATE-FOCUSED-DOMINANT.md)
- [STATE_DISTRIBUTED_BALANCED](../pages/STATE-DISTRIBUTED-BALANCED.md)
- [STATE_UNSTABLE_TRANSITION](../pages/STATE-UNSTABLE-TRANSITION.md)
- [STATE_TENSION_ELEVATED](../pages/STATE-TENSION-ELEVATED.md)
- [STATE_DIFFUSE_SPREAD](../pages/STATE-DIFFUSE-SPREAD.md)

## See also

- [L9 — Pillars, Brand Labels, Action Triggers](../pages/L9-Pillars-Brand-Labels-Action-Triggers.md)
- [STATE_FOCUSED_DOMINANT](../pages/STATE-FOCUSED-DOMINANT.md)
- [STATE_DISTRIBUTED_BALANCED](../pages/STATE-DISTRIBUTED-BALANCED.md)
- [STATE_UNSTABLE_TRANSITION](../pages/STATE-UNSTABLE-TRANSITION.md)
- [STATE_TENSION_ELEVATED](../pages/STATE-TENSION-ELEVATED.md)
- [STATE_DIFFUSE_SPREAD](../pages/STATE-DIFFUSE-SPREAD.md)

## Origin

Hesperia-native fpf_bridge design — no Java prototype ancestor — Theory Explainer: plain_lang: The state machine the LLM actually sees — bridge_to_llm_prompt()'s envelope is a projection (one active state + legal next transitions + evidence requirements + pre-evaluated guard verdicts), never L1-L9's ~190 raw variables directly. author: Hesperia wiki (sphere/fpf_bridge/constants.py). extent: full. reasoning: **HWIKI-CATALOG-BRIDGE:** Source: `docs/foundations/output_catalog.md` §12, re-verified against `sphere/fpf_bridge/constants.py` 2026-08-04. application: [L9 — Pillars, Brand Labels, Action Triggers](../pages/L9-Pillars-Brand-Labels-Action-Triggers.md).

## Notes

**HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-CATALOG-BRIDGE:** Source: `docs/foundations/output_catalog.md` §12, re-verified against `sphere/fpf_bridge/constants.py` 2026-08-04. Evidence surface (as of `fpf_bridge_v7_2`, flag-gated off by default) can additionally join L5 contradiction_pressure/counter_evidence_gate, L7 trust_tier/system_confidence/decision_status, L4 evidence_support_baseline, KME's 6 primitives + kme_ksi, and TRIZ's triz_contradiction_* (explicitly namespaced apart from contradiction_pressure — two independently-computed mechanisms, never averaged) — gated behind `HESPERIA_FPF_EVIDENCE_EXPANSION`/`HESPERIA_FPF_CONTRADICTION_GATE`/`HESPERIA_FPF_KME_EVIDENCE`. None of this changes the projection discipline: still a menu of FGR-scored evidence and legal transitions, never the raw dict.

---
[← back to category](../categories/Evidence-and-Trust.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
