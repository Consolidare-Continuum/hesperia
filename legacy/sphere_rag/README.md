# `sphere_rag/` — HESPERIA reference implementation (minimal)

Deterministic Python reference aligned with 12_SPEC, 13_SPEC, 22_SPEC, 24_SPEC, 26_SPEC (v0.3.2), and guard/shadow policy.

## What exists today (repo-accurate)

**Geometry and invariants (single source)**
- `invariant_catalog.py` — Frozen constants (12/24/250/6), TOTAL_SIDES 432k, CANONICAL_AREA_SET, AREA_FAMILY_MAP, `forward`/`inverse`, `validate_coord`/`validate_side_id`. Replaces standalone geometry.py; use this for all geometry.
- `invariant_enforcer.py` — Σ enforcer: geometry check, bijection check, output contract (exactly 6 keys), domain clamp. No bypass.
- `failure_classes.py` — HARD_STOP, DATA_REJECT, DEGRADED_STATE, WARN.

**Guards and pipeline**
- `gamma_guard.py` — Γ: traversal stability; gammaPenalty ∈ [0,1].
- `theta_gate.py` — Θ: governance gate; G_DEGRADED_MAX, LOOP_DEGRADED_MAX.
- `guard_pipeline.py` — Strict order Sigma → Gamma → Theta; guard coverage logged.
- `safeguard_state_machine.py` — 25_SPEC: TraversalSafeguard, run_traversal_with_safeguard (three consecutive fail → STOP).

**Core math and API**
- `hesperia_v03_core_math.py` — v0.3 core math (22_SPEC): fusion, centroid, base step, aggregation, penalties, metrics. `run_api()` and `run_api_with_guards()` — both pass Sigma; no bypass. Config: `guard_config_v1.json`. Tests: `python3 sphere_rag/hesperia_v03_core_math.py test`.
- `output_contracts_v032.py` — v0.3.2 §2: `to_minimal_operational_result()` (6 keys), `make_error_result()` (3 keys).
- `serve_v033.py` — v0.3.3 §6: GET /health, POST /hesperia/analyze (minimal result or error). Run: `python3 sphere_rag/serve_v033.py [port]` or `python3 sphere_rag/run_simulation.py serve [port]`.

**Simulations and tooling**
- `full_run_simulation.py` — Full v0.3 run (stub topology); optional --S/--L.
- `chroma_books_validation_run.py` — Stub + Chroma books I-Q2.
- `run_simulation.py` — Single entry: `full`, `chroma`, or `serve`.
- `lexical_loader.py` — Dict A/B loader; Spec 20 validation; `_canonical_side_count()` from invariant_catalog.

**Shadow**
- `shadow_layer.py` — Shadow Layer v1.0 (24_SPEC): risk-based activation, candidate set C, mass decay, shadow-adjusted scores, Θ abuse detection. Geometry constants imported from invariant_catalog.

**Not present in repo**
- Dedicated `geometry.py`, `semantic_engine.py`, `metrics.py`, `phase_engine.py` — geometry and metrics are in invariant_catalog + hesperia_v03_core_math; text→attribution (semantic_engine) and phase_engine are future.
- `scripts/phase_traversal.py`, `scripts/phase_traversal_selftest.py` — not in this tree; use run_simulation.py modes or core_math tests.

## CLI / API (v0.3.2) and pre-test

**Pre-test (whole run, small builds):** From repo root (`CLIENTS/hesperia`):
`python scripts/run_hesperia_pre_test.py` or `python sphere_rag/run_simulation.py pretest`
See [RUNNABLE.md](../RUNNABLE.md) for all runnable entry points.

```bash
# Demo run
python3 sphere_rag/hesperia_v03_core_math.py

# Tests
python3 sphere_rag/hesperia_v03_core_math.py test

# Full simulation (stub topology)
python3 sphere_rag/run_simulation.py full [--S path] [--L path] [--out path]

# v0.3.2 API server (GET /health, POST /hesperia/analyze)
python3 sphere_rag/run_simulation.py serve [port]
```
