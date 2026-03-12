<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# HESPERIA v0.5 — Meaningful calibration tasks

Only three calibration tasks matter:

1. **Run full 100×2 dataset** and compute:
   - mean governance per domain
   - mean tension per domain
   - shadow delta magnitude per domain

2. **Measure entropy of family_vector before reduction.**
   If entropy is always low → anchors are too narrow.
   (Max H ≈ log(288) ≈ 5.67; normalized = H / log(288).)

3. **Output:** One report (JSON) with per-domain metrics and entropy stats.

## Script

`scripts/calibration_metrics_v05.py`

- Loads `calibration/data/calibration_100_sentences.json` (100 sentences, 5 domains).
- Runs each sentence in **base** and **shadow** (dense mode).
- Collects: governance, tension_energy, family_vector (for entropy).
- **Per domain:** mean_governance, mean_tension, mean_shadow_delta_governance, mean_shadow_delta_tension, shadow_delta_magnitude, family_vector_entropy_mean/min/max, family_vector_entropy_normalized_mean.

## Run

From `CLIENTS/hesperia`:

```bash
HESPERIA_ATTRIBUTION_MODE=dense PYTHONPATH=. .venv_v040_build/bin/python scripts/calibration_metrics_v05.py [--output path]
```

**Output:** `docs/hesperia_runtime_output/calibration_metrics_v05.json` (default).

## Interpretation

- **Entropy normalized ≈ 0.95+** → family_vector well spread; anchors not narrow.
- **Entropy normalized &lt; 0.5** → concentration in few families; consider broadening anchors.
- **Shadow delta magnitude** → how much shadow perturbs metrics per domain; should be &gt; 0 when core is wired.
