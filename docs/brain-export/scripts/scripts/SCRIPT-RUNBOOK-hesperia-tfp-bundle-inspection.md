---
task_id: "hesperia|tfp|bundle-inspect"
active_md_anchor: "| Hesperia TFP |"
---

# Script runbook — Hesperia TFP bundle output inspection (Cursor MCP agent)

**Purpose:** After a standard TFP pipeline bundle exists under Hesperia `assets/artifacts/tfp_pipeline_runs/`, run a **deterministic machine inspection** (normality / layer coherence / contradiction sanity) and optionally let the **Cursor agent** interpret edge cases using this runbook when numbers are ambiguous.

**Who:** Cursor (default), Gena — any agent with repo + Hesperia checkout.

**Hesperia tool (source of truth):** `tools/inspect_tfp_bundle_output.py` — emits JSON and can write `99_tfp_bundle_inspect.json` into the bundle directory.

**Awareness anchor (Cursor repo):** [governance/HESPERIA-TFP-STANDARD-RUN-AWARENESS-ANCHOR.md](../governance/HESPERIA-TFP-STANDARD-RUN-AWARENESS-ANCHOR.md)

---

## When to use

- After `python3 tools/tfp_pipeline_standard_run.py -i …` (or `run_tfp_file_pipeline`) produced `00_`…`09_` artifacts.
- Before trusting a bundle for **calibration** or **semantic interpretation**.
- When triaging “flat / collapsed / zero TRIZ contradictions” reports.

---

## Procedure (agent loop until checks complete)

1. **Confirm bundle path** — directory containing at least:
   - `00_manifest.json`
   - `04_dlcr_full.json`
   - `06_product_analyze.json`
   - `08_triz_complete.json`
   - `09_session_topology.json`
2. **Run the inspector** (from Hesperia repo root):

   ```bash
   cd /data/hesperia/hesperia
   python3 tools/inspect_tfp_bundle_output.py --bundle-dir /path/to/run --write
   ```

3. **Read** `99_tfp_bundle_inspect.json` (if `--write`) or capture stdout JSON.
4. **Gate decisions**
   - If `bundle_status` is not `ok` → **stop**; bundle incomplete.
   - If `config_status` is `drift` → **do not** compare runs directly; mark calibration cross-run invalid until config aligned.
   - If `semantic_deviation` is `UNRELIABLE` or `semantic_scale_note` is `SEMANTIC_SCALE_UNRELIABLE` → **do not** use semantic interpretation; calibration use only if `usable_for_calibration` is true.
5. **If uncertain** (borderline bands, missing optional files, or contradictory sub-scores): follow the **interpretation rules** in section “Agent interpretation (non-deterministic)” below — infer what is wrong (layer disagreement vs lexical vs TRIZ extraction), cite which coherence check failed, and recommend the next Hesperia engineering action (never invent clinical facts about a patient).

---

## Core machine rules (deterministic — mirrored in tool)

**Config sanity (manifest `tfp_signal_calibration.loaded_config`):** pinned CB-1 knobs:

- `negation_window = 4`
- `inhibition_scale = 1.2`
- `hex_feedback_required = true`
- `area_softmax_temperature = 0.35`

Drift → `CONFIG_DRIFT` / warn; do not cross-compare runs.

**Dominance (topology segments → `invariant_activation`):** `dominance_max_area_probability`

- `< 0.4` → fail dominance
- `0.4–0.6` → weak
- `> 0.8` → strong pass

**Spread (DLCR `calibration_metrics`):** `area_entropy_normalized`, `area_uniformity_proxy`, `top2_area_mass_share` — evaluate **together** (high entropy + high uniformity ⇒ flat diffusion risk; high top-2 + high entropy ⇒ layer mismatch suspicion).

**TRIZ:** If canonical text shows explicit mismatch patterns (expectation vs outcome, “не было”, contrast clauses) **and** `contradiction_count == 0` **and** lexical hits exist → **relational extraction failure**, not lexical failure.

**Semantic scale:** If machine quality is low or contradiction layer is dead on mismatch-rich text → **`SEMANTIC_SCALE_UNRELIABLE`** — do not assign S1–S4.

---

## Agent interpretation (non-deterministic)

Use when:

- `output_normality` is `N1` or `N2` but coherence checks disagree;
- optional files `02_` / `05_` are missing but core exists;
- text is short (single segment) — **do not** punish low segment count; **do** check semantic collapse vs text moves.

**Interpretation targets**

- Is the output structurally normal for a **machine** (N0–N4)?
- Are **layers agreeing** (topology dominance vs DLCR spread vs TRIZ contradictions)?
- Is contradiction absent because the text is neutral, or because **extraction failed**?
- Lexical: distinguish `FAIL_LEXICAL_MATCHING` vs `FAIL_RELATIONAL_INTERPRETATION` using `lexical_hits_accepted` + TRIZ counts.

**Deliverable JSON shape** — align agent narrative to the tool output fields (`output_normality`, `semantic_deviation`, `coherence_checks`, `main_failure_mode`, `usable_for_*`, `recommended_next_action`). Extend with a short `agent_notes` string only in chat/logs, not required in the JSON file.

---

## Failure modes

| Symptom | Action |
|--------|--------|
| Missing core JSON | Re-run pipeline; confirm `--with-topology` and full stack for intended audit |
| `CONFIG_DRIFT` | Record drift; align `tfp_signal_calibration_v2` / manifest loaded_config before calibration |
| Zero TRIZ contradictions on mismatch-rich text | File under relational/TRIZ extraction; not DLCR lexical if hits exist |
| High dominance + diffuse DLCR | `WARN_LAYER_DISAGREEMENT` — treat as engineering mismatch, not “patient” signal |

---

## See also

- Hesperia: `assets/calibration/TFP_VALUES_LIST` — artifact inventory
- Hesperia: `runtime/pipeline/run_tfp_file_pipeline.py` — bundle contract
- Cursor MCP: `get_runbook` id **`SCRIPT-RUNBOOK-hesperia-tfp-bundle-inspection`**

SIGNED: Gena (main developer) | Hesperia TFP bundle inspection runbook | 2026-04-14 | governance+hesperia
