<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Report — L1–L9 full pass (script math)

**Date**: 2026-02-24
**Script**: `python3 -m sphere_rag.layers.run_l1_through_l9`
**Owner**: Gena

## Output log dir (link path)

**Path**: [CLIENTS/hesperia/docs/layer_runs/](.)

- **Latest run JSON**: [latest_L1_L9_output.json](latest_L1_L9_output.json)
- **This report**: [REPORT__L1_L9_Full_Pass.md](REPORT__L1_L9_Full_Pass.md)

From repo root: `CLIENTS/hesperia/docs/layer_runs/`
From CLIENTS/hesperia: `docs/layer_runs/`

## One full pass summary

| Item | Value |
|------|--------|
| Run | L1_through_L9 |
| Text (preview) | justice lie fairness truth good order harm freedom |
| L1 COVERAGE_RATIO | 0.125 |
| L1 DOMINANT_FAMILY_ID | 15 |
| L2 TOTAL_REACHABLE_NODES | 17 |
| L7 DECISION_STATUS_CODE | 0 |
| L7 OUTPUT_TRUST_TAG | LOW |
| L9 BRAND_WORD_TRUST | FRAGILE |
| L9 BRAND_WORD_EVIDENCE | UNSUPPORTED |
| L9 BRAND_WORD_GEOMETRY | CONTAINED |

All nine layers executed; output logged to `latest_L1_L9_output.json`. Reportable: L7 status/tag, L9 brand words. DECISION_STATUS_CODE 0 = OK path; LOW tag and FRAGILE/UNSUPPORTED due to no retrieval (empty R_B/R_S) and zero evidence support — expected for stub run.

**SIGNED: Gena | Hesperia L1–L9 full pass | 2026-02-24 | output log dir + report**
