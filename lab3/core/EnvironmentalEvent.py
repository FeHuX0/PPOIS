from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class EnvironmentalEvent:
    event_id: str
    title: str
    scheduled_for: datetime
    location: Region
    expected_attendance: int

    def reschedule(self, new_time: datetime) -> None:
        self.scheduled_for = new_time

    def change_location(self, new_region: Region) -> None:
        self.location = new_region
