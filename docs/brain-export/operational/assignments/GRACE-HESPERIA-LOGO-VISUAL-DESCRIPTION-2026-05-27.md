# Grace — Hesperia logo canonical visual description (stored)

**Date:** 2026-05-27  
**Operator intent (igareosh):** Store HESPERIA logo canonical visual description **v1** and **v1.2** in Hesperia project documentation; prepare image-set ingestion manifest.

**Canonical location (dev repo only):** `igareosh/hesperia` on alunel — `/data/workspaces/atomic-commit-hesperia`

| Artifact | Path |
|----------|------|
| Index | `docs/brand/logo/README.md` |
| Description v1 | `docs/brand/logo/HESPERIA_LOGO_CANONICAL_VISUAL_DESCRIPTION_v1.md` |
| Description v1.2 (plain language) | `docs/brand/logo/HESPERIA_LOGO_CANONICAL_VISUAL_DESCRIPTION_v1_2.md` |
| Image-set manifest | `assets/brand/logo/logo_image_set_manifest.yaml` |
| Image drop folder | `assets/brand/logo/images/` (`.gitkeep` until assets land) |

**Brain:** pointers only — [CLIENTS/hesperia/README.md](../../CLIENTS/hesperia/README.md) updated.

**Ingestion (2026-05-27):** Operator drop `.cache_to_sort_out` sorted into dev repo.

| Item | Status |
|------|--------|
| `ingestion_status` | `ready` |
| Canonical v1 baseline | `assets/brand/logo/images/canonical/hesperia_logo_v1_baseline.png` |
| Monochrome exploration | `images/exploration/monochrome/` (6 files) |
| Colored deferred | `images/exploration/colored_deferred/` (5 files; `sketch_colored_2` duplicate dropped) |
| Brain cache | `.cache_to_sort_out/` cleared — see folder README |

**Policy:** Canonical lockup = monochrome v1 only; neon/cyan–magenta explorations **not** brand lockup until operator review.

**Out of scope:** SVG vector trace; Chroma bulk ingest (Abelard if/when scheduled).

`SIGNED: Grace (triage/storage) | Hesperia logo image ingest | 2026-05-27 | dev repo assets + manifest`
