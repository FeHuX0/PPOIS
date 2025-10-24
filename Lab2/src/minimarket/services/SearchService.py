from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class SearchService:
    index: dict = field(default_factory=dict)
    last_rebuild: str = ''
    settings: dict = field(default_factory=dict)

    def index_product(self, product: 'Product') -> None:
        self.index[product.sku] = product

    def search(self, query: str) -> list:
        return [p for p in self.index.values() if query in p.sku]
