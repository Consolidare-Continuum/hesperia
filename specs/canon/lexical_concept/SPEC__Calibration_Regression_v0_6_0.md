<!--
HESPERIA — RAD. DLCR-HP canon fragment (INT-001).
-->

# SPEC: Calibration & regression gates — v0.6.0

**ID:** `HES-SPEC-DLCR-HP-REGRESSION`  
**Normative parent:** [SPEC__DLCR_HP_Master_v0_6_0.md](SPEC__DLCR_HP_Master_v0_6_0.md)

## Purpose

Block silent semantic drift: multi-corpus gold checks + CI (INT-008).

## Normative rules

- `tools/check_dlcr_regression.py` runs seed EN + TFP RU corpora in CI.
- Failures must name **corpus** and **case id**.

## Acceptance

- `python3 tools/check_dlcr_regression.py` exits **0** on pinned assets.
- `.github/workflows/sealed-runtime-gate.yml` invokes the regression checker.
