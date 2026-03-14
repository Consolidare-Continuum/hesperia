# Consistency A3 — Stage-limited correctness

**Block:** A — Functional integrity  
**Goal:** Verify that reduced-stage runs (`stages="L1_L2"`, `stages="L1_L2_L3"`, `stages="full"`) behave correctly: no later-stage metrics appear prematurely; evidence extraction consistent; domain metrics only when enabled.

---

## Procedure

1. **L1_L2 only**
   - Run `run_structural_analysis(text, stages="L1_L2")`.
   - **Check:** Output contains only L1 and L2 (and `run`, `text_preview`). No L3, L4, … L9, no `usf`, no `domain_metrics`, no `interpretation_metrics` (or only if explicitly added at this stage by design).
   - **Check:** Evidence extraction: if any evidence-related field exists at L1/L2 level, it is consistent (e.g. same input → same evidence shape).

2. **L1_L2_L3 only**
   - Run `run_structural_analysis(text, stages="L1_L2_L3")`.
   - **Check:** Output contains L1_B, L2_B, L1_S, L2_S, L3 (and `run`, `text_preview`). No L4–L9, no `usf`, no `domain_metrics` unless defined for this stage.
   - **Check:** Evidence extraction remains consistent.

3. **Full**
   - Run `run_structural_analysis(text, stages="full")`.
   - **Check:** Output contains L1–L9 and may contain `usf`, `interpretation_metrics`. No `domain_metrics` unless `enable_domain_metrics=True`.

4. **Domain metrics gating**
   - Run with `enable_domain_metrics=False` (default): **Check** `domain_metrics` key is absent (or null/empty).
   - Run with `enable_domain_metrics=True` and valid `domain_constants_path` if required: **Check** `domain_metrics` key is present and populated.

---

## Expected result

- **L1_L2:** Only L1 and L2 in output; no later stages.
- **L1_L2_L3:** Only L1_B, L2_B, L1_S, L2_S, L3; no L4–L9 or full-pipeline-only fields.
- **full:** Full pipeline output; domain_metrics only when enabled.
- Evidence extraction consistent across stages where it applies.

---

## Failure interpretation

| Symptom | Likely cause |
|--------|---------------|
| L4–L9 appear in L1_L2 or L1_L2_L3 | Stage gate not applied; full pipeline run by mistake. |
| domain_metrics in disabled case | Flag not respected in service or projection. |
| domain_metrics absent when enabled | Config not passed or domain pipeline not run. |

---

## Pass criterion

Stage-limited runs contain only the expected stages; domain_metrics appear only when `enable_domain_metrics=True`. No remediation required.
