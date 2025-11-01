from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Region:
    name: str
    latitude: float
    longitude: float
    habitats: list[Habitat] = field(default_factory=list)
    monitoring_stations: list[MonitoringStation] = field(default_factory=list)

    def add_habitat(self, habitat: Habitat) -> None:
        if habitat not in self.habitats:
            self.habitats.append(habitat)

    def attach_station(self, station: MonitoringStation) -> None:
        if station not in self.monitoring_stations:
            self.monitoring_stations.append(station)
