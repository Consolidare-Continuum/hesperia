# Hesperia API deploy (prichindel)

**Repo**: Atomic-Commits-Team/hesperia @ `/data/workspaces/atomic-commit-hesperia`.
**API**: POST `/hesperia/analyze` — request/response per OpenAI GPT contract (HesperiaAnalyzeRequest / HesperiaAnalyzeResponse).

## Wiring

- **Chroma**: `CHROMA_SERVER_URL=http://127.0.0.1:8002` (prichindel production Chroma). API runs context_rag with `--chroma`; cursor repo `agent_mcp_knowledge.store` used when context_rag is invoked (PYTHONPATH includes `/data/workspaces/cursor`).
- **MCP**: Cursor IDE uses `user-chroma-knowledge` MCP for Chroma queries; GPT calls this API at `hesperia.prichindel.com/hesperia/analyze`. No separate Hesperia MCP tool; API is the external contract.
- **Backend**: systemd `hesperia-api.service` → uvicorn on `127.0.0.1:9005`. Nginx `hesperia.prichindel.com` → `http://127.0.0.1:9005`.

**Log**: One service-wide log file, Apache-style with timestamp. Path: `/data/workspaces/atomic-commit-hesperia/logs/hesperia-api.log`. Each request logs: timestamp, "POST /hesperia/analyze", status (200/500), asked (request text truncated), returned (response JSON) or error (on 5xx).

## Install (Abelard)

```bash
# Venv (once)
cd /data/workspaces/atomic-commit-hesperia && python3 -m venv venv && ./venv/bin/pip install -r requirements-api.txt

# Systemd
sudo cp /data/workspaces/atomic-commit-hesperia/deploy/hesperia-api.service /etc/systemd/system/
sudo systemctl daemon-reload && sudo systemctl enable --now hesperia-api

# Nginx
sudo cp /path/to/cursor/prichindel/nginx/hesperia.prichindel.com.conf /etc/nginx/conf.d/
sudo nginx -t && sudo systemctl reload nginx
```

## Cloudflare tunnel

Add public hostname **hesperia.prichindel.com** → `https://127.0.0.1:443` with **noTLSVerify**.
Ingress JSON (see cursor repo `docs/CLOUDFLARE.md`): include
`{"hostname": "hesperia.prichindel.com", "service": "https://127.0.0.1:443", "originRequest": {"noTLSVerify": true}}`.
Ensure DNS CNAME `hesperia.prichindel.com` → tunnel FQDN.

## Direct LAN (GPT)

If GPT is configured to call the API by IP: **https://192.168.100.21:9005** — then nginx is bypassed; the API listens on 127.0.0.1:9005 only, so either (1) expose 9005 on 0.0.0.0 and use TLS, or (2) have GPT use **hesperia.prichindel.com** (tunnel → nginx → 9005). Recommended: expose via hesperia.prichindel.com.

## Verify

- Local: `curl -k -H "Host: hesperia.prichindel.com" https://127.0.0.1/health` → `{"status":"ok","service":"hesperia-analyze"}`.
- Public: ensure DNS `hesperia.prichindel.com` points to the **primary** tunnel (same as acc/superset); tunnel ingress must include hesperia → https://127.0.0.1:443 (noTLSVerify). If you see another app (e.g. ownCloud), fix DNS or tunnel route.

## Health check returns ownCloud “untrusted domain” (OpenAI / GPT)

Infra is correct: DNS `hesperia.prichindel.com` → `7d7e481d-a53e-47ae-a78b-21901163508e.cfargotunnel.com`; tunnel ingress hesperia → `https://127.0.0.1:443`. If the health check still gets ownCloud HTML:

1. **Action URL** — In the GPT/OpenAI App, set the API base URL to **exactly** `https://hesperia.prichindel.com` (no trailing slash, no `cloud.`, no typo). Health path: `GET https://hesperia.prichindel.com/health`.
2. **Caching / client** — Try from another network or device; clear or retry the action.
3. **Correct response** — A successful health check returns JSON: `{"status":"ok","service":"hesperia-analyze"}`. Any HTML (including “untrusted domain”) is from a different service.
