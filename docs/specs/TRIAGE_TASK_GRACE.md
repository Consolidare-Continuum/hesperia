<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
See LEGAL_NOTICE.md for full terms.
-->

# Triage task — Grace (spec corpus)

**Assigned by:** Ethan (dynamics / calibration thread)  
**Goal:** **Triage all specs listed below** — inventory, consistency, gaps, ownership, and recommended next actions. Output: a short **triage report** (same folder or `docs/specs/triage/GRACE_TRIAGE_REPORT.md`) plus optional issue checklist.

**Doctrine:** Calibration and dynamics docs are **governance-sensitive**; triage should flag conflicts with [TOPOLOGY_INVARIANTS.md](../TOPOLOGY_INVARIANTS.md), [AGENTS.md](../../AGENTS.md), and shipping freeze docs.

---

## 1. Corpus to triage (read in this order)

### A — Dynamics & calibration (Ethan thread)

| # | Path | What to check |
|---|------|----------------|
| 1 | [ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md](ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md) | Part A L0–L10 vs Part B extended IDs; H0–H9 vs H1–H9 “extended”; duplicate narrative; link health |
| 2 | [HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md](HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md) | Alignment with dynamics params in (1); empty promises vs actionable §9 paths |
| 3 | [calibration/README.md](calibration/README.md) | Placedholder vs committed registry; single source of truth |
| 4 | [calibration/dynamics_parameter_registry.example.yaml](calibration/dynamics_parameter_registry.example.yaml) | Completeness vs §2 of calibration spec; naming consistency |

### B — System awareness & research

| # | Path | What to check |
|---|------|----------------|
| 5 | [HESPERIA_SYSTEM_AWARENESS.md](../HESPERIA_SYSTEM_AWARENESS.md) | Stale links; overlap with (1)(2); TFP boundary statement vs AGENTS |
| 6 | [research/HESPERIA_RAD_DEEP_RESEARCH_2026-03-18.md](../research/HESPERIA_RAD_DEEP_RESEARCH_2026-03-18.md) | Redundancy vs (5); cite cleanup; competitive table accuracy |
| 7 | [research/README.md](../research/README.md) | Index completeness |

### C — Product & variable maps

| # | Path | What to check |
|---|------|----------------|
| 8 | [HESPERIA_REPOSITORY_MAP.md](../HESPERIA_REPOSITORY_MAP.md) | Links to all children; “suggested GitHub description” still valid |
| 9 | [HESPERIA_DEPENDENCY_GRAPH.md](../HESPERIA_DEPENDENCY_GRAPH.md) | Layer model vs L0–L10 in (1) — note divergence or merge suggestion |
| 10 | [HESPERIA_VARIABLE_CATALOG.md](../HESPERIA_VARIABLE_CATALOG.md) | ~176 count vs dynamics outputs; Engine vs Derived tags |
| 11 | [HESPERIA_PRODUCT_LINES.md](../HESPERIA_PRODUCT_LINES.md) | Lines A–G vs TRIZ commercial doc |
| 12 | [HESPERIA_PRODUCT_STACK_MAP.md](../HESPERIA_PRODUCT_STACK_MAP.md) | Stack vs L0–L10; fingerprint step alignment |
| 13 | [COMMERCIAL_TRIZ_PRODUCTS.md](../COMMERCIAL_TRIZ_PRODUCTS.md) | API paths vs runtime; overlap with (11) |

### D — Operational anchors

| # | Path | What to check |
|---|------|----------------|
| 14 | [E2E_RUN_ORDER.md](../E2E_RUN_ORDER.md) | Still 9 artifacts; matches `run_e2e_all` |
| 15 | [TOPOLOGY_INVARIANTS.md](../TOPOLOGY_INVARIANTS.md) | Any dynamics spec contradicts 10+2 / hex counts |
| 16 | [AGENTS.md](../../AGENTS.md) | Awareness + calibration + dynamics pointers — one paragraph too long? |

### E — Entry points

| # | Path | What to check |
|---|------|----------------|
| 17 | [specs/README.md](README.md) | Table complete; dead links |
| 18 | [README.md](../../README.md) | “What’s in the repo” not overloaded |

---

## 2. Triage dimensions (score each doc)

Use **P0 / P1 / P2** or **Keep / Merge / Split / Deprecate**.

| Dimension | Question |
|-----------|----------|
| **Accuracy** | Matches code & TOPOLOGY_INVARIANTS today? |
| **Uniqueness** | Duplicates another doc’s job? |
| **Navigability** | Can a new agent find it in ≤2 hops from README or AGENTS? |
| **Implementability** | Clear “next engineering step” or only narrative? |
| **Governance** | Conflicts with RAD freeze / shipping policy? |

---

## 3. Specific conflicts to resolve (Grace decision log)

1. **Equation indices:** Part A **H0–H9** (compact wire) vs Part B **extended H1–H9** (resolution, hex gradients). Recommend: one **master glossary** table in ETHAN spec or separate `DYNAMICS_EQUATION_INDEX.md`?
2. **Dependency graph layers** (0–11) vs **L0–L10** — same story or two views? Merge diagram or crosswalk table?
3. **Calibration registry location:** `docs/specs/calibration/` vs `assets/calibration/` — pick canonical when first YAML lands.
4. **“24 families per area”** in user drafts vs **240 public families / 10 areas** — ensure all specs use TOPOLOGY language.

---

## 4. Deliverables (Grace)

1. **`docs/specs/triage/GRACE_TRIAGE_REPORT.md`** (create folder if needed) with:
   - Summary table: doc → status (OK / needs edit / merge candidate)
   - Top 5 recommended edits (file + one-line fix)
   - Top 3 **new** artifacts if any (e.g. equation index)
2. Optional: **`docs/specs/TRIAGE_CHECKLIST.md`** — checkbox version of §1 for tracking.

---

## 5. Non-goals for this triage

- Do not rewrite dynamics math without Ethan/governance sign-off.  
- Do not delete deep research or awareness docs without archive note.  
- Do not change `legacy/` or production API contracts in this pass unless P0 bug.

---

## 6. Handoff line

> **Grace:** Please run §1 corpus pass, apply §2 dimensions, resolve §3 in the report, and land §4 deliverables. Ethan dynamics + calibration specs are **source of truth for future implementation order** until superseded by a signed v0.2.

---

*Triage task created for Grace — spec corpus consolidation.*
