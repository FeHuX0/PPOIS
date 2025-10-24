from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class Coupon:
    code: str = ''
    discount_percent: float = 0.0
    valid: bool = False

    def apply(self, amount: float) -> float:
        if not self.valid: return amount
        return amount * (1 - self.discount_percent/100)

    def invalidate(self) -> None:
        self.valid = False
