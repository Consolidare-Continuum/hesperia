<!--
HESPERIA — Hesperia Engine Dynamics
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
See LEGAL_NOTICE.md for full terms.
-->

# **Hesperia Engine Dynamics — Canonical Release v0.5** (master index)

**Product line name:** **Hesperia Engine Dynamics** — deterministic multiscale semantic physics (concept → hex → family → area → signals → HSPR).

**This document** is the **single map**: specs → engine modules → E2E artifacts. **TFP testing grounds** are out of the **canonical release** definition (§2); they remain in-tree for CI only.

**Release narrative:** [specs/release/HESPERIA_v0_5_ENGINE_DYNAMICS_RELEASE.md](../specs/release/HESPERIA_v0_5_ENGINE_DYNAMICS_RELEASE.md)  
**Agents:** [AGENTS.md](../AGENTS.md) · **Awareness:** [HESPERIA_SYSTEM_AWARENESS.md](HESPERIA_SYSTEM_AWARENESS.md)  
**Product surface (Task 4):** [PUBLIC_PRODUCT_SURFACE.md](PUBLIC_PRODUCT_SURFACE.md) · **Sealed release audit (Task 5):** [release/v0.5.0/README.md](../release/v0.5.0/README.md) · **Tasks 1–11 wiring:** [ENGINE_TASKS_1_11_INTEGRATION.md](ENGINE_TASKS_1_11_INTEGRATION.md)

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
| **TFP testing grounds** | `assets/testing/tfp_kernberg/` — clinical regression collateral; E2E step 10; **not** part of Engine Dynamics v0.5 spec. |
| **legacy/** | Archived only |

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

---

## 4. Engine modules

| Module | Spec |
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

**Canonical Dynamics Release v0.5** is documented in-repo: [CHANGELOG.md](../CHANGELOG.md), [HESPERIA_v0_5_ENGINE_DYNAMICS_RELEASE.md](../specs/release/HESPERIA_v0_5_ENGINE_DYNAMICS_RELEASE.md). **Tags:** **`v0.5.0`** + **`hesperia-engine-dynamics-v0.5.0`** (same commit; sync: `git push origin v0.5.0 hesperia-engine-dynamics-v0.5.0`). Resume R&D on the next minor.

---

*Hesperia Engine Dynamics — Canonical Release v0.5 — documentation index.*
