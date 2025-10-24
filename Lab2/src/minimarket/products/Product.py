from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class Product:
    sku: str = ''
    price: float = 0.0
    stock: int = 0

    def adjust_stock(self, delta: int) -> None:
        self.stock += delta

    def is_available(self) -> bool:
        return self.stock > 0

    def price_with_tax(self, tax_rate: float) -> float:
        return self.price * (1 + tax_rate)
