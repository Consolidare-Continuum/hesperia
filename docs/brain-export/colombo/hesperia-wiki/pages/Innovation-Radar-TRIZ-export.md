# Innovation Radar (TRIZ export)

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Concept Dictionary](../categories/Concept-Dictionary.md)  
**Type:** Formula / function  
**Responsible (module):** `hesperia/extensions/triz/ (corners/triz_extension.md)`  
**Value / default:** per-cluster + aggregate export

## In plain words

Per cluster: innovation_score, rarity, contradiction_density, propagation_reach. Aggregate: cluster_count, max_innovation_score, mean_innovation_score.

## Definition

- **Receives:** [TRIZ decision-intelligence exports](../pages/TRIZ-decision-intelligence-exports.md), [Louvain communities (seed 42)](../pages/Louvain-communities-seed-42.md)
- **Does:** Per cluster: innovation_score, rarity, contradiction_density, propagation_reach. Aggregate: cluster_count, max_innovation_score, mean_innovation_score.
- **Outputs:** `per-cluster + aggregate export` → *no named wiki consumer yet*
- **Exists for:** **HWIKI-CATALOG-BRIDGE:** Built on the Louvain clustering (seed 42, reproducible run-to-run) — scores each innovation cluster on rarity and reach, not just size

## Yields (formula)

Per cluster: innovation_score, rarity, contradiction_density, propagation_reach. Aggregate: cluster_count, max_innovation_score, mean_innovation_score.

## Produced from (inputs)

- [TRIZ decision-intelligence exports](../pages/TRIZ-decision-intelligence-exports.md)
- [Louvain communities (seed 42)](../pages/Louvain-communities-seed-42.md)

## See also

- [TRIZ decision-intelligence exports](../pages/TRIZ-decision-intelligence-exports.md)
- [Louvain communities (seed 42)](../pages/Louvain-communities-seed-42.md)
- [Policy Contradiction Detector (TRIZ export)](../pages/Policy-Contradiction-Detector-TRIZ-export.md)
- [Narrative Propagation Monitor (TRIZ export)](../pages/Narrative-Propagation-Monitor-TRIZ-export.md)

## Origin

Hesperia-native TRIZ extension design — no Java prototype ancestor — Theory Explainer: plain_lang: Per cluster: innovation_score, rarity, contradiction_density, propagation_reach. Aggregate: cluster_count, max_innovation_score, mean_innovation_score. author: Hesperia wiki (hesperia/extensions/triz/ (corners/triz_extension.md)). extent: full. reasoning: **HWIKI-CATALOG-BRIDGE:** Built on the Louvain clustering (seed 42, reproducible run-to-run) — scores each innovation cluster on rarity and reach, not just size. application: [TRIZ decision-intelligence exports](../pages/TRIZ-decision-intelligence-exports.md), [Louvain communities (seed 42)](../pages/Louvain-communities-seed-42.md).

## Notes

**HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. **HWIKI-CATALOG-BRIDGE:** Built on the Louvain clustering (seed 42, reproducible run-to-run) — scores each innovation cluster on rarity and reach, not just size. Source: `docs/foundations/output_catalog.md` §11.

---
[← back to category](../categories/Concept-Dictionary.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
