# alunel — Hesperia development

**Updated**: 2026-05-19  
**Owner**: Abelard. **2 repos × 2 servers**: [cluster/HESPERIA-REPOS-AND-HOSTS.md](../HESPERIA-REPOS-AND-HOSTS.md) — **dev** = alunel + `igareosh/hesperia`; **prod** = prichindel + **`/data/hesperia/hesperia`** + `Atomic-Commits-Team/hesperia`. Brain: [CLIENTS.md](../../CLIENTS.md), [GITHUB-REPOS.md](../GITHUB-REPOS.md).

## Routing (commit / deploy / smoke)

| Who | Do here on alunel |
|-----|-------------------|
| **Gena** — docs | `git push dev` → `igareosh/hesperia`; team docs in brain repo |
| **Gena** — code | dev first; promote to prod when ready |
| **Gena** — smoke | **this clone only** — not prod |
| **Abelard** — deploy | **prichindel prod only** — not this path |

Policy: [governance/ETHAN-POLICY-HESPERIA-DEV-PROD-CONTENT.md](../../governance/ETHAN-POLICY-HESPERIA-DEV-PROD-CONTENT.md) §4.

## One-shot bootstrap (alunel)

```bash
cd /data/workspaces/cursor
bash scripts/alunel-hesperia-bootstrap.sh
```

## Layout

| Path | Role |
|------|------|
| **`/data/workspaces/atomic-commit-hesperia`** | Git clone **`git@github.com:Atomic-Commits-Team/hesperia.git`** (same path convention as prichindel) |
| **`.venv/`** | Python **3.12.8** (pyenv interpreter — not `/usr/bin/python3` for app work); gitignored |
| **`.env`** | Optional secrets (e.g. **`OPENAI_API_KEY`**) — gitignored; **no values in repo** |

## Python ([PYTHON-STANDARD.md](PYTHON-STANDARD.md))

```bash
cd /data/workspaces/atomic-commit-hesperia
"$HOME/.pyenv/versions/3.12.8/bin/python3.12" -m venv .venv
.venv/bin/pip install -U pip
.venv/bin/pip install -r requirements.txt
```

**Editable install (`pip install -e .`)**: may **fail** on current `pyproject.toml` / flat layout (setuptools discovers many top-level dirs including `tmp/`). For dev on alunel, use **`PYTHONPATH`** to the repo root (see below) — same as running without a local install.

**Convenience (activate + `PYTHONPATH`):**

```bash
source /data/workspaces/cursor/scripts/alunel-hesperia-dev-env.sh
```

## Run / verify

```bash
source /data/workspaces/cursor/scripts/alunel-hesperia-dev-env.sh
python tools/validate_version_consistency.py
python -m hesperia.run --help
# pytest (optional):
# python -m pytest tests/ -q --tb=no
```

**Shipping API** (local, tersagor default): `hesperia-analyze-dev` systemd on **`127.0.0.1:18880`** — install [systemd/hesperia-analyze-dev.service](systemd/hesperia-analyze-dev.service). Manual: `HESPERIA_API_PORT=18880 python -m uvicorn runtime.shipping.api_main:app --host 127.0.0.1 --port 18880` from `/data/hesperia/hesperia` with `.venv` + `PYTHONPATH` (install **`uvicorn`** in `.venv` if not pulled in by your extras).

**Optional extras** (dict / OpenAI / spaCy): `pip install -e ".[dict-calibration]"` may hit the same setuptools discovery issue — install optional deps manually from `pyproject.toml` if needed.

## Secrets

- **Locations only** (see [cluster/GITHUB-REPOS.md](../GITHUB-REPOS.md)): **`OPENAI_API_KEY`** in **`.env`** at repo root or environment.  
- To mirror prichindel: **copy `.env` yourself** (scp/rsync); do not commit.

## Chroma / MCP

- **alunel local Chroma** (dev): [CHROMA.md](CHROMA.md) — `chroma-1.prichindel.local:8002`.  
- **Team MCP + Chroma** still **prichindel**-hosted when using Cursor per [CURSOR-DEV-HOST.md](CURSOR-DEV-HOST.md). Point Hesperia clients at the URL your config expects.

## Git

```bash
cd /data/workspaces/atomic-commit-hesperia
git pull
# Remote: use ~/.ssh/github_key (see cluster/alunel/README.md)
```

**Push policy (Ethan):** Hesperia code may be pushed **only** to `github.com/igareosh/hesperia`, `github.com/igareosh/hesperia-dev-backup`, or `github.com/Atomic-Commits-Team/hesperia`. No other remotes — [governance/ETHAN-POLICY-HESPERIA-PUSH-AND-REMOTES.md](../../governance/ETHAN-POLICY-HESPERIA-PUSH-AND-REMOTES.md).

## References

- Hesperia **README** / **docs/** inside the clone.  
- D3 viewer notes: [agents/abelard/ABELARD_QUICK_OPS.md](../../agents/abelard/ABELARD_QUICK_OPS.md) (prichindel **systemd** viewer — not installed on alunel by default; use `python3 -m http.server` from repo **`hesperia/`** per upstream docs if needed).

SIGNED: DevOps (Abelard) | alunel Hesperia dev | 2026-04-05 | clone + venv + PYTHONPATH workflow
