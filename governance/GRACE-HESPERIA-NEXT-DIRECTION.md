# Hesperia — next direction and locked spec (Grace)

**Purpose**: Record chosen direction and one locked formal spec per ETHAN-HESPERIA-STATE-NOW-ASSESSMENT §VIII–IX. **Owner**: Grace. **Date**: 2026-02-18.

---

## Decision

- **Direction**: **A — Harden structure.** Stay structure-only; add path types, stress tests, multi-ring/cross-family options; strengthen geometry and safeguard. Safe, conservative. No semantic weight or Phase D yet.
- **Locked spec**: **Safeguard State Machine Spec v0.1.** Canonical source: [ETHAN-HESPERIA-LOOP-SAFEGUARD.md](ETHAN-HESPERIA-LOOP-SAFEGUARD.md) + [ETHAN-HESPERIA-OPERATOR-INTERFACE-SPEC.md](ETHAN-HESPERIA-OPERATOR-INTERFACE-SPEC.md) §3.4. No drift on threshold, valid_streak reset, or SAFEGUARD_STOP behaviour until Phase D or explicit change control.

---

## Safeguard State Machine Spec v0.1 (reference)

| Item | Value |
|------|--------|
| **States** | CLEAR (traversing); counting (fail_count 1..2); SAFEGUARD_STOP (fail_count ≥ 3, traversal frozen). |
| **Trigger** | Three consecutive hop_result = 0 (invalid). |
| **Reset** | fail_count = 0 only when valid_streak ≥ 2. |
| **On STOP** | Freeze traversal; mark region LOGICAL_OBSTACLE_CLUSTER (UNSAFE); store last 3 states; return STOP. |
| **Scope** | Per traversal context (hex, family, area). Not global. |
| **Do not change** | CONSECUTIVE_FAIL_THRESHOLD=3, VALID_STREAK_RESET=2; ring/adjacency/geometry. |

Full definition: ETHAN-HESPERIA-LOOP-SAFEGUARD.md, operator spec §3.4, hesperia_logic.py (TraversalSafeguard, run_traversal_with_safeguard).

---

## Next steps (after lock)

- **Gena**: Safeguard stress-test (force safeguard to fire); document. active.md OPEN.
- **Future**: Under direction A — more path types, stress tests, structural expansion only. No B/C/D until boss or Grace re-opens.

---

**SIGNED: Product (Grace) | Hesperia next direction A + Safeguard State Machine Spec v0.1 locked | 2026-02-18 | governance**
