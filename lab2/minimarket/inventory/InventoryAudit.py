from __future__ import annotations

from dataclasses import dataclass, field

from minimarket.exceptions.InventoryAuditException import InventoryAuditException
from minimarket.inventory.InventoryRecord import InventoryRecord


@dataclass
class InventoryAudit:
    audit_id: str
    records: list[InventoryRecord]
    discrepancies: dict[str, int] = field(default_factory=dict)

    def record_discrepancy(self, sku: str, delta: int) -> None:
        if sku in self.discrepancies:
            raise InventoryAuditException(f"Discrepancy for {sku} already recorded.")
        self.discrepancies[sku] = delta

    def summary(self) -> str:
        total = sum(abs(delta) for delta in self.discrepancies.values())
        return f"Audit {self.audit_id} recorded {len(self.discrepancies)} discrepancies totaling {total} units."
