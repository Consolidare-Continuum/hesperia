# Grace triage — Hesperia promotion workflow (`v0_6_0_clr_v052_3`)

**Date:** 2026-03-30  
**Source:** Operator directive (controlled promotion, strict order)

## Mandatory execution order

1. Create sealed candidate path `assets/calibration/dicts/v0_6_0_clr_v052_3/` from filtered/approved artifacts.
2. Run evaluation in `REPORT` mode first (no direct jump to `FAIL`).
3. Compare drift vs A9 baseline and interpret GOOD/BAD drift.
4. Verify critical checkpoints:
   - `concept_activation_from_c_ratio`
   - `blocked_token_ratio`
   - dead-concept recovery (used concepts count)
5. Stage gates only after stable runs:
   - `OFF -> REPORT -> WARN -> FAIL`

## Hard constraints

- Do not overwrite frozen API-calibrated Dict A assets.
- Do not promote unfiltered `draft` artifacts directly.
- Promotion is validation of a new engine path, not only data replacement.

## Team split for this packet

- **Noah:** sealed path build from filtered approved subset.
- **Olivia:** REPORT-mode gate/eval pass with required metrics.
- **Gena:** runtime checkpoint metrics (`concept_activation_from_c_ratio`, `blocked_token_ratio`, phrase/token contributions).
- **Grace:** drift interpretation + staged gate recommendation.
- **Ethan:** final authorization for WARN/FAIL transition after stability evidence.

---

`SIGNED: Grace (triage) | Hesperia promotion workflow v052_3 | 2026-03-30 | operational/assignments`
