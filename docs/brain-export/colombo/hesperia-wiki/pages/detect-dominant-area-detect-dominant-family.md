# detect_dominant_area / detect_dominant_family

**Status:** 🟢 LIVE_SUCCESSOR — same idea, different name/formula than any Java ancestor  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Formula / function  
**Responsible (module):** `core/math/vector_ops.py`  
**Value / default:** —

## Yields (formula)

Returns the index of the dominant area / family (argmax), not a share fraction.

## Produced from (inputs)

- *A_vec[12] (area activation vector)*
- *F_vec[288]*

## Needed by (consumers)

- [dominant_area_share_threshold](../pages/dominant-area-share-threshold.md)

## Origin

Java `X_A, X_F` alignment concept

## Notes

Index-only; the area side has a share-fraction sibling (`compute_dominant_area_share`), the family side does not — see [X_A / X_F alignment (Java)](../pages/X-A-X-F-alignment-Java.md).

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md)
