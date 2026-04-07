# Hesperia `output_views` — Django site builder (HTML)

**Purpose:** Human-facing previews and client-centric HTML. **FastAPI** shipping API remains the JSON contract.

**Safety / compliance:** [SAFETY-SECRETS-AND-PII.md](SAFETY-SECRETS-AND-PII.md) (T26–T27), [LICENSE-EXPORT-NOTE.md](LICENSE-EXPORT-NOTE.md) (T28), [FEATURE-FLAGS.md](FEATURE-FLAGS.md) (T58), [PROXY-ROLLBACK.md](PROXY-ROLLBACK.md) (T61). **Never commit** API keys; use `.env` at Hesperia root (gitignored).

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
- **Session Inspector (MVP):** `http://127.0.0.1:8010/inspector/session_inspector_min/` — fixture JSON under `output_views/tests/fixtures/`; query `?iteration=&sentence=`
- **Export JSON:** `http://127.0.0.1:8010/inspector/session_inspector_min/export.json?iteration=0` — `iteration_segment_openai_v1` + `messages` (attachment `segment.json`)
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
| `HESPERIA_OUTPUT_VIEWS_OPENAI_PROXY` | `1`/`true` to enable POST `/inspector/.../openai-proxy/` (default off) |
| `OPENAI_API_KEY` | Required when proxy enabled |
| `OPENAI_PROXY_MODEL` | Default `gpt-4o-mini` |
| `OPENAI_PROXY_RATE_PER_MINUTE` | Per-IP rolling limit (default 30) |

See [OPENAI_PROXY-RATE-LIMIT.md](OPENAI_PROXY-RATE-LIMIT.md).

Reads optional `../.env` from Hesperia root via `django-environ`.

## Tests

```bash
cd output_views && python3 manage.py test apps.pages
```

From Hesperia repo root (same tests):

```bash
make output-views-test
```

**Pytest marker `output_views`** (T51) is registered in repo `pytest.ini`; primary coverage is Django `manage.py test` above.

## Iteration segment (OpenAI export)

- **Glossary:** [FIELD_GLOSSARY.md](FIELD_GLOSSARY.md)
- **Code:** `output_views/segment/` — session bundle → per-iteration segment → `messages[]` (system + user).

## Session Inspector UI

- **ADR (panes):** [ADR-split-panes-v1.md](ADR-split-panes-v1.md)
- **RU stub:** [I18N_RU_STUB.md](I18N_RU_STUB.md)

## Governance

| Doc (brain repo `cursor`) | Role |
|---------------------------|------|
| `governance/SPEC-ETHAN-HESPERIA-DJANGO-OUTPUT-VIEWS.md` | Django output layer + page builder |
| `governance/SPEC-ETHAN-HESPERIA-OUTPUT-PREVIEW-DESIGN-TEMPLATES.md` | **Canonical preview UI references:** [Black Dashboard Django](https://github.com/creativetimofficial/black-dashboard-django) (operator dashboard), [React Datta Able Django](https://github.com/app-generator/react-datta-able-django) (client SPA + JWT API pattern) |
| `governance/SPEC-ETHAN-HESPERIA-SESSION-ITERATION-INSPECTOR-PAGE.md` | **Session Inspector** — one page = one session; IDE-style panes, iteration dropdown, sentence → parameters + audit |

## Production (Abelard)

Separate process from FastAPI; Gunicorn/uvicorn WSGI on `config.wsgi:application`; Nginx path prefix; `collectstatic` to `staticfiles/`.

`SIGNED: Abelard (DevOps) | Hesperia Django output_views bootstrap | 2026-04-07`
