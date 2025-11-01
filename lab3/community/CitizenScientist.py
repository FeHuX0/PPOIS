from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class CitizenScientist:
    member_id: str
    name: str
    trained_programs: list[str] = field(default_factory=list)
    observations_logged: list[FieldObservation] = field(default_factory=list)
    portable_sensors: list[SensorDevice] = field(default_factory=list)

    def log_observation(self, observation: FieldObservation) -> None:
        self.observations_logged.append(observation)

    def assign_sensor(self, sensor: SensorDevice) -> None:
        if sensor not in self.portable_sensors:
            self.portable_sensors.append(sensor)
