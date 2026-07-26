#!/usr/bin/env bash
# Verify Hesperia prod HTTPS surfaces (run from brain repo; uses ssh prichindel).
set -euo pipefail
HOST="${HESPERIA_HOST:-hesperia.prichindel.com}"
echo "=== Hesperia prod verify: $HOST ==="
ssh prichindel bash -s <<'REMOTE'
set -euo pipefail
echo "-- services --"
systemctl is-active hesperia-output-views hesperia-api nginx
echo "-- local backends --"
curl -sf -o /dev/null -w "inspector 1-11-09-2023: %{http_code}\n" http://127.0.0.1:8010/inspector/1-11-09-2023/
curl -sf -o /dev/null -w "static site.css: %{http_code}\n" http://127.0.0.1:8010/static/output_views/css/site.css
curl -sf -o /dev/null -w "api health: %{http_code}\n" http://127.0.0.1:9005/health
test -f /var/www/hesperia-sites/hex-matrix/index.html && echo "hex-matrix index: OK"
cd /data/hesperia/hesperia && echo "prod tree: $(pwd) @ $(git log -1 --oneline)"
REMOTE
echo "-- public HTTPS (expect 302 → Authentik when unauthenticated) --"
for path in / /hex-matrix/ /inspector/1-11-09-2023/; do
  code=$(curl -sI -o /dev/null -w "%{http_code}" "https://${HOST}${path}")
  loc=$(curl -sI "https://${HOST}${path}" | awk -F': ' 'tolower($1)=="location"{print $2}' | tr -d '\r')
  echo "${path} → HTTP ${code} ${loc:+→ $loc}"
done
echo "OK: prod backends up; HTTPS routes respond (login redirect expected without session)."
