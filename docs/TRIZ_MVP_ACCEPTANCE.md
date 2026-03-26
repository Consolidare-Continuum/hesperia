# TRIZ MVP acceptance criteria

## Functional

| Criterion | Check |
|-----------|--------|
| Analyze one corpus end-to-end | `run_triz_analysis_complete` + `/api/v1/triz/analyze` |
| Compare two corpora | `compare_reports_unified` + `/api/v1/triz/compare` |
| Export deterministic product bundle | `wrap_triz_export_response` + `/api/v1/triz/export` |
| UI payload per product | `build_*_ui_payload()` |

Programmatic runner: `python3 -c "from hesperia.product.mvp_acceptance import run_mvp_acceptance; print(run_mvp_acceptance())"`

## Structural

- No ontology / topology mutation (TRIZ read-only).
- No meta-area lexical activation (guard).
- Deterministic ordering in exports and benchmarks.

## Product

- Every product report has **summary text**.
- JSON + CSV export paths (see Series 3 demo outputs).
- Benchmark-backed demo: `benchmarks/extensions/triz/corpus_policy_polarized` etc.

## Operational

- **Run manifest** written per external run (`run_manifest.json`).
- **Readiness gate** passes (`hesperia.product.release_gate`).
- **API v1** response validates against frozen contract.
- **Tenant isolation**: outputs under `outputs/{tenant_id}/{project_id}/{run_id}/`.

## Pilot summary DTO

`MVPAcceptanceResult`: `passed`, `failed_checks`, `passed_checks`, `generated_artifacts`.

## Human review

Use `review_pack_builder.build_review_pack()` + optional `ReviewerFeedback` for analyst sign-off. See `docs/TRIZ_LIMITATIONS.md`.
