from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class Vendor:
    vendor_id: str = ''
    name: str = ''
    rating: float = 0.0

    def supply_item(self, sku: str, qty: int) -> dict:
        return {'sku': sku, 'qty': qty}

    def update_rating(self, delta: float) -> None:
        self.rating = (self.rating + delta) / 2
