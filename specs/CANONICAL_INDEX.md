# Canonical specification index (Tier 1)

All **binding** system definitions for Hesperia Engine Dynamics **v0.5.0** are listed below.  
**Rule:** If a behavior is not reachable from this index, it is **not** part of the sealed system definition.

| ID | Path | Topic |
|----|------|--------|
| HES-SPEC-CORE-SYSTEM-ARCH | [core/system_architecture.md](core/system_architecture.md) | Concept → hex → family → area pipeline |
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
