# Hesperia — Release V1 fixed point (2026-02-18)

**Purpose**: Draw a line. Consolidated state as of this date; **Cursor is the main invoker of Hesperia** in the cursor repo. This is a **fixed point** in state. Backup taken; **Hesperia project starts all over from here**. **Version**: V1 fixed point. **Date**: 2026-02-18.

---

## 1. Cursor as main invoker of Hesperia (current)

In the cursor repo, **Cursor** (default) and **Cursor main** (when invoked) are the **main invokers** of Hesperia:

| Need | Invocation | Where defined |
|------|------------|----------------|
| **Full context packet** (calculable + coherence_hints + optional retrieval) | Run `cluster/chroma-server/context_rag.py` from repo root; parse JSON, inject into context. | .cursor/rules/cursor-main-awareness.mdc §Context RAG (full packet) |
| **Matrix-derived context** (geometry, path, families) | Run `cluster/chroma-server/matrix_run.py` or query Chroma layer=hesperia_families. | .cursor/rules/cursor-main-awareness.mdc §Matrix-derived context |
| **Core-mode calibration** (all functions, no books/statements, log all) | Run `cluster/chroma-server/run_core_mode_invocation.py` from repo root. Internal calibration; not product spec. | governance/ETHAN-HESPERIA-PLAN-1-INVOCATION-CORE-MODE.md, README §Plan 1 |

**Packet schema**: governance/CONTEXT-RAG-PACKET-SCHEMA.md. **Chroma**: layer=hesperia_families; optional retrieval (families, books chunks) when --query or --area_id or --family_name. **Do not touch**: ring order, adjacency, geometry, safeguard threshold (governance/ETHAN-HESPERIA-STATE-NOW-ASSESSMENT §VI).

---

## 2. What this fixed point contains

- **What Hesperia is**: Geometry-safe semantic traversal kernel; deterministic semantic traversal and validation core. Structure-only; no semantic reasoning yet.
- **What it does**: Fixed geometry (12×24×250), deterministic ring traversal, border tracking, context packet with adjacency hints, logic layer + safeguard (3-fail stop), apple coverage; context governor, path validation, coverage verification.
- **Direction locked**: A (harden structure). **Spec locked**: Safeguard State Machine Spec v0.1 (ETHAN-HESPERIA-LOOP-SAFEGUARD + operator spec §3.4).
- **Scripts**: matrix_run.py, context_rag.py, hesperia_logic.py, run_traversal_with_safeguard, run_core_mode_invocation.py, apple_path_imprint.py, apple_involvements.py, hesperia_safeguard_stress_test.py.
- **Governance**: STATE-NOW-ASSESSMENT, CORE-MODE-MVP, PLAN-1-INVOCATION (calibration), OPERATOR-INTERFACE-SPEC, LOOP-SAFEGUARD, GRACE-HESPERIA-NEXT-DIRECTION, GENA-HESPERIA-SAFEGUARD-STRESS-TEST-RESULTS, CONTEXT-RAG-PACKET-SCHEMA, HESPERIA-FAMILIES-CHROMA-SCHEMA, mid-stage product report, CONTEXT-PACKET, PROJECT-CHARTER.
- **Project**: projects/hesperia/ (charter, CONTEXT-PACKET, scope, roles). **Brain**: CLIENTS/hesperia/. **Code in cursor repo**: cluster/chroma-server/* (matrix_run, context_rag, hesperia_logic, apple scripts, Plan 1 runner, stress test).

---

## 3. Backup

- **Archive**: `archive/hesperia-fixed-point-20260218/` — MANIFEST of paths and copies of this release doc and key governance/project files. Use for restore or reference.
- **Git**: Recommend tag, e.g. `hesperia-v1-fixed-point-20260218`, at current commit after this release is committed.

---

## 4. Start from here

All new Hesperia work in this project **starts from this fixed point**. Baseline = this document + backup. Do not mutate the fixed-point state without explicit change control; extend from it.

**Safe evolution (observability only)**: [HESPERIA_OBSERVABILITY_EXTENSION_v0_1.md](HESPERIA_OBSERVABILITY_EXTENSION_v0_1.md) — discipline from fixed point; loopability as advisory; entropy telemetry; observability fields; no core/traversal/safeguard/geometry changes.

---

**SIGNED: Cursor/Albina | Hesperia Release V1 fixed point — consolidated state, Cursor main invoker, backup, start from here | 2026-02-18 | projects/hesperia**
