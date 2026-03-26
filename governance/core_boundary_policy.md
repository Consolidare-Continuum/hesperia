# Core Boundary Policy

Purpose: freeze the Hesperia kernel boundary so core physics remains deterministic and modules remain replaceable.

## Non-negotiable rule

- Core = physics/kernel/runtime contracts.
- Modules = interpretation/domain injection adapters.
- Core must not import module internals.

## Import boundary

- Allowed direction: `hesperia.modules.* -> hesperia.engine.*` and `core.*`.
- Forbidden direction: `core.*` or `hesperia.engine.*` importing `hesperia.modules.*` internals directly, except loader/registry indirection in engine kernel.

## Enforcement

- CI gate: `python3 tools/check_core_module_boundary.py`
- Any direct import from `core/` to `hesperia.modules` internals is forbidden and fails CI.

## Acceptance for T1

- Gate fails on boundary violation.
- Current tree passes with zero violations.
