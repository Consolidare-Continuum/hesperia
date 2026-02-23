#!/usr/bin/env bash
# Phase 7 — CI for lexical stack. Run from repo root or hesperia_lex.
# 1) Validate JSON schema (Dict A/B)
# 2) validate_lexical.py (side_id in set, no family/area in A, no duplicate alias)
# 3) Optional: run books-off A/B invariant test (full_run_simulation or hesperia_v03_core_math)
set -e
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
LEX_ROOT="$(cd "$SCRIPT_DIR/.." && pwd)"
HESPERIA_ROOT="$(cd "$LEX_ROOT/.." && pwd)"
cd "$HESPERIA_ROOT"

SIDE_ID_FMT="int"
if [ -f "$HESPERIA_ROOT/guard_config_v1.json" ]; then
  SIDE_ID_FMT=$(python3 -c "import json; print(json.load(open('$HESPERIA_ROOT/guard_config_v1.json')).get('side_id_format','int'))")
fi
echo "CI: validate_lexical.py (side_id_format=$SIDE_ID_FMT)"
python3 "$LEX_ROOT/scripts/validate_lexical.py" --curated "$LEX_ROOT/curated" --side-id-format "$SIDE_ID_FMT" || exit 1

echo "CI: sync curated -> assets (required for loader)"
bash "$LEX_ROOT/scripts/sync_curated_to_assets.sh"

echo "CI: lexical_loader load_and_validate (Spec 20 + side_id_format)"
python3 -c "
from pathlib import Path
import json
cfg_path = Path('guard_config_v1.json')
cfg = json.loads(cfg_path.read_text()) if cfg_path.exists() else {}
side_id_format = cfg.get('side_id_format', 'int')
from sphere_rag.lexical_loader import load_and_validate
a, b, errs = load_and_validate(assets_dir=Path('assets'), reject_on_violation=True, side_id_format=side_id_format)
assert not errs, errs
print('Loader OK: Dict A entries', len(a), ', Dict B entries', len(b))
"

echo "CI: acceptance thresholds (full_run_simulation stub)"
python3 -c "
import json, subprocess, sys
from pathlib import Path
r = subprocess.run([sys.executable, 'sphere_rag/full_run_simulation.py', '--n-sides', '72'], capture_output=True, text=True, cwd=Path('.').resolve())
if r.returncode != 0:
    print(r.stderr or r.stdout)
    sys.exit(1)
out = json.loads(r.stdout)
acc = out.get('acceptance', {})
assert acc.get('shadow_hops_ok', False), 'acceptance: shadow_hops must be <= max_shadow_hops'
assert acc.get('conservation_ok', False), 'acceptance: conservation_failures_during_traversal must be 0'
print('Acceptance: shadow_hops_ok, conservation_ok')
"

echo "CI: deterministic snapshot (same inputs -> identical output JSON)"
python3 -c "
import subprocess, sys
from pathlib import Path
cwd = Path('.').resolve()
r1 = subprocess.run([sys.executable, 'sphere_rag/full_run_simulation.py', '--n-sides', '72'], capture_output=True, text=True, cwd=cwd)
r2 = subprocess.run([sys.executable, 'sphere_rag/full_run_simulation.py', '--n-sides', '72'], capture_output=True, text=True, cwd=cwd)
if r1.returncode != 0 or r2.returncode != 0:
    sys.exit(1)
if r1.stdout != r2.stdout:
    sys.exit(1)
print('Deterministic snapshot OK')
"

echo "CI lexical: pass"
