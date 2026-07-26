# Hesperia — Description Object Investigation (v0.6.3)

**Study type:** Runtime transformation trace — academic investigation object  
**Entity:** Colombo (Research / formalization)  
**Version anchor:** Hesperia **0.6.3** (IRC Teacher application run)  
**Product refs:** tag `0.6.3` / `hesperia-0.6.3` → `122d45b`; live runtime `runtime/irc_teacher/` @ `e9eaa07` on `igareosh/hesperia`  
**Brain repo:** investigation drafts live here; canonical specs remain on product repo `docs/specs/`  
**Target size:** comprehensive study across **5 runs** (originally ~2000 lines; **expanded** — no hard cap)  
**Started:** 2026-06-14

---

## 1. Purpose

Produce a **step-by-step Hesperia runtime description**: what each Python file and code block does, which **states** and **scopes** apply at each iteration, which **formulas** transform inputs into outputs, how **concurrent** paths (modular engine vs sealed multiscale vs 0.6.3 Teacher) relate, and how **outputs become parameters** for the next stage.

This is a **study artifact** for ULIM / Hesperia theory work — not a product spec replacement. Implementation claims cite **verified paths** on the dev tree (`/data/workspaces/atomic-commit-hesperia` on alunel, HEAD `e9eaa07` at investigation time).

---

## 2. Five-run plan

| Run | File | Scope | Est. lines | Status |
|-----|------|-------|------------|--------|
| **01** | [HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-RUN-01.md](HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-RUN-01.md) | Architecture, dual spines, global state machine, iteration model, entry points, scope map, 0.6.3 overlay | ~450 | **DONE** |
| **02** | [HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-RUN-02.md](HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-RUN-02.md) | Modular engine kernel: `core.py`, `execution_graph`, modules (`nlp.basic`, `dict_a`, `dict_b`, `topology`, `tfp`, `metrics`), `pipeline_runner`, `runner` | ~400 | **DONE** |
| **03** | [HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-RUN-03.md](HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-RUN-03.md) | Sealed multiscale stack: S0–S11 stages, hex microphysics, energy gate, product signals, HSPR, numeric toy trace | ~550 | **DONE** |
| **04** | [HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-RUN-04.md](HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-RUN-04.md) | Shipping `/analyze`, dual pipeline, public projection, ENGINE-ANALYZE sidecar, `trace[]` iteration | ~480 | **DONE** |
| **05** | [HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-RUN-05.md](HESPERIA-DESCRIPTION-OBJECT-INVESTIGATION-0.6.3-RUN-05.md) | 0.6.3 IRC Teacher E2E, KSI/geometry, MySQL, flags, RU worked trace, bibliography, five-run synthesis | ~520 | **DONE** |

**Study status:** **COMPLETE** (Runs 01–05). Total ~**2,500+ lines** (expanded scope).

**Cumulative deliverable:** single narrative usable as a **description object** for papers and formalization (Colombo → Felix/Gena for spec promotion when ready).

**Presentation manuscript:** [HESPERIA-RUNTIME-ACADEMIC-NARRATION-v0.6.3.md](HESPERIA-RUNTIME-ACADEMIC-NARRATION-v0.6.3.md) — ~18 pages, step-by-step what/how/why for auditorium; links all Runs 01–05.

---

## 3. Source hierarchy (investigation)

| Priority | Source | Use |
|----------|--------|-----|
| 1 | Product code @ `e9eaa07` (alunel) | Implementation truth |
| 2 | `docs/specs/0.6.3-IRC-TEACHER-RUN.md` (product) | 0.6.3 contract |
| 3 | Brain governance: [ETHAN-HESPERIA-0-6-3-IRC-TEACHER-RUN-SPEC.md](../../governance/ETHAN-HESPERIA-0-6-3-IRC-TEACHER-RUN-SPEC.md) | Operator envelope |
| 4 | [ETHAN-HESPERIA-EVOLUTION-TREE-0-TO-NOW-2026-06-14.txt](reports/ETHAN-HESPERIA-EVOLUTION-TREE-0-TO-NOW-2026-06-14.txt) | Cell narrative |
| 5 | [HESPERIA-TFP-RUNTIME-VARIABLES-TABLE.md](../../HESPERIA-TFP-RUNTIME-VARIABLES-TABLE.md) | Env → behavior |
| 6 | CHROMA-1 `query_knowledge` | Team/Hesperia layers (when indexed) |
| 7 | CHROMA-2 Papra | Deferred until library re-ingest |

---

## 4. Notation (used in all runs)

| Symbol | Meaning |
|--------|---------|
| `ctx` | Engine execution context (`dict`) |
| `PHASES` | Fixed tuple `("preprocess", "project", "postprocess")` |
| `A_hex`, `A0`, `A1` | Hex activation tensors `(288, n_hex_per_family)` before/after local step |
| `F` | Family activation vector (288) |
| `A` (area) | Macro area vector (12) |
| `HSPR` | Hesperia structural/product readiness scalar |
| `trace[]` | Per-step activation record in ENGINE-ANALYZE contract |
| `cid`, `run_id` | 0.6.3 correlation and persistence identifiers |

Domain terms remain **English** inside Romanian prose (TFP, engine, hex-sphere, KSI, workflow).

---

## NEXT (Colombo)

1. [ ] Operator review — promote to dev `docs/specs/` if desired — owner: **Grace triage → Colombo/Felix**
2. [ ] 0.7.0 sandbox-apply description object when CELL 15 opens — owner: **Colombo**

**Verified exists:** Runs 01–05; product IRC path @ `e9eaa07`; 0.6.3 exit criteria sealed  
**Still unverified:** live prod OpenAI + full KSI on single RU statement in this session

---

SIGNED: Research (Colombo) | Hesperia description object investigation | 2026-06-14 | v0.6.3 index
