# INTERNAL DEBUG ISOLATION POLICY v1

**Status:** Active  
**Purpose:** Keep development coherent without contaminating runtime. No shared code path where public mode can accidentally emit internal debug state.

---

## 1. Hard Rules

1. **Debug writers disabled in public mode.** Any code that writes full traces, full math intermediates, full layer dumps, or bridge diagnostics must check runtime mode. In `public_runtime` mode such writers must not execute.
2. **Internal docs excluded from public package.** Documents under `docs/internal/` (MATH_LAYER_REGISTRY, PIPELINE_LAYER_REGISTRY, etc.) are not shipped in the public runtime package. They remain in the source tree for internal development only.
3. **Internal trace objects never serialized publicly.** Trace structures that hold layer-by-layer state, propagation path, adjacency path, or formula ids must not be passed to any serializer that can emit to a public artifact (stdout, public log, report, API response). Projection/sanitization produces a separate public trace; the internal trace never leaves the sealed boundary.
4. **Tests verify mode separation.** Tests must confirm that when mode is public_runtime, no internal payload is written and no internal trace is serialized to a public channel.

---

## 2. Modes (summary)

- **internal_debug:** Full traces, full math, full layers. All debug writers enabled. Internal docs available.
- **internal_review:** Reduced internal visibility. No full dumps to external paths.
- **public_runtime:** Projected only. Debug writers disabled. Internal docs not present in deployed package.

---

## 3. Implementation Notes

- Use a single mode flag (e.g. `HESPERIA_RUNTIME_MODE`) or equivalent. Default for entry points that serve API or operator use: `public_runtime`.
- Internal-only code paths (e.g. test harnesses, internal tooling) may set mode to `internal_debug` or `internal_review` and then call layer/bridge code directly; such paths must not be reachable from public API or public CLI without explicit override.
- Packaging: when building the sealed runtime release, exclude `docs/internal/`, internal-only tools, and any module that exists solely for debug dumps.

---

## 4. Acceptance Criterion

There is no shared code path where public mode can accidentally emit internal debug state. Internal debug exists for development; it is isolated by mode and by package exclusion.
