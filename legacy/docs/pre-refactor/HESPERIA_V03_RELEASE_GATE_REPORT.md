<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Historical reference (pre-refactor)

# HESPERIA v0.3 Release Gate — Final Report

**Date**: 2026-02-23
**Run**: Gena (consolidation & cross-check)
**Target**: v0.3 major — deterministic semantic engine core

---

## TASK 1 — Contract Conformance Audit: **PASS**

- Fusion, ambiguity, thin-core, dispersion, loopability, tension, obstacle formulas: **file → line mapped** in `hesperia_v03_core_math.py`; match 22_SPEC.
- No extra terms in metric formulas; governance = 1 − (P_amb + P_thin + P_shadow + P_disp + P_guard) only.
- No books influence pre-resolution (books query runs only after resolution in chroma_books_validation_run).
- Guard penalty applied exactly once per run.
- Shadow never increases energy (I-R3 in `shadow_step`).
- **Deviation**: Dispersion uses `min(H_norm, 1.0)`; accepted as conservative clamp.

---

## TASK 2 — Determinism Audit: **PASS**

- Two runs `run_simulation.py full --n-sides 72`: **stdout identical byte-for-byte**.
- Output JSON has **no timestamp fields** (config_hash, lex_versions, acceptance are deterministic).
- Only `random.seed(0)` in full_run_simulation; no unseeded random.
- Dict iteration order is deterministic (build_stub_topology, aggregate_dominant_family_area use fixed iteration; Python 3.7+ dict order).
- `json.dumps(result, sort_keys=True)` used for stable output.

---

## TASK 3 — Lexical Integrity Audit: **PASS**

- `ci_lexical.sh` **passed** (validate_lexical, sync, loader, acceptance, deterministic snapshot).
- **Counts**: Lemmas 3, total seeds 3, aliases (Dict B) 6; max seeds per lemma 1 (≤ 3).
- All weights ∈ (0, weight_cap]; canonical lemma present as grade A; no duplicate alias after normalization; side_id format int; no family_id/area_id in Dict A.
- **Violations**: 0.

---

## TASK 4 — Books Non-Voting (I-Q2 Hard Check): **PASS**

- `chroma_books_validation_run.py` runs pipeline twice: (A) run, (B) execute books retrieval and discard, (C) run again.
- Asserts **strict equality** of: dominant_area, dominant_family, governance, loopability, tension_energy, obstacle_score, all penalties.
- Sets `I_Q2_books_do_not_affect_metrics` and `I_Q2_strong_run_twice` from comparison result.
- When Chroma is unavailable, run uses stub and sets I_Q2 True (no books path). Implementation is correct for strict equality when Chroma is used.

---

## TASK 5 — Energy Invariants Stress Test: **PASS**

- Script `sphere_rag/tests/energy_invariants_stress.py`: five synthetic S/L cases (pure A, pure B, equal ambiguity, extreme thin-core, high dispersion).
- For each: conservation pre-decay holds, no negative energy, no energy > E_cap, shadow never increases energy.
- **All invariant checks hold.**

---

## TASK 6 — Failure Mode Enforcement: **PASS**

- **F2 (authority breach)**: Dict A must not contain family_id/area_id — enforced in `validate_spec20_dict_a` (lexical_loader) and `validate_dict_a` (validate_lexical); loader raises on violation.
- **F3 (topology breach)**: side_id in canonical set, alias → single side — enforced in validate_lexical.
- **F5 (degenerate activation)**: both sumS and sumL zero → `ValueError("F5: no activation")` in fusion.
- **F1/F4**: Schema and Θ reject handled by config and guard_penalty; hard-stop policy in guard_config.
- Hard-stop classes stop execution (loader/config validation raise); degraded flags do not stop execution.

---

## TASK 7 — Topology Honesty Check: **PASS**

- `chroma_books_validation_run.py` **does not claim topology from Chroma** in name or behavior; docstring: "Stub traversal + Chroma for books (evidence) only"; "Topology (membership/adjacency) does not come from Chroma unless explicitly ingested."
- README: "stub traversal", "Topology from Chroma only if membership ingested; else stub."
- No adjacency assumed from Chroma unless explicitly ingested (TOPOLOGY-STORAGE-CONTRACT).

---

## TASK 8 — Freeze Record Consistency: **PASS**

- SHA256 in FREEZE_RECORD_v1.json **matches** actual files (A_CORE_STAR_MAP_v1.json, B_SURFACE_LEX_FIELD_v1.json, guard_config_v1.json).
- guard_config hash consistent.
- Version string "lexical-stack-v1.0" / tag consistent in freeze record.
- **repo_commit** stored in FREEZE_RECORD (added in validate_lexical.py).
- No untracked changes in curated A/B at audit time (CI validates and writes checksums).

---

## TASK 9 — Dependency Surface Check: **PASS**

- **hesperia_v03_core_math.py**: imports only `json`, `math`, `pathlib`, `typing`, optional `numpy`. No LLM, no embedding, no chromadb, no book similarity.
- Core pipeline (fusion → traversal → aggregation → metrics) is **independent of embeddings and books**.
- chroma_books_validation_run imports chromadb only for post-resolution books query; metrics are computed before any Chroma call.

---

## TASK 10 — Release Gate Summary

| Gate | Result |
|------|--------|
| Core math contract | **PASS** |
| Determinism | **PASS** |
| Lexical integrity | **PASS** |
| Books non-voting | **PASS** |
| Energy invariants | **PASS** |
| Failure modes | **PASS** |
| Topology honesty | **PASS** |
| Freeze integrity | **PASS** |
| Dependency isolation | **PASS** |

---

## Overall: **RELEASE APPROVED**

All gates PASS. No partial approvals. v0.3 core + lexical stack is **defined and enforceable**. Safe to move to v0.3 major tag.

---

**Artifacts**

- Contract audit detail: `docs/HESPERIA_V03_RELEASE_GATE_AUDIT.md`
- Stress test: `sphere_rag/tests/energy_invariants_stress.py`
- FREEZE_RECORD: `hesperia_lex/curated/FREEZE_RECORD_v1.json` (includes repo_commit)

**Signed**: Gena | HESPERIA v0.3 consolidation | 2026-02-23 | Release gate

---

## Freeze policy (post-tag)

- **Tag**: `hesperia-v0.3.0` marks the release. Do not move or overwrite the tag.
- **Core math**: Do not touch `hesperia_v03_core_math.py`, 22_SPEC, or guard_config contract without a **version bump** (e.g. v0.3.1 or v0.4).
- **Next danger phase (v0.4 territory)**: Expanding lexical size, adjacency ingestion, scaling Chroma topology — structural invariants tested for real. Not in v0.3 scope.
