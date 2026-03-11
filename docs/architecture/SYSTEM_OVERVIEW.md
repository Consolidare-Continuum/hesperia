# System Overview

This repository is structured as a reference architecture baseline for Hesperia v0.4.

## Layer Model

1. **Lexical Layer**
Located in `lexicon/`.
Owns curated/frozen lexical artifacts and lexical build + validation tooling.

2. **Semantic Layer**
Located in `core/attribution/`.
Deterministic token normalization, attribution, and family/area landing.

3. **Structural Layer**
Located in `core/layers/`.
L1-L9 deterministic structural computations and profile-aware instrumentation.

4. **Topology Layer**
Located in `core/topology/`.
Frozen canonical geometry/invariant constants and coordinate bijections.

5. **Math Layer**
Located in `core/math/`.
Core mathematical transforms, fusion, traversal math, and dict-B math pipeline.

6. **Dynamics Layer**
Located in `core/propagation/`.
Guard sequencing, enforcement, and propagation behaviors across outputs.

7. **Shadow Layer**
Located in `core/propagation/shadow_layer.py` and L3 in `core/layers/layer_3.py`.
Encodes shadow divergence behavior under deterministic limits.

8. **Logic Layer**
Located in `core/propagation/`.
Safeguard logic, invariant enforcement, and runtime validity gates.

9. **Interpretation Layer**
Located in `core/layers/layer_8.py` and `core/layers/layer_9.py`.
Converts structural state into normalized units and interpretation/branding outputs.

## Runtime Flow

`runtime/pipeline/` orchestrates deterministic `core/` modules.
`runtime/api/` provides service exposure without embedding engine logic.

## Operational Context

- `tools/` contains calibration, diagnostics, and operational scripts.
- `assets/` contains models/artifacts/data only (no orchestration logic).
- `legacy/` isolates deprecated PoC/experimental/history material.
