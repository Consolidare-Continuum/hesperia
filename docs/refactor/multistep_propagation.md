# Multi-step propagation

## Single-step vs multi-step propagation

- **Single-step (default):** Layer-7 applies one diffusion step: `v' = (1 - α) v + α (v @ W)`, then L1-normalizes and projects to families. This is the default (`num_steps=1` or `propagation_steps=1`).
- **Multi-step:** For each step, the following sequence is applied explicitly:

  ```
  for step in range(num_steps):
      vector = diffuse(vector)
      vector = normalize(vector)
      vector = apply_damping(vector)
  ```
  Family projection is applied **only after the final step**.

  Constraints:
  - Normalization after each step.
  - Damping applied every step (default `damping_factor=1.0` = identity).
  - Family projection only after the final step.

  Config: `propagation_steps` (integer ≥ 1); default remains 1.

## When deeper diffusion is useful

- **Wider spread:** More steps allow mass to spread farther along the topology (e.g. across more areas). Useful when you want to model longer-range influence.
- **Stability analysis:** Comparing 1-step vs N-step results can reveal how quickly structure stabilizes under repeated diffusion.
- **Experimentation:** Optional extension for research or tuning without changing default behavior.

## Why it remains optional

- **Canonical behavior:** The reference pipeline and USF are defined with single-step propagation. Multi-step is an extension.
- **Performance:** More steps mean more matrix-vector products; default keeps cost minimal.
- **Interpretability:** Single-step has a clear reading; multi-step may blur direct attribution. Keeping it optional preserves a single canonical interpretation.

Implementation: `sphere.propagation.engine.compute_propagation(..., num_steps=1, damping_factor=1.0)`. Pipeline passes `config.get("propagation_steps", 1)`. Damping is applied each step; default 1.0 preserves mass.
