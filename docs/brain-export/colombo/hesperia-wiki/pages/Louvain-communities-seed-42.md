# Louvain communities (seed 42)

**Status:** 🔵 BEYOND — shipped in LIVE, not proposed in the Java corpus  
**Category:** [Graph and Structural Metrics](../categories/Graph-and-Structural-Metrics.md)  
**Type:** Algorithm  
**Responsible (module):** `hesperia/extensions/triz/novelty_engine.py`  
**Value / default:** LOUVAIN_SEED = 42

## Yields (formula)

networkx.community.louvain_communities — modularity-maximization clustering on the concept graph.

## Needed by (consumers)

- [contradiction_pressure -> tension_energy](../pages/contradiction-pressure-tension-energy.md)

## Origin

Blondel et al. (2008) — Theory Explainer: plain_lang: group concepts into communities by maximizing modularity (denser inside than across); seed 42 makes tie-breaks reproducible. author: Vincent Blondel, Jean-Loup Guillaume, Renaud Lambiotte, Etienne Lefebvre (2008). extent: full (algorithm), Hesperia-specific addition is only the reproducibility seed. reasoning: SCIENCE.md TRIZ/novelty path. application: `detect_concept_clusters_louvain` / novelty_engine; contrast [K(R) / L(R) / fragIndex (Java)](../pages/K-R-L-R-fragIndex-Java.md) (different discipline).

## Notes

**HWIKI-DOC-18:** **Not the same discipline-instance as [K(R) / L(R) / fragIndex (Java)](../pages/K-R-L-R-fragIndex-Java.md)** — community detection by modularity, not connected-component counting.

---
[← back to category](../categories/Graph-and-Structural-Metrics.md) · [wiki home](../index.md)
