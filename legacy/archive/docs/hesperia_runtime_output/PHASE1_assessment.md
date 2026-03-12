<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Phase 1 — Dense contrast lock (T=0.02, gamma=2.0, topK=0)

## Requested run: HESPERIA_TEMPERATURE=0.02, HESPERIA_GAMMA=2.0, HESPERIA_TOP_K=0

| Metric | Value | Target (healthy) |
|--------|--------|-------------------|
| **entropy_norm_mean** | 0.995 | 0.70 – 0.82 |
| **top1_mass_mean** | 0.0071 | 0.05 – 0.10 |
| **top5_mass_mean** | 0.032 | 0.20 – 0.35 |
| **governance_spread_range** | [0.283, 0.344] | — |

**One domain sample (conflict_power):**
- entropy_sharp_norm_mean: 0.992
- top1_mass_mean: 0.0086
- top5_mass_mean: 0.037
- mean_governance: 0.344

**Verdict:** Dense field is **not** in a healthy regime with gamma=2.0. Entropy is >0.85; top1 and top5 are below target.

---

## Check: gamma=1.0 with same T and topK=0

| Metric | Value | Target |
|--------|--------|--------|
| entropy_norm_mean | 0.812 | 0.70 – 0.82 ✓ |
| top1_mass_mean | 0.056 | 0.05 – 0.10 ✓ |
| top5_mass_mean | 0.189 | 0.20 – 0.35 (just below) |
| governance_spread_range | [0.391, 0.480] | — |

With **gamma=1.0**, the dense field **is** in the healthy regime for entropy and top1; top5 is slightly below 0.20.

**Conclusion:** For this centroid set, gamma=2.0 **flattens** the distribution (higher entropy, lower top1/top5). Use **HESPERIA_GAMMA=1.0** to hit Phase 1 targets, or treat persistent high entropy with gamma=2.5 as **anchor overlap** and refine centroids.

---

## Next-step guidance (from your spec)

- If entropy still > 0.85 after gamma=2.5: problem is **anchor overlap**; compute centroid cosine similarity, find families >0.85, refine anchors.
- Do not jump to topK until dense is stable. With gamma=1.0, dense is stable; with gamma=2.0, either lower gamma to 1.0 or move to gamma=2.5 and re-measure before adding topK.

Artifacts: `calibration_metrics_v05_phase1.json` (gamma=2), `calibration_metrics_v05_T02_g1.json` (gamma=1).
