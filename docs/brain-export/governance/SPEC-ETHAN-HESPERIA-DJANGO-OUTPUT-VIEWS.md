# Spec: Hesperia — Django as output view foundation + page builder

**Author:** Ethan (Chief Architect).  
**Purpose:** Define how **Django** is introduced into the **Hesperia** product repo as the **human-facing output layer** (HTML pages, printable reports, internal dashboards), with a **page builder** pattern so the team can ship views without forking ad-hoc templates each time. This is the **can-start** document for implementation once the operator authorizes the work package.

**Status:** Architecture and task boundaries only. No Django code in Hesperia until this spec is accepted and Grace triage assigns rows (or operator directs execution).

**Canonical location:** Brain repo `governance/SPEC-ETHAN-HESPERIA-DJANGO-OUTPUT-VIEWS.md`. Optional mirror later: `hesperia/docs/governance/` (short pointer + Hesperia-local paths).

**Refs:** Hesperia shipping API (`runtime/shipping/api_main.py` — FastAPI), `requirements/runtime.txt`, `pyproject.toml`, brain `HESPERIA-TFP-YIELDED-PARAMETERS-TABLE.md` (output field inventory), `REPO-SELF-SERVICE.md` (Ethan specs; no change to team operational layer files).

**Preview UI design authority:** [SPEC-ETHAN-HESPERIA-OUTPUT-PREVIEW-DESIGN-TEMPLATES.md](SPEC-ETHAN-HESPERIA-OUTPUT-PREVIEW-DESIGN-TEMPLATES.md) — Black Dashboard Django (operator) + React Datta Able Django (client SPA reference).

**Flagship page (session review):** [SPEC-ETHAN-HESPERIA-SESSION-ITERATION-INSPECTOR-PAGE.md](SPEC-ETHAN-HESPERIA-SESSION-ITERATION-INSPECTOR-PAGE.md) — Cursor-style three-pane inspector; one page = one session.

---

## 1. Problem and intent

| Need | Approach |
|------|----------|
| **JSON API** for product / automation | Keep **FastAPI** shipping and dev APIs as today; they remain the **machine contract** (analyze, health, batch, etc.). |
| **Readable outputs** (reports, run summaries, calibration diffs, TFP tables as pages) | Add **Django** as a **separate app surface** that **renders** data already produced by the engine, files, or internal calls. |
| **Repeatable page shapes** | **Page builder**: declarative **page specs** (YAML/JSON) + **typed context** + shared **blocks/partials**; not one-off copy-paste templates for every screen. |

---

## 2. Non-negotiable boundaries

| Rule | Rationale |
|------|-----------|
| **Do not replace FastAPI** with Django for the sealed **public JSON** surface in v1. | License, rate limit, schema guards, and existing clients stay on FastAPI unless a later ADR explicitly migrates. |
| **Django has no silent write path** to production calibration assets or dict packs. | Read-only or explicitly gated admin; writes stay tooling/CI/operator flows. |
| **Single engine truth** | Pages display results from **the same** analysis pipeline / artifacts as JSON API; no second scoring implementation inside Django views. |
| **Secrets** | Django settings use env only (pattern aligned with `HESPERIA_*`); Daniel/SECURITY-BASELINE when auth or cookies are introduced. |

---

## 3. Architecture (logical)

```
┌─────────────────────┐     ┌──────────────────────────────┐
│  FastAPI (existing) │     │  Django (new)                 │
│  JSON / OpenAPI     │     │  HTML / optional internal API │
│  shipping + dev     │     │  output_views / pages         │
└─────────┬───────────┘     └──────────────┬───────────────┘
          │                                │
          └────────────┬───────────────────┘
                       ▼
            hesperia engine / services
            (analysis_service, ctx, artifacts)
```

- **Integration options (pick one primary for v1; others phased):**

| Mode | When | How |
|------|------|-----|
| **A. In-process library** | v1 default | Django view calls Python API already used by FastAPI (e.g. `runtime.services` / engine run) in the **same venv**. |
| **B. HTTP client** | optional | Django calls local FastAPI (`127.0.0.1`) for parity with external clients; adds latency and auth coupling. |
| **C. Artifact reader** | reports | View loads frozen JSON from `assets/artifacts/` or run output paths (E2E, bundles). |

**Recommendation:** **A + C** for v1 — fast iteration, no circular HTTP; artifact-backed pages for CI/gold comparisons.

---

## 4. Repository layout (Hesperia — target)

Paths are **proposed**; exact names are implementation detail if equivalent structure is kept.

| Path | Role |
|------|------|
| `output_views/` (or `hesperia_output/`) | Django **project root**: `manage.py`, `config/settings/`, `config/urls.py`, `wsgi.py` |
| `output_views/apps/pages/` | **Page builder** app: views, URL includes, template tags |
| `output_views/apps/pages/specs/*.yaml` | **Page specifications** (layout id, blocks, optional data source key) |
| `output_views/templates/blocks/` | Reusable fragments (tables, KPI row, TFP profile summary) |
| `output_views/static/` | Collected static for prod (`collectstatic`) |
| `output_views/tests/` | `pytest-django` or Django test runner |

**Dependency management:** Add a **`requirements/output_views.txt`** (or optional extra in `pyproject.toml`) pinning **Django LTS** and minimal stack (e.g. `django-environ`, `whitenoise` for static). Keep **shipping** install lean: CI that does not need HTML must not require Django unless job is `output_views`.

---

## 5. Page builder contract (v1)

| Element | Spec |
|---------|------|
| **PageSpec** | YAML: `id`, `title`, `layout` (`single_column` \| `two_column`), `blocks[]` each with `type` + `props`. |
| **Block types (initial set)** | `markdown` (safe subset or rendered from trusted strings only), `key_value`, `json_table`, `tfp_profile_card`, `artifact_embed` (path key → registered allowlist root). |
| **Context builder** | Python registry: `build_context(spec_id, request) -> dict` mapping block ids to data; **no** arbitrary file paths from query string without allowlist. |
| **Templates** | One base `layout.html`; blocks map `type` → `blocks/<type>.html`. |

**Security:** No raw `|safe` on user input. Report text from engine must pass an explicit **escape** or **bleach** policy if ever user-supplied.

---

## 6. TFP / engine alignment

| Brain reference | Django use |
|-----------------|------------|
| `HESPERIA-TFP-YIELDED-PARAMETERS-TABLE.md` | Block types and table columns for **`tfp.v1`** and **invariant activation** views. |
| Calibration artifacts | Read-only display links + version string from `VERSION.yaml` / env pin. |

---

## 7. Operations (Abelard)

| Topic | Guideline |
|-------|-----------|
| **Process** | Separate **Gunicorn/Uvicorn worker** (Django ASGI/WSGI) from FastAPI process; **different port**. |
| **Reverse proxy** | Nginx path prefix e.g. `/hesperia/views/` → Django; `/hesperia/api/` → FastAPI (example; operator names paths). |
| **Static** | `collectstatic` to known dir; Nginx serves static in prod. |
| **Env** | `DJANGO_SECRET_KEY`, `DJANGO_DEBUG`, `HESPERIA_ASSETS_ROOT` alignment, optional `OUTPUT_VIEWS_ALLOWED_HOSTS`. |

---

## 8. Phased work package (for Grace triage → active.md)

| Phase | Deliverable | Primary owner |
|-------|-------------|---------------|
| **P0** | Pin Django LTS + split requirements; empty project boots; `/health` view | Gena |
| **P1** | One **artifact-backed** page (load JSON from known path under repo) + tests | Gena |
| **P2** | **PageSpec** YAML loader + 2–3 block types + registry context builder | Gena |
| **P3** | **In-process** analysis demo page (single `analyze` path, not full product load) | Gena |
| **P4** | Docs in Hesperia: `docs/governance/HESPERIA-DJANGO-OUTPUT-VIEWS.md` (paths, runbook, dev server command) | Gena + Ethan review |
| **P5** | Deploy recipe + Nginx stub in cluster docs | Abelard |

**Handoff:** Infra beyond localhost → **task Grace** → Abelard; JSON/engine regressions → **Gena**; governance edits → **Ethan**.

---

## 9. Open decisions (operator / Ethan before P2)

| Decision | Options |
|----------|---------|
| **Auth** | None (LAN only) vs Django admin vs SSO later |
| **DB** | No DB v1 (stateless) vs SQLite for page analytics later |
| **Package name** | `output_views` vs `hesperia_web` (pick one, avoid `hesperia` top-level clash with existing package) |

---

`SIGNED: Ethan (Chief Architect) | Hesperia Django output views | 2026-04-07 | governance spec`
