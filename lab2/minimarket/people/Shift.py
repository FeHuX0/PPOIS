from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class Shift:
    shift_id: str
    start: datetime
    end: datetime
    area: str

    def duration_hours(self) -> float:
        delta = self.end - self.start
        return round(delta.total_seconds() / 3600, 2)
