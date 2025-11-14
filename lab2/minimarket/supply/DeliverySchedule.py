from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta

from minimarket.exceptions.SupplierDelayException import SupplierDelayException
from minimarket.supply.Supplier import Supplier


@dataclass
class DeliverySchedule:
    schedule_id: str
    supplier: Supplier
    window_start: datetime
    window_end: datetime

    def delay(self, minutes: int) -> None:
        if minutes > 240:
            raise SupplierDelayException("Delay exceeds allowable buffer.")
        delta = timedelta(minutes=minutes)
        self.window_start += delta
        self.window_end += delta
