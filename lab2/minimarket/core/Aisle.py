from __future__ import annotations

from dataclasses import dataclass, field

from minimarket.core.Shelf import Shelf


@dataclass
class Aisle:
    identifier: str
    category: str
    shelves: list[Shelf] = field(default_factory=list)

    def add_shelf(self, shelf: Shelf) -> None:
        if shelf not in self.shelves:
            self.shelves.append(shelf)

    def list_products(self) -> list[str]:
        products = []
        for shelf in self.shelves:
            products.extend(product.name for product in shelf.products)
        return products
