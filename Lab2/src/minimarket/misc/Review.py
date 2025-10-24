from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class Review:
    id: str = ''
    name: str = ''
    meta: dict = field(default_factory=dict)

    def publish(self) -> None:
        self.published = True

    def short(self) -> str:
        return self.content[:30]
