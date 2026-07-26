# Grace triage — Hesperia dev/prod split (first task after rollback line)

**Date:** 2026-05-18  
**Operator intent:** After draw line (`ff55ef4` / `hesperia/rollback-line-20260518`), **first** continuation = separate **documentation** from **runnable prod**. No team notes, planning, archives, or chat residue on **`Atomic-Commits-Team/hesperia`**. Prod = code + sealed assets + comments in code only. Dev = **`igareosh/hesperia`**.

**Policy:** [governance/ETHAN-POLICY-HESPERIA-DEV-PROD-CONTENT.md](../../governance/ETHAN-POLICY-HESPERIA-DEV-PROD-CONTENT.md)  

**Closure (2026-05-19):** Wave **DONE** — [GRACE-HESPERIA-DEBLOAT-CLOSURE-2026-05-19.md](reports/GRACE-HESPERIA-DEBLOAT-CLOSURE-2026-05-19.md). Prod `18178de` · dev `777c4ef3`.

---

## Triage summary

| Field | Value |
|-------|--------|
| **Rollback anchor** | `ff55ef4` — do not strip below this without new tag |
| **Prod inventory (2026-05-18)** | ~1175 `*.md` on disk; **293** under `docs/`; `.cursor/` present; root `CURSOR_*`, `AGENTS.md`, `ROLLBACK-LINE-2026-05-18.md` |
| **Dev remote** | `igareosh/hesperia` @ same SHA today; receives migrated doc trees |
| **Corpus rule (operator 2026-05-18)** | **Do not** strip/move `hesperia/modules/tfp/data/**` (books, sessions, normalization), sealed `assets/calibration/dicts/**` JSONL, or `specs/canon/*.yaml` runtime config. Drive out only Cursor/Hesperia dev docs, `specs/**/*.md`, tasks, legacy narrative. |
| **Out of scope** | Engine core mutation |

---

## Executable rows (`active.md`)

| ID | Owner | Task |
|----|--------|------|
| **HES-SPLIT-00** | Grace | This packet + Ethan policy linked; rows in `active.md`. |
| **HES-SPLIT-01** | Ethan | Policy locked ([ETHAN-POLICY-HESPERIA-DEV-PROD-CONTENT.md](../../governance/ETHAN-POLICY-HESPERIA-DEV-PROD-CONTENT.md)). |
| **HES-SPLIT-02** | Gena | On alunel: ensure `dev` remote has full `docs/` + root narrative md from `ff55ef4`; push **`igareosh/hesperia`**. |
| **HES-SPLIT-03** | Gena | On prichindel: strip prod tree per §2 forbidden list; **atomic commits** on `main`; push **`origin`** only; tag optional `hesperia/prod-code-only-20260518`. |
| **HES-SPLIT-04** | Daniel | Wire `scripts/verify-hesperia-prod-code-only.sh` in CI or pre-push hook on prod clone. |
| **HES-SPLIT-05** | Abelard | `git pull` prod + `hesperia-prod-deploy.sh` + `verify-hesperia-prod-https.sh` — inspector + hex-matrix. |
| **HES-SPLIT-06** | Ethan | Rule for `research/**` md corpus (keep on prod as data vs move to dev) — separate commit. |

**First IN_PROGRESS:** **HES-SPLIT-02** (dev mirror) then **HES-SPLIT-03** (prod strip).

---

## Prod strip — atomic commit plan (Gena)

Execute on `prichindel:/data/hesperia/hesperia` after **HES-SPLIT-02** pushed:

1. `chore(prod): remove .cursor/`
2. `chore(prod): remove docs/ (documented on igareosh/hesperia)`
3. `chore(prod): remove root team and cursor markdown`
4. `chore(prod): remove _release_tmp/`
5. `chore(prod): gitignore generated outputs markdown`
6. `chore(prod): README pointer to dev repo only`

Replace root `README.md` with:

```markdown
# Hesperia (prod)

Runnable product. Documentation and context: https://github.com/igareosh/hesperia

Rollback: `git checkout hesperia/rollback-line-20260518`
```

Remove: `ROLLBACK-LINE-2026-05-18.md` from prod (keep on dev + git tag).

---

## Verification

```bash
bash scripts/verify-hesperia-prod-code-only.sh /data/hesperia/hesperia
bash scripts/verify-hesperia-prod-https.sh
```

---

## Dependencies

- **Blocks:** HES-LINE-01 (Gena smoke) until HES-SPLIT-03 + HES-SPLIT-05 DONE.
- **Does not block:** brain repo assignments (stay in `operational/`).

`SIGNED: Grace (triage) | Hesperia dev/prod split | 2026-05-18 | first task post draw-line`
