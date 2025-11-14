from __future__ import annotations

from dataclasses import dataclass, field

from minimarket.exceptions.GiftCardBalanceException import GiftCardBalanceException


@dataclass
class GiftCard:
    card_number: str
    balance: float
    transactions: list[str] = field(default_factory=list)

    def redeem(self, amount: float) -> None:
        if amount > self.balance:
            raise GiftCardBalanceException("Not enough balance on the gift card.")
        self.balance -= amount
        self.transactions.append(f"-{amount:.2f}")

    def load(self, amount: float) -> None:
        self.balance += amount
        self.transactions.append(f"+{amount:.2f}")
