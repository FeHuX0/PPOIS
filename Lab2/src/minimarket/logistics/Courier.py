from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional

@dataclass
class Courier:
    courier_id: str = ''
    name: str = ''
    vehicle: str = ''
    current: Optional[str] = None  # ID текущей доставки

    def assign(self, shipment: 'Shipment') -> None:
        """Назначает курьера на доставку."""
        self.current = shipment.shipment_id
        shipment.assigned_courier = self.courier_id
        shipment.status = 'assigned'

    def deliver(self, shipment: 'Shipment') -> None:
        """Отмечает доставку как выполненную."""
        shipment.status = 'delivered'
        self.current = None
