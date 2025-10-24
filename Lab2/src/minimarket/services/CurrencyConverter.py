from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class CurrencyConverter:
    base: str = ''
    rates: dict = field(default_factory=dict)
    last_updated: str = ''

    def convert(self, amount: float, to: str) -> float:
        r = self.rates.get(to,1)
        return amount * r

    def update_rate(self, cur: str, val: float) -> None:
        self.rates[cur]=val
