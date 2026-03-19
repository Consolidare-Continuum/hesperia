<!--
HESPERIA — Reference Architecture Definition (RAD)
Grace — spec triage workflow complete.
-->

# Grace triage report — spec corpus

**Date:** 2026-03-18 (workflow execution)  
**Task ref:** [../TRIAGE_TASK_GRACE.md](../TRIAGE_TASK_GRACE.md)  
**Scope:** Items §1 A–E of triage task (18 docs). No code or legacy changes.

---

## 1. Summary table

| # | Document | Status | Priority | Notes |
|---|----------|--------|----------|-------|
| 1 | ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md | **needs edit** | P1 | Two equation namespaces (H0–H9 vs extended H1–H9) documented in §13 but still cognitively heavy; cross-ref VARIABLE_CATALOG should say H0–H9 for wire + extended for lattice |
| 2 | HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md | **OK** | P2 | Narrative + §9 paths; no committed registry yet — expected |
| 3 | calibration/README.md | **OK** | P2 | Honest placeholder |
| 4 | dynamics_parameter_registry.example.yaml | **needs edit** | P2 | Only 3 params; calibration spec lists dozens — mark as “stub” or expand 10–15 canonical symbols |
| 5 | HESPERIA_SYSTEM_AWARENESS.md | **OK** | P2 | Dense but navigable; links valid |
| 6 | research/HESPERIA_RAD_DEEP_RESEARCH_2026-03-18.md | **OK** | P2 | Long; keep as archive; competitive table is illustrative |
| 7 | research/README.md | **OK** | P2 | Minimal index — sufficient |
| 8 | HESPERIA_REPOSITORY_MAP.md | **OK** | P2 | Many outbound links — spot-check on edit passes |
| 9 | HESPERIA_DEPENDENCY_GRAPH.md | **merge candidate** | P1 | Layers 0–11 + runtime vs **L0–L10** dynamics wire — **two views**; add 12-row **crosswalk** (L0≈input, L1–L2≈lexicon+NLP, L4–L6≈sphere+KME slices, etc.) or link to ETHAN §A.2 |
| 10 | HESPERIA_VARIABLE_CATALOG.md | **needs edit** | P1 | Dynamics blurb says “H1–H9” — **should say H0–H9 compact + Part B extended** to match ETHAN |
| 11 | HESPERIA_PRODUCT_LINES.md | **OK** | P2 | Complements COMMERCIAL_TRIZ; intentional overlap |
| 12 | HESPERIA_PRODUCT_STACK_MAP.md | **OK** | P2 | Static stack + future dynamics — fingerprint present; L0–L10 noted |
| 13 | COMMERCIAL_TRIZ_PRODUCTS.md | **OK** | P2 | API-oriented; product lines are market-oriented |
| 14 | E2E_RUN_ORDER.md | **OK** | P0 | Matches `run_e2e_all` **19** baseline JSON (+ optional field dynamics; `E2E_OUTPUTS`) |
| 15 | TOPOLOGY_INVARIANTS.md | **OK** | P0 | No dynamics spec contradicts 12/288/72k; Ethan uses same |
| 16 | AGENTS.md | **needs edit** | P2 | Awareness + dynamics + calibration + **Grace triage** in one block — **split** into bullet list or “See docs/specs/README.md” hub |
| 17 | specs/README.md | **needs edit** | P1 | **[DOC_INDEX.md](../DOC_INDEX.md) link broken** — file absent at `docs/DOC_INDEX.md` |
| 18 | README.md (root) | **OK** | P2 | v0.5 + CHANGELOG + 19-artifact E2E; docs hub via HESPERIA_v0_5 |

**Legend:** OK = no mandatory change this pass · needs edit = small fix recommended · merge candidate = add crosswalk, don’t delete.

---

## 2. §3 Conflicts — Grace decisions

| Conflict | Decision |
|----------|----------|
| **H0–H9 vs extended H1–H9** | **Add** `specs/dynamics/DYNAMICS_EQUATION_INDEX.md` (single table: compact ID, extended ID, name, section) **or** expand ETHAN §A.4 + §13 into one printable matrix. Prefer **separate index file** ≤80 lines to keep ETHAN readable. |
| **Dependency layers vs L0–L10** | **Two views:** Dependency graph = **testing / change-impact** (what breaks if you edit X). L0–L10 = **temporal dynamics pipeline**. Add **crosswalk table** in DEPENDENCY_GRAPH appendix **or** one row in new equation index doc. |
| **Calibration registry path** | **Canonical when implemented:** `assets/calibration/dynamics_parameter_registry.yaml` (runtime-adjacent). **Authoring / review:** copy or symlink note from `specs/calibration/` — document in calibration spec §9. |
| **24 families per area** | **Not asserted** in committed Ethan/calibration specs as fixed constant; VARIABLE_CATALOG uses TOPOLOGY language. **Rule:** any future draft mentioning “24 per area” must say **~24 mean / 240÷10 operational**. |

---

## 3. Top 5 recommended edits (file + one-line fix)

1. **docs/specs/README.md** — Replace or remove dead `DOC_INDEX.md` link; point to `HESPERIA_SYSTEM_AWARENESS.md` + `specs/README` table as hub.  
2. **docs/HESPERIA_VARIABLE_CATALOG.md** — Dynamics paragraph: **H0–H9 (wire) + Part B extended IDs** instead of bare “H1–H9”.  
3. **docs/HESPERIA_DEPENDENCY_GRAPH.md** — Add **“Dynamics crosswalk (L0–L10)”** subsection with 5–8 rows mapping L-layers to dependency layers.  
4. **docs/HESPERIA_DEPENDENCY_GRAPH.md** — Footer link text: **H0–H9** not “H1–H9” for ETHAN.  
5. **AGENTS.md** — Replace long dynamics paragraph with **3 bullets** + link to `docs/specs/README.md`.

---

## 4. Top 3 new artifacts (recommended)

| Artifact | Purpose |
|----------|---------|
| **specs/dynamics/DYNAMICS_EQUATION_INDEX.md** | Single glossary: H0–H9 ↔ extended IDs ↔ layer (L2/L4/L5…) |
| **docs/specs/DYNAMICS_L_LAYER_CROSSWALK.md** *(optional merge into DEPENDENCY_GRAPH)* | L0–L10 ↔ dependency layers 0–11 |
| **assets/calibration/dynamics_parameter_registry.yaml** *(when seeded)* | Authoritative Class B registry; keep example in specs/calibration as mirror |

---

## 5. Governance / RAD

- No spec triaged here **violates** TOPOLOGY_INVARIANTS or RAD freeze narrative.  
- Dynamics + calibration remain **forward-looking**; no shipping surface change implied.  
- **Ethan spec v3** remains **source of truth for implementation order** until v0.2 signed.

---

## 6. Grace sign-off

Triage **complete**. Next owner: **governance** (approve edits 1–5) or **Ethan** (equation index content). Optional: execute checklist in [../TRIAGE_CHECKLIST.md](../TRIAGE_CHECKLIST.md).

---

*Grace — spec corpus triage workflow.*
