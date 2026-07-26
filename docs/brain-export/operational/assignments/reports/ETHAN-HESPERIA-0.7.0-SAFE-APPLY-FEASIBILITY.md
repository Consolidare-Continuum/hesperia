# ETHAN — HESPERIA 0.7.0 Safe Apply Feasibility Memo

**SPEC ID:** HESPERIA-RESEARCH-KSI-RELATION-REPAIR-0.7.0  
**Date:** 2026-06-14  
**Author:** Colombo (research draft for Ethan/Grace)  
**Status:** Proposed — research only  
**Anchors:** Evolution tree CELL 15 · tag `122d45b` (0.6.3) · main `e9eaa07` · `applied=0` doctrine  

---

## 1. Should 0.7.0 include real graph apply?

**Yes — one narrow slice only.**

0.6.3 deliberately stops at **observe → inspect → propose → store pending** ([ETHAN-HESPERIA-0-6-3-IRC-TEACHER-RUN-SPEC.md](../../../governance/ETHAN-HESPERIA-0-6-3-IRC-TEACHER-RUN-SPEC.md)). Evolution tree CELL 15: *“mutation without sandbox is how calibrated graphs die.”*

0.7.0 minimum viable molt:

```text
One approved proposal → sandbox copy → apply → replay → score → canonical write → rollback artifact
```

Not: batch auto-apply, not CD field mutation at scale, not concept creation.

---

## 2. Which proposal types are safe enough for first apply?

| Type | First apply? | Rationale |
|------|--------------|-----------|
| `update_edge_weight` | **Yes** | Already in Teacher + `reweight_preview`; bounded scalar; easy diff |
| `add_edge` (new relation candidate) | **Second** | Needs stronger false-bridge checks; extend Teacher schema |
| `mark_rejected` / `mark_needs_human_review` | **Yes** (ledger only) | No graph write |
| `update_cd_field` | **Defer** | Higher blast radius; present in Teacher code but conflicts with “narrow 0.7.0” |
| `remove_edge`, split/merge concept | **No** (0.8+) | Ontology-level surgery |

---

## 3. What metrics prove improvement?

Deterministic **replay set** (fixed Russian TFP / benchmark statements — extend 0.6.3 archive examples):

| Metric | Definition |
|--------|------------|
| `incident_count_delta` | ↓ semantic incidents on replay set |
| `missing_bridge_delta` | ↓ count or ↓ aggregate `bridge_need_score` |
| `phi_residual_norm_delta` | ↓ Φ_e residual on affected edges |
| `contradiction_flag_delta` | ↓ contradiction triggers (0.5.8 track) |
| `trace_stability` | Same activation topology except declared diff hunk |

Improvement gate: **≥1 primary metric improves** and **no regression on hard counterexamples**.

---

## 4. What metrics prove damage?

| Metric | Threshold idea |
|--------|----------------|
| New incidents on replay set | Any new → fail |
| Contradiction introduced | Any → fail |
| Propagation trace divergence outside proposal hunk | Fail |
| CD invariant violations | Fail |
| Benchmark runtime / determinism hash change | Fail unless documented |

**Semantic damage score** = weighted sum of above; must stay **below threshold T** (Ethan to calibrate on first sandbox runs).

---

## 5. What must Inspector Pane 2 show?

Minimum rational approval UI (KSI-19 / CELL 15):

1. Proposal ID + Teacher action + parameters (numeric only)  
2. **Graph diff hunk** (edges/weights touched)  
3. Before/after replay table (per benchmark ID)  
4. Improvement score + damage score + pass/fail per gate  
5. Evidence handles: `incident_id`, `source_edge_id`, `run_id`, `correlation_id`  
6. Rollback artifact link (graph snapshot SHA / file path)  
7. Approval state: pending → approved/rejected (no prose from LLM)

---

## 6. What must remain pending/rejected?

- Any proposal failing replay or damage threshold  
- Any proposal touching forbidden fields (justification keys — already rejected at parse)  
- `update_cd_field` until explicit 0.7.1 charter  
- All proposals when sandbox copy fails or rollback artifact missing  
- Batch apply without per-proposal gate record  

---

## Final research question (spec §11)

**Can HESPERIA 0.7.0 safely apply one approved relation repair?**

**Feasibility: YES**, if implementation order is:

1. Sandbox graph copy (filesystem or in-memory CD snapshot)  
2. Apply **single** `update_edge_weight`  
3. Run frozen replay set  
4. Persist scores + diff + rollback  
5. Approval MCP / human record  
6. Only then write canonical graph + set `applied=1` in MySQL  

This matches the organism lineage: 0.6.3 Teacher is the **nerve**; 0.7.0 is the **molt** with exit criteria, not a silent flag.

---

**SIGNED:** Research (Colombo) | Hesperia 0.7.0 safe apply feasibility | 2026-06-14 | draft for Ethan
