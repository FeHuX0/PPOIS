from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from minimarket.inventory.StockItem import StockItem


@dataclass
class InventoryRecord:
    record_id: str
    items: list[StockItem] = field(default_factory=list)
    last_updated: datetime | None = None

    def add_item(self, stock_item: StockItem) -> None:
        if stock_item not in self.items:
            self.items.append(stock_item)
        self.last_updated = datetime.now()

    def total_skus(self) -> int:
        return len(self.items)

    def find_low_stock(self) -> list[StockItem]:
        return [item for item in self.items if item.needs_restock()]
