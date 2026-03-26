# HESPERIA Task 3 — Primitive Metric Calculator

Computes the six primitive metrics **[LD, COH, NC, PR, PV, CI]** from an **ActiveGraph** and **DomainConstants**. All outputs are in **[0, 1]**. Deterministic: same inputs → same primitives.

## Inputs

- **ActiveGraph** — from Task 2 (nodes: conceptId → hitCount; edges: source, target, type).
- **DomainConstants** — from Task 1 (domainNodeCount, domainDegreeP95, domainDistanceP95).

## Output

**PrimitiveMetrics**: LD, COH, NC, PR, PV, CI (canonical order for serialization).

## Formulas (summary)

| Metric | Meaning |
|--------|--------|
| **NC** | NodeCoverage = n / N (clamped). |
| **CI** | ConcentrationIndex = normalized HHI; 0 when n ≤ 1. |
| **LD** | LogicalDensity = (2m/n) / Deg95; 0 when n = 0. |
| **COH** | Coherence = 0.6×Conn + 0.4×Trans; Conn = largest component / n, Trans = 3×triangles / connected triplets; 0 when n < 3. |
| **PR** | PropagationRadius = mean distance to nearest anchor (non-anchors) / Dist95. |
| **PV** | PropagationVolume = sum(d*(v,S)+1) over V_prop, divided by N×(Dist95+1). |

Anchors: k = max(1, ⌈0.10×n⌉), top by probability mass p_i, tie-break by conceptId.

## Usage

```python
from core.domain import compute_primitives, load_domain_graph_from_json, load_frozen_constants
from core.domain import build_active_graph
from core.domain.models import ConceptHit, RelationCandidate

domain = load_domain_graph_from_json("assets/data/domain_graph.json")
constants = load_frozen_constants("assets/data/domain_constants.json")
hits = [ConceptHit("a", 0), ConceptHit("b", 1), ...]
relations = [RelationCandidate("a", "b", "rel"), ...]
graph = build_active_graph(hits, relations, domain)

metrics = compute_primitives(graph, constants)
# metrics.LD, .COH, .NC, .PR, .PV, .CI

out = metrics.to_dict()  # {"LD": ..., "COH": ..., ...}
```

## Empty graph

If `graph.nodes` is empty (or graph/constants are null):

LD = COH = NC = PR = PV = CI = **0.0**.

## Acceptance tests (A–E)

- **A** — Empty graph → all zeros.
- **B** — Single node → LD=0, COH=0, NC>0, PR=0, PV>0, CI=0.
- **C** — Chain 1–2–3–4–5 → LD>0, COH=0.6, PR>0, PV>0.
- **D** — Triangle → COH=1.0, LD high, PV>0.
- **E** — Two disconnected pairs → COH<1 (fragmentation).

## Summary

After Task 3, HESPERIA has a deterministic **primitive vector** [LD, COH, NC, PR, PV, CI] as the base measurement layer for downstream use.
