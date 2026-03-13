# HESPERIA Task 1 — Domain Constants Extractor

Domain constants are computed from the **reference domain graph** and frozen for use downstream.

## Constants

| Constant | Description |
|----------|-------------|
| `domain_node_count` | \|V_R\| — number of nodes in the reference graph |
| `domain_degree_p95` | 95th percentile of node degree (undirected); clamped ≥ 1 |
| `domain_distance_p95` | 95th percentile of shortest-path distances in the giant component (BFS, sampled starts); clamped ≥ 1 |

## Reference domain graph (JSON)

- **Path (default):** `assets/data/domain_graph.json`
- **Schema:**
  - `nodes`: list of `{ "conceptId": "<id>" }` or dict of id → `{ "conceptId": "..." }`
  - `edges`: list of `{ "sourceConceptId", "targetConceptId", "relationType" }`
- Graph is treated as **undirected** for metrics; self-loops ignored; duplicate edges removed during load.

## Frozen constants output

- **Path (default):** `assets/data/domain_constants.json`
- **Example:**
  ```json
  {"domain_degree_p95":14,"domain_distance_p95":6,"domain_node_count":72000}
  ```

## Usage

```bash
# Compute from reference graph and write frozen constants
python3 -m tools.domain_constants_extract --graph assets/data/domain_graph.json --out assets/data/domain_constants.json
```

## Loading frozen constants in code

```python
from core.domain import load_frozen_constants

constants = load_frozen_constants("assets/data/domain_constants.json")
# constants.domain_node_count, .domain_degree_p95, .domain_distance_p95
```

Formulas and determinism: see the Java-style machine-readable specification (Task 1).
