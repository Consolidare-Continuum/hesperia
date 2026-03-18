# TRIZ product CLIs (Series 3)

Run from repository root:

```bash
python3 tools/triz/run_policy_detector.py --corpus benchmarks/triz/corpus_policy_polarized
python3 tools/triz/run_innovation_radar.py --corpus benchmarks/triz/corpus_innovation_sparse
python3 tools/triz/run_narrative_monitor.py --corpus benchmarks/triz/corpus_narrative_spillover
```

Demo pack generation:

```bash
python3 demo/triz/make_demo_reports.py
```

SKUs: `HSP-TRIZ-P1` (policy), `HSP-TRIZ-I1` (innovation), `HSP-TRIZ-N1` (narrative).
