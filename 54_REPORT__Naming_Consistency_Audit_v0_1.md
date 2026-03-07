# 54_REPORT__Naming_Consistency_Audit_v0_1

Date: 2026-03-07  
Scope: repository-wide quick consistency pass for terminology, file naming, code naming, and Markdown variable/definition coverage.

## 1) Terminology consistency (HESPERIA vs legacy HISPERIA)

### Findings
- Active root specs and operational docs mostly use **HESPERIA**.
- Legacy snapshots in `v0.1/` and `archive/v0.1/` still contain **HISPERIA** spellings. This is expected historical content.
- A few user-facing titles still include mixed casing or natural-language long names (e.g., tutorial/report docs).

### Recommendation
- Keep legacy `HISPERIA*` filenames unchanged in `archive/` and `v0.1/`.
- For future docs, standardize on `HESPERIA` in file titles and body text.

## 2) File naming consistency against ORDER.md

### Findings
- The repository currently follows a mixed model:
  - canonical numbered specs using `NN_CATEGORY__Title_vX_Y.*`
  - operational docs with short non-versioned names (`README.md`, `ORDER.md`, etc.)
  - legacy and archive files with historical names.
- There are many existing exceptions to strict "up to 4 words + version" if applied mechanically.

### Recommendation (best-practice migration path)
1. Keep currently referenced canonical files stable (do not mass rename in one pass).
2. Apply strict ORDER naming for **all new files**.
3. Plan staged renames with compatibility index updates (`DOC_INDEX.md`) for high-traffic docs.

## 3) Code naming consistency check (Python)

### Findings
- General convention is `snake_case` for modules/functions/variables.
- A small set of local temporary variables in math modules still use camel-like names (`sumS`, `sumL`, `sumE`, `sumD`, `gapF`, `sumE0`, `sumE_end`) concentrated in:
  - `sphere_rag/core_math.py`
  - `sphere_rag/hesperia_v03_core_math.py`
  - `sphere_rag/full_run_simulation.py`

### Recommendation
- Keep runtime behavior unchanged.
- In a dedicated follow-up refactor, rename temporary variables to snake_case only where safe and covered by tests.

## 4) Markdown variable coverage (.md)

### Action completed
- Expanded `VARIABLES.md` runtime variable table with additional environment variables discovered in code paths (attribution mode, model revision pin, lexical provenance tags, transformer backend toggles).
- Expanded alias list in `VARIABLES.md` with additional Markdown hashtag variables currently used in docs/specs.

### Outcome
- `VARIABLES.md` now provides better cross-reference between runtime env vars and academic/spec alias surface.

## 5) ACADEMIC definition surface check

### Findings
- `ACADEMIC.md` provides broad canonical definitions for geometry, attribution, loopability, governance, and threshold vocabulary.
- Definitions and hashtag variables are now aligned with an expanded alias list in `VARIABLES.md`.

### Recommendation
- Keep `ACADEMIC.md` as semantic definition source.
- Keep `VARIABLES.md` as practical variable index and compatibility map.
- Update both in the same PR whenever new governance/metric symbols are introduced.
