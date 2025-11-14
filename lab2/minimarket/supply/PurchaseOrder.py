from __future__ import annotations

from dataclasses import dataclass, field

from minimarket.supply.Supplier import Supplier


@dataclass
class PurchaseOrder:
    po_number: str
    supplier: Supplier
    items: dict[str, int] = field(default_factory=dict)
    status: str = "draft"
    total_value: float = 0.0

    def add_item(self, sku: str, quantity: int, price: float) -> None:
        self.items[sku] = self.items.get(sku, 0) + quantity
        self.total_value += quantity * price

    def mark_received(self) -> None:
        self.status = "received"
