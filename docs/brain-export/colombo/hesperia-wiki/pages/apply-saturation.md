# apply_saturation

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Concept Dictionary](../categories/Concept-Dictionary.md)  
**Type:** Formula / function  
**Responsible (module):** `hesperia/engine/concept_dictionary/executor.py:13`  
**Value / default:** saturation_k (per-concept)

## In plain words

closed-form curve that caps concept-dictionary weights so no single weight runs away — documented saturation, not the dead Java composite score.

## Definition

- **Receives:** [LIVE_SUCCESSOR (status term)](../pages/LIVE-SUCCESSOR-status-term.md)
- **Does:** Closed-form weight-capping curve, documented in `docs/governance/cd_v1/SATURATION_CLOSED_FORM.md`.
- **Outputs:** `saturation_k (per-concept)` → *no named wiki consumer yet*
- **Exists for:** LIVE weight-capping; distinct from Java 23_PROTOTYPE saturation

## Yields (formula)

Closed-form weight-capping curve, documented in `docs/governance/cd_v1/SATURATION_CLOSED_FORM.md`.

## Produced from (inputs)

- [LIVE_SUCCESSOR (status term)](../pages/LIVE-SUCCESSOR-status-term.md)

## See also

- [LIVE_SUCCESSOR (status term)](../pages/LIVE-SUCCESSOR-status-term.md)
- [saturation (Java, 23_PROTOTYPE)](../pages/saturation-Java-23-PROTOTYPE.md)

## Origin

No Java ancestor (narrower, differently-scoped concept than Java's composite decision-layer `saturation`) — Theory Explainer: plain_lang: closed-form curve that caps concept-dictionary weights so no single weight runs away — documented saturation, not the dead Java composite score. author: Hesperia wiki (hesperia/engine/concept_dictionary/executor.py:13). extent: full. reasoning: LIVE weight-capping; distinct from Java 23_PROTOTYPE saturation. application: Concept Dictionary.

## Notes

**HWIKI-WIRE:** attached to category anchor [LIVE_SUCCESSOR (status term)](../pages/LIVE-SUCCESSOR-status-term.md). **HWIKI-PLAIN-C:** algebra plain_lang polished 2026-08-04. **HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. Not a gap against [saturation (Java, 23_PROTOTYPE)](../pages/saturation-Java-23-PROTOTYPE.md) — different, correctly-scoped tool for a different job.

---
[← back to category](../categories/Concept-Dictionary.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
