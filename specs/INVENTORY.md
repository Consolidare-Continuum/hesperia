# Specification inventory & tier classification (Task 3 Phase A)

| Tier | Meaning |
|------|---------|
| **T1** | Canonical — equations/rules live here |
| **T2** | Derived / explanatory — must reference T1 |
| **T3** | Research / draft — non-binding |

## T1 — Canonical (this repo, `specs/`)

| Path | Note |
|------|------|
| `specs/core/*.md` | Core pipeline + observables |
| `specs/dynamics/semantic_field_dynamics.md` | **Only** family-field dynamics equations |
| `specs/calibration/calibration_system.md`, `hspr_index.md` | Calibration law + scalars |
| `specs/triz/*.md` | TRIZ contradiction + innovation |
| `specs/schema/public_output_schema.md` | Public JSON mirror |
| `specs/system/versioning_and_governance.md` | Governance |
| `specs/canon/*.yaml`, `*.json`, `*.pl`, … | Loader assets (not prose duplicates) |

## T2 — Derived (still under `specs/` but not duplicate law)

| Path | Role |
|------|------|
| `specs/dynamics/ETHAN_SEMANTIC_FIELD_DYNAMICS_SPEC.md` | L0–L10 **wire** / narrative |
| `specs/dynamics/DYNAMICS_EQUATION_INDEX.md` | Implementer index |
| `specs/dynamics/FIELD_MATRIX_BUILDERS_v1.md` | Ontology → matrices |
| `specs/dynamics/HESPERIA_DYNAMICS_CALIBRATION_SPEC_v0_1.md` | Extended calibration blueprint |
| `specs/architecture/*.md` | LEVEL / dossier historical architecture prose |
| `specs/release/*.md` | Release narrative |

## T2 — Docs (`docs/`)

All `docs/**/*.md` — **explain**; must **not** introduce new binding equations (link to `specs/CANONICAL_INDEX.md`).

## T3 — Research (`research/`)

`research/**/*.md`, `research/clinical_tfp/**` — experimental; not system definition.

## Stubs / redirects

| Path | Points to |
|------|-----------|
| `specs/canon/hex_microphysics_canon.md` | `specs/core/hex_microphysics_canon.md` |
| `specs/canon/hex_family_bridge.md` | `specs/core/family_aggregation.md` |
| `specs/canon/semantic_field_canon.md` | `specs/core/system_architecture.md` + `specs/dynamics/semantic_field_dynamics.md` |
| `specs/canon/product_signal_layer.md` | `specs/core/product_observables.md` + `specs/triz/innovation_metrics.md` |
| `specs/canon/hspr_calibration_index.md` | `specs/calibration/hspr_index.md` |
| `specs/dynamics/SEMANTIC_FIELD_EQUATIONS_v1.md` | `specs/dynamics/semantic_field_dynamics.md` |
| `specs/dynamics/HSPR_CALIBRATION_INDEX_v1.md` | `specs/calibration/hspr_index.md` §2 |
