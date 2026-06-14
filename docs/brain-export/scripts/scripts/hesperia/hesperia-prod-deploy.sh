#!/usr/bin/env bash
# Deploy Hesperia product surfaces on prichindel from /data/hesperia/hesperia (no git push).
# Brain repo: run from /data/altitudine/prichindel.com — uses ssh prichindel.
set -euo pipefail
REPO="/data/hesperia/hesperia"
echo "=== Hesperia prod deploy (prichindel) ==="
ssh prichindel bash -s <<REMOTE
set -euo pipefail
cd ${REPO}
if ! git diff --quiet || ! git diff --cached --quiet; then
  echo "FAIL: ${REPO} has uncommitted changes — commit or stash first." >&2
  git status -sb
  exit 1
fi
echo "Tree @ \$(git log -1 --oneline)"
cd output_views
export DJANGO_SETTINGS_MODULE=config.settings
export DJANGO_DEBUG=False
python3 manage.py collectstatic --noinput
cd ..
curl -sf -o /dev/null -w "static css: %{http_code}\n" http://127.0.0.1:8010/static/output_views/css/site.css || {
  echo "FAIL: site.css not served — run collectstatic" >&2
  exit 1
}
sudo cp tools/scripts/hesperia.prichindel.com.conf /etc/nginx/conf.d/hesperia.prichindel.com.conf
sudo cp tools/scripts/hesperia-output-views.service /etc/systemd/system/hesperia-output-views.service
sudo systemctl daemon-reload
sudo nginx -t
sudo systemctl reload nginx
sudo rsync -a --delete --chown=www-data:www-data output_views/hex_matrix_viewer/dist/ /var/www/hesperia-sites/hex-matrix/
sudo systemctl restart hesperia-output-views
sleep 2
systemctl is-active hesperia-output-views hesperia-api nginx
curl -sf -o /dev/null -w "inspector: %{http_code}\n" http://127.0.0.1:8010/inspector/1-11-09-2023/
curl -sf -o /dev/null -w "api: %{http_code}\n" http://127.0.0.1:9005/health
echo "OK"
REMOTE
bash "$(dirname "$0")/verify-hesperia-prod-https.sh"
