# HESPERIA v0.5.1 — Temperature Sharpening Layer

**Objective:** Reduce entropy of family_vector and increase domain contrast without breaking determinism.

## Where it applies

Inside dense path: after computing value_f = pos_sim − neg_sim; before entropy measurement, reduction to 5 buckets, shadow perturb.

**Order:** Dense projection → temperature sharpen → optional shadow perturb → reduce_288_to_5 → core.

## Formula

1. v_f = clamp(pos_sim − neg_sim, -1, 1)
2. m_f = |v_f|, s_f = sign(v_f)
3. w_f = exp(min(m_f/T, 50)) / Σ exp(min(m_i/T, 50))
4. v_f_sharp = s_f * w_f

T default 0.15; override via `HESPERIA_TEMPERATURE`. Cap 50 prevents exp overflow.

## Guarantees

Deterministic; no randomness, dropout, or stochastic ordering.

## Calibration expectations

- entropy_norm_mean: drop from 0.95–0.97 toward 0.65–0.80
- Domain means spread more; shadow delta magnitude increases slightly
- If entropy > 0.9: T too high. If < 0.4: T too low (over-sparse).

**Operational tuning (2026-02-24):** With default T=0.15, entropy stays ~0.996 (no drop). To reach target band 0.65–0.80 set `HESPERIA_TEMPERATURE=0.02`. T=0.04 gives ~0.94; T=0.08 ~0.98. See `docs/hesperia_runtime_output/REPORT__v051_calibration_temperature.md`.

## Implementation

- `dense_projection_v05.temperature_sharpen(v, T)` + `get_temperature()`
- `attribution_v05`: after _sentence_vector_dense, call temperature_sharpen; expose family_vector (sharp) and family_vector_pre_sharpen (raw) in extended.
