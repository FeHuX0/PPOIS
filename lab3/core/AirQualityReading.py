from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime

from ecology.exceptions.PollutionLevelException import PollutionLevelException


@dataclass
class AirQualityReading:
    reading_id: str
    station: MonitoringStation
    recorded_at: datetime
    particulate_matter: float
    co2_ppm: float

    def evaluate(self, threshold: float) -> None:
        if self.particulate_matter > threshold:
            raise PollutionLevelException("Air pollution above safe threshold.")

    def co2_status(self) -> str:
        return "high" if self.co2_ppm > 400 else "normal"
