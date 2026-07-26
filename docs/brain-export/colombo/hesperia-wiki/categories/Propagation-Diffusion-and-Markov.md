# Propagation, Diffusion and Markov

[← wiki home](../index.md)

**How to read this map (HWIKI-DOC-29):** Propagation is *diffusion on neighborhoods* — YAML radial weights (center→inner→middle→outer + bridge) feed how mass spreads; [Transition matrix (W)](../pages/Transition-matrix-W.md) + [λ](../pages/lambda-lazy-step.md) are the Markov-like walk; [Chapman-Kolmogorov Multi-Step](../pages/Chapman-Kolmogorov-Multi-Step.md) and [Mixing Diagnostics](../pages/Mixing-Diagnostics.md) are multi-step diagnostics. PageRank is a [structural analogy](../pages/PageRank-shaped-walk-structural-analogy.md) only.

| Item | Status | Type |
|---|---|---|
| [bridge_weight](../pages/bridge-weight.md) | LIVE_FULL | Parameter (YAML weight) |
| [center_to_inner](../pages/center-to-inner.md) | LIVE_FULL | Parameter (YAML weight) |
| [Chapman-Kolmogorov Multi-Step](../pages/Chapman-Kolmogorov-Multi-Step.md) | BEYOND | Formula / function |
| [decay_factor (propagation)](../pages/decay-factor-propagation.md) | PARTIAL | Parameter (YAML weight) |
| [inner_to_middle / middle_to_inner](../pages/inner-to-middle-middle-to-inner.md) | LIVE_FULL | Parameter (YAML weight) |
| [middle_to_outer / outer_to_middle](../pages/middle-to-outer-outer-to-middle.md) | LIVE_FULL | Parameter (YAML weight) |
| [Mixing Diagnostics](../pages/Mixing-Diagnostics.md) | BEYOND | Formula / function |
| [Transition matrix (W)](../pages/Transition-matrix-W.md) | BEYOND | Data structure / formula |

