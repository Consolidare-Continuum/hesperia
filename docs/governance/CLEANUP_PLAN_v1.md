# Repository cleanup plan v1

**Goal:** Reduce duplication and clutter; keep one canonical copy of each asset; archive historical docs.

---

## Phase 1 — Archive historical specs ✓

- **Move:** `docs/specs/history/` → `docs/archive/specs_history/` → **`legacy/docs/specs_history/`** (v0.5.1: quarantine under `legacy/`).
- **Why:** Dozens of old numbered specs (00_, 10_, 11_, …) are reference-only; not needed in active specs tree. Governance docs treat this content as internal/excluded from bundle.
- **Refs:** Use **`legacy/docs/specs_history/`** in new docs and policies.

---

## Phase 2 — Remove duplicate data files ✓

## Phase 2b — Repo root cleanup ✓
- **Moved:** `guard_config_v1.json` → `assets/config/guard_config_v1.json`
- **Moved:** `layer_1_9_predefined_defaults_v1_0.json` → `core/layers/`
- Root no longer holds guard/layer config; all references updated.

- **Remove:** `assets/data/A_CORE_STAR_MAP_v1.json` — identical to `lexicon/curated/A_CORE_STAR_MAP_v1.json`; no code references the assets path.
- **Keep:** Single source of truth for lexical maps in `lexicon/curated` (and `lexicon/frozen` where build output is required). Do not add copies under `assets/data` for these.

---

## Phase 3 — Consolidate run scripts (later)

- **Canonical entrypoint:** `python3 -m runtime.pipeline.run_l1_through_l9` (and sealed CLI/API).
- **Review:** `runtime/execution_flow/run_*.py`, `runtime/provenance/run_manifest.py`, `runtime/runners/run_reference_pipeline.py` — keep only those that are entrypoints or used by CI; document or merge the rest.

---

## Phase 4 — Lexicon frozen vs curated (document only for now)

- **curated:** Source-of-truth JSON built by lexicon build.
- **frozen:** Copy used at runtime; synced via `lexicon/build/sync_curated_to_assets.sh` or similar. Avoid adding duplicate copies elsewhere.

---

## Phase 5 — Large / legacy code (optional)

- **core_math_legacy.py:** Still used by `tests/energy_invariants_stress.py` and `core_math_compat.py`. Leave in place until migration.
- **debug_interface.py:** Move to `sphere/interfaces/` or remove if unused; confirm with tests.

---

*Run `./tools/detect_unused.sh` periodically. Prefer archiving (move) over delete so history stays in git.*
