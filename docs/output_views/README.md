# Hesperia `output_views` — Django site builder (HTML)

**Purpose:** Human-facing previews and client-centric HTML. **FastAPI** shipping API remains the JSON contract.

**Django LTS:** Pinned in `requirements/output_views.txt` ([supported versions](https://www.djangoproject.com/download/)).

## Install

From Hesperia repo root:

```bash
python3 -m pip install -r requirements/output_views.txt
```

## Run (development)

```bash
cd output_views
python3 manage.py migrate
python3 manage.py runserver 0.0.0.0:8010
```

- Operator home: `http://127.0.0.1:8010/`
- Health JSON: `http://127.0.0.1:8010/health/`
- Client preview shell: `http://127.0.0.1:8010/preview/client/`
- E2E artifact listing (read-only): `http://127.0.0.1:8010/preview/artifacts/`

## Environment

| Variable | Role |
|----------|------|
| `DJANGO_SECRET_KEY` | Required in production |
| `DJANGO_DEBUG` | `True` / `False` (default `True` for local) |
| `DJANGO_ALLOWED_HOSTS` | Comma-separated (default `127.0.0.1,localhost,[::1]`) |
| `HESPERIA_FASTAPI_ANALYZE_URL` | Optional HTTP bridge to FastAPI (Phase B) |

Reads optional `../.env` from Hesperia root via `django-environ`.

## Tests

```bash
cd output_views && python3 manage.py test apps.pages
```

## Iteration segment (OpenAI export)

- **Glossary:** [FIELD_GLOSSARY.md](FIELD_GLOSSARY.md)
- **Code:** `output_views/segment/` — session bundle → per-iteration segment → `messages[]` (system + user).

## Governance

| Doc (brain repo `cursor`) | Role |
|---------------------------|------|
| `governance/SPEC-ETHAN-HESPERIA-DJANGO-OUTPUT-VIEWS.md` | Django output layer + page builder |
| `governance/SPEC-ETHAN-HESPERIA-OUTPUT-PREVIEW-DESIGN-TEMPLATES.md` | **Canonical preview UI references:** [Black Dashboard Django](https://github.com/creativetimofficial/black-dashboard-django) (operator dashboard), [React Datta Able Django](https://github.com/app-generator/react-datta-able-django) (client SPA + JWT API pattern) |
| `governance/SPEC-ETHAN-HESPERIA-SESSION-ITERATION-INSPECTOR-PAGE.md` | **Session Inspector** — one page = one session; IDE-style panes, iteration dropdown, sentence → parameters + audit |

## Production (Abelard)

Separate process from FastAPI; Gunicorn/uvicorn WSGI on `config.wsgi:application`; Nginx path prefix; `collectstatic` to `staticfiles/`.

`SIGNED: Abelard (DevOps) | Hesperia Django output_views bootstrap | 2026-04-07`
