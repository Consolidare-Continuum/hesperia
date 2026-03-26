# Canonical specification index (Tier 1)

All **binding** system definitions for Hesperia Engine Dynamics **v0.5.0** are listed below.  
**Rule:** If a behavior is not reachable from this index, it is **not** part of the sealed system definition.

| ID | Path | Topic |
|----|------|--------|
| HES-SPEC-CORE-SYSTEM-ARCH | [core/system_architecture.md](core/system_architecture.md) | Concept → hex → family → area execution_flow |
| HES-SPEC-CORE-HEX-MICRO | [core/hex_microphysics_canon.md](core/hex_microphysics_canon.md) | Hex state, adjacency, local update, continuous equation |
| HES-SPEC-CORE-FAMILY-AGG | [core/family_aggregation.md](core/family_aggregation.md) | \(F_j = \sum_h w_{hj} A_h\) |
| HES-SPEC-CORE-AREA-AGG | [core/area_aggregation.md](core/area_aggregation.md) | Area sums over families |
| HES-SPEC-CORE-PRODUCT-OBS | [core/product_observables.md](core/product_observables.md) | Hotspot, propagation, density (not **I**) |
| HES-SPEC-DYN-SEMANTIC-FIELD | [dynamics/semantic_field_dynamics.md](dynamics/semantic_field_dynamics.md) | Family field **F** — **only** canonical dynamics equations |
| HES-SPEC-CAL-SYSTEM | [calibration/calibration_system.md](calibration/calibration_system.md) | Classes A/B/C, registry, procedure |
| HES-SPEC-CAL-HSPR | [calibration/hspr_index.md](calibration/hspr_index.md) | HSPR_sys + HCI |
| HES-SPEC-TRIZ-CONTRADICTION | [triz/contradiction_engine.md](triz/contradiction_engine.md) | Typed relations, pair score, ordering |
| HES-SPEC-TRIZ-INNOVATION | [triz/innovation_metrics.md](triz/innovation_metrics.md) | \(I = C_d \cdot N\) |
| HES-SPEC-DLCR-HP | [canon/lexical_concept/SPEC__DLCR_HP_Master_v0_6_0.md](canon/lexical_concept/SPEC__DLCR_HP_Master_v0_6_0.md) | Deterministic lexical-concept bridge + hex projection; **§ fragments + scale:** [canon/lexical_concept/README.md](canon/lexical_concept/README.md) |
| HES-SPEC-SCHEMA-PUBLIC-OUT | [schema/public_output_schema.md](schema/public_output_schema.md) | Public JSON shape (mirror of `.json`) |
| HES-SPEC-SYSTEM-GOV | [system/versioning_and_governance.md](system/versioning_and_governance.md) | Version + structure + spec tiers |

**YAML / data under `specs/canon/`** (via `spec/` symlink) remain authoritative for loaders where noted in registry docs.

**Inventory / classification:** [INVENTORY.md](INVENTORY.md).

---

### v0.5.1 implementation anchors (not Tier-1 until promoted into `specs/canon/`)

These documents govern **in-tree engine code** (lexical → concept → optional sparse operator → multiscale stack) for seal **v0.5.1** without extending Tier-1 sealed equations until explicitly migrated.

| Link | Role |
|------|------|
| [docs/governance/working/ETHAN-MAINLINE-CODE-CARRYOVER-NO-CLINICAL-TERMS.md](../docs/governance/working/ETHAN-MAINLINE-CODE-CARRYOVER-NO-CLINICAL-TERMS.md) | Mainline carryover: **implementation and structure only**; **no medical/clinical vocabulary** in canon or shipping narrative |
| [docs/semantic_dynamics_operator_spec.md](../docs/semantic_dynamics_operator_spec.md) | Optional fixed sparse concept operator (`H_total`), segment state `ψ`, calibration gate |
| [docs/HESPERIA_v0_5_ENGINE_DYNAMICS.md](../docs/HESPERIA_v0_5_ENGINE_DYNAMICS.md) | Master index §8: full **code envelope** vs clinical collateral |

**Master index cross-link:** [docs/HESPERIA_v0_5_ENGINE_DYNAMICS.md](../docs/HESPERIA_v0_5_ENGINE_DYNAMICS.md) also points here for Tier-1 discovery.
