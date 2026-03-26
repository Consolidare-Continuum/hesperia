# Vocabulary migration — inventory (plan only; **do not execute** from this file)

**Purpose:** Single checklist of **terms to change** and **files to touch** when adopting **R1–R10**, **Tier 0–11**, **F0–F10**, semantic **field phase names**, **Attribution**, and **multiscale chain** language repo-wide.

**Normative vocabulary:** [LAYER_VOCABULARY_AND_STRUCTURE.md](../../LAYER_VOCABULARY_AND_STRUCTURE.md)  
**Sequencing:** [ETHAN-LAYER-VOCABULARY-AND-REPO-STRUCTURE-PLAN.md](ETHAN-LAYER-VOCABULARY-AND-REPO-STRUCTURE-PLAN.md)

**Status:** Inventory only — no mass edits until Phase 0 ACK.

---

## 1. Terms to alter (conceptual map)

| Legacy / overloaded | Replace in **new prose** with | Notes |
|---------------------|-------------------------------|--------|
| Sphere “Layer L1–L9”, “L10” | **Metric cascade** stages **R1–R9**, **R10** | Code may keep `layer_id` / `L1` until Phase 4 |
| “L1–L9 execution_flow” (generic) | **R1–R9** or **metric cascade** | Disambiguate from Ethan |
| Dependency “Layer 0–11” | **Tier 0–Tier 11** | Optional table shorthand **T0–T11** + legend |
| Ethan Part A “L0–L10” | **Field phases F0–F10** + **semantic name** per phase | Add name column in spec (e.g. F2 = Attribution …) — **to be filled from Part A** |
| “word layers” / informal | **Attribution** (lexical front) | No R/F index |
| “layers” for concept→HSPR | **Multiscale chain** + step names | Already named |
| Bare “L5”, “L7” in docs | Either **R5**, **F7**, or **Tier *k*** per input_context | Never ambiguous bare L |
| `run_l1_through_l9`, CLI help text | Keep **filename** in Phase 1–2; update **user-facing strings** to “metric cascade R1–R9” | Rename component → Phase 4 + release note |
| `layer_1` … `layer_9` (core paths) | Docstrings: **R1–R9**; symbols optional enum later | Large surface |

**Ethan semantic alignment (additional, not a letter change):** For each **F*k***, add a **short semantic title** (one line) in ETHAN spec — e.g. what “really happens” at that phase — **list to be drafted against Part A section boundaries** (separate sub-table in §2.1 below after manual spec read).

---

## 2. Files to alter — **Tier A (binding / entry traffic)**

High impact; do first after Phase 0.

| File | Alter |
|------|--------|
| [specs/dynamics/ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md](../../../specs/dynamics/ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md) | Part A: **F0–F10**; terminology box; per-phase **semantic names**; legacy footnote “formerly L0–L10” once per major section |
| [docs/LAYER_PIPELINE_ORDER.md](../../LAYER_PIPELINE_ORDER.md) | Title + table: **Metric cascade (R1–R10)**; stage column R1…R10 |
| [docs/HESPERIA_DEPENDENCY_GRAPH.md](../../HESPERIA_DEPENDENCY_GRAPH.md) | Headings **Tier 0 … Tier 11**; intro legacy map; crosswalk table F vs R vs Tier |
| [docs/HESPERIA_SYSTEM_SPEC_v1.md](../../HESPERIA_SYSTEM_SPEC_v1.md) | Registry narrative: **R1–R10**; dual column legacy L if needed |
| [docs/HESPERIA_v0_5_ENGINE_DYNAMICS.md](../../HESPERIA_v0_5_ENGINE_DYNAMICS.md) | Index links; multiscale vs metric cascade wording |
| [AGENTS.md](../../../AGENTS.md) | `core/` bullet: **metric cascade R1–R9** (not “L1–L9” alone); CLI line: **R1–R9** narrative + keep command name note |
| [docs/ENGINE_DYNAMICS_CANONICAL_NAMING_v0.5.md](../../ENGINE_DYNAMICS_CANONICAL_NAMING_v0.5.md) | Multiscale chain + pointer to R/Tier/F |
| [docs/LAYER_VOCABULARY_AND_STRUCTURE.md](../../LAYER_VOCABULARY_AND_STRUCTURE.md) | Already normative; tweak if F semantic table added centrally vs only in Ethan spec |

---

## 3. Files — **Tier B (internal registries & math)**

| File | Alter |
|------|--------|
| [docs/internal/MATH_LAYER_REGISTRY_v1.md](../../internal/MATH_LAYER_REGISTRY_v1.md) | Column **R*k*** + legacy L*k* |
| [docs/internal/PIPELINE_LAYER_REGISTRY_v1.md](../../internal/PIPELINE_LAYER_REGISTRY_v1.md) | Same; clarify vs **F** orchestration |
| [docs/NOTE__2026-02-24_Layer1_Instrumentation_v0_4.md](../../NOTE__2026-02-24_Layer1_Instrumentation_v0_4.md) | Historical note at top: **R*** naming; body optional gradual replace |

---

## 4. Files — **Tier C (governance & operator docs)**

Grep hit set (~40+); batch in one or two PRs by theme.

**Governance (`docs/governance/*.md` and `working/`):**  
`ENTRYPOINT_CLASSIFICATION_v1.md`, `VOCABULARY_SEPARATION_POLICY_v1.md`, `MATH_NAMING_SEALING_POLICY_v1.md`, `PUBLIC_PIPELINE_NARRATIVE_v1.md`, `PACKAGE_BOUNDARY_POLICY_v1.md`, `RUNTIME_MODE_POLICY_v1.md`, `PUBLIC_METRIC_EXPOSURE_POLICY_v1.md`, `MATH_SERIALIZATION_POLICY_v1.md`, `SERIALIZATION_AUDIT_v1.md`, `SHIPPING_*`, `PUBLIC_*`, `SEALED_*`, `FACADE_*`, `REFLECTION_*`, etc. — replace **layer** where it means **R** or **Tier** with correct term.

**Ethan / Gena working notes:**  
`ETHAN-OPEN-WORKFLOW-PROCEED.md`, `ETHAN-DLCR-*.md`, `ETHAN-CALIBRATION-*.md`, `ETHAN-TFP-*.md`, `GENA-OPEN-WORKFLOW-PROCEED.md`, `GENA-DYNAMICS-*.md`, `REPORT-ETHAN-DYNAMICS-IMPLEMENTATION.md`, `TASK-GRACE-ETHAN-*.md` — **F*k*** + semantic short names in new paragraphs.

**Maps / spine / awareness:**  
`ACTIVE_STACK_MAP_v0_5_0.md`, `RUNTIME_EXECUTION_SPINE_v0_5_0.md`, `HESPERIA_REPOSITORY_MAP.md`, `HESPERIA_SYSTEM_AWARENESS.md`, `HESPERIA_PRODUCT_STACK_MAP.md` (if L-laden), `E2E_RUN_ORDER.md`, `CURSOR_OPEN_WORKFLOW.md`, `DOMAIN_METRICS_REFERENCE.md`, `ARCHITECTURE_BOUNDARIES.md`.

**Specs / triage / audit:**  
`docs/specs/output_*.md`, `TRIAGE_TASK_GRACE.md`, `docs/audit/*.md`, `docs/testing/TFP_KERNBERG_TESTING.md`, `FREEZE_v0_6.md`, `RUN_FROM_SCRATCH.md`, `OPERATIONAL_CHECKLIST.md`.

---

## 5. Files — **Tier D (`specs/` outside dynamics)**

| Area | Examples |
|------|----------|
| Dynamics / calibration | `HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md`, `DYNAMICS_EQUATION_INDEX.md`, `semantic_field_dynamics.md` |
| Architecture | `LEVEL1_AREA_STRUCTURE.md` (name collision with “Level” vs **Tier** — review disambiguation), `LEVEL15_CALIBRATION_AND_SPARSIFICATION.md`, `dossier_schema_v1.md` |
| Lexical v0.6 canon | `specs/canon/lexical_concept/*.md` — **Attribution** / **F** references where they mean Ethan vs **R** |
| Inventory | `specs/INVENTORY.md` |

---

## 6. Code & tooling — **Tier E (later; breaking risk)**

**Do not rename modules in Phase 1.** Track for Phase 2–4:

| Locus | Alter |
|-------|--------|
| `runtime/execution_flow/run_l1_through_l9.py` | Docstrings, `--help`, logs: **R1–R9**; optional symlink/alias `run_metric_cascade_r1_r9.py` later |
| `runtime/execution_flow/run_l1_l2.py`, `run_l1_l2_l3.py` | Same |
| `sphere/execution_flow/pipeline_runner.py`, `layer_registry` | Comments + enum aliases **MetricStageId** |
| `core/layer_*` or `core/layers/*` | Folder naming is legacy; doc crosswalk only unless v0.6+ rename approved |
| Tests referencing “L5” in assertion messages | Clarify **R5** in failure text |
| `CHANGELOG.md`, `CONTRIBUTING.md` | Entry when user-visible strings change |

**JSON / public schema:** Any `layer` key in **public** outputs — **Phase 4** + snapshot + seal.

---

## 7. Ethan **F*k*** → semantic name table (to be filled)

*Execute later:* read `ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md` Part A section list and fill:

| Phase ID | Proposed semantic name (draft) | Spec section anchor |
|----------|--------------------------------|---------------------|
| F0 | *TBD* | *TBD* |
| … | … | … |
| F10 | *TBD* | *TBD* |

---

## 8. Suggested PR split (when execution is allowed)

1. **PR1 — Tier A + vocabulary hub** (docs only; Ethan F + semantic table).  
2. **PR2 — Tier B internal registries.**  
3. **PR3 — Tier C governance batch.**  
4. **PR4 — Tier D specs.**  
5. **PR5 — Tier E** comments/help only.  
6. **PR6 — Breaking** identifiers / CLI rename / JSON (release gated).

---

*Inventory maintained for Ethan vocabulary migration — plan only.*
