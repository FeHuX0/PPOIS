from __future__ import annotations

from dataclasses import dataclass, field

from minimarket.promotions.LoyaltyAccount import LoyaltyAccount


@dataclass
class Customer:
    name: str
    loyalty_account: LoyaltyAccount | None = None
    orders: list[object] = field(default_factory=list)
    preferences: set[str] = field(default_factory=set)

    def add_order(self, order: object) -> None:
        self.orders.append(order)

    def add_preference(self, preference: str) -> None:
        self.preferences.add(preference)
