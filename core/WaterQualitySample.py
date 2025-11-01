from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class WaterQualitySample:
    sample_id: str
    taken_by: CitizenScientist
    location: Region
    taken_at: datetime
    ph_level: float
    contamination_level: float

    def is_safe(self, max_contamination: float) -> bool:
        return self.contamination_level <= max_contamination

    def adjust_ph(self, new_ph: float) -> None:
        self.ph_level = new_ph
