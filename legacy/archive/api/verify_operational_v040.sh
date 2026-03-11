#!/usr/bin/env bash
# HESPERIA Action v0.4.0 — operational verification harness
# Usage: API_KEY=<secret> [BASE_URL=https://hesperia.prichindel.com] [BAD_HOST=...] ./verify_operational_v040.sh
# Exits non-zero if any check fails.

set -e
BASE_URL="${BASE_URL:-https://hesperia.prichindel.com}"
FAIL=0
HAS_JQ=false
command -v jq &>/dev/null && HAS_JQ=true

red () { printf '\033[0;31m%s\033[0m\n' "$1"; }
green () { printf '\033[0;32m%s\033[0m\n' "$1"; }

check () {
  local n="$1" desc="$2" ok="$3"
  if [[ "$ok" == "1" || "$ok" == "true" || "$ok" == "yes" ]]; then
    green "  $n. $desc — PASS"
  else
    red "  $n. $desc — FAIL"
    FAIL=1
  fi
}

# 1. GET /health → 200 and JSON "ok":true
r=$(curl -sS -w '\n%{http_code}' "$BASE_URL/health" 2>/dev/null) || true
code=$(echo "$r" | tail -n1)
body=$(echo "$r" | sed '$d')
ok1="0"
[[ "$code" == "200" ]] && { ($HAS_JQ && echo "$body" | jq -e '.ok == true' &>/dev/null) || [[ "$body" == *'"ok":true'* || "$body" == *'"ok": true'* ]]; } && ok1="1"
check "1" "GET /health returns 200 and JSON contains ok:true" "$ok1"

# 2. GET /openapi.json → 200 and bearerAuth
r=$(curl -sS -w '\n%{http_code}' "$BASE_URL/openapi.json" 2>/dev/null) || true
code=$(echo "$r" | tail -n1)
body=$(echo "$r" | sed '$d')
ok2="0"
[[ "$code" == "200" ]] && [[ "$body" == *'bearerAuth'* ]] && ok2="1"
check "2" "GET /openapi.json returns 200 and contains bearerAuth" "$ok2"

# 3. POST /hesperia/analyze no auth → 401 code=401
r=$(curl -sS -w '\n%{http_code}' -X POST "$BASE_URL/hesperia/analyze" -H "Content-Type: application/json" -d '{"text":"x"}' 2>/dev/null) || true
code=$(echo "$r" | tail -n1)
body=$(echo "$r" | sed '$d')
ok3="0"
[[ "$code" == "401" ]] && { ($HAS_JQ && echo "$body" | jq -e '.code == 401' &>/dev/null) || [[ "$body" == *'"code":401'* || "$body" == *'"code": 401'* ]]; } && ok3="1"
check "3" "POST /hesperia/analyze with no auth returns 401 JSON code=401" "$ok3"

# 4. POST /hesperia/analyze wrong auth → 401 code=401
r=$(curl -sS -w '\n%{http_code}' -X POST "$BASE_URL/hesperia/analyze" -H "Authorization: Bearer wrong-token" -H "Content-Type: application/json" -d '{"text":"x"}' 2>/dev/null) || true
code=$(echo "$r" | tail -n1)
body=$(echo "$r" | sed '$d')
ok4="0"
[[ "$code" == "401" ]] && { ($HAS_JQ && echo "$body" | jq -e '.code == 401' &>/dev/null) || [[ "$body" == *'"code":401'* || "$body" == *'"code": 401'* ]]; } && ok4="1"
check "4" "POST /hesperia/analyze with wrong auth returns 401 JSON code=401" "$ok4"

# 5. POST correct auth + text/plain → 415
if [[ -z "${API_KEY:-}" ]]; then
  red "  5. POST with correct auth + text/plain → 415 — SKIP (API_KEY not set)"
else
  r=$(curl -sS -w '\n%{http_code}' -X POST "$BASE_URL/hesperia/analyze" -H "Authorization: Bearer $API_KEY" -H "Content-Type: text/plain" -d 'x' 2>/dev/null) || true
  code=$(echo "$r" | tail -n1)
  body=$(echo "$r" | sed '$d')
  ok5="0"
  [[ "$code" == "415" ]] && { ($HAS_JQ && echo "$body" | jq -e '.code == 415' &>/dev/null) || [[ "$body" == *'"code":415'* || "$body" == *'"code": 415'* ]]; } && ok5="1"
  check "5" "POST /hesperia/analyze with correct auth + Content-Type text/plain returns 415 JSON" "$ok5"
fi

# 6. POST correct auth + JSON extra field → 422 stable message
if [[ -z "${API_KEY:-}" ]]; then
  red "  6. POST with extra field → 422 — SKIP (API_KEY not set)"
else
  r=$(curl -sS -w '\n%{http_code}' -X POST "$BASE_URL/hesperia/analyze" -H "Authorization: Bearer $API_KEY" -H "Content-Type: application/json" -d '{"text":"x","extra":1}' 2>/dev/null) || true
  code=$(echo "$r" | tail -n1)
  body=$(echo "$r" | sed '$d')
  ok6="0"
  if [[ "$code" == "422" ]]; then
    if ($HAS_JQ && echo "$body" | jq -e '.code == 422' &>/dev/null) || [[ "$body" == *'"code":422'* || "$body" == *'"code": 422'* ]]; then
      [[ "$body" == *'Invalid request body'* || "$body" == *'extra fields not permitted'* ]] && ok6="1"
    fi
  fi
  check "6" "POST /hesperia/analyze with correct auth + JSON extra field returns 422 with stable message" "$ok6"
fi

# 7. POST correct auth + valid JSON → 200 or 400 and JSON
if [[ -z "${API_KEY:-}" ]]; then
  red "  7. POST with valid JSON + auth → 200 or 400 — SKIP (API_KEY not set)"
else
  r=$(curl -sS -w '\n%{http_code}' -X POST "$BASE_URL/hesperia/analyze" -H "Authorization: Bearer $API_KEY" -H "Content-Type: application/json" -d '{"text":"some sentence"}' 2>/dev/null) || true
  code=$(echo "$r" | tail -n1)
  body=$(echo "$r" | sed '$d')
  ok7="0"
  if [[ "$code" == "200" || "$code" == "400" ]]; then
    ($HAS_JQ && echo "$body" | jq -e . &>/dev/null) && ok7="1" || { [[ "$body" == *'"'* && "$body" != *'<'* ]] && ok7="1"; }
  fi
  check "7" "POST /hesperia/analyze with correct auth + valid JSON returns 200 or 400 and JSON" "$ok7"
fi

# 8. OPTIONS /hesperia/analyze → 204 and Allow
r=$(curl -sS -w '\n%{http_code}' -D - -o /dev/null -X OPTIONS "$BASE_URL/hesperia/analyze" 2>/dev/null) || true
code=$(echo "$r" | head -1 | grep -oE '[0-9]{3}')
allow=$(echo "$r" | grep -i '^Allow:' | head -1)
ok8="0"
[[ "$code" == "204" ]] && [[ -n "$allow" ]] && ok8="1"
check "8" "OPTIONS /hesperia/analyze returns 204 and has Allow header" "$ok8"

# 9. GET /docs → 404
code=$(curl -sS -o /dev/null -w '%{http_code}' "$BASE_URL/docs" 2>/dev/null) || true
check "9" "GET /docs returns 404" "$( [[ "$code" == "404" ]] && echo 1 || echo 0 )"

# 10. GET / → 404
code=$(curl -sS -o /dev/null -w '%{http_code}' "$BASE_URL/" 2>/dev/null) || true
check "10" "GET / returns 404" "$( [[ "$code" == "404" ]] && echo 1 || echo 0 )"

# 11. X-Content-Type-Options: nosniff on /health
h=$(curl -sS -D - -o /dev/null "$BASE_URL/health" 2>/dev/null | grep -i '^X-Content-Type-Options:' | head -1)
ok11="0"
[[ "$h" == *'nosniff'* ]] && ok11="1"
check "11" "Header X-Content-Type-Options: nosniff present on /health" "$ok11"

# 12. Host-guard best-effort
code=$(curl -sS -o /dev/null -w '%{http_code}' --connect-timeout 5 -H "Host: not-hesperia.example.com" "$BASE_URL/health" 2>/dev/null) || code="000"
ok12="0"
[[ "$code" == "000" || "$code" == "444" || "$code" != "200" ]] && ok12="1"
check "12" "Host-guard wrong Host yields non-200 or close (best-effort)" "$ok12"

echo ""
if [[ "$FAIL" -eq 0 ]]; then
  green "All checks PASSED."
  exit 0
else
  red "One or more checks FAILED."
  exit 1
fi
