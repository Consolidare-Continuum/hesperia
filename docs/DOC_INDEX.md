# Hesperia documentation index

**Updated:** 2026-06-22 (METRIC wave)

## Geometry and metric

| Doc | Topic |
|-----|--------|
| [24_SPEC__Hesperia_Metric_and_Distance_v0_1.md](specs/24_SPEC__Hesperia_Metric_and_Distance_v0_1.md) | **HesperiaMetric** registry, `metric_layer` enum, `S_path`, runtime emit flags |
| [ENGINE-ANALYZE-CONTRACT.md](../ENGINE-ANALYZE-CONTRACT.md) | `/analyze` response — optional `meta.hesperia_metric` when `HESPERIA_METRIC_EMIT=1` |

## Cross-links (brain authority)

- **20_GEOMETRY** — icosahedral area layout (brain `user_documents/HESPERIA_ACADEMIA/`)
- **22_SPEC** — GCS + Interior Point of World View ([brain draft](https://github.com/igareosh/cursor/blob/main/user_documents/HESPERIA_ACADEMIA/HESPERIA-FORMALIZATION-GEODESIC-SPHERE-AND-INTERIOR-POINT-OF-WORLD-VIEW-v0_1.md))
- **23_SPEC** — General Thought Propagation ([brain draft](https://github.com/igareosh/cursor/blob/main/user_documents/HESPERIA_ACADEMIA/HESPERIA-FORMALIZATION-GENERAL-THOUGHT-PROPAGATION-v0_1.md))
- **Ethan ratification** — [SPEC-ETHAN-HESPERIA-METRIC-AND-DISTANCE](https://github.com/igareosh/cursor/blob/main/governance/SPEC-ETHAN-HESPERIA-METRIC-AND-DISTANCE.md)

## Concept-graph metric layer (BELL/KSI)

| Term | Qualified form | Layer |
|------|---------------|-------|
| `path_mass` | BELL `path_mass` on corridor bundles | `metric_layer=concept_graph` |
| KSI | **KSI-Inspector** (inspection tool) | `metric_layer=concept_graph` |
| KSI (score) | **KME-KSI-score** (quality metric) | engine output, not a spatial distance |

BELL `path_mass` uses edge weight W_e / resistance R_e on Floor-2 concept relations (24_SPEC §4.6, §5).
Bare "KSI" in runtime docs is ambiguous — always qualify (24_SPEC §7).

## Environment flags (metric emit)

| Variable | Default | Effect |
|----------|---------|--------|
| `HESPERIA_METRIC_EMIT` | `0` | When `1`, attach `meta.hesperia_metric` + `coordinate_fingerprint` on analyze |
| `HESPERIA_GCS_EMIT` | `0` | When `1`, emit static `geodesic_sphere` block (requires frozen `anchor_map_v1`) |

See 24_SPEC §10 and promotion checklist §12.
