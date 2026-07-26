# Hesperia version tag registry

**Updated:** 2026-06-14 (pass 4 audit — reconcile + e9eaa07 HEAD row)  
**Repos:** `igareosh/hesperia` (dev) · `Atomic-Commits-Team/hesperia` (prod) — **same SHAs after promote**

| Tag | Commit | Date | What it marks |
|-----|--------|------|----------------|
| `hesperia-v0.2-20260220` | `eea358a` | 2026-02-20 | ΣΓΘ guards + v0.2 release |
| `hesperia-v0.3.0` | `ffc5371` | 2026-02-22 | Math contract + shadow layer |
| `hesperia-v0.4.0` | `dcbb38b` | 2026-02-24 | L1–L9 runnable stack (tag → commit; was listed as tag object d9abcbf) |
| `v0.5.0` … `v0.5.8` | (see git tag -l) | Mar–Apr 2026 | Engine dynamics + contradiction seals |
| `hesperia/dev-ready-line-20260518` | `d9a7cdf` | 2026-05-19 | Prod debloat complete; docs on dev |
| `0.6.0` | `d06f674` | 2026-05-28 | Sealed runtime baseline |
| **`hesperia-0.6.1`** | **`f87b2bb`** | 2026-06-14 tag | HES-61-01: Python `/analyze` `engine_result` contract |
| **`hesperia-0.6.2`** | **`cc94b09`** | 2026-06-14 tag | 6.1-final + model default; KSI layer sealed in brain + tersagor |
| **`0.6.3`** / **`hesperia-0.6.3`** | **`122d45b`** | 2026-06-14 | **Reconciled main:** 0.6.3 archive (`16286fa`) merged with 6.1 line (`cc94b09`) |
| **`main` HEAD** | **`e9eaa07`** | 2026-06-14 | **Product:** `runtime/irc_teacher/` on dev+prod (post-tag) |

## Reconcile note (2026-06-14)

Prior inconsistency: `origin/main` and tag `0.6.3` pointed at **`cc94b09`** while dev tag `hesperia-0.6.3` pointed at **`16286fa`** on a **diverged branch** after `d06f674`.

**Fixed:** merge `origin/main` → dev, retag `0.6.3` and `hesperia-0.6.3` to merge commit **`122d45b`**; add retro tags `hesperia-0.6.1`, `hesperia-0.6.2`; push both remotes; prod disk fast-forwarded.

**Live 0.6.3 IRC Teacher** runtime on **product** `runtime/irc_teacher/` @ **`e9eaa07`**; tersagor integration @ **`0149120`**. Tag **`0.6.3`** remains **`122d45b`** (reconcile).

Verify: `git rev-parse 0.6.3^{commit} hesperia-0.6.3^{commit}` on either clone → **`122d45b`**.

## Reasoning artifact (0.6.0 → 0.6.3)

| Artifact | Path |
|----------|------|
| KAN feasibility + concept-layer spec (PDF) | Brain: [operational/assignments/reports/hesperia-0.6.x/HESPERIA-KAN-FEASIBILITY-RESEARCH-AND-CONCEPT-LAYER-SPECIFICATION-0.6.0-0.6.3-REASONING.pdf](../operational/assignments/reports/hesperia-0.6.x/HESPERIA-KAN-FEASIBILITY-RESEARCH-AND-CONCEPT-LAYER-SPECIFICATION-0.6.0-0.6.3-REASONING.pdf) |
| Dev mirror | `igareosh/hesperia` → `docs/reference/` (same filename) |
| Evolution companion | [operational/assignments/reports/ETHAN-HESPERIA-EVOLUTION-TREE-0-TO-NOW-2026-06-14.txt](../operational/assignments/reports/ETHAN-HESPERIA-EVOLUTION-TREE-0-TO-NOW-2026-06-14.txt) |

SIGNED: Ethan | version tag registry | 2026-06-14 | pass 4 audit align + KAN PDF index
