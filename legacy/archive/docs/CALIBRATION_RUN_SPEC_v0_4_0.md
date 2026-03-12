<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# HESPERIA v0.4.0 — Calibration Run Spec

**Version:** 0.4.0
**Purpose:** Structural behavior calibration. Not correctness testing.

## Objective

Measure:

- **Determinism stability**
- **Coverage distribution**
- **Dominance volatility**
- **Base vs Shadow divergence**
- **Metric dispersion** across semantic domains

## Phase 1 — Dataset

- **100 short sentences**, controlled, domain-separated.
- **20 sentences per domain × 5 domains.**
- Domains: Social cohesion | Conflict/Power | Economic/Exchange | Identity/Culture | Technical/Systems.
- Each sentence: 8–15 tokens, 2–4 domain keywords, minimal fluff, no sarcasm, declarative.
- Dataset: `calibration/data/calibration_100_sentences.json`.

## Phase 2 — Run Protocol

For each of 100 sentences:

1. **Run 1:** Base mode (`shadow_enabled=False`)
2. **Run 2:** Shadow enabled (`shadow_enabled=True`)

**Collected per run:**

- `dominant_area`, `dominant_family`
- `governance`, `loopability`, `tension_energy`, `obstacle_score`
- `matched_tokens`, `coverage` (attribution_coverage)

**Output:** One parsable file (JSONL). One JSON object per line. Total runs = 200.

**Determinism check:** 5 random sentences × 10 runs each (base only). Same JSONL; field `determinism_run: true`, `repetition`: 1..10. Total +50 lines.

## Phase 3 — Metrics to Compute (post-run)

- **A. Determinism:** 5 sentences × 10 runs → expect exact match across runs.
- **B. Coverage distribution:** Mean, median, min/max, % with coverage < 0.25.
- **C. Dominance stability:** % sentences where base vs shadow change `dominant_family` / `dominant_area`. If >25%, shadow too aggressive.
- **D. Metric dispersion:** Per metric (governance, loopability, tension_energy, obstacle_score): mean, std, range. Avoid tight clustering.
- **E. Gap detection:** Sentences with coverage > 0.4 but tension ≈ 0 or dominance tie cases → structural flatness.

## Phase 4 — Shadow Differential

For each sentence: `delta_governance`, `delta_loopability`, `delta_tension`, `delta_obstacle`. Mean delta, std delta, outliers. Shadow should slightly increase dispersion, not invert domains randomly.

## Phase 5 — Calibration Questions

- Is coverage acceptable?
- Is dominance meaningful or mostly tie-break artifact?
- Are governance and loopability discriminating?
- Is shadow adding structural insight or just noise?
- Which domain has weakest activation?

## Implementation

- **Runner:** `scripts/run_calibration_v040.py`. Loop sentences, call `analyze_v033` base then shadow, append one JSON per run to JSONL. No UI. Pure data.
- **Output path:** `docs/hesperia_runtime_output/calibration_run.jsonl` (override with `--output path`).
- **Dataset:** `calibration/data/calibration_100_sentences.json` (100 items: id, domain, text).
- **Autorun:** From `CLIENTS/hesperia`: `PYTHONPATH=. python3 scripts/run_calibration_v040.py`. Optional: `--no-determinism` to skip 5×10 runs; `--seed 42` for reproducible determinism sample.
- **Interpretation:** Only distributions. Calibration is statistical, not anecdotal.
