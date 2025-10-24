from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class InventoryItem:
    sku: str = ''
    quantity: int = 0
    location: str = ''

    def reserve(self, qty: int) -> None:
        from src.minimarket.errors.OutOfStockError import OutOfStockError
        if qty > self.quantity:
            raise OutOfStockError('Not enough')
        self.quantity -= qty

    def restock(self, qty: int) -> None:
        self.quantity += qty
