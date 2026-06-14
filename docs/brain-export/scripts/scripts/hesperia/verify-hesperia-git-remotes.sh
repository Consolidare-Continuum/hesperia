#!/usr/bin/env bash
# Verify Hesperia clones use only ETHAN-approved push URLs; brain repo has no Hesperia remotes.
# Ref: governance/ETHAN-POLICY-HESPERIA-PUSH-AND-REMOTES.md (§2a: hesperia_mrt archived — not allowed as push remote).
set -euo pipefail

# SSH or HTTPS, optional .git suffix
ALLOW='^(git@github\.com:|https://github\.com/)(igareosh/hesperia(\.git)?|igareosh/hesperia-dev-backup(\.git)?|Atomic-Commits-Team/hesperia(\.git)?)$'

bad=0

check_hesperia_clone() {
  local dir="$1"
  if ! { [ -d "$dir/.git" ] || [ -f "$dir/.git" ]; }; then
    return 0
  fi
  local url
  while read -r url; do
    [ -n "$url" ] || continue
    if ! echo "$url" | grep -qE "$ALLOW"; then
      echo "VERIFY FAIL: disallowed push URL in Hesperia tree $dir -> $url" >&2
      bad=1
    fi
  done < <(git -C "$dir" remote -v 2>/dev/null | awk '/\(push\)/ {print $2}' || true)
}

check_cursor_brain() {
  local dir="$1"
  if ! { [ -d "$dir/.git" ] || [ -f "$dir/.git" ]; }; then
    return 0
  fi
  # Brain repo must not carry Hesperia product remotes (avoid accidental push to wrong place).
  if git -C "$dir" remote -v 2>/dev/null | awk '/\(push\)/ {print $2}' | grep -qE 'github\.com[:/][^ ]*hesperia'; then
    echo "VERIFY FAIL: cursor brain repo has a GitHub URL containing 'hesperia' — remove that remote" >&2
    bad=1
  fi
}

# Default Hesperia working trees (add more paths as args)
DEFAULTS=(
  "/data/workspaces/atomic-commit-hesperia"
  "/data/hesperia/hesperia"
)

for d in "${DEFAULTS[@]}" "$@"; do
  [ -n "$d" ] || continue
  check_hesperia_clone "$d"
done

for brain in "/data/altitudine/prichindel.com" "/data/workspaces/cursor"; do
  [ -d "$brain/.git" ] || [ -f "$brain/.git" ] || continue
  check_cursor_brain "$brain"
done

if [ "$bad" -ne 0 ]; then
  echo "verify-hesperia-git-remotes: FAILED" >&2
  exit 1
fi
echo "verify-hesperia-git-remotes: OK (Hesperia paths checked + cursor brain has no hesperia remotes)"
