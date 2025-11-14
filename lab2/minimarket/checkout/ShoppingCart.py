from __future__ import annotations

from dataclasses import dataclass, field

from minimarket.checkout.CartItem import CartItem
from minimarket.core.Product import Product
from minimarket.exceptions.DuplicateItemException import DuplicateItemException
from minimarket.exceptions.QuantityLimitException import QuantityLimitException
from minimarket.exceptions.VoucherExpiredException import VoucherExpiredException
from minimarket.promotions.Coupon import Coupon


@dataclass
class ShoppingCart:
    max_unique_items: int = 50
    items: dict[str, CartItem] = field(default_factory=dict)
    applied_coupons: list[Coupon] = field(default_factory=list)

    def add_item(self, product: Product, quantity: int) -> None:
        if quantity <= 0:
            raise QuantityLimitException("Quantity must be positive.")
        key = product.sku
        if key not in self.items:
            if len(self.items) >= self.max_unique_items:
                raise QuantityLimitException("Cart reached maximum unique items.")
            self.items[key] = CartItem(product=product)
        self.items[key].increase(quantity)

    def remove_item(self, sku: str) -> None:
        if sku in self.items:
            del self.items[sku]

    def apply_coupon(self, coupon: Coupon) -> None:
        if coupon in self.applied_coupons:
            raise DuplicateItemException(f"Coupon {coupon.code} already applied.")
        if not coupon.is_valid():
            raise VoucherExpiredException(f"Coupon {coupon.code} is no longer valid.")
        coupon.mark_use()
        self.applied_coupons.append(coupon)

    def calculate_total(self) -> float:
        total = sum(item.total_price() for item in self.items.values())
        for coupon in self.applied_coupons:
            total -= coupon.apply_discount(total)
        return round(max(total, 0.0), 2)

    def total_items(self) -> int:
        return sum(item.quantity for item in self.items.values())
