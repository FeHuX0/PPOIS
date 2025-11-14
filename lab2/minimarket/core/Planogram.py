from __future__ import annotations

from dataclasses import dataclass, field

from minimarket.core.Product import Product
from minimarket.core.Shelf import Shelf
from minimarket.exceptions.DuplicateItemException import DuplicateItemException


@dataclass
class Planogram:
    department: str
    placements: dict[str, Shelf] = field(default_factory=dict)
    version: str = "v1"

    def assign_product(self, product: Product, shelf: Shelf) -> None:
        if product.sku in self.placements:
            raise DuplicateItemException(f"Product {product.sku} already placed.")
        self.placements[product.sku] = shelf

    def relocate(self, product: Product, shelf: Shelf) -> None:
        self.placements[product.sku] = shelf
