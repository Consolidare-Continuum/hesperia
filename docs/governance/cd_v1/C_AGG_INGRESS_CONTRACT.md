# C_agg ingress from CD (v1)

**Input** to hex projection / family-area aggregation after CD:

- **`concept_weights`**: `dict[concept_id: str, weight: float]` — sorted keys, quantized floats per `core.dynamics.numeric.quantize`.
- **`cd_trace`** (optional, Phase 2): `{ "cd_version": str, "cd_path": str, "phase": int, "dropped": [concept_id, ...] }`.

Consumers must not assume pre-CD masses; read only post-CD dict when `HESPERIA_CD_ENABLED=1`.

SIGNED: Backend (Olivia) | ingress contract | 2026-03-27
