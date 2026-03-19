# HESPERIA Engine Dynamics — **v0.5.1** sealed release audit

Governed **enforcement** release: architecture, boundaries, and runtime behavior are locked by CI, integrity tests, and this audit tree (determinism, schema validation, system seal, pytest).

## Regenerate

```bash
export HESPERIA_RELEASE_BUILD_TIMESTAMP=2026-03-19T18:00:00Z
python3 tools/release/build_release_audit_v0_5_1.py
python3 tools/release/build_release_audit_v0_5_1.py --quick   # subset only
```

**Canonical input:** `tests/fixtures/release_v0_5_0/canonical_input.txt` (UTF-8).

**Exit code:** `0` only if **all gates pass** (including **clean git worktree**). See `audit_report.json` → `seal_decision` and **`final_gate_status.json`**.

**Checklist discipline:** `docs/CODEX_EXECUTION_CHECKLIST_v0_5_0_SEAL.md` (same process; builder: `build_release_audit_v0_5_1.py`).

## Artifacts

| File | Role |
|------|------|
| `manifest.json` | Version, commit, determinism hash, routes, seal_status |
| `BUILD_PROVENANCE.json` | Builder metadata |
| `audit_report.json` | `seal_decision.may_tag_v0_5_1` |
| `final_gate_status.json` | **`sealed`: true** when all gates pass |
| `determinism_report.json` | Triplicate hash |
| `schema_validation_report.json` | jsonschema + schema_guard |
| `system_seal.json` | Task 11 |
| `e2e_reference_output.json` | Frozen product-path JSON |
| `schema.json` | Public output schema copy |
| `checksums.txt` | SHA256 of sibling files |

## Tag

```bash
git tag -a v0.5.1 -m "Hesperia Engine Dynamics v0.5.1 — governed enforcement baseline"
git push origin v0.5.1
```

Only when `final_gate_status.json` → `"sealed": true` and the tree that produced this bundle was clean.
