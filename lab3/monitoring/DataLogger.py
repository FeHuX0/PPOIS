from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class DataLogger:
    logger_id: str
    station: MonitoringStation
    data_points: list[float] = field(default_factory=list)
    timestamps: list[str] = field(default_factory=list)

    def record(self, value: float, timestamp: str) -> None:
        self.data_points.append(value)
        self.timestamps.append(timestamp)

    def latest_value(self) -> float | None:
        return self.data_points[-1] if self.data_points else None
