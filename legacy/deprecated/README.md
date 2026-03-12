<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# Deprecated (v0.5)

Scripts and tools not used in the full wired e2e run. Kept for reference or one-off use.

- **tools/calibration/** — `calibration_metrics_v06.py`, `run_calibration_v06.py`
- **tools/diagnostics/** — `verify_v06_operational.py`
- **lexicon_validation/** — `validate_b1_dict_b_v0414.py`, `validate_b0_dict_b_v0414.py`, `validate_families_yaml_v0412.py`, `validate_families_yaml_v0413.py`, `validate_surface_map_v040.py`
- **build/** — `build_v040.py`

Active stack is v0.5; entrypoints: `python3 -m runtime.pipeline.run_e2e_all`, `python3 -m runtime.pipeline.run_l1_through_l9`, etc.
