# GitHub mirror setup v1

**Purpose:** One-time setup of the backup mirror, then use `./tools/push_mirrors.sh` after significant releases.

---

## 1. Create the mirror repository on GitHub

- **Name:** `hesperia-dev-backup`
- **Owner:** `igareosh` (or your preferred org)
- **Visibility:** private
- **Initialize:** **NO** — do not add README, license, or .gitignore

---

## 2. Push the mirror (once)

From repo root:

```bash
git push backup --mirror
```

This copies everything: branches, tags, refs, full history.

---

## 3. Verify

```bash
git remote -v
```

You should see:

- `origin` → `github.com/Atomic-Commits-Team/hesperia`
- `backup` → `github.com/igareosh/hesperia-dev-backup`

---

## 4. Optional: protect the mirror

In the GitHub repo **Settings → Branches**: add a rule that **disables force pushes**. The mirror is a recovery archive; nobody should rewrite it.

---

## 5. Ongoing: sync after releases

```bash
./tools/push_mirrors.sh
```

Pushes `main` and tags to `origin`, then does a full `git push backup --mirror`.

Run after significant releases so the mirror stays current.
