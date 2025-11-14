from __future__ import annotations

from dataclasses import dataclass
from datetime import date

from minimarket.exceptions.UnauthorizedDiscountException import UnauthorizedDiscountException


@dataclass
class Coupon:
    code: str
    discount_percentage: float
    expires_on: date
    usage_limit: int = 1
    used_count: int = 0
    stackable: bool = False

    def is_valid(self, today: date | None = None) -> bool:
        today = today or date.today()
        if self.used_count >= self.usage_limit:
            return False
        return today <= self.expires_on

    def apply_discount(self, total: float) -> float:
        return round(total * (self.discount_percentage / 100), 2)

    def mark_use(self) -> None:
        if self.used_count >= self.usage_limit:
            raise UnauthorizedDiscountException(f"Coupon {self.code} exceeded usage limit.")
        self.used_count += 1

    def reset_usage(self) -> None:
        self.used_count = 0
