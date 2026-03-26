<!--
HESPERIA — Hesperia Engine Dynamics
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
See LEGAL_NOTICE.md for full terms.
-->

# Hesperia Engine Dynamics — **Canonical Release v0.5**

**2026.** This release is the **sealed dynamics stack**: multiscale semantic physics with deterministic math, product signals, HSPR, and E2E proof — **not** a claim of generative truth or clinical certification.

**Full index:** [HESPERIA_v0_5_ENGINE_DYNAMICS.md](../../HESPERIA_v0_5_ENGINE_DYNAMICS.md)

---

## What v0.5 ships

1. Concept → hex → family → area execution_flow (documented + implemented).  
2. Hex microphysics + family bridge + sealed multiscale runner.  
3. Product signal layer + field HSPR + **system** HSPR index.  
4. **19** E2E JSON artifacts (+ optional field dynamics).  

---

## Explicitly not the canonical release definition

- **TFP / Kernberg session smoke** — testing collateral; CI only.  
- **legacy/** — archival.

---

## Verify

```bash
python3 -m runtime.execution_flow.run_e2e_all
```

---

## Closure (v0.5.0)

- **Changelog:** [CHANGELOG.md](../../../CHANGELOG.md)  
- **Naming guide:** [ENGINE_DYNAMICS_CANONICAL_NAMING_v0.5.md](../../ENGINE_DYNAMICS_CANONICAL_NAMING_v0.5.md)  
- **Git tags (same commit, push both):**  
  - **`v0.5.0`** — semver  
  - **`hesperia-engine-dynamics-v0.5.0`** — product-line release name (GitHub Release title: *Hesperia Engine Dynamics v0.5.0*)

## After v0.5

Continue Engine Dynamics R&D on v0.5.1+; preserve `specs/canon/` and sealed-stack contracts as normative unless versioned.

---

*Hesperia Engine Dynamics — Canonical Release v0.5.*
