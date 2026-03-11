# Historical reference (pre-refactor)

# TASK__v0412_FAMILIES_DEFINITION_CANONICAL_FILE

**Target**: v0.4.1.2
**Scope**: Replace pool-driven semantics with canonical definition-driven semantics
**Artifact**: Single authoritative YAML file

## Status

Implemented. Canonical source: `hesperia_lex/definitions/v0412/families.yaml`. Builder and validator in `hesperia_lex/scripts/`.

## Canonical file

- **Location**: `hesperia_lex/definitions/v0412/families.yaml`
- Only authoritative semantic definition source. No per-family YAML files. No per-area pools. No duplicate sources.

## File structure

- `version`: "v0.4.1.2"
- `total_families`: 288
- `families`: list of entries with `family_id`, `area_id`, `label`, `core_definition`, `positive_axis`, `negative_axis`, `excluded_neighbors`, `central_examples`, `boundary_examples`

## Validation (build fails if violated)

- Any family missing; duplicate `family_id`; `central_examples` < 3; `boundary_examples` < 2; label mismatch with `31_FAMILIES__area_family_table_full.txt`; any multi-word phrase in examples (contains space).

## Usage

- **Validate**: `python3 hesperia_lex/scripts/validate_families_yaml_v0412.py`
- **Build Dict A**: `python3 hesperia_lex/scripts/build_dict_a_v0412_from_definitions.py` → `hesperia_lex/curated/A_CORE_STAR_MAP_v0_4_1_2.json`
- **Generate stub from table**: `python3 hesperia_lex/scripts/generate_families_yaml_v0412.py`

## Builder process

Load `families.yaml` → validate schema → derive anchors from central + boundary examples → apply weight policy → merge structural fallback (≤4) → emit Dict A (legacy list format: `side_id`, `weight`, `map_code`).
