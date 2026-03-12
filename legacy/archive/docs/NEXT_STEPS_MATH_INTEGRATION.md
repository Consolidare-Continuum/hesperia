<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Next steps: math integration (scripting layers)

**Date**: 2026-02-24

## Standard for all 9 layers (the line)

Every layer math run must end the same way:

**Run layer math X → output → logged → reportable.**

- **Run**: Execute compute_LX (or equivalent) with correct inputs and predefined defaults.
- **Output**: 25 variables (or spec-defined) as a deterministic dict/struct.
- **Logged**: Output written to a known place (e.g. run log, artifact, or report file).
- **Reportable**: Result can be summarized or exported (e.g. JSON, note, table) for inspection and audit.

L1 is the reference: run → dict of 25 vars → can be logged and reported. L2–L9 must achieve the same pattern.

## Status

- **L1** implemented: `sphere_rag/layers/layer_1.py` — `compute_L1(...)` returns 25 variables (34_SPEC).
- **L2–L9** implemented: `sphere_rag/layers/layer_2.py` … `layer_9.py`. Each layer: run → output (25 vars) → logged → reportable.
- **Full stack run**: `python3 -m sphere_rag.layers.run_l1_through_l9 [--out path.json]` — L1..L9 in one pipeline; output JSON + reportable summary (L7 DECISION_STATUS_CODE, OUTPUT_TRUST_TAG; L9 BRAND_WORD_*). **Output log dir (canonical path)**: [docs/layer_runs/](docs/layer_runs/) — latest run: `docs/layer_runs/latest_L1_L9_output.json`; report: `docs/layer_runs/REPORT__L1_L9_Full_Pass.md`.
- L2: stub adjacency `build_canonical_stub_adjacency(F,A)`; L3: B vs S (same run twice = zero divergence); L4/L5: empty R_B/R_S and R_neg → deterministic; L6: no perturbation → stub stability; L7–L9: aggregate and SI_*.
## Pipeline wiring

1. **Attribution** (existing): `attribution_v033.attribute(tokens, dict_a, dict_b)` → `matched: list[tuple[int, float]]`, metrics.
2. **L1**: `compute_L1(len(tokens), matched, F=defaults["F"], A=defaults["A"], eps=defaults["eps"])` → dict of 25 L1 variables.
3. **L2** (next): Needs L1 output + adjacency graph, area mapping, MAX_ALLOWED_DEPTH. Input: dominant_family_id, hits, visited set from BFS on family graph.
4. **L3–L7**: Chain L2→L3→…→L7; then L8 (units), L9 (brand).

## Suggested order

1. **L2** — BFS from dominant family, compute 25 traversal variables (35_SPEC). Requires: adjacency (e.g. from invariant_catalog or topology), area[f], MAX_ALLOWED_DEPTH from defaults.
2. **L3** — Only when baseline + shadow runs exist; compare B vs S, 25 variables (36_SPEC).
3. **L4** — Retrieval R_B, R_S + L1/L3 context; 25 variables (37_SPEC).
4. **L5–L7** — Then L8/L9.

## Run L1 only (current)

From repo root (CLIENTS/hesperia):

```bash
python -c "
from sphere_rag.attribution_v033 import tokenize, normalize, attribute, load_dict_a_v033
from sphere_rag.layers import load_defaults, compute_L1
from pathlib import Path
p = Path('hesperia_lex/curated')
dict_a = load_dict_a_v033(assets_root=p)
dict_b = {}  # or load Dict B
text = 'some input text'
tokens = tokenize(normalize(text))
matched, _ = attribute(tokens, dict_a, dict_b)
defaults = load_defaults()
L1 = compute_L1(len(tokens), matched, F=defaults['F'], A=defaults['A'], eps=defaults['eps'])
print('L1 COVERAGE_RATIO', L1['COVERAGE_RATIO'], 'DOMINANT_FAMILY_ID', L1['DOMINANT_FAMILY_ID'])
"
```

## L1–L9 interoperability and internationalization

- **Data flow**: L1 (attribution metrics) → L2 (traversal) → L3 (B vs S) → L4 (evidence) → L5 (counter-evidence + trig) → L6 (stability) → L7 (gates, DECISION_STATUS_CODE, OUTPUT_TRUST_TAG) → L8 (units) → L9 (branding). Each layer consumes only prior layers and frozen config; no back-edges.
- **Units (L8)**: Single taxonomy for all metrics: COUNT, RATIO, PERCENT, U1000, BOOLEAN. L8 converts L1–L7 outputs to SI_* (e.g. SI_COVERAGE_U1000, SI_SYSTEM_CONFIDENCE_PCT). One place for logs, APIs, dashboards; deterministic conversion (clamp, ratioToPct, ratioToU1000).
- **Branding (L9)**: Consumes L3, L4, L7, L8 SI_*. Emits U1000 bands (critical/weak/fair/good/strong/excellent), pillars (INPUT_QUALITY, GEOMETRY, EVIDENCE, CONSISTENCY, STABILITY, GOVERNANCE), BRAND_WORD_* (TRUST, EVIDENCE, CONTRADICTION, GEOMETRY, SHADOW), ACTION_* flags. All 9 layers propagate to human-facing labels via L8→L9; no locale-specific strings in L1–L7, so i18n can sit on top of L9 output.
- **Cross-check script**: `run_l1_through_l9.py` chains L1…L9 in order, passes defaults, and writes one JSON; keys match spec variable names. Run from CLIENTS/hesperia: `python3 -m sphere_rag.layers.run_l1_through_l9 --out path.json`.

## References

- CORE_CONSOLIDATION.md — core definition, config map
- LAYER_1_9_PREDEFINED_DEFAULTS_v1_0.txt — default values
- 34_SPEC … 42_SPEC — layer specs
