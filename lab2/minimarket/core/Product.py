from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Product:
    sku: str
    name: str
    base_price: float
    tax_rate: float = 0.1
    tags: set[str] = field(default_factory=set)

    def price_with_tax(self) -> float:
        return round(self.base_price * (1 + self.tax_rate), 2)

    def apply_markup(self, percentage: float) -> None:
        self.base_price = round(self.base_price * (1 + percentage / 100), 2)

    def add_tag(self, tag: str) -> None:
        self.tags.add(tag)
