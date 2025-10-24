from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class Supplier:
    supplier_id: str = ''
    contact: str = ''
    lead_time_days: int = 0

    def quote(self, items: list) -> dict:
        return {'eta_days': self.lead_time_days}

    def confirm(self, po: 'PurchaseOrder') -> bool:
        return True
