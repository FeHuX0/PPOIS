from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date

from minimarket.core.Product import Product


@dataclass
class PromotionCampaign:
    name: str
    start_date: date
    end_date: date
    products: list[Product] = field(default_factory=list)
    budget: float = 0.0

    def add_product(self, product: Product) -> None:
        if product not in self.products:
            self.products.append(product)

    def is_active(self, today: date | None = None) -> bool:
        today = today or date.today()
        return self.start_date <= today <= self.end_date
