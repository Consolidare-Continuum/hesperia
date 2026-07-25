# dominant_area_share_threshold

**Status:** 🟢 LIVE_SUCCESSOR — same idea, different name/formula than any Java ancestor  
**Category:** [Activation and Diagnostic Thresholds](../categories/Activation-and-Diagnostic-Thresholds.md)  
**Type:** Parameter (constant)  
**Responsible (module):** `sphere/diagnostics/monotony_detector.py`  
**Value / default:** 0.65

## Yields (formula)

compute_dominant_area_share(area_vector) >= threshold triggers dominance classification.

## Produced from (inputs)

- *A_vec[12] (area activation vector)*

## Needed by (consumers)

- [X_A / X_F alignment (Java)](../pages/X-A-X-F-alignment-Java.md)

## Origin

Java 20_GEOMETRY `X_A` alignment concept

## Notes

Real, wired successor of Java's X_A — has a threshold AND a rule trigger in `rule_registry.py`. No family-share (`X_F`) counterpart exists yet — see [X_A / X_F alignment (Java)](../pages/X-A-X-F-alignment-Java.md).

---
[← back to category](../categories/Activation-and-Diagnostic-Thresholds.md) · [wiki home](../index.md)
