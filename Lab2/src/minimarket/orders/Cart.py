from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

from src.minimarket.orders.Order import Order

@dataclass
class Cart:
    customer_id: str = ''
    items: list = field(default_factory=list)
    total: float = 0.0

    def add_product(self, product: 'Product', qty: int = 1) -> None:
        self.items.append({'sku': product.sku, 'qty': qty, 'price': product.price})
        self.total += product.price * qty

    def clear(self) -> None:
        self.items = []
        self.total = 0.0

    def checkout(self, customer: 'Customer', payment: 'PaymentProcessor') -> 'Order':
        order = Order('ord-'+self.customer_id, [], self.customer_id)
        # transform items
        for it in self.items:
            order.add_item(__import__('types').SimpleNamespace(sku=it['sku'], qty=it['qty'], price=it['price']))
        return order
