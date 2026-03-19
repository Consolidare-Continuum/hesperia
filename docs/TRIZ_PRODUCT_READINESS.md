# TRIZ Product Readiness

## What the TRIZ layer does

- Detects **typed contradictions** (conflict / negation / opposition) on an active semantic graph.
- Classifies pairs into **TRIZ-style resolution patterns** (e.g. segmentation, parameter_change).
- Scores **innovation clusters** (Louvain on the active graph) and **narrative propagation** metrics.
- **Series 2** binds outputs to **HESPERIA areas / families / hex** and canonical **icosahedral adjacency**.

## Inputs

- **Active graph**: concepts (nodes with hit counts), relations (edges with types).
- **Topology (optional but recommended)**: `concept_to_area`, `concept_to_family`, or `concept_matrix` with `area_id` / `family_id` / `hex_id`.
- **Corpus text** (for baselines only): plain text alongside `graph.json` in benchmark packs.

## Outputs

- **Policy-oriented**: tension index, family/area hotspots, TRIZ classes, cross-domain flags.
- **Innovation-oriented**: ranked clusters, rarity, reach.
- **Narrative-oriented**: penetration, velocity, stability, routes, blockage/spillover hints.
- **Product layer**: named SKUs (`HSP-TRIZ-P1`, `HSP-TRIZ-I1`, `HSP-TRIZ-N1`), summaries, dashboard contracts (`triz_ui_v1`), investor snapshots.

## Benchmark behavior

- Corpora under `benchmarks/extensions/triz/` with `corpus.txt` + `graph.json`.
- Manifest defines expected **qualitative profiles** (low/medium/high tension, etc.).
- **Profile fit score** is a stability/demo metric, not ground truth.

## Baseline comparison

- **Keyword**: opposing-term co-occurrence window.
- **Graph**: Louvain clusters + polarity edge count on token graph.
- **TF-IDF-style**: opposing term emphasis.
- **TRIZ** adds typed relations, topology-bounded propagation, and structured reports.

## Product packages

| SKU | Package |
|-----|---------|
| HSP-TRIZ-P1 | Policy Contradiction Detector |
| HSP-TRIZ-I1 | Innovation Radar |
| HSP-TRIZ-N1 | Narrative Monitor |

## Limits

See [TRIZ_LIMITATIONS.md](./TRIZ_LIMITATIONS.md). The TRIZ layer does **not** alter ontology or topology; it is **read-only** over structural semantics (guards enforce meta-area lexical rules).
