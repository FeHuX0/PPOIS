from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class LoyaltyProgram:
    id: str = ''
    name: str = ''
    meta: dict = field(default_factory=dict)

    def add_points(self, customer_id: str, pts: int) -> None:
        self.meta.setdefault(customer_id, 0)
        self.meta[customer_id] += pts

    def redeem(self, customer_id: str, pts: int) -> bool:
        if self.meta.get(customer_id,0) < pts: return False
        self.meta[customer_id] -= pts
        return True
