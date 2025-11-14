from __future__ import annotations

from dataclasses import dataclass, field

from minimarket.checkout.ShoppingCart import ShoppingCart
from minimarket.exceptions.InsufficientStockException import InsufficientStockException
from minimarket.exceptions.OrderStateException import OrderStateException
from minimarket.inventory.StockItem import StockItem


@dataclass
class Order:
    order_id: str
    cart: ShoppingCart
    status: str = "draft"
    allocations: dict[str, int] = field(default_factory=dict)
    history: list[str] = field(default_factory=list)

    def allocate_stock(self, stock_item: StockItem, quantity: int) -> None:
        if quantity <= 0:
            raise InsufficientStockException("Allocation quantity must be positive.")
        if quantity > stock_item.available_quantity():
            raise InsufficientStockException("Not enough stock to allocate for the order.")
        stock_item.reserve(quantity)
        self.allocations[stock_item.product.sku] = self.allocations.get(stock_item.product.sku, 0) + quantity
        self.history.append(f"Allocated {quantity} units of {stock_item.product.sku}.")

    def mark_status(self, new_status: str) -> None:
        allowed = {"draft", "confirmed", "picking", "completed", "cancelled"}
        if new_status not in allowed:
            raise OrderStateException(f"Status {new_status} is not allowed.")
        self.status = new_status
        self.history.append(f"Status changed to {new_status}.")

    def total_due(self) -> float:
        return self.cart.calculate_total()
