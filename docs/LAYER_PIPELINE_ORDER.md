<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# HESPERIA RAD — Layer Pipeline Order

The pipeline executes layers in **strict order**. The runtime registry must match this order.

| Layer | Role |
|-------|------|
| **L1** | Semantic / coverage: token attribution, coverage ratio, dominance, entropy, Gini, area spread. |
| **L2** | Dict activation / traversal: stub adjacency, visited IDs, reach ratio, clustering, cross-area, loops. |
| **L3** | Structural shadow: baseline vs shadow comparison, deltas, acceptability gate. |
| **L4** | Topology: retrieval, evidence, area vector, family→area, adjacency, area sequence. |
| **L5** | Math / reality gates: anti-region, contradiction pressure, trig/geometry residuals. |
| **L6** | Dynamism: trajectory, transition matrix, curvature, jump rate, Lyapunov, stability score. |
| **L7** | Propagation: consistency gates, trust tier, decision status, output trust tag; consumes Δ stability. |
| **L8** | Shadow (scale-invariant): SI metrics, policy mode, interpretation scope. |
| **L9** | Logic: bands, pillars, BRAND_WORD_*, actions. |
| **L10** | Interpretation: structural state, entropy/tension/propagation state, active events, flags (used by USF). |

## Registry contract

- Layers are registered in a single ordered sequence: L1 → L2 → … → L9.
- L10 is applied after L9 (interpretation) in the canonical pipeline; it is not a core layer module but sphere interpretation.
- No reordering without design review and update to this document.
