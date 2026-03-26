---
spec_version: "1.0"
system_version: "0.5.0"
status: canonical
id: HES-SPEC-TRIZ-INNOVATION
---

# TRIZ innovation metrics — canonical

## 1. Innovation potential (**I**) — binding

\[
I = C_d \cdot N
\]

where:

- \(C_d\) = **contradiction_density** — normalized measure of active contradiction load at the scope of the report (hex, family, or product layer per execution_flow). **Computation must use** scores from [contradiction_engine.md](contradiction_engine.md) when TRIZ path is active; otherwise a **structural proxy** from the family contradiction matrix applied to active families (documented in run metadata).
- \(N\) = **novelty** — bounded **entropy-based** concentration measure on family activation (or declared substitute vector), mapped to **[0,1]** per `hesperia.engine.product_signals` / TRIZ report builders.

**I** is real-valued and **bounded** for product output by implementation clip policy.

## 2. Non-redundancy

Product-layer narrative equations in [../core/product_observables.md](../core/product_observables.md) **must not** redefine **I**; they reference this spec.

## 3. Code

`hesperia.engine.product_signals`, `hesperia.extensions.triz.report_builders`, `hesperia.extensions.triz.direct_outputs` — must remain consistent with §1.
