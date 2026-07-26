# TRIZ module inventory — `hesperia/extensions/triz/`

**Date:** 2026-07-23  
**ID:** HWIKI-TRIZ-01  
**Owner:** Felix  
**Checkout:** `/data/hesperia/hesperia` (package path `hesperia/extensions/triz/`)  
**Count:** 34 Python modules (+ `__init__.py`) under the package; Louvain already wikified — this inventory lists the rest for wiki batch planning  
**Related (outside package):** `hesperia/extensions/dynamics/triz_signal.py` · product/API/tests under `hesperia/product/`, `runtime/api/`, `tests/triz/`

---

## Already on wiki

| Symbol / topic | Module | Notes |
|----------------|--------|-------|
| Louvain communities (seed 42) | `novelty_engine.py` (`LOUVAIN_SEED`, `detect_concept_clusters_louvain`) | BEYOND page exists |

---

## Package modules (inventory)

Paths relative to package root `hesperia/extensions/triz/`.

| Module | Role (from headers / public defs) | Wiki batch hint |
|--------|-----------------------------------|-----------------|
| `__init__.py` | Package export surface | skip / note only |
| `models.py` | Dataclasses: `ContradictionSignal`, `InnovationCluster`, `NarrativeSignal`, `TRIZSignals`, … | concept dictionary / types |
| `pipeline.py` | `run_triz_layer`, `run_triz_analysis_complete`, ActiveGraph bridge | orchestration hub page |
| `triz_pipeline.py` | `run_triz_analysis` entry | orchestration / API edge |
| `triz_classifier.py` | `classify_contradiction(s)` principle table | classification science |
| `contradiction_engine.py` | `detect_contradictions`, `build_contradiction_signals`, pattern classify | core contradiction |
| `contradiction_contract.py` | Canonical field sets / forbidden synonyms (v0.5.8) | contract / governance |
| `contradiction_calibration.py` | Default calibration + `validate_contradiction_calibration` | params / LIVE values |
| `contradiction_coupling.py` | Pressure accum, row support, coupling version | energy / pressure |
| `contradiction_feedback.py` | Lexical/concept/pair calibration risk scores | feedback loop |
| `contradiction_negation.py` | Negation / inhibition / mode summary | negation mode |
| `contradiction_uncertainty.py` | Uncertainty package / entropy-normalized weights | uncertainty |
| `crossplane_contradiction.py` | Cross-plane contradiction aggregates | crossplane |
| `family_contradiction.py` | Family pressure matrix, fragmentation, bridge conflict | family metrics |
| `family_clustering.py` | Cluster contradictions by family/area; hotspots | clustering (≠ Louvain) |
| `family_weights_sparsify_v052.py` | Weight sparsify constants / promote rules | config / DEAD-or-LIVE check |
| `conflict_release_gating.py` | Release gates PASS/WARN/FAIL; promotion verdict | governance gates |
| `novelty_engine.py` | Density, clusters, **Louvain**, innovation clusters | Louvain DONE; rest still open |
| `propagation_engine.py` | Activation propagate, narrative signals, history | propagation |
| `narrative_routes.py` | BFS narrative paths / monitor summary | narrative |
| `topology_binding.py` | Bind concepts/contradictions to matrix coords | topology bind |
| `topology_metrics.py` | Area adjacency, locality score, distance | topology metrics |
| `topology_activation_pipeline.py` | Coactivation graph, raw concept contradictions | activation pipeline |
| `topology_contradiction_coupling.py` | Segment loads, transition pressure, momentum | segment coupling |
| `kme_bridge.py` | Topology from activation/KME graph; signal attach | KME↔TRIZ bridge |
| `direct_outputs.py` | `TRIZDirectMetrics`, `build_triz_direct_metrics` | direct metrics suite |
| `commercial_intelligence.py` | Commercial / comparative intelligence bundles | product slice |
| `hex_signals.py` | Hex pressure aggregate / peaks / volatility | hex signals |
| `signal_normalization.py` | Smoothing, z-score, min thresholds | normalization |
| `time_series.py` | Persistent contradiction/narrative/cluster history | time series |
| `meta_synthesis.py` | Cross-domain signal aggregate | meta |
| `guards.py` | Read-only / meta-area / adjacency immutability guards | safety |
| `exporters.py` | Policy/innovation/narrative/CSV exports | export |
| `report_builders.py` | Contradiction/innovation/narrative report dicts | reports |
| `report_extractors.py` | Pull TRIZ summary from `MetricReport` | reports |
| `triz_classifier.py` | (listed above) | — |

---

## Suggested wiki sub-batches (beyond Louvain)

| Sub-batch | Modules | Owner hint |
|-----------|---------|------------|
| **TRIZ-CONTRA** | `contradiction_*.py`, `crossplane_*`, `conflict_release_gating` | Colombo + Felix pins |
| **TRIZ-TOPO** | `topology_*`, `propagation_engine`, `narrative_routes` | Felix |
| **TRIZ-FAM** | `family_*`, `hex_signals` | Colombo |
| **TRIZ-PIPE** | `pipeline`, `triz_pipeline`, `kme_bridge`, `direct_outputs` | Felix |
| **TRIZ-PROD** | `commercial_intelligence`, `exporters`, `report_*`, `guards` | Felix / product |

Do **not** mark individual symbol pages DONE from this inventory alone — this file only opens the map.

---

## Evidence method

```bash
find /data/hesperia/hesperia/hesperia/extensions/triz -name '*.py' ! -path '*/__pycache__/*' | sort
# heads + rg '^(def |class )' per file — 2026-07-23 on altitudine
```

---

SIGNED: Developer (Felix) | TRIZ extensions inventory for wiki batch | 2026-07-23 | HWIKI-TRIZ-01
