<!--
HESPERIA — RAD. DLCR-HP canon fragment (INT-001).
Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.
-->

# SPEC: Dict A (lexical evidence) — v0.6.0

**ID:** `HES-SPEC-DLCR-HP-DICT-A`  
**Normative parent:** [SPEC__DLCR_HP_Master_v0_6_0.md](SPEC__DLCR_HP_Master_v0_6_0.md)

## Purpose

Dict **A** proposes lexical candidates from normalized text. It must **not** directly assign family or area.

## Normative rules

- Phrase-first matching, then token fallback (master §Core invariants).
- Entries validate against `schemas/lexical_concept/dict_a.schema.json`.
- Dict A output feeds L2 resolution only.

## Acceptance

- Validator `tools/validate_dict_a.py` exits **0** on pinned packs.
- No Dict A field encodes sole family/area classification as the default path.
