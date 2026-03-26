<!--
HESPERIA — Hesperia Engine Dynamics v0.5
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. See LEGAL_NOTICE.md.
-->

# Canonical naming — Engine Dynamics v0.5

**Purpose:** One vocabulary for code, docs, and APIs so future work stays aligned with the **sealed dynamics** model. Prefer these terms in new modules and public copy.

**Disambiguation:** Do not overload **L*** across ladders. Use **R1–R10** (metric cascade), **Tier 0–11** (dependency), **F0–F10** (Ethan field phases). See [LAYER_VOCABULARY_AND_STRUCTURE.md](LAYER_VOCABULARY_AND_STRUCTURE.md).

## Product & release

| Use | Avoid (informal / legacy) |
|-----|---------------------------|
| **Hesperia Engine Dynamics** | “Hesperia RAD” alone when meaning the dynamics product line |
| **v0.5.0** — `pyproject.toml`, `hesperia.__version__`, API OpenAPI, `release_meta.ENGINE_DYNAMICS_VERSION` | Unversioned “dynamics stack”; mismatched version strings across surfaces |
| **KME** (Knowledge Metrics Engine), component `hesperia.engine.kme` | Scattered “domain metrics” without KME context |

## Multiscale chain (normative order)

1. **Concept** — Dict A/B attribution → family hits.  
2. **Hex** — Discrete hex substrate; **hex microphysics** (field ODE + local step).  
3. **Hex→family bridge** — Weighted aggregation \(F_j = \sum_h w_{hj} A_h\); weights in `data/topology/hex_family_weights.json`.  
4. **Family** — Semantic field equations, observables, KME hooks.  
5. **Area** — Icosahedral **10+2** topology internally; **public projection** exposes **10** operational areas.  
6. **Product signals** — Hotspots, tension/contradiction, propagation, density, innovation proxy.  
7. **HSPR** — Field-level + **system** scalar (`hspr_index`).

## Python modules ↔ concepts

| Concept | Primary component(s) |
|---------|-------------------|
| Sealed one-shot chain | `hesperia.engine.sealed_multiscale_stack` |
| Hex microphysics | `hesperia.engine.hex_dynamics` |
| Bridge | `hesperia.engine.hex_family_bridge` |
| Product layer | `hesperia.engine.product_signals` |
| System KPI | `hesperia.engine.hspr_index` |
| Field calibration helpers | `hesperia.engine.calibration` (`hspr_field`, …) |

## Spec files (Tier 1 — binding)

**Index:** `specs/CANONICAL_INDEX.md`

| Topic | Path |
|-------|------|
| System architecture | `specs/core/system_architecture.md` |
| Semantic field dynamics (\(\mathbf{F}\)) | `specs/dynamics/semantic_field_dynamics.md` |
| Hex substrate | `specs/core/hex_microphysics_canon.md` |
| Family aggregation | `specs/core/family_aggregation.md` |
| Area aggregation | `specs/core/area_aggregation.md` |
| Product observables | `specs/core/product_observables.md` |
| TRIZ innovation **I** | `specs/triz/innovation_metrics.md` |
| HSPR / HCI | `specs/calibration/hspr_index.md` |
| Public JSON shape | `specs/schema/public_output_schema.md` |

`specs/canon/*.md` names above are **redirects** only (historical paths / `spec/` symlink).

## Topology language

- **12-node icosahedral surface graph** — 10 operational areas + 2 reserved service areas.  
- Say **“public 10 areas”** when describing customer-facing outputs; say **10+2** when discussing full internal geometry.

## E2E artifacts

- Baseline count: **19** JSON files from `run_e2e_all`; **+1** for optional field dynamics.  
- **Sealed multiscale** artifact: `run_output_e2e_sealed_multiscale.json`.  
- **TFP / hex microstructure TFP** steps are **testing collateral**, not the v0.5 canonical product definition (still run in full E2E).

## Active stack roots (AGENTS.md)

Use: `core/`, `hesperia/` (incl. `hesperia/extensions/`), `runtime/`, `lexicon/`, `research/`, `specs/`, `schemas/`, `examples/`, `outputs/` (generated), `tools/`, `assets/`, `tests/`, `docs/`, `legacy/`.  
Do not reintroduce deprecated top-level roots (`sphere_rag/`, `hesperia_lex/`, …) as architecture.

---

*Hesperia Engine Dynamics — Canonical Release v0.5 — naming guide.*
