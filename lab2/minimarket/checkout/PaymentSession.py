from __future__ import annotations

from dataclasses import dataclass, field

from minimarket.checkout.Order import Order
from minimarket.exceptions.PaymentAuthorizationException import PaymentAuthorizationException


@dataclass
class PaymentSession:
    session_id: str
    order: Order
    amount_due: float
    payments: list[float] = field(default_factory=list)
    status: str = "pending"

    def authorize_payment(self, amount: float) -> None:
        if amount <= 0:
            raise PaymentAuthorizationException("Payment amount must be positive.")
        self.payments.append(amount)
        if sum(self.payments) >= self.amount_due:
            self.status = "captured"
        else:
            self.status = "partial"

    def remaining_balance(self) -> float:
        return max(self.amount_due - sum(self.payments), 0.0)
