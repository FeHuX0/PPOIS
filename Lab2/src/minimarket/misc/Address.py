from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class Address:
    id: str = ''
    name: str = ''
    meta: dict = field(default_factory=dict)

    def full(self) -> str:
        return f"{self.name}, {self.meta.get('city','')}"

    def validate(self) -> bool:
        return bool(self.name)
