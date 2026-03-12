<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# HESPERIA archive — deprecated / moved out of operational repo

**Operational version:** v0.6 only. **Freeze:** v0.6.

Everything under `archive/` is deprecated or superseded. Kept for history and reference; not on the v0.6 code path.

## Layout

- `archive/scripts/` — v0.4/v0.5 calibration and verify; v060 compat; report runners; v040 shell scripts (canonicalize, freeze, build, checksum)
- `archive/sphere_rag/` — v0.5 attribution, dense projection, build_family_centroids_v05, verify_dense_projection_v05
- `archive/hesperia_lex/` — v0.5 FAMILY_ANCHORS, FAMILY_CENTROIDS, build_family_anchors_skeleton_v05
- `archive/docs/` — v0.4/v0.5 specs, runbooks, reports; docs/hesperia_runtime_output (old runs); docs/layer_runs
- `archive/api/` — v0.4 verify script, OPERATIONAL_SPEC action v0.4
- `archive/releases/` — v0.2, v0.4 release notes
- `archive/layer_runners/` — run_l1_through_l9, run_l1_l2, run_l1_l2_l3 (layer math code stays in sphere_rag/layers/)

## Operational v0.6 (not in archive)

See [docs/OPERATIONAL_SPEC_v0_6.md](../docs/OPERATIONAL_SPEC_v0_6.md) and root [OPERATIONAL_INDEX_v0_6.md](../OPERATIONAL_INDEX_v0_6.md).
