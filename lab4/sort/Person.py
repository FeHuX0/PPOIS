from __future__ import annotations

from dataclasses import dataclass


@dataclass(order=True)
class Person:
    """Example user-defined type for demonstrating generic sorting."""

    age: int
    name: str
    score: float = 0.0

    def __repr__(self) -> str:
        return f"Person(name='{self.name}', age={self.age}, score={self.score})"
