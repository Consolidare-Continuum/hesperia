# VERSION.yaml bump plan — V7 campaign (HSR-V7-A-08)

**Sealed base:** `0.6.3` (current `system_version`)  
**Brain owner:** Gena · **Architect:** Ethan

---

## Version ladder

| Version | Stage | Meaning |
|---------|-------|---------|
| **0.6.3** | `irc_teacher_application_run` | **Current sealed** — physics + assets frozen; prod gate |
| **0.6.5** | `v7_router_governed` | Router envelope, post-LLM audit, `/product/interpret`, fpf-thinking-map calibration — **no sealed physics change** |
| **0.7.0** | `modular_branches` | Class A drain complete; TFP/MRT/COBALT modules registered; Gate C tag |

---

## Bump rules

1. **Patch (0.6.x):** router/governance/API-only — no `sealed_multiscale_stack` or asset hash change.
2. **Minor 0.6.5:** requires Gate D exit + Ava gold matrix + Ethan A-19.
3. **0.7.0:** requires Gate B drain resolution (B-21) + Gate C exit + COBALT gates G1–G4 if COBALT prod flag considered.

---

## Fields to update at 0.6.5

- `system_version`, `components.*` aligned to `0.6.5`
- `release_stage: v7_router_governed`
- `build.git_commit` from promote SHA
- `runtime/shipping/version_info.py` drift fix (currently shows `0.6.0`)

---

## Promote path

Dev: `igareosh/hesperia` branch `hsr-v7-router-implementation` → prod: `Atomic-Commits-Team/hesperia` after Abelard A-12 clean + tag.
