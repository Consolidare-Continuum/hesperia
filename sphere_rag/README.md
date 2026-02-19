# `sphere_rag/` — HESPERIA reference implementation (minimal)

This package is a small, deterministic Python reference aligned with:

- `12_SPEC__Semantic_Engine_v0_4.txt` (semantic attribution intent)
- `13_SPEC__Indexing_and_Coordinates_v1_0.txt` (canonical indexing)
- `governance/ETHAN-HESPERIA-WATERLINE-PRINCIPLE.md` (waterline/cut doctrine)

## What exists today

- `sphere_rag/geometry.py` — canonical constants + `SideCoord` + `sideId` mappings.
- `sphere_rag/semantic_engine.py` — deterministic **keywords → (Area, Family) → seed sides** using `31_FAMILIES__area_family_table_full.txt` (name-based + hashed fallback).
- `sphere_rag/metrics.py` — region metrics: entropy(A), coherence C(R), tension energy, fragmentation, intersection matrix.
- `sphere_rag/phase_engine.py` — deterministic two-phase flow:
  - **Phase I (exploration)**: builds an active region from the keyword seed, traversing around the Area ring and allowing cross-area and new-family discovery.
  - **Phase II (core half-sphere reasoning)**: performs a deterministic **waterline cut** by side weight, keeping the smallest set of sides whose cumulative truth mass reaches `alpha · T_total` (default `alpha=0.50`).

## CLI usage

Run deterministic seeding + Phase I/II and print JSON:

```bash
python3 scripts/phase_traversal.py --keywords "Altruism,Truth,Order"
```

Self-test (determinism + ≥50% mass invariant):

```bash
python3 scripts/phase_traversal_selftest.py
```

