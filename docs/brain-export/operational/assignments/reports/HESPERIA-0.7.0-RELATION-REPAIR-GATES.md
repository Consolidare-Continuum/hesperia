# HESPERIA 0.7.0 — Relation Repair Acceptance Gates

**SPEC ID:** HESPERIA-RESEARCH-KSI-RELATION-REPAIR-0.7.0  
**Date:** 2026-06-14  
**Author:** Colombo  
**Status:** Proposed (research deliverable)  
**Target:** CELL 15 / v0.7.0 — does not alter 0.6.3 exit criteria  

---

## Gate chain (canonical)

```text
G1  Proposal schema accepted (hesperia.teacher_response.v063 + 0.7.0 extensions)
G2  Sandbox graph copy created (immutable parent SHA recorded)
G3  Apply produces deterministic diff (single hunk, allowlisted action)
G4  Replay benchmark set completes (same engine SHA, flags documented)
G5  Improvement score positive (primary metrics)
G6  Damage score below threshold (no new incidents/contradictions)
G7  Human or approval-gate record (MCP / operator)
G8  Rollback artifact exists (snapshot id, restorable)
G9  Canonical graph mutation allowed ONLY after G1–G8
```

---

## Gate definitions

| Gate | Pass condition | Fail action |
|------|----------------|-------------|
| **G1** | JSON schema valid; no forbidden keys; action ∈ allowlist | Reject proposal; log validation error |
| **G2** | Sandbox ID created; parent = prod graph git SHA or snapshot id | BLOCKED; no apply |
| **G3** | Diff JSON lists only declared edges/weights; deterministic re-run same diff | Reject; sandbox discard |
| **G4** | All replay benchmarks return engine envelope; no timeout | PAUSE; fix replay set |
| **G5** | ≥1 improvement metric improved vs baseline | Reject unless operator override (logged) |
| **G6** | damage_score < T; zero new hard failures | Reject |
| **G7** | `record_approval` or operator ACK with proposal_id | Stay pending |
| **G8** | Rollback blob written; verify restore dry-run | BLOCKED |
| **G9** | Write canonical CD/graph; MySQL `applied=1`; audit JSONL | N/A — success path |

---

## 0.7.0 allowlist (first molt)

```text
apply_allowed:
  - update_edge_weight
  - add_edge          # phase 0.7.0b after weight-only proven
ledger_only:
  - mark_rejected
  - mark_needs_human_review
forbidden_apply:
  - update_cd_field   # defer
  - remove_edge
  - split_concept / merge_concept / add_concept
```

---

## Relation to 0.6.3 gates (G1–G5)

0.6.3 exit criteria ([governance/HESPERIA-0-6-3-EXIT-CRITERIA.md](../../../governance/HESPERIA-0-6-3-EXIT-CRITERIA.md)) remain sealed at `122d45b`.  
0.7.0 gates **extend** — they do not retroactively redefine 0.6.3 `reweight_preview.applied=0`.

---

## Inspector Pane 2 binding

Pane 2 must display gate state machine:

`pending → sandbox → replay → scored → awaiting_approval → applied | rejected`

Operator never sees LLM justification — only scores, diff, evidence IDs.

---

**SIGNED:** Research (Colombo) | Hesperia 0.7.0 relation repair gates | 2026-06-14 | v0.1
