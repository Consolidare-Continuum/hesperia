# HESPERIA — RAD. Semantic field dynamics (Ethan spec), phased implementation.
# Flags: FIELD_DYNAMICS; PHASE2 (L5); PHASE3 (L4). HEX_CAP optional.

from hesperia.extensions.dynamics import matrix_builders
from hesperia.extensions.dynamics.calibration import (
    CalibrationCandidate,
    calibrate_parameter_grid,
    compute_hspr_calibration_index,
    evaluate_candidate,
    generate_candidate_grid,
)
from hesperia.extensions.dynamics.equations import (
    FieldStepResult,
    SemanticFieldParams,
    TimelineStep,
    aggregate_family_to_area,
    build_contradiction_matrix,
    build_family_laplacian,
    build_identity_family_mapping,
    build_resistance_matrix,
    compute_energy,
    run_until_convergence,
    step_field,
)
from hesperia.extensions.dynamics.phase1 import field_dynamics_enabled, step_phase1
from hesperia.extensions.dynamics.phase2 import field_dynamics_phase2_enabled, step_phase2
from hesperia.extensions.dynamics.phase3 import field_dynamics_phase3_enabled, step_phase3
from hesperia.extensions.dynamics.phase4 import field_dynamics_phase4_enabled
from hesperia.extensions.dynamics.xi_proxy import (
    apply_xi_to_contradiction_signal,
    field_dynamics_xi_enabled,
    xi_proxy_from_triz_rows,
)
from hesperia.extensions.dynamics.semantic_field_v1 import (
    SPEC_ID as SEMANTIC_FIELD_EQUATIONS_SPEC_ID,
    SemanticFieldParamsV1,
    build_default_matrices,
    build_stub_matrices_dev_only,
    load_semantic_field_params_v1,
    semantic_field_e2e_bundle,
    step_field_euler,
)
from hesperia.extensions.dynamics.state import (
    FieldDynamicsState,
    Phase1Theta,
    Phase2Theta,
    Phase3Theta,
    Phase4Theta,
)

__all__ = [
    "matrix_builders",
    "SemanticFieldParams",
    "FieldStepResult",
    "TimelineStep",
    "build_family_laplacian",
    "build_resistance_matrix",
    "build_contradiction_matrix",
    "step_field",
    "compute_energy",
    "run_until_convergence",
    "aggregate_family_to_area",
    "build_identity_family_mapping",
    "CalibrationCandidate",
    "compute_hspr_calibration_index",
    "generate_candidate_grid",
    "evaluate_candidate",
    "calibrate_parameter_grid",
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
    "SEMANTIC_FIELD_EQUATIONS_SPEC_ID",
    "SemanticFieldParamsV1",
    "load_semantic_field_params_v1",
    "build_default_matrices",
    "build_stub_matrices_dev_only",
    "semantic_field_e2e_bundle",
    "step_field_euler",
]
