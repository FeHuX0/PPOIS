from __future__ import annotations

from dataclasses import dataclass, field

from minimarket.core.Product import Product


@dataclass
class Supplier:
    name: str
    lead_time_days: int
    catalog: list[Product] = field(default_factory=list)

    def add_product(self, product: Product) -> None:
        if product not in self.catalog:
            self.catalog.append(product)
