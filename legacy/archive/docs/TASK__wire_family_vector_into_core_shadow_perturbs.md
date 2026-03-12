<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Task: Wire family_vector into core; shadow perturbs vector

**Status:** Done (v0.5 core wiring)
**The only engineering step that now mattered:** Replace uniform seed initialization in core with dense family_vector.

## Minimal implementation

1. **Pass family_vector to core** (from attribution_v05 dense path).
2. **Normalize it** (e.g. L1 or L2 so it is a valid distribution).
3. **Use it as initial energy distribution** in core (replace uniform/placeholder seed).
4. **Shadow perturbs this vector pre-core** (so shadow acts on the input state, not after the fact).

Once that is done:
- Shadow deltas become real.
- Calibration dataset becomes meaningful.
- Tension dispersion becomes non-trivial.

Until then, shadow is dormant.

## Mechanical spec

1. **attribution_v05** (or caller) returns `family_vector`: 288 floats (sentence-level projection); optionally topK.
2. **Pipeline core** takes `family_vector` as initial state (normalized); no uniform seed.
3. **Shadow layer** perturbs `family_vector` (or derived transition weights) before core consumes it.

## Acceptance

- Same sentence, base vs shadow: at least one of governance / loopability / tension_energy / obstacle_score differs.
- Determinism preserved (fixed sentence → fixed base, fixed shadow).
