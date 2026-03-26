"""Engine context guard utilities."""

from __future__ import annotations

from typing import Any


class GuardedContext(dict[str, Any]):
    def __init__(self, *args: Any, protected_keys: set[str] | None = None, **kwargs: Any) -> None:
        super().__init__(*args, **kwargs)
        self._protected_keys = set(protected_keys or set())
        self._mutation_log: list[str] = []

    @property
    def mutation_log(self) -> list[str]:
        return list(self._mutation_log)

    def __setitem__(self, key: str, value: Any) -> None:
        if key in self._protected_keys:
            self._mutation_log.append(f"blocked_mutation:{key}")
            raise ValueError(f"engine_context_readonly_mutation_blocked:{key}")
        super().__setitem__(key, value)

