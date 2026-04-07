# OpenAI proxy rollback — one screen (T61)

If the server-side OpenAI proxy causes issues (cost, errors, policy change):

1. **Disable the flag:** set `HESPERIA_OUTPUT_VIEWS_OPENAI_PROXY=0` (or unset) in the process environment for the Django/Gunicorn service.
2. **Restart** the WSGI application (e.g. `systemctl restart …` or redeploy container) so workers pick up env.
3. **Optional:** remove or blank `OPENAI_API_KEY` in that environment so accidental enable fails closed.
4. **Verify:** `POST /inspector/<id>/openai-proxy/` returns **404**; Session Inspector no longer shows the proxy form.
5. **Client-side exports** (copy / `export.json` download) remain available; they do not require the proxy.

No database migration is involved.

`SIGNED: Daniel (safety baseline) | 2026-04-07 | T61`
