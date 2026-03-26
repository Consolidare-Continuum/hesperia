# TASK GEO-02 — API schema cleanup + product-safe docs rewrite

**Status:** OPEN — phased, compatibility-first.  
**Primary objective:** remove geometry-leaking public terminology from schema/doc surfaces while preserving runtime behavior and client compatibility.  
**Proceed log:** [ETHAN-OPEN-WORKFLOW-PROCEED.md](ETHAN-OPEN-WORKFLOW-PROCEED.md)

---

## 0. Scope gate (mandatory)

This task is **surface decontamination** (API/docs language), not a blind core-engine rename.

- Allowed first: schema keys/descriptions/examples, API docs, product/dev docs, compatibility adapters.
- Blocked without separate sign-off: package/component path renames, canonical topology identifiers in sealed internals, frozen artifacts.

If a replacement would break imports, public contracts, or release artifacts, route it to a dedicated migration task with aliases and versioning.

---

## 1. Objective

Phase 2 deliverables:

1. API schema/public contract terminology cleanup (operational language).
2. Backward compatibility layer for legacy request/response keys.
3. Product-safe docs rewrite (function/measurement/topology language).
4. Audit/validation outputs for deterministic review.

Required outputs:

- `api_schema_cleanup_report.json`
- `api_schema_rename_map.json`
- `api_schema_validation_report.json`
- `docs_rewrite_report.json`
- `docs_rewrite_validation_report.json`
- `docs_internal_marking_report.json`
- `geometry_decontamination_phase2_summary.md`

---

## 2. Approved replacement map (representational usage)

| Legacy | Canonical |
|--------|-----------|
| hex / hexagon | unit |
| hexes / hexagons | units |
| sphere | domain |
| spherical | domain-based |
| loop | cycle |
| geometry / geometric | topology / structural |
| mesh / lattice | topology |
| coordinate | index |
| coordinates | indices |
| distance | interaction_score |
| neighbors / neighbour | related_units |
| grid | layout |

Do not force replacements where usage is genuinely mathematical, graphical, or unrelated to Hesperia semantic representation.

---

## 3. Part A — API schema cleanup

### Targets

- `openapi*.json`, `openapi*.yaml`
- `*.schema.json`
- `schemas/**/*.json`, `schemas/**/*.yaml`
- `api/**/*.py`, `server/**/*.py`, `routes/**/*.py`
- docs carrying API examples (`docs/**/*.md`, `README*.md`, `SPEC*.txt`, `*.md`)

### Script

Create:

- `tools/api_schema_cleanup.py`

Required CLI:

- `python3 tools/api_schema_cleanup.py` (dry-run)
- `python3 tools/api_schema_cleanup.py --apply`
- `python3 tools/api_schema_cleanup.py --validate`

### Behavior

- Detect leaking terms in:
  - key names
  - title/description text
  - enums
  - examples/snippets
- Classify findings:
  - `key_rename`
  - `description_rewrite`
  - `unsafe_no_change`
- In `--apply` mode:
  - rewrite safe keys/text
  - generate rename map + cleanup report
- In `--validate` mode:
  - assert no unresolved public leakage in target scope

### Backward compatibility (required)

Create if missing:

- `hesperia/io/schema_aliases.py`

With helpers:

- `LEGACY_TO_CANONICAL = {...}`
- `normalize_legacy_keys(payload: dict) -> dict`
- `emit_compat_keys(payload: dict, include_legacy: bool = False) -> dict`

Use recursively for nested dict/list payloads.

Public API changes must accept legacy raw_text aliases and provide optional legacy output compatibility mode where practical.

---

## 4. Part B — docs rewrite (product-safe language)

### Script

Create:

- `tools/rewrite_docs_product_safe.py`

Required CLI:

- `python3 tools/rewrite_docs_product_safe.py`
- `python3 tools/rewrite_docs_product_safe.py --apply`
- `python3 tools/rewrite_docs_product_safe.py --validate`

### Priority

1. `README.md`
2. `docs/**/*.md`
3. `SPEC*.txt`, `PROJECT*.md`, `PITCH*.md`, `presentation/**/*.md`

### Rules

- Rewrite sentence/phrase-level (not only blind word-swap).
- Prefer operational clarity: function, bounded coupling, deterministic mapping, auditability.
- Keep internal-only research wording only where necessary and mark file header:
  - `INTERNAL MODEL NOTE: This document uses internal representational terminology not intended for product/API language.`

---

## 5. Exclusions and safety

Do not rewrite inside:

- `.git/`, `assets/`, `build/`, `dist/`, `calibration_runs/`, `legacy/`, `release/`, vendored code, binaries.

Do not break:

- import paths
- class names (unless explicitly migrated with compatibility)
- serialized artifact compatibility
- unrelated tests
- genuine mathematical formulas in internal research materials

---

## 6. Validation sequence

1. Dry run:
   - `python3 tools/api_schema_cleanup.py`
   - `python3 tools/rewrite_docs_product_safe.py`
2. Apply:
   - `python3 tools/api_schema_cleanup.py --apply`
   - `python3 tools/rewrite_docs_product_safe.py --apply`
3. Validate:
   - `python3 tools/api_schema_cleanup.py --validate`
   - `python3 tools/rewrite_docs_product_safe.py --validate`

---

## 7. Acceptance criteria

Phase 2 is complete only if:

- public API schemas no longer expose geometry leakage (within approved exclusions),
- docs describe operation and measurable behavior, not internal visual metaphors,
- backward compatibility exists for major renamed keys,
- validation reports are green with explicit residual exceptions (if any),
- final summary exists: `geometry_decontamination_phase2_summary.md`.

Commit message (when completed scope is ready):

- `refactor: clean API schemas and rewrite docs with product-safe terminology`

---

*Ethan — GEO-02 API/schema/docs decontamination task spec.*
