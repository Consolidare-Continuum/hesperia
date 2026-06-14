# Grace — Hesperia v0.5.8: Tasks 1–11 closure and release (2026-04-14)

**Role:** Project ops / triage documentation (not a new active.md row).  
**Repos:** Implementation and tag on **Hesperia** (`igareosh/hesperia` or org remote); this file lives in the **brain** repo (`igareosh/cursor`) under `operational/assignments/reports/`.

---

## 1. What shipped (contradiction track, Tasks 1–11)

| Range | Theme |
|-------|--------|
| 1–2 | Contradiction pressure into TFP activation + runtime |
| 3 | Topology segment dynamics |
| 4 | Cross-plane package (DLCR / sealed / product / topology) |
| 5–6 | Uncertainty + negation/inhibition coupling |
| 7 | Family-level structure |
| 8 | Feedback / calibration diagnostics |
| 9 | Conflict integrity release gating (`PASS` / `QUALIFIED_PASS` / `FAIL`) |
| 10 | Contradiction contract + field registry (v0.5.8 specs) |
| 11 | **Single calibration profile** — JSON + loader + bundle snapshot + usage trace + inspector checks |

Canonical register (Hesperia tree): `docs/governance/project/HESPERIA-v0.5.8-CONTRADICTION-TASKS-01-11-REGISTER.md`.

---

## 2. v0.5.8 “all in one” TFP input → defined folder (Gena pipeline)

**Primary combined entrypoint (recommended):**

```bash
cd /path/to/hesperia
python3 tools/gena_tfp_bundle_run.py -i path/to/session.md -o path/to/out_dir \
  --with-triz --with-topology
```

**Optional:** custom contradiction calibration profile (Task 11):

```bash
python3 tools/gena_tfp_bundle_run.py -i path/to/session.md -o path/to/out_dir \
  --with-triz --with-topology \
  --contradiction-calibration-json assets/data/engine_dynamics_v060/tfp/contradiction_calibration_v1.json
```

**What it does:** calls `runtime.pipeline.run_tfp_file_pipeline` → then `tfp_calibration_audit` → `validate_tfp_bundle_schemas` → optional gold → `calibration_release_gate` (writes `11_*` gate report). Exit codes documented in `tools/gena_tfp_bundle_run.py`.

**Direct pipeline only (no post-steps):**  
`python3 -m runtime.pipeline.run_tfp_file_pipeline -i … -o …` (same flags; `--contradiction-calibration-json` supported).

**Authoritative bundle files for audit:** `00_manifest.json`, `20_main_engine_full_context.json`, `99_tfp_bundle_inspect.json` (after inspection step when run).

---

## 3. GitHub release — done (operator)

- **Repo:** [Atomic-Commits-Team/hesperia](https://github.com/Atomic-Commits-Team/hesperia)
- **Tag:** `v0.5.8` (contradiction track merge; sealed product line for Tasks 1–11).
- **Edit release UI:** [releases/edit/v0.5.8](https://github.com/Atomic-Commits-Team/hesperia/releases/edit/v0.5.8) — paste **Section 5** below into the description field; set title as given.
- **Note:** `main` may be **ahead** of the tag with post-release CI/tooling commits; the tag still marks the **v0.5.8 contradiction + calibration surface** drop. Next contradiction scope = new minor or explicit v0.5.9 plan.

---

## 4. Sealed state statement

**Hesperia v0.5.8** is **released** for the **contradiction + calibration** track: Tasks **1–11** registered DONE in-repo (`docs/governance/project/HESPERIA-v0.5.8-CONTRADICTION-TASKS-01-11-REGISTER.md` on Hesperia `main`). Task **11** delivers a **single calibration profile** (JSON + loader + bundle snapshot + inspector), governable without scattered knobs.

---

## 5. GitHub Release — paste payload (title + description)

**Release title (copy):**

```text
Hesperia v0.5.8 — TFP contradiction track (Tasks 1–11) + unified calibration surface
```

**Release description (copy everything below the line into GitHub):**

---

### Summary

Hesperia **v0.5.8** closes the **TFP contradiction evolution** line (**Tasks 1–11**): semantics, cross-plane propagation, uncertainty/negation/family layers, feedback, **conflict release gating**, formal **contract + field registry**, and a **unified contradiction calibration surface** (Task 11).

Canonical register: [`docs/governance/project/HESPERIA-v0.5.8-CONTRADICTION-TASKS-01-11-REGISTER.md`](https://github.com/Atomic-Commits-Team/hesperia/blob/main/docs/governance/project/HESPERIA-v0.5.8-CONTRADICTION-TASKS-01-11-REGISTER.md)

### Highlights

| Area | What |
|------|------|
| Activation / runtime | Contradiction pressure into TFP activation and `runtime/pipeline` interpretation |
| Topology | Contradiction-aware segment dynamics |
| Cross-plane | DLCR / sealed / product / topology propagation |
| Uncertainty / negation / family | Dedicated coupling modules + tests |
| Gating | Conflict integrity release gating (`PASS` / `QUALIFIED_PASS` / `FAIL`) |
| Contract | Specs: `TFP_CONTRADICTION_CONTRACT_V058`, `TFP_CONTRADICTION_FIELD_REGISTRY_V058` |
| Task 11 | **One calibration profile**: [`assets/data/engine_dynamics_v060/tfp/contradiction_calibration_v1.json`](https://github.com/Atomic-Commits-Team/hesperia/blob/main/assets/data/engine_dynamics_v060/tfp/contradiction_calibration_v1.json) — spec [`TFP_CONTRADICTION_CALIBRATION_PROFILE_V058.md`](https://github.com/Atomic-Commits-Team/hesperia/blob/main/docs/specs/TFP_CONTRADICTION_CALIBRATION_PROFILE_V058.md) |

### Combined TFP run (Gena bundle)

Full bundle (pipeline + audit + schema + optional gold + release gate):

```bash
python3 tools/gena_tfp_bundle_run.py -i path/to/session.md -o path/to/out_dir \
  --with-triz --with-topology
```

Optional Task 11 profile override:

```bash
python3 tools/gena_tfp_bundle_run.py -i path/to/session.md -o path/to/out_dir \
  --with-triz --with-topology \
  --contradiction-calibration-json assets/data/engine_dynamics_v060/tfp/contradiction_calibration_v1.json
```

Audit-facing artifacts (typical): `00_manifest.json`, `20_main_engine_full_context.json`, `99_tfp_bundle_inspect.json` (when inspection step is in the run).

### References

- Task 11 merge context (historic): `b87ca97` — centralize contradiction calibration surface and profile  
- Grace operational note (brain repo): `operational/assignments/reports/GRACE-HESPERIA-v0.5.8-TASKS-01-11-AND-RELEASE-2026-04-14.md` on `igareosh/cursor`

---

SIGNED: Grace (Project Ops) | brain repo operational report | 2026-04-14 | v0.5.8 GitHub release text filled
