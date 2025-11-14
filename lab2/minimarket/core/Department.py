from __future__ import annotations

from dataclasses import dataclass, field

from minimarket.core.Aisle import Aisle


@dataclass
class Department:
    name: str
    manager: str
    aisles: list[Aisle] = field(default_factory=list)

    def add_aisle(self, aisle: Aisle) -> None:
        if aisle not in self.aisles:
            self.aisles.append(aisle)

    def count_products(self) -> int:
        return sum(len(aisle.list_products()) for aisle in self.aisles)
