from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class Order:
    order_id: str = ''
    items: list = field(default_factory=list)
    customer_id: str = ''

    def add_item(self, item: 'OrderItem') -> None:
        self.items.append(item)

    def total_amount(self) -> float:
        return sum(i.price * i.qty for i in self.items)

    def submit(self) -> str:
        self.status = 'submitted'
        return self.order_id
