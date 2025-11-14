from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime

from minimarket.checkout.Order import Order


@dataclass
class Receipt:
    order: Order
    printed_at: datetime
    footnotes: list[str] = field(default_factory=list)

    def summary(self) -> str:
        total = self.order.total_due()
        notes = " | ".join(self.footnotes) if self.footnotes else "No notes"
        return f"Receipt for order {self.order.order_id}: total={total:.2f}, notes={notes}"
