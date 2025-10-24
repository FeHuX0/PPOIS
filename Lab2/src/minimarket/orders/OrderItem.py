from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class OrderItem:
    sku: str = ''
    qty: int = 0
    price: float = 0.0

    def line_total(self) -> float:
        return self.qty * self.price

    def increase_qty(self, n: int) -> None:
        self.qty += n
