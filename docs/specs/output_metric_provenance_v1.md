# Metric provenance & reverse trace (v1)

**Goal:** For surfaced scalars, operators can see **which layer** produced the value and **which transforms** applied.

## Trace object shape

```json
{
  "metric_path": "sessions[0].summary.governance",
  "value": 0.37,
  "source_layers": ["core.attribution", "core.math", "propagation"],
  "upstream_dependencies": ["family_vector", "dominant_family"],
  "calculation_path": "analyze: attribution → core_analyze → minimal summary",
  "normalization_path": "v06 dense bundle; values in [0,1] where documented",
  "trace_sample": { "dominant_family": 228, "token_count": 1678 },
  "mode": "compact | verbose"
}
```

## API

- Component: `hesperia.engine.output_trace`
- Function: `explain_metric(artifact: dict, metric_path: str, *, verbose: bool = False) -> dict`

**Zero outputs:** trace must include `signal_loss_stage` when known (e.g. `hex_microphysics_line_search`).

## Scope v1

Implemented for **representative** `analyze()` summary keys and **structural** L1 coverage; extended coverage is incremental.

## Examples (pinned paths)

See [tfp_trace_examples_v1.json](../benchmarks/tfp_trace_examples_v1.json) for metric_path strings to run through `explain_metric`.
