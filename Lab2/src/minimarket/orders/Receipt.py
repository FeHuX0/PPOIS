from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class Receipt:
    id: str = ''
    name: str = ''
    meta: dict = field(default_factory=dict)

    def total(self) -> float:
        return sum(i['price'] * i.get('qty',1) for i in getattr(self, 'items', []))

    def to_dict(self) -> dict:
        return {'id': self.receipt_id}
