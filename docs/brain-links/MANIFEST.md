# Brain repo links (cursor) — manifest only

**Generated:** 2026-06-29T16:15Z  
**Brain path:** `/data/altitudine/prichindel.com`  
**Policy:** brain `governance/ETHAN-POLICY-HESPERIA-BRAIN-DEV-LINK.md`  
**Dev-ready tag:** `hesperia/dev-ready-line-20260518`

This file is a **pointer index**. It does **not** copy the brain repo into Hesperia git.

## Team / triage (brain only)

| What | Brain path |
|------|------------|
| Active tasks | `active.md` |
| Hesperia 2×2 map | `cluster/HESPERIA-REPOS-AND-HOSTS.md` |
| Dev/prod content policy | `governance/ETHAN-POLICY-HESPERIA-DEV-PROD-CONTENT.md` |
| Brain↔dev link policy | `governance/ETHAN-POLICY-HESPERIA-BRAIN-DEV-LINK.md` |
| Push remotes | `governance/ETHAN-POLICY-HESPERIA-PUSH-AND-REMOTES.md` |
| Link index (brain) | `CLIENTS/hesperia/README.md` |
| Prod deploy | `scripts/hesperia-prod-deploy.sh` |
| Prod verify HTTPS | `scripts/verify-hesperia-prod-https.sh` |
| Prod code-only verify | `scripts/verify-hesperia-prod-code-only.sh` |
| Debloat wave 2 closure | `operational/assignments/GRACE-TRIAGE-HES-DEBLOAT-WAVE2-2026-06-14.md` (stub → brain-export) |

## Brain-export (wave 2 — canonical on this repo)

Moved from brain 2026-06-14. **Do not re-import into cursor.**

| What | Path on `igareosh/hesperia` |
|------|-------------------------------|
| Full export tree | `docs/brain-export/` |
| Operational reports / formalization | `docs/brain-export/operational/` |
| Governance specs | `docs/brain-export/governance/` |
| Archives (0.6.3 zip) | `docs/brain-export/root/` |
| Dev-ready line (historical) | `docs/brain-export/operational/assignments/HESPERIA-DEV-READY-LINE-2026-05-18.md` |

**Dev host:** **altitudine** VM (`192.168.100.65`) — not alunel bare metal. Clone: `/data/workspaces/atomic-commit-hesperia`.

## Canonical Hesperia documentation (this repo — dev)

| What | Path on `igareosh/hesperia` |
|------|-------------------------------|
| All `docs/` | this repo |
| Prod strip backup | `docs/backup/prod-immaculate-2026-05-18/` |
| Dev-ready line | `docs/DEV-READY-LINE-2026-05-18.md` |
| Dev/prod split | `docs/DEV_PROD_SPLIT.md` |

## Forbidden

- Ingest Hesperia product tree into brain repo root.
- Commit `cursor-brain-mirror/` into either repo (disk-only optional).

