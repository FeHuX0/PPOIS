from __future__ import annotations

from dataclasses import dataclass, field

from ecology.exceptions.MonitoringStationOfflineException import MonitoringStationOfflineException


@dataclass
class MonitoringStation:
    station_id: str
    region: Region
    sensors: list[SensorDevice] = field(default_factory=list)
    active: bool = True
    collected_samples: list[EnvironmentalSample] = field(default_factory=list)

    def add_sensor(self, sensor: SensorDevice) -> None:
        if sensor not in self.sensors:
            self.sensors.append(sensor)

    def validate_online(self) -> None:
        if not self.active:
            raise MonitoringStationOfflineException("Station is offline.")
