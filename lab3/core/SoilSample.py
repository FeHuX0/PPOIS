from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class SoilSample:
    sample_id: str
    collected_by: Volunteer
    location: Region
    collected_at: datetime
    nutrient_index: float
    moisture_percent: float

    def update_nutrients(self, new_value: float) -> None:
        self.nutrient_index = new_value

    def is_optimal(self, floor: float, ceiling: float) -> bool:
        return floor <= self.nutrient_index <= ceiling
