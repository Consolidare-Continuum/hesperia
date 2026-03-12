<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# HESPERIA RAD — USF Schema and Fingerprint

## Rule

**USF schema changes require a version bump.** Otherwise structural fingerprint comparisons become meaningless.

## Schema and fingerprint

- **USF** (Unit Summary Format): canonical output of the pipeline; includes `usf_version`, `schema_version`, `raw_metrics`, `dynamism_metrics`, `propagation_metrics`, `logic_outputs`, `provenance`, and the structural **fingerprint** used for drift.
- **Fingerprint** (for comparison/drift): subset of USF state used by `sphere.usf.drift` and `sphere.usf.fingerprint_diff` — e.g. `structural_state`, `dominant_area_id`, `entropy_state`, `tension_state`, `propagation_state`, `active_events`. Drift formula and thresholds are defined in code and docs; changing them affects comparability.
- **Comparability**: Two USFs are comparable only if they share the same schema/version. Changing the shape or semantics of the fingerprint or of key USF fields without a version bump breaks drift and regression checks.

## When to bump

- Adding or removing top-level USF keys that are used for fingerprint or comparison.
- Changing the meaning or type of fingerprint keys.
- Changing the drift formula or thresholds in a way that invalidates existing baselines.

## RAD freeze

Schema and fingerprint are stable. Changes require design review and a version bump documented here or in the code (e.g. `usf_version`, `schema_version`).
