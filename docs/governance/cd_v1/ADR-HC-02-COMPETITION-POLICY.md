# ADR — HC-02 Unified competition policy (CD Phase 2)

## Context

Operator CONTROL SPEC §2 and CD `co_occurs` must not double-apply. **Single** suppression surface: CD executor Phase 2.

## Decision

- **Default mode:** `winner_takes_most` (not hard_winner).
- **Winner:** `i* = argmax_j score_j` within competition scope (family-local / contradiction cluster / equivalence band — scope from CD row metadata when present).
- **Adjusted scores:** `adjusted_i = score_i * s(r_i)` where `r_i = score_i / score_{i*}` and `s` is monotone:
  - `s(1) = 1`
  - `s(r) = 0.25 + 0.35 * r` for `r < 1` (example band; final constants in `cd_calibration_vN`).
- **Tie-break (determinism):** lexicographic `concept_id` ascending when scores equal within ε.

## Consequences

- Must document ε and tie-break in executor alongside `co_occurs` formula (see `CO_OCCURS_MATH_PHASE2.md` when merged).

`SIGNED: Marcus (task HC-02) | ADR competition | 2026-03-27 | Hesperia repo`
