# PACKAGE BOUNDARY POLICY v1

**Status:** Active  
**Purpose:** Make the codebase structure non-instructional. Public runtime cannot infer the engine's true internal decomposition.

---

## 1. Boundary Definition

### Sealed internal zone (no direct public traversal)

- **Math and layer logic** — All 9 math layers (L1–L9), formulas, dependency graph, intermediate states. Implementations live under core (e.g. `core.layers`, `core.math`). Not for direct import by public API or public runtime entry points.
- **Pipeline computation** — All 10 pipeline/computation stages, layer-to-layer orchestration, transformation order. Internal only.
- **Bridge logic** — Hit-to-node construction, relation synthesis, adjacency/expansion, structural compression. Internal only.
- **Topology internals** — Invariant catalog, coordinate system, reserve loader (used only behind projection). Internal only.
- **Dictionary build internals** — Dict A/B construction doctrine, placement logic, anchor mapping. Internal only.
- **Fingerprint internals** — Full metric set, dependency chain, internal semantics. Internal only.

**Logical mapping (target shape):**

| Internal concern | Logical zone | Physical location (current) |
|------------------|--------------|-----------------------------|
| Math layers | internal_math | core/math, core/layers |
| Pipeline layers | internal_pipeline | core/layers, sphere/pipeline |
| Bridge | internal_bridge | core/domain (bridge), hesperia/engine/kme |
| Topology | internal_topology | core/topology |
| Dict build | internal_dict_build | core/attribution, lexicon |
| Debug / traces | internal_debug | (guarded by mode) |

### Public runtime zone

- **Input interfaces** — Text/corpus ingestion, calibration profile loading.
- **Calibration interfaces** — Profile selection, threshold knobs (public calibration surface only).
- **Public projection** — Single boundary through which all external-facing output passes (`core.projection`).
- **Public reports and artifacts** — Reports, manifests, evidence traces that have passed projection.
- **Service façades** — Public code calls only: `run_structural_analysis`, `run_calibration_review`, `build_public_report`, `export_public_artifacts` (and similar narrow APIs). No raw graph constructors, raw metric layer calls, or raw layer-to-layer operators.

**Logical mapping:**

| Public concern | Logical zone | Physical location |
|----------------|--------------|-------------------|
| API / entry | public_api | runtime/api, runtime/pipeline (entry scripts) |
| Reports | public_reports | runtime/public_reports, runtime/dossier (via projection) |
| Calibration | public_calibration | runtime + calibration profile schema |
| Projection | public_projection | core/projection |
| Evidence | public_evidence | Via projection + PUBLIC_EVIDENCE_TRACE_POLICY |

---

## 2. Rules

1. **Public runtime imports internal core through narrow service interfaces only.** No public module shall `import compute_L3`, `import core.math.core_math`, or traverse deep internal modules directly.
2. **All external-facing output** (reports, dossiers, API responses, logs intended for operators) **must pass through the public projection layer** before emission.
3. **No public artifact** may expose raw L1–L9 outputs, bridge internals, topology coordinates, or full math-layer semantics.
4. **Service façades** in `core/services/` (analysis_service, calibration_service, report_service) are the intended call targets for any public-originating workflow. Internal orchestration remains behind these façades.

---

## 3. Import Discipline

- **Public entry points** (e.g. `runtime.pipeline.run_l1_through_l9`, `runtime.api.main`) may import:
  - `core.projection` (apply_public_projection, etc.)
  - `core.services` (analysis_service, calibration_service, report_service)
  - Runtime utilities (provenance, dossier writer that applies projection)
- **Public entry points must not import** directly: `core.layers.compute_L*`, `core.math.*` (except as used inside services), `core.domain.bridge` internals, `core.topology.invariant_catalog` (for exposure), or any module that exposes layer order / formula / topology to callers.

---

## 4. Acceptance Criterion

A reader of the **public** runtime packages (runtime/api, runtime/public_reports, runtime/pipeline as entry layer, core/projection, core/services) cannot infer the engine's true internal decomposition (nine math layers, ten pipeline stages, bridge doctrine, topology geometry).
