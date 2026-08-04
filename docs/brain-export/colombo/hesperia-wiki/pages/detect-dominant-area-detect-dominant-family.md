# detect_dominant_area / detect_dominant_family

**Status:** 🟢 LIVE_SUCCESSOR — same idea, different name/formula than any Java ancestor  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Formula / function  
**Responsible (module):** `core/math/vector_ops.py`  
**Value / default:** —

## In plain words

Returns the index of the dominant area / family (argmax), not a share fraction.

## Definition

- **Receives:** *A_vec[12] (area activation vector)*, *F_vec[288]*
- **Does:** Returns the index of the dominant area / family (argmax), not a share fraction.
- **Outputs:** `—` → [dominant_area_share_threshold](../pages/dominant-area-share-threshold.md)
- **Exists for:** Index-only; the area side has a share-fraction sibling (`compute_dominant_area_share`), the family side does not — see [X_A / X_F alignment (Java)](../pages/X-A-X-F-alignment-Java.md)

## Yields (formula)

Returns the index of the dominant area / family (argmax), not a share fraction.

## Produced from (inputs)

- *A_vec[12] (area activation vector)*
- *F_vec[288]*

## Needed by (consumers)

- [dominant_area_share_threshold](../pages/dominant-area-share-threshold.md)

## See also

- [dominant_area_share_threshold](../pages/dominant-area-share-threshold.md)
- [X_A / X_F alignment (Java)](../pages/X-A-X-F-alignment-Java.md)

## Origin

Java `X_A, X_F` alignment concept — Theory Explainer: plain_lang: Returns the index of the dominant area / family (argmax), not a share fraction. author: Hesperia wiki (core/math/vector_ops.py). extent: full. reasoning: Index-only; the area side has a share-fraction sibling (`compute_dominant_area_share`), the family side does not — see [X_A / X_F alignment (Java)](../pages/X-A-X-F-alignment-Java.md). application: [dominant_area_share_threshold](../pages/dominant-area-share-threshold.md).

## Notes

**HWIKI-PLAIN-B:** plain_lang backfilled from formula/notes 2026-08-04. Index-only; the area side has a share-fraction sibling (`compute_dominant_area_share`), the family side does not — see [X_A / X_F alignment (Java)](../pages/X-A-X-F-alignment-Java.md).

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
