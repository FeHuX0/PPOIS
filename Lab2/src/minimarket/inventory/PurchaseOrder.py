from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class PurchaseOrder:
    po_id: str = ''
    supplier_id: str = ''
    items: list = field(default_factory=list)

    def add_line(self, sku: str, qty: int) -> None:
        self.items.append({'sku':sku,'qty':qty})

    def total_items(self) -> int:
        return sum(i['qty'] for i in self.items)
