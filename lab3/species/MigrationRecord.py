from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class MigrationRecord:
    record_id: str
    species: Species
    route: MigrationRoute
    departed_on: datetime
    arrived_on: datetime | None = None

    def mark_arrival(self, arrival_time: datetime) -> None:
        self.arrived_on = arrival_time

    def travel_time_days(self) -> float:
        if not self.arrived_on:
            return 0.0
        return (self.arrived_on - self.departed_on).days
