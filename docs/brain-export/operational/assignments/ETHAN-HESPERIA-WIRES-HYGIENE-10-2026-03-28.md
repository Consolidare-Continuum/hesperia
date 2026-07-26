# Ethan — Hesperia **wires hygiene** (10 tasks, project team)

**Date:** 2026-03-28  
**Role:** Architect (Ethan)  
**Execution host:** Hesperia repo — clone path **`/data/hesperia/hesperia`**; canonical remote **Atomic-Commits-Team/hesperia**.  
**Tracking:** **cursor** repo `active.md` rows **WIRE-01 … WIRE-10**; per-task artifacts under **`operational/assignments/reports/`** (this workspace).

## Intent

Post–dict/CD closure and control-layer delivery, run a **project-native hygiene pass**: the team that ships Hesperia verifies that **descriptions, scripts, CI, config, and runtime paths match** — not a feature sprint. **Serious gaps** (broken entrypoints, doc/code contradictions, CI↔local drift, silent wrong env) must be **named in prose** with **repro or file:line**, not hand-waved.

## Non-goals

- No edits to **sealed** calibration trees without **igareosh** (same rule as DICT-CAL seal).
- No new product claims; this is **wiring truth**.

## Task table (executable)

| ID | Owner | Scope | Acceptance (minimum) |
|----|--------|--------|----------------------|
| **WIRE-01** | **Gena** | **Runtime entrypoints + env** — `python -m hesperia.run`, main pipeline modules, `HESPERIA_*` flags actually read on cold path. | Report: table **env → reader site**; list **undocumented** or **dead** flags; any **wrong default** vs docs. |
| **WIRE-02** | **Liam** | **Scripts & runbooks** — `tools/*.sh`, top-level runbooks (`RUNBOOK-*`, `SCRIPT-RUNBOOK` refs), root `README` / `CONTRIBUTING` invocations. | Report: **orphan scripts**, **doc references to missing paths**, **one** consolidated “how to run gates locally” pointer. |
| **WIRE-03** | **Daniel** | **CI ↔ local parity** — `.github/workflows/*.yml` steps vs `tools/run_*`, `pytest` paths, conditional skips; no network flakes called out. | Report: **drift matrix** (workflow step vs local command); **gaps** where CI is weaker than runbook. |
| **WIRE-04** | **Noah** | **Calibration / DLCR asset wiring** — `assets/calibration/**`, dict validators, `HESPERIA_CALIB_DICT_VERSION`, clone-without-large-assets behavior. | Report: **paths that break minimal clone**; **doc missing** for SKIP patterns; link to **`run_dict_release_gates.sh`**. |
| **WIRE-05** | **Marcus** | **Governance doc graph** — `docs/governance/**`, `docs/governance/working/**`, cross-links to CD / MODEL_CARD / HC; stale or duplicate authorities. | Report: **broken internal links**, **two conflicting “source of truth”** topics, suggested **single canonical** pointer each. |
| **WIRE-06** | **Sophia** | **Config & registry** — `configs/pipeline.yaml` (and related), module registry / loader: keys consumed vs ignored. | Report: **dead keys**, **required keys not validated**, **version fields** consistency. |
| **WIRE-07** | **Olivia** | **Product / public output shape** — metric registry, schema snapshots, `dossier` / product JSON fields vs docs. | Report: **field drift** (doc vs code), **missing registry entries** for shipped keys. |
| **WIRE-08** | **Ava** | **Product API / guards** — HTTP or CLI product surfaces vs T17-style contracts; read-only / mutation guards still aligned. | Report: **route↔doc** map; **guard bypass** risk if any. |
| **WIRE-09** | **Gena** | **Import boundary & packages** — `check_import_boundary` / T1 policy vs `hesperia/engine` and `core/` edges; test layout. | Report: **violations or false sense of safety**; **one** recommended fix order (no mass refactor in this task). |
| **WIRE-10** | **Grace** | **Roll-up** — merge WIRE-01..09 into a single **gap register**; propose **P2** follow-up rows only for serious items. | **`operational/assignments/reports/WIRE-GAPS-REGISTER-2026-03-28.md`** (or dated successor) + note in Link column on `active.md`. |

## Artifact naming

Each owner files **`operational/assignments/reports/WIRE-{NN}-{TOPIC}-2026-03-28.md`** in **cursor** (or states path if placed in Hesperia `docs/governance/working/` with mirror note in cursor report).

## Dependency

- **WIRE-10** starts after **WIRE-01..09** reports exist (can be PAUSED until others DONE).

## Implementation log

| Date | Note |
|------|------|
| 2026-03-28 | Ethan issued packet; `active.md` **WIRE-01..WIRE-10** OPEN. |
| 2026-03-28 | **Grace WIRE-GRACE-01 PASS:** triage [reports/GRACE-TRIAGE-WIRE-HYGIENE-2026-03-28.md](reports/GRACE-TRIAGE-WIRE-HYGIENE-2026-03-28.md) — owners/deps OK; **WIRE-10** stays **PAUSED** until WIRE-01..09 reports exist; zero reports on disk at triage. |
| 2026-03-28 | **WIRE-02..WIRE-09 DONE** + **WIRE-10 DONE:** reports filed; [WIRE-GAPS-REGISTER-2026-03-28.md](reports/WIRE-GAPS-REGISTER-2026-03-28.md). |

---

`SIGNED: Architect (Ethan) | Hesperia wires hygiene 10-pack | 2026-03-28 | cursor operational`
