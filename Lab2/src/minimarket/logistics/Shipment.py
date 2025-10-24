from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class Shipment:
    shipment_id: str = ''
    order_id: str = ''
    courier_id: str = ''

    def dispatch(self, courier: 'Courier') -> None:
        self.courier_id = courier.courier_id

    def track(self) -> str:
        return 'in_transit'
