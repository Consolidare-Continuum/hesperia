# Task 6: Codex execution checklist (v0.5.0 seal)

Execute phases in order. If a gate fails, stop and fix before continuing.

## Phase 0: Inventory

| Step | Command / action |
|------|------------------|
| 0.1 | `git checkout -b release/v0.5.0-seal` (manual) |
| 0.2-0.5 | `python3 tools/seal_phase0_inventory.py` writes `tmp/repo_inventory.txt`, `tmp/version_reference_scan.txt`, `tmp/module_classification_draft.yaml`, `tmp/preseal_snapshot.json` |

`tmp/` is gitignored (except `tmp/.gitkeep`).

## Phase 1: Version authority

- Canonical file: **repository root** `VERSION.yaml`. Symlink: `hesperia/VERSION.yaml` -> `../VERSION.yaml`.
- Loader: `hesperia.system.version`.
- Validate: `python3 tools/validate_version_consistency.py`

## Phase 2: Repo topology

- Read: `REPO_STRUCTURE_POLICY.md`, `EXTENSION_STATUS.yaml`, `GENERATED_ARTIFACT_POLICY.md`.
- Gate: imports and pytest discovery still work.

## Phase 3: Specs

- Heuristic scan: `python3 tools/doc_authority_scan.py` -> `tmp/doc_authority_scan.yaml`
- Index preview: `python3 tools/build_specs_index.py` -> `tmp/specs_index_preview.json`
- Tier-1 spec paths enforced by `tools/release/build_release_audit_v0_5_0.py`.

## Phase 4: Product boundary

- Validate: `python3 tools/audit_public_surface.py`
- Projection: `hesperia.engine.projection.project_to_public` via `analysis_service`.

## Phase 5-6: Release package

Unified builder:

```bash
export HESPERIA_RELEASE_BUILD_TIMESTAMP=2026-03-19T12:00:00Z
python3 tools/release/build_release_audit_v0_5_0.py
```

Or: `./tools/release/run_release_reference.sh`

Thin wrappers (same builder): `tools/release/run_release_audit.py`, `run_determinism_check.py` (`--determinism-only`), `build_checksums.py` (`--checksums-only`), `build_release_manifest.py`, `run_schema_validation.py`.

Fixture: `tests/fixtures/release_v0_5_0/canonical_input.txt` (alias: `examples/release_fixture_input.txt`).

Required under `release/v0.5.0/`: README, manifest, build_info, checksums, capabilities copy, specs_index, test_report, audit_report, determinism_report, schema_validation_report, e2e_reference_output, schema.json, **final_gate_status.json**.

## Phase 7: Final gate

- Read `final_gate_status.json`: `sealed` must be **true** for tag.
- `release_audit` must be **pass** (run builder **without** `--quick`).
- Working tree must be **clean** (no `git_worktree_dirty` in reasons_fail).
- Then: `git tag -a v0.5.0 -m "..."` and `git push origin v0.5.0`.

## Stop conditions

Do not seal if: projection not mandatory; determinism triplicate fails; schema disagrees with runtime; product ships research/clinical; version files disagree.

## Definition of done

Phases run in order; full audit bundle exists; `sealed: true` only with full pytest and clean tree; tag only after that.

See also: `release/v0.5.0/README.md`, `AGENTS.md`, `docs/PUBLIC_PRODUCT_SURFACE.md`.
