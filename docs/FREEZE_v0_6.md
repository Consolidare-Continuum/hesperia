# HESPERIA v0.6 — Freeze

**Date:** 2026-02-24
**Status:** Frozen. Operational repo is v0.6 only.

## Scope

- **In scope:** Dict A + Dict B (structural layer), surface map, core math (22_SPEC), layer math (L1–L9), API 0.6.0. All code and artifacts use v0.6 naming (analyze.py, attribution.py, dict_b.py, assets/v06, dict_a_v06.jsonl, etc.).
- **Out of scope (archived):** v0.4/v0.5 attribution, dense projection, v05 builds, v04 calibration, layer runner scripts, old reports and runtime outputs.

## Rules

1. No changes to core math or Dict A/B v0.6 semantics without a version bump.
2. New work: extend in new files or new versioned specs; do not alter frozen artifacts.
3. Operational index: [OPERATIONAL_INDEX_v0_6.md](../OPERATIONAL_INDEX_v0_6.md). Archive: [archive/ARCHIVE_MANIFEST.md](../archive/ARCHIVE_MANIFEST.md).
