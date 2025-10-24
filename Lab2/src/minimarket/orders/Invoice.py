from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class Invoice:
    invoice_id: str = ''
    po_id: str = ''
    amount: float = 0.0

    def pay(self, amount: float) -> None:
        self.amount -= amount

    def is_paid(self) -> bool:
        return self.amount <= 0
