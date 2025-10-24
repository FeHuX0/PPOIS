from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class Account:
    id: str = ''
    balance: float = 0.0
    owner_id: str = ''

    def deposit(self, amount: float) -> None:
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        from src.minimarket.errors.InsufficientFundsError import InsufficientFundsError
        if amount > self.balance:
            raise InsufficientFundsError('Not enough funds')
        self.balance -= amount

    def transfer_to(self, other: 'Account', amount: float) -> None:
        other.deposit(amount)
        self.withdraw(amount)
