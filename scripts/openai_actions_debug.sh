#!/usr/bin/env bash
set -euo pipefail

HOST="${1:-https://hesperia.prichindel.com}"
ANALYZE_ENDPOINT="$HOST/hesperia/analyze"
HEALTH_ENDPOINT="$HOST/health"

HEALTH_HEADERS="/tmp/hesperia_health.headers"
HEALTH_BODY="/tmp/hesperia_health.json"
ANALYZE_HEADERS="/tmp/hesperia_analyze.headers"
ANALYZE_BODY="/tmp/hesperia_analyze.json"

echo "1) Checking /health"
curl -sS -D "$HEALTH_HEADERS" "$HEALTH_ENDPOINT" -o "$HEALTH_BODY"

echo -e "\nHeaders for /health:"
sed -n '1,25p' "$HEALTH_HEADERS"
echo -e "\nBody:"
cat "$HEALTH_BODY"

echo -e "\n2) Checking CORS for /health (preflight OPTIONS)"
curl -sS -D - -o /dev/null -X OPTIONS "$HEALTH_ENDPOINT" \
  -H "Origin: null" \
  -H "Access-Control-Request-Method: GET"

echo -e "\n3) Testing POST /hesperia/analyze with valid JSON"
curl -sS -D "$ANALYZE_HEADERS" "$ANALYZE_ENDPOINT" \
  -H "Content-Type: application/json" \
  -H "Origin: null" \
  -d '{"text":"This is a test."}' -o "$ANALYZE_BODY"

echo -e "\nHeaders for /hesperia/analyze:"
sed -n '1,25p' "$ANALYZE_HEADERS"
echo -e "\nBody:"
cat "$ANALYZE_BODY"

echo -e "\n4) Checking CORS for /hesperia/analyze (preflight OPTIONS)"
curl -sS -D - -o /dev/null -X OPTIONS "$ANALYZE_ENDPOINT" \
  -H "Origin: null" \
  -H "Access-Control-Request-Method: POST" \
  -H "Access-Control-Request-Headers: content-type"

echo -e "\nDone."
