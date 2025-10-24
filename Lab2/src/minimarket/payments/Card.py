from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class Card:
    number: str = ''
    expiry: str = ''
    cvv: str = ''

    def validate(self) -> bool:
        return self.number.isdigit() and len(self.number) in (15,16)

    def mask(self) -> str:
        return '**** **** **** ' + self.number[-4:]

    def charge(self, amount: float) -> bool:
        from src.minimarket.errors.InvalidCardError import InvalidCardError
        if not self.validate():
            raise InvalidCardError('Card invalid')
        # pretend charge succeeds
        return True
