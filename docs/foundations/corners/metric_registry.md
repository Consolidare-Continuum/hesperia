# Corner: HesperiaMetric Registry — `24_SPEC` / `anchor_map_v1`

**Location:** `docs/specs/24_SPEC__Hesperia_Metric_and_Distance_v0_1.md`,
`schemas/anchor_map_v1.json`, `schemas/hesperia_metric_v01.json`,
`runtime/services/anchor_map_registry.py`, `runtime/services/path_metric.py`,
`runtime/services/family_graph.py`, `runtime/services/gcs_lookup.py`,
`runtime/services/hesperia_metric_emit.py` (all uncommitted, v0.7.0 working-tree state).

**Born:** 2026-06-22, "METRIC wave," scoped in `release/v0.7.0/RELEASE_SCOPE.md` as the
`v7_consolidated` track.

## Why this is a distinct concern

Before this corner existed, "distance" appeared in at least four structurally unrelated senses
across the codebase and papers: geodesic distance on the 12-area icosahedral sphere, zone
shortest-path cost on the 288-family lattice, hop count on the 72k hex adjacency graph, and an
ambiguous "KSI" used both as a tool name and a quality score (`docs/DOC_INDEX.md` makes this
collision explicit: "Bare 'KSI' in runtime docs is ambiguous — always qualify"). Ambiguous distance
language is a determinism leak of the same kind the guard triad exists to prevent elsewhere: two
readers (or two code paths) agreeing on a number while disagreeing on what manifold it lives on is
unauditable in exactly the way Sigma/Gamma forbid for structural shape and execution order.

The registry's normative rule is the minimal fix: every distance claim must be written as
`distance(metric_layer=<layer>, from=<id>, to=<id>, value=<float>, units=<string>)`, with
`metric_layer` drawn from a fixed enum (`area_sphere`, `family_graph`, `hex_graph`, `gcs_surface`,
`ipow_volume`, `concept_graph`, `state_gram`). This is the same "name the layer you're operating in"
discipline applied to concept resolution (Dict A vs Dict B) and to hex vs. family vs. area, now
extended to distance vocabulary specifically because it had drifted without anyone formalizing it.

`anchor_map_v1` is the frozen artifact this corner depends on for any cross-layer ("semantic ↔
geodesic") mapping: `runtime/services/anchor_map_registry.py` enforces, at load time, both that the
loaded map's ID matches `anchor_map_v1` *and* that its `status` field is literally `"FROZEN"` —
raising `ValueError` otherwise. This is the same freeze-and-verify pattern the lexicon corner uses
for Dict A/B, applied to the geometry-to-geometry mapping layer instead.

## What would break without it

Without a `metric_layer` qualifier, a path-action computation summing costs across area-sphere
geodesic distance, family zone cost, and hex hop count could silently add incommensurable
quantities (radians, zone-step units, hop counts) as if they were the same kind of number — the
path-action formula `S_path = Σ w(e)·ℓ(e)` only makes sense because each edge type's `ℓ(e)` is
explicitly defined per-layer in `24_SPEC §5`'s table, with layer-specific default weights absorbing
the unit mismatch. Without the frozen `anchor_map_v1` check, a semantic-hex-to-GCS-slot lookup could
run against a map that was mid-edit, silently producing a geometry computation that does not
correspond to any single coherent assignment.

## How it relates to neighbors

This corner is explicitly a thin service layer over geometry that already existed (see
`corners/topology_geometry.md`, `corners/hex_substrate.md`): `24_SPEC §4.1` names
`sphere/topology/embedding.py` directly as the `area_sphere` implementation; `§4.2` builds on
`family_embedding.py`'s zone keys; `§4.3` is the hex substrate's adjacency graph. The spec is
careful to scope out what it is *not*: "Einstein field equations; clinical interpretation of IPoW;
DB migration to 251 semantic hex rows; Poisson solver" — explicitly deferring `HESPERIA_GCS_EMIT=1`,
full `interior_point_of_world_view` live emit, and `path_metric_cost` on traversal to "follow-on
rows," per `release/v0.7.0/RELEASE_SCOPE.md`. It is gated behind `HESPERIA_METRIC_EMIT` /
`HESPERIA_GCS_EMIT` env flags, shipping disabled by default — the same incremental, reversible
rollout discipline the sealed-release era (`corners/release_governance.md`) uses for everything
that touches canonical output.
