# SCRIPT-RUNBOOK — Hesperia prod API enablement

**ID:** `hesperia-prod-api-enable`  
**Owner:** Abelard  
**Task:** HINS-16 / HINS-01  
**Host:** prichindel

---

## Preconditions

- Prod tree: `/data/hesperia/hesperia` @ `Atomic-Commits-Team/hesperia`
- Env file: `/etc/hesperia/hesperia-api.env` with `HESPERIA_API_KEY=<secret>`
- Brain unit: `cluster/hesperia-api.service` (shipping `runtime.shipping.api_main:app` on :9005)

---

## Enable (first time or after disable)

```bash
# On prichindel
cd /data/hesperia/hesperia
test -x .venv/bin/python || python3 -m venv .venv && .venv/bin/pip install -r requirements.txt uvicorn fastapi django django-environ

sudo cp /data/workspaces/cursor/cluster/hesperia-api.service /etc/systemd/system/hesperia-api.service
sudo cp /data/workspaces/cursor/cluster/prichindel/systemd/hesperia-output-views-prichindel.service /etc/systemd/system/hesperia-output-views.service
sudo systemctl daemon-reload
sudo systemctl enable --now hesperia-api hesperia-output-views
```

## Django static (inspector)

```bash
cd /data/hesperia/hesperia/output_views
../.venv/bin/python manage.py collectstatic --noinput
sudo systemctl restart hesperia-output-views
```

## Verify

```bash
curl -s http://127.0.0.1:9005/health
curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:8010/inspector/1-11-09-2023/
bash /data/workspaces/cursor/scripts/verify-hesperia-prod-https.sh   # from brain via ssh
bash /data/workspaces/cursor/scripts/verify-hesperia-prod-code-only.sh /data/hesperia/hesperia
```

## Expected

| Check | OK |
|-------|-----|
| `systemctl is-active hesperia-api` | `active` |
| `:9005/health` | `{"status":"ok"}` |
| `:8010/inspector/...` | `200` |
| Public `/health` via nginx | `200` (API path exempt Authentik) |

## Rollback

```bash
sudo systemctl disable --now hesperia-api
```

---

SIGNED: DevOps (Marcus runbook / Abelard ops) | prod API enablement | 2026-06-14 | HINS-16
