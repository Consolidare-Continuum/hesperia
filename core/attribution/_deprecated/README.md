# Deprecated attribution modules

Modules in this directory are retired — zero production importers as of the 2026-07-30 canon-matrix
consolidation pass (see `docs/archive/ARCHIVE-MANIFEST.md`). Kept for reference/history only, not
for reuse or reverse-engineering.

- `lexical_loader.py` — oldest generation (Spec-20 v0.3). Loaded `A_CORE_STAR_MAP_v0_4_1_1.json` +
  `B_SURFACE_LEX_FIELD_v1.json` (now archived under `lexicon/curated/_deprecated/`).
- `attribution_compat.py` — a deprecation shim re-exporting from `core.attribution.structural`.
  Already stale advice by the time it was retired: `structural` was never the sole canonical
  module either, just one of three live paths.

Live attribution modules: `core.attribution.attribution` (v0.6, production default),
`core.attribution.attribution_shared` (v0.3.3 fallback + r1_r4 surface-map capability),
`core.attribution.structural` (r1_r4 non-surface-map branch + `exclude_landing_sources` guard).

See [docs/foundations/attribution_layer.md](../../../docs/foundations/attribution_layer.md) for
the full picture.
