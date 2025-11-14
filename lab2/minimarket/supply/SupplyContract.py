from __future__ import annotations

from dataclasses import dataclass

from minimarket.supply.Supplier import Supplier


@dataclass
class SupplyContract:
    contract_id: str
    supplier: Supplier
    terms: str
    active: bool = True

    def terminate(self) -> None:
        self.active = False
