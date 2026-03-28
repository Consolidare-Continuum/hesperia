# Ethan — Lock: Dict A, normalized, proposals, anchors (freeze `v0_6_0_clr_v052_1`)

**Date:** 2026-03-28  
**Role:** Architect (Ethan)  
**Authority:** **Locked** calibration line completed under operator direction (Dict **A**, **normalized** lexical rows, **proposal** / draft lineage, **anchor** / link / dict_b freeze for this version). **No agent, automation, or team member may edit, replace, or delete** the artifacts below **without direct written permission from igareosh** (or a superseding **Ethan-signed** governance packet that explicitly lifts or re-versions this lock).

## Locked path (whole directory)

All files under:

`assets/calibration/dicts/v0_6_0_clr_v052_1/`

Including at minimum (non-exhaustive enumeration):

| File | Role in locked line |
|------|---------------------|
| `dict_a.jsonl` | Frozen calibration **Dict A** (runtime when `HESPERIA_CALIB_DICT_VERSION=v0_6_0_clr_v052_1`) |
| `dict_a_normalized.jsonl` | **Normalized** lexical layer for this freeze |
| `dict_a_candidates.jsonl` | Candidate lineage tied to this freeze |
| `dict_b_draft.jsonl` | **Proposal** / draft lineage retained for audit |
| `dict_b.jsonl` | Frozen **Dict B** after anchor pass for this version |
| `links.jsonl` | **A↔B links** (anchor / binding surface) |
| `metrics.json` | Freeze **metrics** snapshot |

**Rule:** Treat the directory as a **single sealed artifact**. Do not partially edit one file “for a quick fix” without owner approval.

## Mirrors

Copies under `hesperia/modules/tfp/data/dicts/calibration/v0_6_0_clr_v052_1/` (from `sync_tfp_module_data.sh`) are **derived**. **Source of truth** is the path above; refreshing mirrors is allowed **only** after the source is intentionally updated **with owner approval**.

## Promotion to `engine_dynamics_v060`

Any **promotion** (e.g. merged `dict_a` / `dict_b` under `assets/data/engine_dynamics_v060/`) that is documented as **carrying this freeze** is subject to the **same** permission rule until Ethan issues a new promotion charter.

## Workflow / CI

Validators may **read** these files. **CI must not** auto-commit changes into this directory. **DICT-CAL-*** active rows that imply mutating this freeze require **Grace + igareosh** triage or a **new version directory** (e.g. `v0_6_0_clr_v052_2`) instead of in-place edits.

## Amendment — successor pack `v0_6_0_clr_v052_2` (2026-03-28)

**igareosh** (Ethan voice) **unfroze** DICT-CAL-02 / TFP dict workflow. **New default runtime directory:** `assets/calibration/dicts/v0_6_0_clr_v052_2/` — **copy** of `v052_1` plus **append-only** `dict_b.jsonl` rows (66 `concept_id`s) from engine `dict_b_tfp.jsonl`; `TFP_CLUSTER_*` **hex_anchor** **HX-2609**–**HX-2615** in engine + anchors registry. **`v052_1` directory is not edited**; it remains the sealed predecessor. Defaults: `HESPERIA_CALIB_DICT_VERSION=v0_6_0_clr_v052_2`, `tools/run_b_cd_wave_after_a.sh`, `tools/sync_tfp_module_data.sh`, CI gate env.

---

`SIGNED: Architect (Ethan) | Dict A / norm / propose / anchor lock | 2026-03-28 | Hesperia governance/working`
