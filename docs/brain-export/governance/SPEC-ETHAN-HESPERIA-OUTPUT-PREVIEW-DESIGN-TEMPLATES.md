# Spec: Hesperia — canonical output preview design templates (Ethan)

**Author:** Ethan (Chief Architect).  
**Purpose:** Lock **two** approved **reference implementations** for Hesperia-wide **HTML / dashboard / client preview** work so design and engineering do not fork one-off UIs per feature. Teams **align** `output_views` and future surfaces to these templates (layout, components, density), subject to license clearance before **vendoring** third-party assets wholesale.

**Status:** Design authority for previews. Implementation = Gena (and Abelard for deploy); **Grace** triages integration tasks. Does not replace `SPEC-ETHAN-HESPERIA-DJANGO-OUTPUT-VIEWS.md` (Django role + page builder contract).

**Refs:** [Black Dashboard Django](https://github.com/creativetimofficial/black-dashboard-django) (Creative Tim), [React Datta Able Django](https://github.com/app-generator/react-datta-able-django) (App Generator), Hesperia `output_views/`, brain `HESPERIA-TFP-YIELDED-PARAMETERS-TABLE.md`.

---

## 1. Template A — operator / internal dashboard (primary)

| Field | Choice |
|-------|--------|
| **Name** | **Black Dashboard Django** |
| **Repository** | [creativetimofficial/black-dashboard-django](https://github.com/creativetimofficial/black-dashboard-django) |
| **Stack** | Django, **Bootstrap 4**, dark admin shell, charts, dynamic tables, session auth (template includes Vite for assets in upstream) |
| **Use in Hesperia** | **Operator previews**, run summaries, calibration / TFP table pages, internal tooling that fits a **dashboard** metaphor. |
| **Visual language** | Dark chrome, card-based layout, data-dense tables — default **reference** for `output_views` styling when extending beyond the minimal bootstrap shipped in v0. |

**Adoption pattern (preferred):** Extract **layout shell** (sidebar + top bar + content area), **typography**, **card/table/chart** patterns into Hesperia-owned templates and static; **do not** copy entire upstream repo into Hesperia without a **license review** (upstream README cites both **MIT** and **Creative Tim** licensing text — **igareosh / legal confirms** before redistribution).

---

## 2. Template B — client-centric / SPA-style previews (secondary)

| Field | Choice |
|-------|--------|
| **Name** | **React Datta Able Django** (full-stack seed) |
| **Repository** | [app-generator/react-datta-able-django](https://github.com/app-generator/react-datta-able-django) |
| **Stack** | **React** UI (Datta Able / CodedThemes lineage) + **Django API** with **JWT** (DRF-style patterns in product doc) |
| **Use in Hesperia** | **Client-facing** or **demo** experiences that need a **modern SPA** shell, separate from server-rendered Django pages. **Not** the default for sealed product JSON (FastAPI remains machine API unless ADR says otherwise). |
| **Integration note** | Hesperia may keep **FastAPI** as analyze API and use Django only for **auth + BFF** to that API, or expose read-only JSON from Django views — architecture must stay **single engine truth** per Django output spec. |

**Adoption pattern:** Treat as **reference** for React layout, navigation, and auth flow; **Node build chain** is required for the React app. Prefer **new** `react-ui/` (or named sibling) under a clearly bounded folder, not mixed into `hesperia` Python package roots.

---

## 3. Decision matrix (which template when)

| Scenario | Template |
|----------|----------|
| Internal operator sees E2E artifacts, metrics gates, TFP profile cards | **A — Black Dashboard** (or components derived from it) |
| Printable / PDF-friendly report page from PageSpec | **A** first (server-rendered) |
| Branded external demo, interactive client portal, multi-page SPA | **B — React Datta** pattern |
| Minimal dependency, no Node in CI | **A** server-rendered only |

---

## 4. Non-goals (this spec)

| Item | Rule |
|------|------|
| Replacing **FastAPI** shipping JSON | Out of scope unless separate ADR. |
| **PRO** / paid Creative Tim or App Generator SKUs | Optional later; not required to satisfy this spec. |
| **Django admin** as primary UX | Admin remains secondary; previews use **pages** apps. |

---

## 5. Team execution

| Role | Action |
|------|--------|
| **Ethan** | Maintains this spec; approves deviations. |
| **Gena** | Maps PageSpec blocks to Template **A** components; scaffolds Template **B** only when a task explicitly targets SPA previews. |
| **Abelard** | Nginx paths, static build artifacts for Template **B**, separate deploy units if React + Django API split. |
| **Grace** | Triage rows: “Align `output_views` shell to Black Dashboard”, “Spike React preview BFF”, etc. |

---

## 6. Cross-references

- Django output foundation: [SPEC-ETHAN-HESPERIA-DJANGO-OUTPUT-VIEWS.md](SPEC-ETHAN-HESPERIA-DJANGO-OUTPUT-VIEWS.md)  
- **Session Inspector** (IDE-style flagship page): [SPEC-ETHAN-HESPERIA-SESSION-ITERATION-INSPECTOR-PAGE.md](SPEC-ETHAN-HESPERIA-SESSION-ITERATION-INSPECTOR-PAGE.md)  
- Hesperia runbook (when added): `hesperia/docs/output_views/README.md`

---

`SIGNED: Ethan (Chief Architect) | Hesperia output preview design templates | 2026-04-07 | governance spec`
