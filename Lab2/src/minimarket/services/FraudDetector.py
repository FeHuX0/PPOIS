from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class FraudDetector:
    threshold: float = 0.0
    rules: list = field(default_factory=list)
    blacklist: set = field(default_factory=set)

    def check(self, transaction: 'Transaction') -> bool:
        if transaction.amount > self.threshold:
            return True
        return False

    def blacklist_add(self, identifier: str) -> None:
        self.blacklist.add(identifier)
