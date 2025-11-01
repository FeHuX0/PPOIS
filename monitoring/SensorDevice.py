from __future__ import annotations

from dataclasses import dataclass


@dataclass
class SensorDevice:
    sensor_id: str
    type: str
    calibration_date: str
    accuracy: float
    active: bool = True

    def recalibrate(self, new_date: str, new_accuracy: float) -> None:
        self.calibration_date = new_date
        self.accuracy = new_accuracy

    def deactivate(self) -> None:
        self.active = False
