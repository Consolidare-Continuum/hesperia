<!--
Ethan PO-27 — human-readable instrumentation outline (pair with PO-26 API/CLI).
-->

# DLCR instrumentation report template

Use after `tools/dump_dlcr_trace.py` or `POST /hesperia/internal/dlcr_trace` (with `HESPERIA_API_INSTRUMENTATION=1`).

## Sections

1. **Preprocess** — `preprocess_meta.analysis_text_fingerprint`, `policy_mode`
2. **Spans** — each `span_resolutions[]`: `source_text_span`, `winning_concept_id`, `audit.candidates_detail`
3. **Hex** — `hex_concentration`, `hex_dispersion`, top keys in `hex_activation`
4. **Families** — `cross_family_sketch.top_families`, top pair rows
5. **Trajectory** — `segment_trajectory`, `segment_hex_geometry.l1_drifts`
6. **Co-occurrence** — `cooccurrence_token_pairs_top` (deterministic window PMI-lite)

## Product safety

Do not paste raw traces into **public** channels if they contain clinical text. Redact identifiers.
