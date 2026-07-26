# Ethan — Hesperia full inspection wave (code + repo)

**Date:** 2026-06-14  
**Entity:** Ethan (Hesperia-as-product governance)  
**Scope:** Runnable product repos (`igareosh/hesperia`, `Atomic-Commits-Team/hesperia`, `igareosh/tersagor`) + prod surfaces — **not** brain workflow replay.  
**Policies:** [ETHAN-POLICY-HESPERIA-DEV-PROD-CONTENT.md](../../../governance/ETHAN-POLICY-HESPERIA-DEV-PROD-CONTENT.md), [ETHAN-POLICY-HESPERIA-PUSH-AND-REMOTES.md](../../../governance/ETHAN-POLICY-HESPERIA-PUSH-AND-REMOTES.md), founder loop [ETHAN-HESPERIA-FOUNDER-SCOPE-INSPECTION-WORKFLOW-2026-04-03.md](ETHAN-HESPERIA-FOUNDER-SCOPE-INSPECTION-WORKFLOW-2026-04-03.md)  
**Prior close:** [GRACE-WRAP-UP-HESPERIA-0-6-1-0-6-2-2026-06-14.md](../GRACE-WRAP-UP-HESPERIA-0-6-1-0-6-2-2026-06-14.md) (board OPEN: 0)  
**New wave:** [HINS-2026-REGISTER.md](../../../governance/HINS-2026-REGISTER.md) — **HINS-00..16**

---

## 1. Executive summary

0.6.1/0.6.2 workflow rows are **DONE** on the brain board, and **dev-side KSI pytest (53)** passes on tersagor with `PYTHONPATH=src`. **Live prod and dev hygiene do not match the sealed narrative:**

| Area | Finding | Severity |
|------|---------|----------|
| **prichindel prod API** | `hesperia-api` **disabled**; `:9005/health` unreachable; public `/health` **503** | **P0** |
| **prichindel prod verify** | `verify-hesperia-prod-code-only.sh` **FAIL** — `output_views/staticfiles/**/LICENSE*.md` | **P1** |
| **alunel analyze-dev** | Service **active** but `.venv` path **missing** on disk (zombie `/usr/bin/python3.13` from deleted venv) | **P1** |
| **dev clone venv** | `atomic-commit-hesperia/.venv` → `python3.12` **missing**; dev pytest blocked | **P1** |
| **env_guard KSI** | `grep HESPERIA_KSI` on alunel `/data/hesperia/hesperia` → **0** (HFIX-26 DONE drift) | **P1** |
| **SHA divergence** | prichindel `d313bfd` · alunel mirror `cc94b09` · dev `6df2695` | **P2** |
| **tersagor full pytest** | 39 collection errors without `PYTHONPATH=src` (KSI subset OK) | **P2** |

**Argue:** Calling 0.6.2 “sealed” on governance docs while **prod API is disabled** breaks G8 evidence (“Python `/analyze` at prod path”). **Propose:** HINS wave closes **live prod + verify script + venv** before any 0.7.0 scope.

---

## 2. Inspection targets (2×2)

| | **Dev (alunel)** | **Prod (prichindel)** |
|---|------------------|------------------------|
| **hesperia** | `/data/workspaces/atomic-commit-hesperia` @ `6df2695` | `/data/hesperia/hesperia` @ `d313bfd` |
| **tersagor** | `/data/workspaces/tersagor` — KSI 53 PASS (`-k ksi`, `PYTHONPATH=src`) | N/A (agent bridge dev-only) |
| **Analyze API** | `hesperia-analyze-dev` :18880 **200** (zombie venv) | `hesperia-api` **disabled**, :9005 down |
| **HTTPS** | N/A | Site root **302** → inspector; `/health` **503** |

**alunel mirror (not dev clone):** `/data/hesperia/hesperia` @ `cc94b09` — used by systemd `hesperia-analyze-dev`; no `.venv` directory.

Ref: [cluster/HESPERIA-REPOS-AND-HOSTS.md](../../../cluster/HESPERIA-REPOS-AND-HOSTS.md) (SHA table **stale** — HINS-13).

---

## 3. Commands run (evidence)

```bash
# prichindel
cd /data/hesperia/hesperia && git log -1 --oneline   # d313bfd
bash scripts/verify-hesperia-prod-code-only.sh       # FAIL (2 LICENSE md under staticfiles)
systemctl is-enabled hesperia-api                    # disabled
curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:9005/health  # 000

# alunel
systemctl is-active hesperia-analyze-dev             # active
curl -s -o /dev/null -w "%{http_code}" http://127.0.0.1:18880/health # 200
ls /data/hesperia/hesperia/.venv/bin/python          # missing
ls /data/workspaces/atomic-commit-hesperia/.venv/bin/python  # broken symlink (python3.12)
cd /data/workspaces/tersagor && PYTHONPATH=src .venv/bin/python -m pytest tests/ -k ksi -q  # 53 passed
grep -c HESPERIA_KSI /data/hesperia/hesperia/runtime/shipping/env_guard.py  # 0
curl -s -o /dev/null -w "%{http_code}" https://hesperia.prichindel.com/health  # 503
```

---

## 4. Pipeline trace (founder contract §4)

```json
{
  "hesperia_ref": "cc94b09 (alunel mirror) / d313bfd (prichindel prod)",
  "tersagor_ref": "alunel /data/workspaces/tersagor (KSI 53 pass)",
  "target_repo": "Hesperia product 2×2 — atomic-commit-hesperia + prichindel prod + tersagor",
  "profile_or_module": "ethan_full_inspection_wave_2026_06_14",
  "pipeline_trace": [
    {"step": "policy_read", "artifact": "governance/ETHAN-POLICY-HESPERIA-DEV-PROD-CONTENT.md"},
    {"step": "prod_verify_script", "result": "FAIL", "artifact": "scripts/verify-hesperia-prod-code-only.sh"},
    {"step": "prod_systemd", "result": "hesperia-api disabled"},
    {"step": "dev_analyze_health", "result": "200", "port": 18880},
    {"step": "tersagor_ksi_pytest", "result": "53 passed", "note": "PYTHONPATH=src required"},
    {"step": "env_guard_ksi", "result": "0 matches on alunel mirror"},
    {"step": "gap_register", "artifact": "governance/HINS-2026-REGISTER.md"}
  ],
  "outcome_artifacts": [
    "operational/assignments/reports/ETHAN-HESPERIA-FULL-INSPECTION-2026-06-14.md",
    "governance/HINS-2026-REGISTER.md",
    "operational/assignments/GRACE-TRIAGE-HINS-2026-06-14.md"
  ],
  "operator_notes": "Board showed OPEN:0 after 0.6.2; live prod API off. HINS wave tasks Grace-triaged to active.md."
}
```

---

## 5. Exit criteria G1–G8 (re-check)

| Gate | Inspection verdict |
|------|-------------------|
| G1–G3 | Brain rows DONE; Grace H62-072 signed — **accept workflow** |
| G4 | **Partial** — tersagor KSI PASS; **hesperia dev clone pytest blocked** (venv); prod no venv |
| G5 | tersagor `ksi/` present — **OK on dev** |
| G6–G7 | Boundary doc + runbook exist in brain — **OK** |
| G8 | **FAIL live** — prod `/analyze` API unit **disabled**; dev `:18880` OK but fragile (missing venv dir) |

---

## 6. Gap → task mapping

See [HINS-2026-REGISTER.md](../../../governance/HINS-2026-REGISTER.md). Operator asked Ethan to **set tasks directly**; rows queued via [GRACE-TRIAGE-HINS-2026-06-14.md](../GRACE-TRIAGE-HINS-2026-06-14.md) → **active.md**.

**Explicitly out of HINS (0.7.0):** live LLM Teacher API, sandbox apply, KSI Inspector UI (KSI-19).

---

## 7. What / where / why (orientation bundles)

### Bundle A — Prod must run

- **What:** Enable Hesperia API on prichindel, restore health endpoints.
- **Where:** `/etc/systemd/system/hesperia-api.service`, `/data/hesperia/hesperia/runtime`, nginx upstream :9005.
- **Why:** G8 and GPT Actions depend on prod `/health` + `/hesperia/analyze`; sealed docs assumed this.

### Bundle B — Prod immaculate policy

- **What:** `verify-hesperia-prod-code-only.sh` green.
- **Where:** Strip or gitignore `output_views/staticfiles/**/LICENSE*.md`; avoid committing collectstatic vendor md.
- **Why:** [ETHAN-POLICY-HESPERIA-DEV-PROD-CONTENT.md](../../../governance/ETHAN-POLICY-HESPERIA-DEV-PROD-CONTENT.md) §2 — prod `main` is code+corpus only.

### Bundle C — Dev venv + analyze-dev

- **What:** Recreate venvs on alunel (mirror + dev clone); restart analyze-dev cleanly.
- **Where:** `/data/hesperia/hesperia/.venv`, `/data/workspaces/atomic-commit-hesperia/.venv`, `hesperia-analyze-dev.service`.
- **Why:** Gena smoke policy = dev clone; tersagor E2E uses `:18880`; zombie process hides missing venv.

### Bundle D — Code drift

- **What:** `env_guard` KSI vars; SHA promotion plan across three trees.
- **Where:** `runtime/shipping/env_guard.py`; git remotes `dev` / `origin`.
- **Why:** HFIX-26 marked DONE but mirror disk lacks `HESPERIA_KSI_*`; promotion line unclear after 0.6.2.

### Bundle E — Test gate for re-inspection

- **What:** Document/fix tersagor `PYTHONPATH`; dev hesperia pytest baseline script.
- **Where:** `tersagor/pyproject.toml` or `pytest.ini`; brain `scripts/verify-hesperia-dev-pytest.sh`.
- **Why:** Founder re-runs must not depend on tribal `PYTHONPATH=src` knowledge.

---

SIGNED: Team lead (Ethan) | Hesperia full inspection wave + HINS tasking | 2026-06-14 | HINS-14
