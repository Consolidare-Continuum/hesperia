# Task: Grace — Hesperia observability extension v0.1 (Ethan → Grace)

**Purpose**: **Ethan tasks Grace**: Triage the Hesperia observability extension (v0.1). Add to active.md the implementation task(s) per spec; assign owner(s). No geometry/traversal/safeguard/core changes — observability and soft gates only. **From**: Ethan. **To**: Grace. **Added**: 2026-02-18.

**Spec**: [projects/hesperia/HESPERIA_OBSERVABILITY_EXTENSION_v0_1.md](../projects/hesperia/HESPERIA_OBSERVABILITY_EXTENSION_v0_1.md) — loopability_band, entropy_metric, border_passings_count, direction, ring_distance_from_start, safeguard_events_count; all read-only/telemetry; wrapper or context_rag only; kernel untouched.

**Refs**: [RELEASE-V1-FIXED-POINT-2026-02-18.md](../projects/hesperia/RELEASE-V1-FIXED-POINT-2026-02-18.md), [CONTEXT-RAG-PACKET-SCHEMA.md](CONTEXT-RAG-PACKET-SCHEMA.md).

---

## 1. Scope (Grace)

| Action | Description |
|--------|-------------|
| **Triage** | Add one or more rows to active.md for implementing the observability extension v0.1 (fields in packet or observability block; logic in wrapper/context_rag only). |
| **Assign** | Set owner(s) (e.g. Gena for code in context_rag/post-process; Cursor for schema/rules if needed). |
| **Link** | Row link = this task or the spec. |

---

## 2. Constraints (from spec)

- No engine modification. No traversal cost. No adjacency change.
- Loopability band = classification from L_full (e.g. stable ≥ 0.6, transitional 0.4–0.6, unstable ≤ 0.4).
- Entropy = unique_areas_visited / steps; report only.
- ring_distance_from_start, safeguard_events_count = derived/telemetry; append in wrapper.
- Tension file / chord / radial specs = dormant (format only); no implementation in this triage unless Grace adds a separate “validate format” task.

---

## 3. Deliverables

1. **active.md**: New row(s) for observability extension implementation (OPEN), owner assigned, link to this task or to HESPERIA_OBSERVABILITY_EXTENSION_v0_1.
2. **Optional**: Ensure CONTEXT-PACKET / project summary already reference the spec (done in same session as spec creation).

---

**SIGNED: Architecture (Ethan) | Task Grace — Hesperia observability extension v0.1 triage | 2026-02-18 | governance**
