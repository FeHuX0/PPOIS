from __future__ import annotations
from dataclasses import dataclass

from src.minimarket.inventory.InventoryItem import InventoryItem

@dataclass
class Warehouse:
    warehouse_id: str = ''
    address: str = ''
    capacity: int = 0

    def store_item(self, sku: str, qty: int) -> None:
        """Уменьшает вместимость склада после размещения товара."""
        if qty > self.capacity:
            raise ValueError("Недостаточно места на складе")
        self.capacity -= qty

    def find_item(self, sku: str) -> 'InventoryItem':
        """Возвращает объект InventoryItem для данного SKU."""
        return InventoryItem(sku=sku, quantity=0, location=self.address)
