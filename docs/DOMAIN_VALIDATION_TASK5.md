# HESPERIA Task 5 — Validation & Toy-Graph Test Suite

Validation suite for the metric engine (Tasks 1–4). Confirms:

- **Deterministic behavior** — same graph → same primitives and derived
- **Mathematical sanity** — range [0,1], no NaN/Inf
- **Division safety** — zero denominators handled
- **Propagation correctness** — PR increase → TDS, SPS non-decreasing
- **Structural sensitivity** — empty, single, chain, triangle, star, disconnected

No new formulas; verification only.

## Test Fixtures

- **TEST_CONSTANTS**: `domain_node_count=100`, `domain_degree_p95=10`, `domain_distance_p95=5`
- **build_graph(nodes, edges)** — builds `ActiveGraph` with `hit_count=1` per node, `relation_type="test"` per edge

## Graph Scenarios

| Test | Graph | Expected |
|------|--------|----------|
| A | Empty | LD=COH=NC=PR=PV=CI=0; all derived zero |
| B | Single node | LD=0, COH=0, NC>0, PR=0, PV>0, CI=0 |
| C | Two nodes A—B | LD>0, COH=0, PR>0, PV>0 |
| D | Chain A—B—C—D—E | COH=0.6 |
| E | Triangle A—B—C | COH=1.0 |
| F | Star (center A, B,C,D,E) | LD>0, COH<1 |
| G | Disconnected A—B, C—D | COH<0.6 |

## Behavioral Tests

- **test_range_guarantees** — random primitives in [0,1] → all derived in [0,1]
- **test_division_safety** — NC=0, PV=0 → no NaN or Infinity in derived vector
- **test_determinism** — same chain graph twice → identical primitives
- **test_monotonicity** — LD increase → KDI non-decreasing
- **test_propagation_behavior** — PR increase → TDS, SPS non-decreasing
- **test_performance** — primitive + derived on 50-node graph < 50 ms (sanity bound)

## Running the Suite

```bash
pytest tests/domain/test_validation_toy_graphs.py -v
```

Or with the rest of the domain tests:

```bash
pytest tests/domain/ -v
```

## Completion Criteria

- All graph scenarios (A–G) pass
- No NaN or Infinity in any metric
- All metrics in [0, 1]
- Determinism verified
- Monotonicity and propagation behavior checks pass
