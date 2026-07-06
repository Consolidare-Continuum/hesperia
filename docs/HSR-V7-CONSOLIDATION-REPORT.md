# Hesperia consolidation report

Date: 2026-07-06

## Completed

- Synced root `VERSION.yaml` and `hesperia/VERSION.yaml`.
- Moved active calibration default to `v0_6_0_clr_v052_5`.
- Marked `archive_063_minimal` as archive-only placeholder metadata.
- Updated version loaders to resolve from repo root first and packaged copy second.
- Replaced hardcoded `0.6.0` fallbacks in runtime/package metadata with `0.6.5`.
- Renamed pipeline metadata constant away from `ENGINE_VERSION`.
- Added metrics-file resolution with fallback support for baseline metrics files.
- Added repository truth navigation docs.
- Updated stale v7 source-truth verification text.
- Renamed `docs/SOURCE_OF_TRUTH.md` to `docs/HSR-V7-SOURCE-TRUTH.md`.
- Renamed `docs/CONSOLIDATION_REPORT.md` to `docs/HSR-V7-CONSOLIDATION-REPORT.md`.
- Moved `docs/brain-export/README.md` to `docs/archive/brain-export/README.md`.
- Added `docs/archive/ARCHIVE-MANIFEST.md` and `docs/archive/HSR-V7-CONSOLIDATION-INVENTORY.md`.

## Notes

- Historical payloads under `docs/brain-export/archive/` remain in place for a later prune/move pass.
- The repo now prefers the complete calibration pack for active development; archive placeholder remains explicitly labeled.
