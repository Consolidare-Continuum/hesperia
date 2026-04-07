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
- **Goldset stem fixture (pipeline-shaped):** `http://127.0.0.1:8010/inspector/1-11-09-2023/` — JSON built from `tests/fixtures/tfp_calibration_bundle_ci` via `scripts/generate_inspector_fixture.py` (synthetic CI bundle; same `session_id` as calibration goldset `1-11-09-2023`). **session_id** = fixture filename stem (no `.json`); must match `^[a-zA-Z0-9_-]{1,120}$`.
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

**Golden segment (T29 / T53):** `tests/fixtures/golden/iteration_segment_openai_v1_iter0.json` — verify with `python3 scripts/validate_golden_segment.py verify` (see [PRE-COMMIT-SEGMENT.md](PRE-COMMIT-SEGMENT.md)).

**Regenerate `1-11-09-2023` Inspector fixture (OUT-VIEW-FULL-02):**

```bash
cd output_views
python3 scripts/generate_inspector_fixture.py --from-ci-bundle
# writes tests/fixtures/1-11-09-2023.json
```

From a full `run_tfp_file_pipeline` output directory (real engine run):

```bash
python3 scripts/generate_inspector_fixture.py --bundle-dir /path/to/pipeline_out [--session-id <id>]
```

To run the pipeline then generate in one step (slow):

```bash
python3 scripts/generate_inspector_fixture.py --run-pipeline \
  --input ../hesperia/modules/tfp/data/tfp_v1/corpus/sessions/11-09-2023.md \
  --out-bundle /tmp/tfp_11_09 --session-id 11-09-2023
```

(`session_id` for a single `.md` input defaults to the file **stem** — e.g. `11-09-2023.md` → `11-09-2023`; use `--session-id` to align with other naming.)

From Hesperia repo root:

```bash
make output-views-inspector-fixture
```

**Quality notes:** [LIGHTHOUSE-NOTES.md](LIGHTHOUSE-NOTES.md) (T32), [BUNDLE-SIZE-LIMITS.md](BUNDLE-SIZE-LIMITS.md) (T64).

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

**Edge:** [DEPLOY-NGINX-TLS-AUTH-CSP.md](DEPLOY-NGINX-TLS-AUTH-CSP.md) (T33–T35, T56). **`/robots.txt`** disallows `/inspector/` (T57).

`SIGNED: Abelard (DevOps) | Hesperia Django output_views bootstrap | 2026-04-07`
