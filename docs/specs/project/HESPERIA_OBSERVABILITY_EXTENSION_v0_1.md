<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Hesperia — Observability extension v0.1 (safe evolution from fixed point)

**Purpose**: Define the **only acceptable** post–fixed-point evolution: observability and soft gates only. No geometry, no traversal rewrite, no safeguard changes, no Hesperia core refactor. **Baseline**: [RELEASE-V1-FIXED-POINT-2026-02-18.md](RELEASE-V1-FIXED-POINT-2026-02-18.md). **Ownership**: Ethan (direction); implementation per Grace/Gena handoff. **Version**: v0.1. **Date**: 2026-02-18.

---

## 1. Discipline from fixed point onward

We stay disciplined.

| Do not | Reason |
|--------|--------|
| Geometry changes | Fixed point is stable. |
| Traversal rewrite | Deterministic ring walk is an asset. |
| Safeguard changes | Spec v0.1 locked; three-fail stop. |
| Refactoring of Hesperia core | Infrastructure hardening phase. |

**Direction**: Safe development. No tension layer yet. **Only acceptable move**: make loopability an **advisory signal**, not a structural modifier.

- We do **not** inject physics.
- We do **not** alter behavior.
- We add **observability and soft gates only**.

---

## 2. Safe evolution path (zero refactor)

### 2.1 Loopability as read-only control signal

- Do **not** multiply tension.
- Do **not** change traversal cost.
- Do **not** change adjacency.

**Add to context packet** (classification only):

```text
loopability_band: "stable" | "transitional" | "unstable"
```

Pure classification. **No engine modification.**

### 2.2 Advisory layer only (outside core)

Create **wrapper logic around** traversal, not inside it.

Example (policy layer, not kernel):

```text
if L_full < 0.4:
    restrict external caller from enabling chord jumps
```

The kernel remains untouched. Policy layer enforces behavior. Hesperia core stays pure.

### 2.3 Entropy as telemetry only

Compute:

```text
entropy = unique_areas_visited / steps
```

- **Log it.**
- **Expose it in packet.**

Do **not** make traversal react to it. Signal only; no change to system dynamics.

### 2.4 Tension coefficients file (dormant)

You may define:

```text
AREA_TENSION_MATRIX_v0_1.json
```

- **Do not** use it in traversal.
- **Do not** add cost.
- **Do not** alter path.
- **Only**: validate format and loadability. Prepare future expansion without activating. Forward-compatible but inert.

### 2.5 Preserve determinism

Current strengths:

- Deterministic ring walk.
- Deterministic safeguard.
- Deterministic coverage.
- Deterministic packet.

Do **not** compromise with adaptive behavior yet. Determinism is the asset.

---

## 3. What we can safely add now (without refactoring)

| Addition | Use |
|----------|-----|
| Loopability band classification | In packet; read-only. |
| Entropy metric | Report only; no traversal reaction. |
| Border tension file | Inactive; format/load only. |
| Chord spec | Inactive. |
| Radial bands spec | Inactive. |
| Additional logging fields | Outside traversal core. |

All **outside** traversal core.

---

## 4. What we must not do (Phase D material)

- No dynamic modulation.
- No traversal cost model.
- No internal state expansion.
- No adaptive safeguards.
- No probabilistic routing.
- No semantic weighting.

---

## 5. Strategic position

**Phase**: Infrastructure hardening.

- **Observability** > intelligence
- **Stability** > expressiveness
- **Determinism** > sophistication

Mutating traversal logic now risks destabilizing the fixed point.

---

## 6. Observability extension — fields (v0.1)

Add to the context packet (or to a dedicated observability block consumed by the same contract) the following. **All read-only / telemetry; no engine modification.**

| Field | Type | Description |
|-------|------|-------------|
| `loopability_band` | `"stable" \| "transitional" \| "unstable"` | Classification from L_full (or equivalent); advisory only. |
| `entropy_metric` | number | `unique_areas_visited / steps`; telemetry only; not used in traversal. |
| `border_passings_count` | object | `{ area_border_passings: number, family_border_passings: number }` — already in coherence_hints; include in observability block for completeness. |
| `direction` | number or string | Path direction (e.g. 1 / -1 or "CW" / "CCW"); already in path_params; expose in observability for convenience. |
| `ring_distance_from_start` | number | Distance along the ring from start area to current (e.g. steps along ring, or arc length in area units). Read-only. |
| `safeguard_events_count` | number | Count of safeguard-relevant events in the run (e.g. failures counted toward SAFEGUARD_STOP); telemetry only. |

**Placement**: Either extend `coherence_hints` with these fields or add a sibling `observability` object to the packet. Schema update: [governance/CONTEXT-RAG-PACKET-SCHEMA.md](../../governance/CONTEXT-RAG-PACKET-SCHEMA.md) to be updated when this extension is implemented; until then this document is the spec.

---

## 7. Implementation notes

- **Loopability band**: Derive from existing `calculable.loopability.L_full` (when present) via thresholds; e.g. stable ≥ 0.6, transitional in (0.4, 0.6), unstable ≤ 0.4. No change to how L_full is computed.
- **Entropy**: Compute from `road_coordinates` (unique area_id count) and `traversal_length`; append to packet / log.
- **ring_distance_from_start**: From path_params and road; derived, not stored in core.
- **safeguard_events_count**: From logic/safeguard run output (e.g. fail count or event list length); append to packet when run_traversal_with_safeguard or equivalent is used.

All logic for these fields lives **outside** matrix_run traversal kernel and **outside** safeguard state machine; wrapper or context_rag/post-process only.

---

**SIGNED: Architecture (Ethan) | Hesperia observability extension v0.1 — safe evolution from fixed point, no core refactor | 2026-02-18 | projects/hesperia**
