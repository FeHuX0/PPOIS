from __future__ import annotations

from dataclasses import dataclass


@dataclass
class BundleOffer:
    name: str
    items_required: dict[str, int]
    bundle_price: float

    def is_applicable(self, cart: 'ShoppingCart') -> bool:
        for sku, qty in self.items_required.items():
            if sku not in cart.items or cart.items[sku].quantity < qty:
                return False
        return True
