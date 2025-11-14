from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TemperatureLog:
    probe_id: str
    threshold: float
    readings: list[float] = field(default_factory=list)

    def record(self, value: float) -> None:
        self.readings.append(value)

    def average(self) -> float:
        if not self.readings:
            return 0.0
        return round(sum(self.readings) / len(self.readings), 2)

    def is_out_of_range(self) -> bool:
        return any(read > self.threshold for read in self.readings)
