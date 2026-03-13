# HESPERIA Task 2 — Active Graph Canonicalizer

Deterministic construction of the text-activated semantic graph **A = (V_A, E_A)** from concept hits and relation candidates. Guarantee: **same text + same domain graph → identical active graph**.

## Inputs

- **Domain graph** — reference graph (Task 1); only concepts and edges present here may appear in the active graph.
- **Concept hits** — from upstream NLP: `conceptId`, `tokenIndex`.
- **Relation candidates** — detected co-occurrence or relation extraction: `conceptA`, `conceptB`, `relationType`.

## Output

- **ActiveGraph**: `nodes` (map conceptId → `{ hitCount }`), `edges` (list of `{ source, target, type }`), canonically ordered and validated.

## Rules (invariants)

1. **V_A ⊆ V_R** — only domain concepts allowed; unknown concepts ignored.
2. **E_A ⊆ E_R** — edge (u, v, r) is included only if it exists in the domain graph (undirected).
3. **Canonical edge order** — `source = min(conceptA, conceptB)`, `target = max(conceptA, conceptB)`.
4. **No self-loops** — source ≠ target.
5. **No duplicate edges** — one edge per (source, target, relationType).

## Usage

```python
from core.domain import (
    build_active_graph,
    load_domain_graph_from_json,
)
from core.domain.models import ConceptHit, RelationCandidate

domain = load_domain_graph_from_json("assets/data/domain_graph.json")
hits = [
    ConceptHit("contract_law", 0),
    ConceptHit("legal_obligation", 1),
    ConceptHit("law", 2),
]
relations = [
    RelationCandidate("contract_law", "law", "is_subdomain"),
    RelationCandidate("contract_law", "legal_obligation", "defines"),
]
graph = build_active_graph(hits, relations, domain)

# Serialize for downstream (e.g. Task 3)
out = graph.to_dict()  # {"nodes": {...}, "edges": [...]}
```

## Integrity checks

Before return:

- |V_A| ≤ |V_R|
- |E_A| ≤ |E_R|
- No duplicate edges in the output.

## Example output (spec)

```json
{
  "nodes": {
    "contract_law": {"hitCount": 3},
    "legal_obligation": {"hitCount": 1},
    "law": {"hitCount": 1}
  },
  "edges": [
    {"source": "contract_law", "target": "law", "type": "is_subdomain"},
    {"source": "contract_law", "target": "legal_obligation", "type": "defines"}
  ]
}
```

## Edge cases

- **No concept hits** → empty graph (nodes and edges empty).
- **No valid relations** → nodes present, edges list empty.
- **Unknown concepts** → silently ignored.

Next: **Task 3 — Primitive Metric Calculator** (LD, COH, NC, PR, PV, CI) consuming this active graph.
