# v0.4.1.3 — Families semantic canonicalization

Canonical source: `hesperia_lex/definitions/v0413/families.yaml`.

## Goals
- Replace v0412 scaffold text with mechanism-specific semantic definitions.
- Keep deterministic local validation (no network pools, no WordNet, no LLM synsets).
- Enforce overlap/duplication controls and mirror handling.

## Validation
```bash
python3 hesperia_lex/scripts/validate_families_yaml_v0413.py
```
Writes audit report to:
- `assets/v0413/families_semantic_audit_report.txt`

## Build Dict A v0.4.1.3
```bash
python3 hesperia_lex/scripts/build_dict_a_v0413_from_definitions.py
```
Output:
- `hesperia_lex/curated/A_CORE_STAR_MAP_v0_4_1_3.json`

Weights:
- central tier1 (first 2): `0.78`
- central tier2 (next 2): `0.62`
- central tier3 (remaining): `0.52`
- boundary: `0.35`
- structural label slug: `0.40` (up to 2)
