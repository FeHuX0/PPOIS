from __future__ import annotations

from dataclasses import dataclass, field

from ecology.exceptions.DataCollectionException import DataCollectionException


@dataclass
class DataCollectionLog:
    log_id: str
    collector: CitizenScientist
    station: MonitoringStation
    collected_values: list[float] = field(default_factory=list)
    notes: list[str] = field(default_factory=list)

    def record_value(self, value: float, note: str) -> None:
        if value < 0:
            raise DataCollectionException("Value must be non-negative.")
        self.collected_values.append(value)
        self.notes.append(note)

    def average_value(self) -> float:
        if not self.collected_values:
            return 0.0
        return sum(self.collected_values) / len(self.collected_values)
