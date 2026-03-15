# HESPERIA Clinical: interpretation (LEVEL 8) and session topology (LEVEL 10)
from hesperia.clinical.interpretation import (
    get_dominant_area,
    get_dominant_family,
    classify_aggression_level,
    detect_defense_pattern,
    detect_object_relation_pattern,
    estimate_relational_capacity,
    interpret_session,
    DEFENSE_MAP,
    OBJECT_RELATION_MAP,
)
from hesperia.clinical.session_topology import (
    segment_session,
    analyze_session_segments,
    detect_state_transitions,
    detect_defense_shifts,
    detect_aggression_escalation,
    build_session_state_sequence,
    run_session_topology,
)
from hesperia.clinical.safety_layer import (
    get_minimum_evidence_threshold,
    get_min_markers_for_interpretation,
    apply_safety_filter,
)
from hesperia.clinical.report_generator import (
    generate_session_summary,
    describe_defense_patterns,
    describe_object_relations,
    describe_aggression_profile,
    describe_session_trajectory,
    detect_clinical_flags,
    generate_clinical_report,
    generate_report_markdown,
    generate_report_json,
    generate_report_text,
    generate_clinical_report_readable,
)
from hesperia.clinical.transference_detection import (
    detect_transference,
    transference_summary,
)
from hesperia.clinical.stage_detection import (
    detect_tfp_stage,
    stage_from_timeline,
    TFP_STAGES,
)
from hesperia.clinical.longitudinal import (
    compare_session_activations,
    build_longitudinal_curves,
    detect_defense_evolution,
    detect_aggression_trend,
    detect_relational_capacity_trend,
    estimate_structural_change,
    analyze_treatment_trajectory,
    export_trajectory_json,
    export_trajectory_markdown,
)
from hesperia.clinical.intervention_classifier import (
    classify_intervention,
    classify_intervention_with_scores,
)
from hesperia.clinical.affect_intensity import (
    estimate_affect_intensity,
    estimate_affect_intensity_with_breakdown,
)
from hesperia.clinical.object_representation_tracking import track_object_representations
from hesperia.clinical.interaction_loop_detection import detect_interaction_loops
from hesperia.clinical.affect_defense_coupling import (
    couple_affect_defense,
    infer_affect_from_areas,
)
from hesperia.clinical.session_summary import (
    build_session_summary,
    build_session_summary_with_timeline,
)
from hesperia.clinical.confidence_scoring import (
    compute_confidence_scores,
    add_confidence_to_interpretation,
)
__all__ = [
    "get_dominant_area",
    "get_dominant_family",
    "classify_aggression_level",
    "detect_defense_pattern",
    "detect_object_relation_pattern",
    "estimate_relational_capacity",
    "interpret_session",
    "DEFENSE_MAP",
    "OBJECT_RELATION_MAP",
    "segment_session",
    "analyze_session_segments",
    "detect_state_transitions",
    "detect_defense_shifts",
    "detect_aggression_escalation",
    "build_session_state_sequence",
    "run_session_topology",
    "generate_session_summary",
    "describe_defense_patterns",
    "describe_object_relations",
    "describe_aggression_profile",
    "describe_session_trajectory",
    "detect_clinical_flags",
    "generate_clinical_report",
    "generate_report_markdown",
    "generate_report_json",
    "generate_report_text",
    "compare_session_activations",
    "build_longitudinal_curves",
    "detect_defense_evolution",
    "detect_aggression_trend",
    "detect_relational_capacity_trend",
    "estimate_structural_change",
    "analyze_treatment_trajectory",
    "export_trajectory_json",
    "export_trajectory_markdown",
    "detect_transference",
    "transference_summary",
    "detect_tfp_stage",
    "stage_from_timeline",
    "TFP_STAGES",
    "classify_intervention",
    "classify_intervention_with_scores",
    "estimate_affect_intensity",
    "estimate_affect_intensity_with_breakdown",
    "track_object_representations",
    "detect_interaction_loops",
    "couple_affect_defense",
    "infer_affect_from_areas",
    "build_session_summary",
    "build_session_summary_with_timeline",
    "compute_confidence_scores",
    "add_confidence_to_interpretation",
    "generate_clinical_report_readable",
    "get_minimum_evidence_threshold",
    "get_min_markers_for_interpretation",
    "apply_safety_filter",
]
