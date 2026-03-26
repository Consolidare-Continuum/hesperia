<!--
HESPERIA — Hesperia Engine Dynamics
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
See LEGAL_NOTICE.md for full terms.
-->

# **Hesperia Engine Dynamics — Canonical Release v0.5** (master index)

**Product line name:** **Hesperia Engine Dynamics** — deterministic multiscale semantic physics (concept → hex → family → area → signals → HSPR).

**This document** is the **single map**: specs → engine modules → E2E artifacts. **v0.5.1** treats the **in-repo code base** as the full capability envelope (lexical → concept evidence → optional carried concept state / sparse operator → hex → family → area → signals); **clinical domain packs, fixtures, and medical vocabulary** stay outside the **sealed product narrative** and public canon wording (§2, §8). See [ETHAN-MAINLINE-CODE-CARRYOVER-NO-CLINICAL-TERMS.md](governance/working/ETHAN-MAINLINE-CODE-CARRYOVER-NO-CLINICAL-TERMS.md).

**Release narrative:** [specs/release/HESPERIA_v0_5_ENGINE_DYNAMICS_RELEASE.md](../specs/release/HESPERIA_v0_5_ENGINE_DYNAMICS_RELEASE.md)  
**Agents:** [AGENTS.md](../AGENTS.md) · **Awareness:** [HESPERIA_SYSTEM_AWARENESS.md](HESPERIA_SYSTEM_AWARENESS.md) · **Layer vs structure vocabulary:** [LAYER_VOCABULARY_AND_STRUCTURE.md](LAYER_VOCABULARY_AND_STRUCTURE.md)  
**Product surface (Task 4):** [PUBLIC_PRODUCT_SURFACE.md](PUBLIC_PRODUCT_SURFACE.md) · **Sealed release audit (Task 5):** [release/v0.5.1/README.md](../release/v0.5.1/README.md) (historical [v0.5.0](../release/v0.5.0/README.md)) · **Tasks 1–11 wiring:** [ENGINE_TASKS_1_11_INTEGRATION.md](ENGINE_TASKS_1_11_INTEGRATION.md)  
**Optional sparse concept operator (H_total):** [semantic_dynamics_operator_spec.md](semantic_dynamics_operator_spec.md) · **Mainline carryover policy (code vs clinical wording):** [governance/working/ETHAN-MAINLINE-CODE-CARRYOVER-NO-CLINICAL-TERMS.md](governance/working/ETHAN-MAINLINE-CODE-CARRYOVER-NO-CLINICAL-TERMS.md) · **Spec index (Tier 1 + v0.5.1 hooks):** [specs/CANONICAL_INDEX.md](../specs/CANONICAL_INDEX.md)

---

## 1. Canonical release scope (in)

| Layer | Sealed dynamics |
|-------|-----------------|
| **Concept** | Dict-A/B → family hits |
| **Hex** | Microphysics (field ODE + local discrete step), hex→family bridge |
| **Family** | Semantic field equations, observables, KME, TRIZ hooks |
| **Area** | Icosahedral 10+2 topology, public projection to 10 areas |
| **Product signals** | Hotspots, tension, propagation, density, innovation proxy |
| **HSPR** | Field-level + system scalar |
| **E2E** | `run_e2e_all` — [E2E_RUN_ORDER.md](E2E_RUN_ORDER.md) |

---

## 2. Out of canonical release definition (in repo, not product core)

| Item | Note |
|------|------|
| **Clinical / TFP domain collateral** | Domain-specific fixtures (e.g. `tests/fixtures/clinical_tfp/`), modality labels, and experimental runners that **import** `research.clinical_tfp` for interpretation — **not** part of sealed **product** definition or public vocabulary. |
| **legacy/** | Archived only |

**Distinction (v0.5.1):** Shared **implementation** (lexical→concept invariant path, versioned calibration JSON, optional `H_total` / `ψ` update, segmentation with carried state) lives in **`hesperia/nlp`**, **`hesperia/engine`**, and **`assets/data/engine_dynamics_v060/`** and **does** belong to the full in-tree engine; only **clinical semantics and naming** are excluded from mainline canon and shipping narrative per [ETHAN-MAINLINE-CODE-CARRYOVER-NO-CLINICAL-TERMS.md](governance/working/ETHAN-MAINLINE-CODE-CARRYOVER-NO-CLINICAL-TERMS.md).

---

## 3. Specs (file by file)

### `specs/canon/*.md`

| File | Role |
|------|------|
| [semantic_field_canon.md](../specs/canon/semantic_field_canon.md) | Family field ODE; multiscale chain |
| [hex_microphysics_canon.md](../specs/canon/hex_microphysics_canon.md) | Hex substrate, P_HF, P_CH, local §7b |
| [hex_family_bridge.md](../specs/canon/hex_family_bridge.md) | Weighted F ← A_hex |
| [product_signal_layer.md](../specs/canon/product_signal_layer.md) | Product observables |
| [hspr_calibration_index.md](../specs/canon/hspr_calibration_index.md) | System HSPR |

### `specs/dynamics/` (selected long-form)

| File | Role |
|------|------|
| [semantic_field_dynamics.md](../specs/dynamics/semantic_field_dynamics.md) | Family-field stepping (canonical) |
| [TOPOLOGY_INVARIANTS.md](TOPOLOGY_INVARIANTS.md) | Geometry lock |
| [ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md](../specs/dynamics/ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md) | L0–L10 target |
| [E2E_RUN_ORDER.md](E2E_RUN_ORDER.md) | Artifact order |

### Docs (v0.5.1 lexical / concept-state hooks; not Tier-1 canon unless promoted)

| File | Role |
|------|------|
| [semantic_dynamics_operator_spec.md](semantic_dynamics_operator_spec.md) | Sparse bounded `H_total`, segment `ψ`, calibration gate |
| [governance/working/ETHAN-MAINLINE-CODE-CARRYOVER-NO-CLINICAL-TERMS.md](governance/working/ETHAN-MAINLINE-CODE-CARRYOVER-NO-CLINICAL-TERMS.md) | What may enter mainline: **code decisions only**; no medical terms in canon/shipping |

---

## 4. Engine modules

| Component | Spec |
|--------|------|
| `hesperia/extensions/dynamics/*` | Ethan + semantic_field_v1 |
| `hesperia/engine/hex_*.py`, `hex_outputs/*` | Hex canon + product maps |
| `hesperia/engine/hex_family_bridge.py` | Bridge spec |
| `hesperia/engine/product_signals.py`, `hspr_index.py` | Product + system KPI |
| `hesperia/engine/sealed_multiscale_stack.py` | One-shot canonical stack |
| `hesperia/engine/kme/*` | KME |

---

## 5. E2E (v0.5)

| Core | Testing-only |
|------|--------------|
| Most artifacts incl. **sealed_multiscale**, **hex_microstructure_tfp** | **tfp_smoke** |

---

## 6. Post–v0.5.0 maintenance

Future refactors (v0.5.1+): sphere vs `core.layers`; sparse hex weights; projection aliases; 10+2 vs public 10. See [ENGINE_DYNAMICS_CANONICAL_NAMING_v0.5.md](ENGINE_DYNAMICS_CANONICAL_NAMING_v0.5.md).

---

## 7. Release closure

**Canonical Dynamics Release v0.5** is documented in-repo: [CHANGELOG.md](../CHANGELOG.md), [HESPERIA_v0_5_ENGINE_DYNAMICS_RELEASE.md](../specs/release/HESPERIA_v0_5_ENGINE_DYNAMICS_RELEASE.md). **Current enforcement seal:** **`v0.5.1`** / **`hesperia-engine-dynamics-v0.5.1`** · **Historical baseline:** **`v0.5.0`** / **`hesperia-engine-dynamics-v0.5.0`**. Resume R&D on the next minor after the v0.5.1 gate is green.

---

## 8. v0.5.1 full code envelope: promote engine work into the main execution_flow

**Intent:** Anything structurally useful that was first wired through experimental bundles (TFP file execution_flow, clinical topology helpers) should be **available from shared modules** and, where appropriate, **reachable from the main E2E / sealed stack** — without importing clinical **meaning** into product language.

| Direction | Action |
|-----------|--------|
| **Concept evidence + invariant path** | Already centralized in `hesperia/nlp/session_parser.py` + `hesperia/nlp/tfp_activation.py` (rename to neutral component name is a follow-up refactor). |
| **Sparse concept operator (`H_total`, `ψ`)** | Spec: [semantic_dynamics_operator_spec.md](semantic_dynamics_operator_spec.md); enable via `semantic_dynamics` in `tfp_signal_calibration_v2.json` after a release-pinned matrix covers the active concept index. |
| **Segmentation + carried state** | `research/clinical_tfp/session_topology.py` and `hesperia/nlp/session_topology.py` thread `psi_prev` when the operator is on; consider invoking the same path from non-clinical runners. |
| **Role-weighted lexical aggregation** | **`analyze_session_speaker_aware`** — **ML-07 closed (2026-03-26):** documented as **multi-channel / role-weighted lexical evidence** (utterance streams × per-stream weights → combined areas/families/concepts). API docstring + this row; internal stream keys follow the dialogue parser; **no care-setting claims** in canon. |
| **Stage / phase labels from areas** | Keep **`research.clinical_tfp.stage_detection`** in research; if mainline needs discrete phases, add a **domain-neutral** mapper behind a non-clinical enum. |
| **Gaps vs `run_e2e_product` / minimal product path** | Optional: one internal E2E step that runs lexical→concept→(optional `H`)→projection smoke **without** clinical fixtures; extend release audit keys when `semantic_dynamics.operator_enabled` becomes true by default. |

**`analyze_session_speaker_aware` (mainline description):** Structured dialogue is parsed into utterance streams; each stream’s markers are scaled by a numeric **weight**, then aggregated into a single lexical-evidence vector (`areas` / `families` / `concepts`) plus per-stream breakdowns. **Canonical product wording:** *multi-channel, role-weighted lexical evidence*—deterministic marker physics only; stream labels in code and JSON reflect the dialogue parser’s schema, not a medical or therapeutic ontology in sealed narrative.

**Backlog detail:** [governance/working/ETHAN-MAINLINE-CODE-CARRYOVER-NO-CLINICAL-TERMS.md](governance/working/ETHAN-MAINLINE-CODE-CARRYOVER-NO-CLINICAL-TERMS.md) (Section 6).

---

*Hesperia Engine Dynamics — Canonical Release v0.5 — documentation index.*
