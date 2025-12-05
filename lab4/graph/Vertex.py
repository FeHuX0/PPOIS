from __future__ import annotations

from dataclasses import dataclass
from typing import Generic, TypeVar


T = TypeVar("T")


@dataclass(frozen=True)
class Vertex(Generic[T]):
    """Wrapper for vertex value to keep graph internals hidden."""

    value: T

    def __repr__(self) -> str:
        return f"Vertex({self.value!r})"
