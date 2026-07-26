# HESPERIA — Hex microphysics → product analytical maps
from hesperia.engine.hex_outputs.e2e_integration import (
    hex_microstructure_bundle_for_text,
    slim_microstructure_for_json,
)
from hesperia.engine.hex_outputs.hex_output_engine import (
    HexOutputParams,
    attach_hex_product_outputs,
    attach_microstructure_analytics_public,
    build_sparse_hex_scene,
    compute_hex_outputs,
    serialize_hex_outputs,
)

__all__ = [
    "HexOutputParams",
    "compute_hex_outputs",
    "serialize_hex_outputs",
    "build_sparse_hex_scene",
    "attach_hex_product_outputs",
    "attach_microstructure_analytics_public",
    "hex_microstructure_bundle_for_text",
    "slim_microstructure_for_json",
]
