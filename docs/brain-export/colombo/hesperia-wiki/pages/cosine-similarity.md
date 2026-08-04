# cosine_similarity

**Status:** 🟢 LIVE_SUCCESSOR — same idea, different name/formula than any Java ancestor  
**Category:** [Similarity and Retrieval](../categories/Similarity-and-Retrieval.md)  
**Type:** Formula / function  
**Responsible (module):** `core/domain/fingerprint.py (cosine_similarity, fingerprint_cosine)`  
**Value / default:** —

## In plain words

angle between two vectors — 1 means same direction, 0 means orthogonal.

## Definition

- **Receives:** *none declared (constant, hub, or external)*
- **Does:** Dot product over norms — fingerprint / hit-vector comparison.
- **Outputs:** `—` → [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md), [cumulativeDrift / turnCoherence](../pages/cumulativeDrift-turnCoherence.md)
- **Exists for:** SCIENCE.md; repurposed from Java turn-coherence toward KME fingerprints

## Yields (formula)

Dot product over norms — fingerprint / hit-vector comparison.

## Needed by (consumers)

- [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md)
- [cumulativeDrift / turnCoherence](../pages/cumulativeDrift-turnCoherence.md)

## See also

- [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md)
- [cumulativeDrift / turnCoherence](../pages/cumulativeDrift-turnCoherence.md)
- [Jaccard overlaps](../pages/Jaccard-overlaps.md)
- [LIVE_SUCCESSOR (status term)](../pages/LIVE-SUCCESSOR-status-term.md)

## Origin

Gerard Salton (1975) VSM — Theory Explainer: plain_lang: angle between two vectors — 1 means same direction, 0 means orthogonal. author: Gerard Salton (1975) vector-space model; also Java 21_MATH `cosine` (turn-drift use). extent: full (formula); LIVE_SUCCESSOR for use-site (fingerprints, not turn-drift). reasoning: SCIENCE.md; repurposed from Java turn-coherence toward KME fingerprints. application: [KME Primitives and Derived Metrics](../pages/KME-Primitives-and-Derived-Metrics.md); contrast dead [cumulativeDrift / turnCoherence](../pages/cumulativeDrift-turnCoherence.md).

## Notes

**HWIKI-DOC-17:** LIVE_SUCCESSOR — fingerprint comparison, not Java turn-to-turn drift.

---
[← back to category](../categories/Similarity-and-Retrieval.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
