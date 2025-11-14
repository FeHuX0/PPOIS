from __future__ import annotations

from dataclasses import dataclass

from minimarket.core.Product import Product


@dataclass
class ReorderRequest:
    request_id: str
    product: Product
    requested_by: str
    quantity: int
    status: str = "draft"

    def approve(self) -> None:
        self.status = "approved"

    def mark_received(self) -> None:
        self.status = "received"
