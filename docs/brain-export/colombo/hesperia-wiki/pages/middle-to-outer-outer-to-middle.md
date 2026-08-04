# middle_to_outer / outer_to_middle

**Status:** 🟢 LIVE_FULL — matches proposal (if any), running in production path  
**Category:** [Propagation, Diffusion and Markov](../categories/Propagation-Diffusion-and-Markov.md)  
**Type:** Parameter (YAML weight)  
**Responsible (module):** `assets/specs/canon/propagation_weights.yaml`  
**Value / default:** 0.12

## In plain words

outermost ring gets the thinnest local weight — periphery thins by design.

## Definition

- **Receives:** [inner_to_middle / middle_to_inner](../pages/inner-to-middle-middle-to-inner.md)
- **Does:** Peripheral thinning, distance [decay](../pages/decay.md).
- **Outputs:** `0.12` → [bridge_weight](../pages/bridge-weight.md)
- **Exists for:** completes the radial diffusion ladder

## Yields (formula)

Peripheral thinning, distance [decay](../pages/decay.md).

## Produced from (inputs)

- [inner_to_middle / middle_to_inner](../pages/inner-to-middle-middle-to-inner.md)

## Needed by (consumers)

- [bridge_weight](../pages/bridge-weight.md)

## See also

- [inner_to_middle / middle_to_inner](../pages/inner-to-middle-middle-to-inner.md)
- [bridge_weight](../pages/bridge-weight.md)

## Origin

Graph diffusion on layered neighborhoods — Theory Explainer: plain_lang: outermost ring gets the thinnest local weight — periphery thins by design. author: Hesperia propagation YAML. extent: full. reasoning: completes the radial diffusion ladder. application: [inner_to_middle / middle_to_inner](../pages/inner-to-middle-middle-to-inner.md), [decay_factor (propagation)](../pages/decay-factor-propagation.md).

## Notes

**HWIKI-DOC-24:** Peripheral thinning weight.

---
[← back to category](../categories/Propagation-Diffusion-and-Markov.md) · [wiki home](../index.md) · [Wire Map](Wiki-Wire-Map.md)
