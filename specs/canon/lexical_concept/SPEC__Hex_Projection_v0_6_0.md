<!--
HESPERIA — RAD. DLCR-HP canon fragment (INT-001).
-->

# SPEC: L3 hex projection — v0.6.0

**ID:** `HES-SPEC-DLCR-HP-L3`  
**Normative parent:** [SPEC__DLCR_HP_Master_v0_6_0.md](SPEC__DLCR_HP_Master_v0_6_0.md)  
**Scale note:** [SPEC__72k_Phased_Scale_v0_6_0.md](SPEC__72k_Phased_Scale_v0_6_0.md)

## Purpose

**L3** maps concept weights to symbolic hex activations using anchor registry + topology helpers.

## Normative rules

- Concept evidence maps to hex **before** family/area aggregation (master).
- Symbolic IDs map into engine index space via `hex_index_map.json` and `core.hexmap.topology` (INT-005).

## Acceptance

- `core.hexmap.projection` + topology loaders covered by lexical_concept / hexmap tests.
- No code comment claims full **72k** lattice unless implemented; see phased-scale spec.
