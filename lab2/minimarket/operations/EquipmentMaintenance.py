from __future__ import annotations

from dataclasses import dataclass
from datetime import date, timedelta


@dataclass
class EquipmentMaintenance:
    equipment_id: str
    frequency_days: int
    last_service_date: date

    def schedule_next(self) -> date:
        return self.last_service_date + timedelta(days=self.frequency_days)

    def needs_service(self, today: date | None = None) -> bool:
        today = today or date.today()
        return today >= self.schedule_next()
