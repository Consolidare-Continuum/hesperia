# Grace triage — Hesperia web outputs (pages, OpenAI, CSS)

**Date:** 2026-05-19  
**Operator intent (igareosh):** Grace add tasks so Hesperia **web outputs** deliver:

1. **All pages and links available atm** — properly working (no dead nav, 404s, or broken query links).
2. **OpenAI feature to respond** — not copy/export only; operator sees a **model reply** in the UI.
3. **CSS added and enabled** — coloring per available data (inspector chips, panes, hex-matrix heatmap / RU surface).

**Out of scope this packet:** TMX-10..24 polish rows (separate epic); engine/dictionary work; bulk re-open OUT-VIEW-01..09.

**Prod gate reality (Abelard 2026-05-18):** `hesperia.prichindel.com` nginx currently serves **`/hex-matrix/`** SPA + FastAPI **`/hesperia/`**; Django `output_views` routes are **in prod repo** but **not** on public nginx until **HES-WEB-05** aligns deploy. Dev acceptance = `runserver 8010` per [Hesperia `docs/output_views/README.md`](../../../../hesperia/hesperia-dev/docs/output_views/README.md) on dev mirror.

**Policy:** Prod code on `Atomic-Commits-Team/hesperia`; dev docs on `igareosh/hesperia`. Deploy/smoke routing: [governance/ETHAN-POLICY-HESPERIA-DEV-PROD-CONTENT.md](../../governance/ETHAN-POLICY-HESPERIA-DEV-PROD-CONTENT.md) §4.

---

## Surfaces “available atm” (inventory)

### Django `output_views` (repo — prod tree has code)

| Route | Purpose |
|-------|---------|
| `/` | Operator home — cards to Inspector, client preview, artifacts |
| `/sessions/` | Sessions index |
| `/inspector/<session_id>/` | Session Inspector (fixtures: `session_inspector_min`, `1-11-09-2023`, …) |
| `/inspector/<session_id>/export.json` | OpenAI segment JSON download |
| `/inspector/<session_id>/openai-proxy/` | POST proxy → Chat Completions (flag-gated) |
| `/health/` | Health JSON |
| `/preview/client/` | Client preview shell |
| `/preview/artifacts/` | E2E artifact listing |

**Nav links** (`base.html`): Operator, Sessions, Inspector (min fixture), Client preview, Health.

**OpenAI today:** Copy + download when `export_segment` present; proxy button only if `HESPERIA_OUTPUT_VIEWS_OPENAI_PROXY=1` — response is JSON (`content`) but UI may not render reply inline (**HES-WEB-03**).

**CSS today:** `static/output_views/css/site.css` linked from `base.html` — dark theme, chips, inspector grid (**HES-WEB-04** verify collectstatic/nginx).

### Hex matrix SPA (`output_views/hex_matrix_viewer/dist/`)

| Route (prod) | Purpose |
|--------------|---------|
| `https://hesperia.prichindel.com/hex-matrix/` | Static SPA — RU i18n (`src/i18n/ru.js`), RelationsPanel, D3 coloring |

Deploy: `rsync` dist → `/var/www/hesperia-sites/hex-matrix/`; do not rsync-delete from stale alunel without git log check (Abelard WORKFLOW-NOTES 2026-05-18).

---

## Executable rows (`active.md`)

| ID | Owner | Task |
|----|--------|------|
| **HES-WEB-00** | Grace | This packet + rows in `active.md`. |
| **HES-WEB-01** | Gena | **Link inventory** — document every operator-facing URL; fix broken template/nav/session links. |
| **HES-WEB-02** | Gena | **Page smoke** — all routes above 200 on dev (`manage.py runserver`); gold fixtures load. |
| **HES-WEB-03** | Gena | **OpenAI respond** — in-page model reply (proxy or fetch); errors surfaced; env documented. |
| **HES-WEB-04** | Felix | **CSS coloring** — `site.css` + inspector chips + hex-matrix dist CSS enabled and served. |
| **HES-WEB-05** | Abelard | **Prod gate** — nginx/service so chosen surfaces live on `hesperia.prichindel.com`; HTTPS smoke links + CSS. |
| **HES-WEB-06** | Daniel | **QA checklist** — browser: links, OpenAI one reply, visible coloring. |
| **HES-WEB-07** | Grace | **Closure** — DoD vs three operator bullets; short report. |

**Suggested execution order:** **HES-WEB-01** → **02** → **03** + **04** (parallel) → **05** → **06** → **07**.

**First IN_PROGRESS:** **HES-WEB-01** (Gena).

---

## Definition of done (operator)

| Bullet | Done when |
|--------|-----------|
| Pages/links | Every link in operator nav + home cards + sessions list + inspector iteration/sentence links works on dev; prod matches deploy decision in **05**. |
| OpenAI respond | Operator triggers one action and sees **assistant text** in UI (not silent POST / copy-only). |
| CSS coloring | Inspector and/or hex-matrix show intended colors (chips, heatmap, theme) — not unstyled HTML. |

---

`SIGNED: Grace (triage) | HES-WEB-00..07 | 2026-05-19 | active.md + this packet`
