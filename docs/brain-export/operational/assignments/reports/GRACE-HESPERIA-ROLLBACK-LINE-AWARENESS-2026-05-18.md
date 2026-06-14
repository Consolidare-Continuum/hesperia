# Grace — Hesperia rollback line awareness (unpause readiness)

**Date:** 2026-05-18  
**Audience:** Grace, Ethan, Gena, Abelard, operator (igareosh)  
**Project:** hesperia — **output_views / deploy** (not engine core)

---

## Situation as-is (facts)

| Item | Value |
|------|--------|
| **Rollback line commit** | `ff55ef4` — `draw-line(2026-05-18): rollback marker — README + ROLLBACK-LINE doc` |
| **Git tag (all three remotes)** | `hesperia/rollback-line-20260518` |
| **Prior product pin** | `2aa1d43` — prod deploy pins (inspector nginx/systemd); tag `hesperia/line-clean-20260518` on disk where present |
| **Pre-merge disk tag (prod only)** | `backup/pre-align-20260518` |

**GitHub truth (same SHA on all allowed remotes):**

- `Atomic-Commits-Team/hesperia` (`origin`)
- `igareosh/hesperia` (`dev`)
- `igareosh/hesperia-dev-backup` (`backup`)

**Product repo paths:** prod `prichindel:/data/hesperia/hesperia` · dev `alunel:/data/workspaces/atomic-commit-hesperia` · brain pointers `cluster/HESPERIA-REPOS-AND-HOSTS.md`

**Canonical doc in product repo:** `ROLLBACK-LINE-2026-05-18.md` + README Status row (no engine code in that commit).

---

## What was aligned (2026-05-18)

- Merged `origin/main` TMX / hex-matrix track with local OUT-VIEW Session Inspector cherry-picks (**keep max**).
- Prod deploy: Django `output_views` on `:8010`, static hex-matrix under `/var/www/hesperia-sites/hex-matrix/`, nginx + Authentik on `hesperia.prichindel.com`.
- Pushed to all three GitHub remotes; alunel `main` hard-aligned to same SHA.

**Out of scope for this line:** Hesperia **engine core** (`hesperia/engine/`, sealed product surface, apocalyptic archive policy) — unchanged by draw-line commit.

---

## Live baseline (operator verification)

| Surface | URL |
|---------|-----|
| Session Inspector | https://hesperia.prichindel.com/inspector/1-11-09-2023/ |
| Inspector min fixture | https://hesperia.prichindel.com/inspector/session_inspector_min/ |
| Hex matrix | https://hesperia.prichindel.com/hex-matrix/ |

**Deploy script (brain):** `bash scripts/hesperia-prod-deploy.sh` · **Verify:** `bash scripts/verify-hesperia-prod-https.sh`

---

## OUT-VIEW — question CLOSED (2026-05-19)

- **OUT-VIEW epics** in `active.md` (**OUT-VIEW-00..09**, **OUT-VIEW-FULL-01..05**, **OUT-VIEW-CONSIST-01**; Ethan **T01–T45** + Cursor **T46–T65**) are **DONE** on historical branch **`ed-0.5.6-calibration-baseline`** — commits in epic outcome columns and [GRACE-OUT-VIEW-FULL-WAVE-CLOSURE-2026-04-07.md](GRACE-OUT-VIEW-FULL-WAVE-CLOSURE-2026-04-07.md).
- **No continuation track** for OUT-VIEW: proposed **HES-LINE-00..04** **withdrawn**; formal ack **HES-OUT-VIEW-ACK-00** DONE — [GRACE-HESPERIA-OUT-VIEW-QUESTION-CLOSED-2026-05-19.md](GRACE-HESPERIA-OUT-VIEW-QUESTION-CLOSED-2026-05-19.md).
- **Product line now:** **`hesperia/dev-ready-line-20260518`** (debloat closed) — new features = **new Grace rows** only; do not bulk-reopen OUT-VIEW epics.
- **Parameter Golf** **purged** 2026-06-03 — [archive/parameter_golf_purged_2026-06-03/GRACE-PURGE-PARAMETER-GOLF-2026-06-03.md](../../../archive/parameter_golf_purged_2026-06-03/GRACE-PURGE-PARAMETER-GOLF-2026-06-03.md).

---

## Rollback commands (team)

```bash
git fetch --all --tags
git checkout main
git reset --hard hesperia/rollback-line-20260518   # → ff55ef4
```

Earlier: `hesperia/line-clean-20260518` (`2aa1d43`), `backup/pre-align-20260518` (prod disk, pre-merge) — see product `ROLLBACK-LINE-2026-05-18.md`.

---

## References

| Doc | Path |
|-----|------|
| Grace triage (unpause — closed) | [GRACE-TRIAGE-HESPERIA-ROLLBACK-LINE-UNPAUSE-2026-05-18.md](../GRACE-TRIAGE-HESPERIA-ROLLBACK-LINE-UNPAUSE-2026-05-18.md) |
| OUT-VIEW question closed | [GRACE-HESPERIA-OUT-VIEW-QUESTION-CLOSED-2026-05-19.md](GRACE-HESPERIA-OUT-VIEW-QUESTION-CLOSED-2026-05-19.md) |
| Ethan — further dev tasking | [ETHAN-HESPERIA-POST-REVOLUTION-DEV-TASKING-2026-05-19.md](ETHAN-HESPERIA-POST-REVOLUTION-DEV-TASKING-2026-05-19.md) |
| Brain 2×2 map | [cluster/HESPERIA-REPOS-AND-HOSTS.md](../../../cluster/HESPERIA-REPOS-AND-HOSTS.md) |
| OUT-VIEW closure | [GRACE-OUT-VIEW-FULL-WAVE-CLOSURE-2026-04-07.md](GRACE-OUT-VIEW-FULL-WAVE-CLOSURE-2026-04-07.md) |
| Product rollback doc | https://github.com/Atomic-Commits-Team/hesperia/blob/main/ROLLBACK-LINE-2026-05-18.md |

`SIGNED: Cursor (repo entity) | Grace awareness — Hesperia rollback line | 2026-05-18 | OUT-VIEW question closed 2026-05-19`
