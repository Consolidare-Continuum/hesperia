# Deploy — Nginx, TLS, auth, CSP (T33–T35, T56)

**Owner:** Abelard (prichindel) applies on the edge; this file is the **contract** for `output_views` behind a reverse proxy.

## T33 — Nginx location

Django `output_views` listens on **one** upstream (e.g. `127.0.0.1:8010`) via Gunicorn/uvicorn WSGI. Two common mounts:

### A) Path prefix `/hesperia/` → app root

Use when public URL is `https://<host>/hesperia/...` and Django `FORCE_SCRIPT_NAME` is set to `/hesperia` (separate task). **Without** `FORCE_SCRIPT_NAME`, prefer **B**.

### B) Subdomain or dedicated path copy (recommended for MVP)

Proxy **only** the paths this Django app serves (Inspector lives at `/inspector/`):

```nginx
# Upstream (example)
upstream hesperia_output_views {
    server 127.0.0.1:8010;
}

server {
    listen 443 ssl http2;
    server_name hesperia.example.com;

    # T34 — TLS: same certificate policy as other internal tools on this host (Let’s Encrypt / org CA).

    # T35 — optional Basic Auth when exposed beyond localhost
    # auth_basic "Hesperia output_views";
    # auth_basic_user_file /etc/nginx/.htpasswd_hesperia_output_views;

    location /inspector/ {
        proxy_pass http://hesperia_output_views;
        proxy_http_version 1.1;
        proxy_set_header Host $host;
        proxy_set_header X-Real-IP $remote_addr;
        proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
        proxy_set_header X-Forwarded-Proto $scheme;
        # T56 — CSP (tune if you add nonces; inline scripts exist in Session Inspector MVP)
        add_header Content-Security-Policy "default-src 'self'; script-src 'self' 'unsafe-inline'; style-src 'self' 'unsafe-inline'; img-src 'self' data:; connect-src 'self'; frame-ancestors 'none'; base-uri 'self'; form-action 'self'" always;
    }

    location /health/ {
        proxy_pass http://hesperia_output_views;
        proxy_set_header Host $host;
        proxy_set_header X-Forwarded-Proto $scheme;
    }

    location = /robots.txt {
        proxy_pass http://hesperia_output_views;
        proxy_set_header Host $host;
    }
}
```

If the **entire** site is this Django app, use `location / { proxy_pass ... }` and keep CSP on `location /inspector/` only if you need stricter rules there.

## T34 — TLS

Terminate TLS on Nginx (or Cloudflare) with the **same host policy** as other prichindel internal tools: valid cert, HSTS only if operator policy requires it.

## T35 — Auth beyond localhost

- **Nginx Basic Auth** (snippet above) is the fastest gate for LAN/VPN operators.
- **SSO / OIDC** belongs in front of Nginx or on a dedicated auth proxy; document the chosen integration in `cluster/` when wired.

## T56 — CSP

- Inspector uses **inline scripts** for PII gate / clipboard → `script-src` includes `'unsafe-inline'` until nonces are implemented.
- Tighten `connect-src` if OpenAI proxy is enabled and calls leave the origin.

`SIGNED: Abelard (DevOps) | Hesperia output_views deploy notes | 2026-04-07 | T33–T35, T56`
