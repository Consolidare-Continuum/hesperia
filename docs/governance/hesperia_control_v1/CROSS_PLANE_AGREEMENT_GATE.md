# Cross-plane agreement gate (HC-09)

## Purpose

Release / audit metric only until each plane exposes **comparable** fields (schema subset + version).

## Minimum comparable tuple (per segment or session unit)

- `plane_id` (enum: structural | multiscale | product | topology)  
- `top_area_id` + `top_area_score`  
- `runner_version` + `calibration_id`  

## Outcomes

- `pass` — top areas match or within adjacency matrix (config)  
- `warn` — mismatch under tolerance  
- `fail` — contradiction or missing plane  

Link: `tools/tfp_calibration_audit.py` / `calibration_release_gate` patterns in repo.

`SIGNED: Olivia (task HC-09) | gate contract sketch | 2026-03-27 | Hesperia repo`
