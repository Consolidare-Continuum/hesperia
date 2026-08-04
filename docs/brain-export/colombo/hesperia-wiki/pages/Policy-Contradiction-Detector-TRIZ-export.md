# Policy Contradiction Detector (TRIZ export)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Concept Dictionary](../categories/Concept-Dictionary.md)  
**Type:** Formula / function  
**Responsible (module):** `hesperia/extensions/triz/ (corners/triz_extension.md)`  
**Value / default:** per-item export

## In plain words

Per contradicting item: contradiction_score, contradiction_density, area_id, family_ids, triz_principle (segmentation/counterbalance/parameter_change/dynamic_adaptation).

## Definition

- **Receives:** [TRIZ decision-intelligence exports](../pages/TRIZ-decision-intelligence-exports.md)
- **Does:** Per contradicting item: contradiction_score, contradiction_density, area_id, family_ids, triz_principle (segmentation/counterbalance/parameter_change/dynamic_adaptation).
- **Outputs:** `per-item export` → *no named wiki consumer yet*
- **Exists for:** **HWIKI-CATALOG-BRIDGE:** The `triz_principle` field borrows Altshuller's TRIZ inventive-principle vocabulary (segmentation, counterbalance, parameter_change, dynamic_adaptation) to label *how* a detected contradiction could structurally re

## Yields (formula)

Per contradicting item: contradiction_score, contradiction_density, area_id, family_ids, triz_principle (segmentation/counterbalance/parameter_change/dynamic_adaptation).

## Produced from (inputs)

- [TRIZ decision-intelligence exports](../pages/TRIZ-decision-intelligence-exports.md)

## See also

- [TRIZ decision-intelligence exports](../pages/TRIZ-decision-intelligence-exports.md)
- [Innovation Radar (TRIZ export)](../pages/Innovation-Radar-TRIZ-export.md)
- [Narrative Propagation Monitor (TRIZ export)](../pages/Narrative-Propagation-Monitor-TRIZ-export.md)

## Origin

Hesperia-native TRIZ extension design, TRIZ inventive-principle naming (Altshuller) applied to Hesperia's own contradiction detection — no Java prototype ancestor — Theory Explainer: plain_lang: Per contradicting item: contradiction_score, contradiction_density, area_id, family_ids, triz_principle (segmentation/counterbalance/parameter_change/dynamic_adaptation). author: Hesperia wiki (hesperia/extensions/triz/ (corners/triz_extension.md)). extent: full. reasoning: **HWIKI-CATALOG-BRIDGE:** The `triz_principle` field borrows Altshuller's TRIZ inventive-principle vocabulary (segmentation, counterbalance, parameter_change, dynamic_adaptation) to label *how* a detected contradiction could structurally re. application: [TRIZ decision-intelligence exports](../pages/TRIZ-decision-intelligence-exports.md).

## Notes

**HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-CATALOG-BRIDGE:** The `triz_principle` field borrows Altshuller's TRIZ inventive-principle vocabulary (segmentation, counterbalance, parameter_change, dynamic_adaptation) to label *how* a detected contradiction could structurally resolve, not just that one exists. Source: `docs/foundations/output_catalog.md` §11.

---
[← back to category](../categories/Concept-Dictionary.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
