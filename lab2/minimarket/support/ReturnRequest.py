from __future__ import annotations

from dataclasses import dataclass

from minimarket.checkout.Order import Order
from minimarket.core.Product import Product
from minimarket.exceptions.ReturnWindowExpiredException import ReturnWindowExpiredException


@dataclass
class ReturnRequest:
    request_id: str
    order: Order
    product: Product
    reason: str
    status: str = "pending"
    days_since_purchase: int = 0

    def approve(self) -> None:
        if self.days_since_purchase > 14:
            raise ReturnWindowExpiredException("Return window expired.")
        self.status = "approved"

    def reject(self, note: str) -> None:
        self.status = f"rejected: {note}"
