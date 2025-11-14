from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Invoice:
    invoice_number: str
    amount_due: float
    paid: bool = False
    payments: list[float] = field(default_factory=list)

    def record_payment(self, amount: float) -> None:
        self.payments.append(amount)
        if sum(self.payments) >= self.amount_due:
            self.paid = True
