from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from minimarket.core.Product import Product


@dataclass
class PriceTag:
    product: Product
    display_price: float
    last_updated: datetime

    def refresh(self) -> None:
        self.display_price = self.product.price_with_tax()
        self.last_updated = datetime.now()
