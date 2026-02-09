"""
Sphere-based RAG prototype package.

This package exposes a minimal, deterministic interface around the
Sphere geometry, attribution engine, traversal, and governance layer.

The goal is to:
- Take raw text (query, context, candidate output)
- Attribute it into Areas/Families
- Run loop traversal over the semantic sphere
- Produce clear numeric signals for any LLM to consume.
"""
