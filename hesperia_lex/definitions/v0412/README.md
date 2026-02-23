# v0.4.1.2 — Canonical family definitions

**Single authoritative source**: `families.yaml`

- No per-family YAML files. No per-area pools. No duplicate sources.
- **Validate**: `python3 hesperia_lex/scripts/validate_families_yaml_v0412.py` (from `CLIENTS/hesperia`)
- **Build Dict A**: `python3 hesperia_lex/scripts/build_dict_a_v0412_from_definitions.py` → `hesperia_lex/curated/A_CORE_STAR_MAP_v0_4_1_2.json`
- **Generate stub from table**: `python3 hesperia_lex/scripts/generate_families_yaml_v0412.py` (overwrites `families.yaml`)

Validation rules: schema; label match to `31_FAMILIES__area_family_table_full.txt`; central_examples ≥ 3; boundary_examples ≥ 2; no multi-word in examples; family_id 1–288 unique; area_id 1–12.
