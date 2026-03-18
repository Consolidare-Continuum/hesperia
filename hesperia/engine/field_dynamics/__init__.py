# HESPERIA — RAD. Semantic field dynamics (Ethan spec), phased implementation.
# Flags: FIELD_DYNAMICS; PHASE2 (L5); PHASE3 (L4). HEX_CAP optional.

from hesperia.engine.field_dynamics.phase1 import field_dynamics_enabled, step_phase1
from hesperia.engine.field_dynamics.phase2 import field_dynamics_phase2_enabled, step_phase2
from hesperia.engine.field_dynamics.phase3 import field_dynamics_phase3_enabled, step_phase3
from hesperia.engine.field_dynamics.phase4 import field_dynamics_phase4_enabled
from hesperia.engine.field_dynamics.xi_proxy import (
    apply_xi_to_contradiction_signal,
    field_dynamics_xi_enabled,
    xi_proxy_from_triz_rows,
)
from hesperia.engine.field_dynamics.state import (
    FieldDynamicsState,
    Phase1Theta,
    Phase2Theta,
    Phase3Theta,
    Phase4Theta,
)

__all__ = [
    "FieldDynamicsState",
    "Phase1Theta",
    "Phase2Theta",
    "Phase3Theta",
    "Phase4Theta",
    "field_dynamics_enabled",
    "field_dynamics_phase2_enabled",
    "field_dynamics_phase3_enabled",
    "field_dynamics_phase4_enabled",
    "step_phase1",
    "step_phase2",
    "step_phase3",
    "apply_xi_to_contradiction_signal",
    "field_dynamics_xi_enabled",
    "xi_proxy_from_triz_rows",
]
