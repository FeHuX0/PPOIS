from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class WasteReport:
    report_id: str
    items_wasted: dict[str, int] = field(default_factory=dict)
    reason: str = "expired"

    def add_waste(self, sku: str, quantity: int) -> None:
        self.items_wasted[sku] = self.items_wasted.get(sku, 0) + quantity

    def total_units(self) -> int:
        return sum(self.items_wasted.values())
