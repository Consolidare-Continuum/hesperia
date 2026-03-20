<!--
HESPERIA — RAD. DLCR-HP canon fragment (INT-001).
-->

# SPEC: Dict B (concept identity) — v0.6.0

**ID:** `HES-SPEC-DLCR-HP-DICT-B`  
**Normative parent:** [SPEC__DLCR_HP_Master_v0_6_0.md](SPEC__DLCR_HP_Master_v0_6_0.md)

## Purpose

Dict **B** defines concept identity, linkage, and structural metadata used for resolution and hex projection.

## Normative rules

- Concept rows validate against `schemas/lexical_concept/dict_b.schema.json`.
- Winning concept IDs drive hex activation before family/area aggregation (master §Layer stack).

## Acceptance

- Validator `tools/validate_dict_b_dlcr.py` exits **0** on pinned packs.
- Resolver consumes Dict B rows keyed by `concept_id`.
