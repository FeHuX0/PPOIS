from __future__ import annotations

from dataclasses import dataclass

from minimarket.core.Product import Product
from minimarket.exceptions.QuantityLimitException import QuantityLimitException


@dataclass
class CartItem:
    product: Product
    quantity: int = 0
    discount: float = 0.0

    def increase(self, amount: int) -> None:
        if amount <= 0:
            raise QuantityLimitException("Cart items must increase by a positive amount.")
        self.quantity += amount

    def decrease(self, amount: int) -> None:
        if amount <= 0 or amount > self.quantity:
            raise QuantityLimitException("Cannot remove more than the current quantity.")
        self.quantity -= amount

    def total_price(self) -> float:
        subtotal = self.product.price_with_tax() * self.quantity
        subtotal -= self.discount
        return round(max(subtotal, 0.0), 2)
