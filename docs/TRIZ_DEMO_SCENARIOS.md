# TRIZ Demo Scenarios

## 1. Policy contradiction (coherent vs polarized)

- **Inputs**: `benchmarks/triz/corpus_policy_coherent` vs `corpus_policy_polarized`.
- **Show**: side-by-side **Policy Tension Score**, family hotspots, dominant TRIZ patterns.
- **Artifacts**: `examples/triz_demo/triz/outputs/demo1_*` (JSON, CSV, executive markdown).

## 2. Innovation discovery (sparse cross-sector)

- **Input**: `corpus_innovation_sparse`.
- **Show**: ranked **Innovation Pressure Score**, rare concept clusters, cross-area reach.
- **Artifacts**: `demo2_innovation_radar.json`, `demo2_clusters.csv`.

## 3. Narrative spread (multi-area spillover)

- **Input**: `corpus_narrative_spillover`.
- **Show**: route sequence across areas, blockage endpoints, spillover targets.
- **Artifacts**: `demo3_narrative_monitor.json`, `demo3_routes.csv`, investor snapshot.

## Running demos

```bash
python3 examples/triz_demo/triz/make_demo_reports.py
```

## CLI (single product)

```bash
python3 tools/triz/run_policy_detector.py --corpus benchmarks/triz/corpus_policy_polarized
```
