from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class AccountingLedger:
    ledger_id: str = ''
    entries: list = field(default_factory=list)
    currency: str = ''

    def post_entry(self, entry: dict) -> None:
        self.entries.append(entry)

    def balance(self) -> float:
        return sum(e.get('amount',0) for e in self.entries)
