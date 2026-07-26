# Hesperia project — single repo at /data/hesperia

**Hesperia is a separate project.** Prichindel cluster has no involvement. One repo, one GitHub repo, one VS Code workspace.

**Goal**: One Git repo at `/data/hesperia`; contents from prichindel + sphere as subdirs `prichindel/` and `sphere/`; deprecated repo configs (old .git) removed; single remote; workspace root `/data/hesperia`.

**Confirm before running** (deployment/move).

---

## 1. Result layout

```
/data/hesperia/          ← one .git, one GitHub repo, VS Code workspace root
├── prichindel/          ← former repo, now subdir (no .git)
├── sphere/              ← former repo, now subdir (no .git)
├── .git/
├── .gitignore
└── README.md            (optional)
```

---

## 2. Steps (single repo)

1. **Create target**: `sudo mkdir -p /data/hesperia && sudo chown "$USER:$USER" /data/hesperia`
2. **Move content** (no .git): move or copy `/home/igareosh/prichindel` and `/home/igareosh/sphere` into `/data/hesperia/` so you have `/data/hesperia/prichindel/` and `/data/hesperia/sphere/`. Remove any `.git` inside those subdirs (deprecated): `rm -rf /data/hesperia/prichindel/.git /data/hesperia/sphere/.git`
3. **Init one repo**: `cd /data/hesperia && git init && git add . && git commit -m "Initial: prichindel + sphere merged"` (or add remote first: `git remote add origin <hesperia-github-url>`)
4. **One remote**: `git remote add origin https://github.com/<user>/hesperia.git` (or existing URL). Push: `git push -u origin main`
5. **Workspace**: Open VS Code / Cursor with folder `/data/hesperia`.

---

## 3. Script

`prichindel/scripts/move-to-hesperia.sh` — run from workspace that still has prichindel; it creates /data/hesperia, moves prichindel and sphere as subdirs, **removes** their .git, inits **one** repo at /data/hesperia. Add remote and push manually. **Confirm before running.**

---

## 4. Deprecated / optional cleanup

- Old separate prichindel repo (.git in prichindel) — removed when building hesperia; originals under /home/igareosh can be deleted after you verify /data/hesperia.
- Old separate sphere repo (.git in sphere) — same.
- Prichindel cluster: no involvement. Hesperia is not under SURVEILLANCE or CLUSTER_SYSADMIN.
