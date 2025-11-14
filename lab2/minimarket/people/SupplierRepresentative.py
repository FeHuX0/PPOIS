from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class SupplierRepresentative:
    name: str
    supplier_name: str
    visits: list[str] = field(default_factory=list)

    def log_visit(self, store_name: str) -> None:
        self.visits.append(store_name)
