from __future__ import annotations

from dataclasses import dataclass

from minimarket.core.Product import Product
from minimarket.exceptions.InsufficientStockException import InsufficientStockException


@dataclass
class StockItem:
    product: Product
    quantity: int
    reserved: int = 0
    low_stock_threshold: int = 5

    def reserve(self, amount: int) -> None:
        if amount <= 0:
            raise InsufficientStockException("Reservation amount must be positive.")
        if amount > self.available_quantity():
            raise InsufficientStockException("Insufficient stock to reserve.")
        self.reserved += amount

    def release(self, amount: int) -> None:
        self.reserved = max(self.reserved - amount, 0)

    def restock(self, amount: int) -> None:
        self.quantity += amount

    def available_quantity(self) -> int:
        return max(self.quantity - self.reserved, 0)

    def needs_restock(self) -> bool:
        return self.available_quantity() <= self.low_stock_threshold
