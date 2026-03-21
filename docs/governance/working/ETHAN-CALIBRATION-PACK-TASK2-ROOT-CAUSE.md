# Ethan — Calibration pack Task 2 — root cause (dead-zero structural / sealed)

**Date:** 2026-03-21  
**Symptom:** For RU transcripts with **zero lexicon marker hits** (`core.attribution.structural` on `lexicon/curated`), `01_structural_batch.json` showed `ATTRIBUTED_TOKENS=0`, `COVERAGE_RATIO=0`, near-zero trust, and `microcell_activation_map` sample slices all **0.0**, while `06_product_analyze.json` still showed full attribution (different pipeline: `analyze()` / v06 dense path).

## Chain

1. **`markers_to_concept_activation`** → `a_concept_counts` sum **0** (no Dict A/B landing for Cyrillic-heavy clinical text).
2. **`run_sealed_multiscale_stack`** applies **uniform** `1/288` concept prior when sum ≤ 0 → **A0** after PCH still has **total mass 1**.
3. **`step_hex_local_microphysics`** (energy-controlled, soft mode) proposed a **strongly negative** raw update; **η=1** clipped to **all zeros**, and **`energy_acceptable`** accepted it because **energy dropped** → **mass annihilation** treated as valid.
4. **Downstream:** `A1.sum()==0` → `F` and `area` **zero** → L1 from raw `matched` stays **zero**; hex samples round to **0.0**.

## Fixes (landed)

| Layer | Change |
|-------|--------|
| `hesperia/engine/hex_dynamics.py` | Reject line-search proposals that drive **total mass** below a floor when input mass is positive (prevents η=1 annihilation). |
| `hesperia/engine/sealed_multiscale_stack.py` | Track `marker_concept_mass`, `uniform_concept_prior_fallback_used`; **defensive** `hex_upstream_fallback_used` if `A1` still collapses while `A0` has mass (copy `A0` → `A1`). |
| `hesperia/engine/multiscale_product_bridge.py` | When L1 has **zero** attributed tokens but sealed **`family_activation_vector`** has mass, rebuild L1 via **largest-remainder** synthetic `matched` from that vector; set `CALIBRATION_FALLBACK_USED` + `diagnostics.calibration_status`. |

## Regression

`tests/test_runtime_spine_integrity.py::test_zero_marker_hits_hex_and_L1_not_silently_annihilated`

## Before / after (representative)

- **Before:** `hex_activation_map.total_mass == 0`, `L1.ATTRIBUTED_TOKENS == 0`.  
- **After:** `total_mass > 0`, `uniform_concept_prior_fallback_used == true`, `L1` populated with `CALIBRATION_FALLBACK_USED == "sealed_family_activation_to_L1"` when markers are empty.

**Note:** L1 after fallback reflects **calibrated alignment to sealed aggregates**, not raw lexicon matches — see `docs/specs/output_calibration_contract_v1.md`.
