from __future__ import annotations

from dataclasses import dataclass, field

from minimarket.core.Product import Product
from minimarket.exceptions.DuplicateItemException import DuplicateItemException


@dataclass
class Shelf:
    code: str
    capacity: int
    products: list[Product] = field(default_factory=list)
    temperature_zone: str = "ambient"

    def add_product(self, product: Product) -> None:
        if len(self.products) >= self.capacity:
            raise DuplicateItemException("Shelf capacity reached.")
        self.products.append(product)

    def available_slots(self) -> int:
        return self.capacity - len(self.products)
