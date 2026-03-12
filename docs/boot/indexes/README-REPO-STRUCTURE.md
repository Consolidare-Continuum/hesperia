<!--
HESPERIA — Reference Architecture Definition (RAD)
Copyright © 2026 igareosh.com — Platonov Igor (aka @igareosh). All rights reserved.
Restricted Research Disclosure License. Inspection and reference only.
No reproduction, redistribution, or use without explicit written permission.
See LEGAL_NOTICE.md for full terms.
-->

# HESPERIA Repository Structure (Canonical)

This document is the canonical structure reference for the post-refactor repository.

```text
HESPERIA
│
├── core/
│   ├── layers/
│   ├── topology/
│   ├── math/
│   └── propagation/
│
├── runtime/
│   ├── pipeline/
│   └── api/
│
├── lexicon/
│   ├── dictionaries/
│   └── validation/
│
├── tools/
│
├── assets/
│
├── tests/
│
├── docs/
│   └── specs/
│
└── legacy/
```

## Notes

- `runtime/`, `core/`, and `lexicon/` form the active execution stack.
- `legacy/` is historical and excluded from active runtime and test-path assumptions.
