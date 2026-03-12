# Prolog-style Logic Layer: symbolic inference (future phase).
from sphere.prolog_logic.rule_compiler import (
    parse_rule,
    parse_fact,
    compile_knowledge_base,
)
from sphere.prolog_logic.knowledge_base import (
    build_knowledge_base,
    add_fact,
    add_rule,
    query_predicate,
)
from sphere.prolog_logic.inference_executor import (
    infer,
    evaluate_rule,
    derive_new_facts,
)

__all__ = [
    "parse_rule",
    "parse_fact",
    "compile_knowledge_base",
    "build_knowledge_base",
    "add_fact",
    "add_rule",
    "query_predicate",
    "infer",
    "evaluate_rule",
    "derive_new_facts",
]
