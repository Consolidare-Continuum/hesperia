<!--
HESPERIA — Reference Architecture Definition (RAD)
-->

# Versioning gate — structural vs behavioral (v0.5.0 → v0.5.1)

## Status (v0.5.1 sealed)

The **v0.5.1** line cut (2026-03-19) applies a coordinated **`VERSION.yaml` / `pyproject.toml` → 0.5.1** bump, new audit tree **`release/v0.5.1/`**, schema snapshot **`schemas/public_api_v0_5_1.snapshot.json`** (no normative schema change vs v0.5.0 — byte freeze of the same `public_output_schema.json`), and documented product E2E envelope drift in **`CHANGELOG.md`**.

## What happened in the repo refresh (pre-seal context)

The **2026-03-19 structural refresh** (layout, quarantine, docs moves, optional TRIZ paths, clinical test relocation) was intended to be **non-behavioral** relative to the sealed engine **until** the v0.5.1 seal:

- **Before v0.5.1:** staying on v0.5.0 without a new audit was correct.
- **After v0.5.1:** enforcement artifacts and version authority are locked per **`release/v0.5.1/final_gate_status.json`**.

## Rules

### Structural-only change (no version bump)

Allowed without touching `system_version` when:

- Paths, docs, CI wiring, or quarantine moves **do not** alter deterministic execution_flow outputs for the same inputs, **or**
- Any artifact drift is **reverted** before merge (e.g. accidental regeneration of committed E2E JSON).

### Real **v0.5.1** (requires full gate)

A **minor** line bump is **not** a rename exercise. It requires:

1. **New audit tree:** `release/v0.5.1/` (or successor policy) with regenerated **manifest**, **provenance**, **seal status**, **determinism** artifacts per `tools/release/build_release_audit_v0_5_0.py` successor / checklist.
2. **Authority files updated in lockstep:** `VERSION.yaml`, `pyproject.toml`, `hesperia.engine.release_meta`, `hesperia.__version__` tests, `runtime/shipping/version_info.py` (on sealed build).
3. **Schema contract:** `schemas/public/public_output_schema.json` updated only with intent; **`schemas/public_api_v0_5_0.snapshot.json` renamed or superseded** with a new snapshot id (e.g. `public_api_v0_5_1.snapshot.json`) and CI verifier updated.
4. **E2E bytes:** `e2e_reference_output.json` / committed E2E artifacts must match the new version **exactly**, or the diff must be **explicitly justified** in CHANGELOG + audit notes (no “mysterious drift”).
5. **Import graph:** regenerate `docs/IMPORT_GRAPH_v0_5_0.md` (or v0.5.1 successor) and ensure CI diff passes.

## Summary

| Change type | Version | Snapshot / E2E |
|-------------|---------|------------------|
| Move files, docs, optional paths | Stay on **0.5.0** | Must stay **bit-identical** unless documented test-only |
| Engine / projection / schema | **0.5.1+** | New seal + new snapshot + justified E2E diff |
