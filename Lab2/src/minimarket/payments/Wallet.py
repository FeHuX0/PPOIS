from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class Wallet:
    wallet_id: str = ''
    owner_id: str = ''
    balance: float = 0.0

    def credit(self, amount: float) -> None:
        self.balance += amount

    def debit(self, amount: float) -> None:
        from src.minimarket.errors.InsufficientFundsError import InsufficientFundsError
        if amount > self.balance:
            raise InsufficientFundsError('Wallet dry')
        self.balance -= amount

    def transfer_to_wallet(self, other: 'Wallet', amount: float) -> None:
        self.debit(amount)
        other.credit(amount)
