# TASK — v0.4.1.3 Families Semantic Canonicalization

Status: implemented.

## Delivered artifacts
- `hesperia_lex/definitions/v0413/families.yaml` (288 canonical family entries with semantic fields).
- `hesperia_lex/definitions/v0413/validate.py` (semantic validator + deterministic audit report generation payload).
- `hesperia_lex/scripts/validate_families_yaml_v0413.py` (CLI validator; emits audit report).
- `hesperia_lex/scripts/build_dict_a_v0413_from_definitions.py` (Dict A builder with v0413 weights and 12 anchors/family).
- `assets/v0413/families_semantic_audit_report.txt` (generated report).
- `hesperia_lex/curated/A_CORE_STAR_MAP_v0_4_1_3.json` and frozen copy/hash.

## Review workflow
1. Edit `families.yaml` only (single canonical file).
2. Run validator.
3. Inspect `assets/v0413/families_semantic_audit_report.txt`:
   - per-area overlap maxima,
   - global duplicate token hot spots,
   - mirror pairs,
   - per-family central/boundary/structural counts.
4. Rebuild Dict A and confirm deterministic hash.

## Editor guide (short)
- Keep `core_definition` concise: scope + mechanism + boundary.
- Use single-token example anchors only.
- Keep central anchors family-specific; avoid generic global tokens.
- Keep mirror families explicitly connected via `mirrors` and distinct definitions.
- Use `notes` for deterministic editorial rationale.
