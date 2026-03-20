<!--
HESPERIA — RAD. DLCR-HP scale contract (INT-006).
-->

# SPEC: 72k substrate — phased scale (v0.6.0)

**ID:** `HES-SPEC-DLCR-HP-72K-PHASED`  
**Related:** `docs/TOPOLOGY_INVARIANTS.md` (10+2 areas, family grid), master spec.

## Purpose

Clarify the relationship between DLCR **bounded** hex maps (`HX-*` anchors + `hex_index_map.json`) and the full **~72k** hex substrate used by the wider engine.

## Normative statement

- **v0.6.0 implementation:** DLCR operates on a **bounded** symbolic hex registry and integer cell indices derived from `hex_index_map.json`. This is **not** a claim of full 72k lattice traversal per token.
- **Phased expansion:** Full-grid alignment (sharding, complete addressing) is a **future phase** gated by explicit spec + code; until then, docs and comments must not imply exhaustive 72k projection in the DLCR path.

## Acceptance

- Code comments in `core/hexmap` / pipeline refer to **bounded** or **mapped** indices where appropriate.
- This file is linked from hex projection spec and integration runbook.
