<!--
HESPERIA — Hesperia Engine Dynamics
Copyright © 2026 igareosh.com. See LEGAL_NOTICE.md.
-->

# Version policy (strict) — Engine Dynamics 0.5+

> **Task 3 — document tier:** This file is **Tier 2 (explanatory)**. Binding version + governance rules are also summarized in **`specs/system/versioning_and_governance.md`** (Tier 1). If they disagree, **the spec wins**.

## Single source of truth

| Authority | Path |
|-----------|------|
| **System + components + schema + pipeline ids** | **`VERSION.yaml`** (repo root) |
| **Active vs legacy asset tracks** | **`assets/version_registry.yaml`** |
| **Runtime injection** | **`hesperia.system.version`** |

There is **one** active `system_version` for the sealed product surface. `pyproject.toml` / `hesperia.__version__` **must** match `VERSION.yaml` (verified in tests).

## Rules

1. **Semantic + stage** — `system_version` uses semver for the engine; `release_stage` documents integration maturity (e.g. `dynamic_integration`).
2. **No mixed active versions** — Do not imply multiple “current” engine versions. Legacy asset **filenames** (e.g. `v0_4_1_3`) remain only where frozen files require it; they are **not** the active system version.
3. **Experimental components** — Must declare a suffix or label in `VERSION.yaml` → `components` (e.g. `clinical: "0.5.0-experimental"`).
4. **Schema bumps** — Any change to public output shape or required trace fields → bump `schema.public_output` (and document in **`schemas/public/public_output_schema.json`**; `assets/public/public_output_schema.json` remains a **symlink** for legacy paths).
5. **Calibration bumps** — Material calibration / profile changes → **at least** a minor `system_version` bump.
6. **No silent overrides** — `build.git_commit`, `build.timestamp`, and `build_id` are injected at runtime from git/env; do not hand-edit committed `build` values in `VERSION.yaml` (keep `null` in file).
7. **No version from folder names alone** — Logical paths (`v0_5_0`) are registered in `assets/version_registry.yaml`; code resolves via canonical paths, not ad-hoc directory guessing.

## Public output trace (mandatory)

Every **public** JSON (API, sealed CLI, E2E artifacts, `write_public_json`) must carry:

- `system_version`
- `build_id`
- `schema_version` (public output schema id, e.g. `v1`)
- `calibration_profile`

E2E adds: `run_id`, `pipeline_version` (`e2e_v2`), `modules_used`.

## Legacy

- **SPEC-era label “v0.4.x”** in `core/layers/*` comments = historical document numbering only.
- **`lexicon/frozen/v06`** = legacy physical bundle id; **active** alias: **`lexicon/frozen/v0_5_0`** (symlink + registry).

## Verification

```bash
python3 -m pytest tests/test_release_version.py tests/test_e2e_flows.py -q
```

See also: [CHANGELOG.md](../CHANGELOG.md), [HESPERIA_v0_5_ENGINE_DYNAMICS.md](HESPERIA_v0_5_ENGINE_DYNAMICS.md).
