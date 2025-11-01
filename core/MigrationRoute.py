from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class MigrationRoute:
    route_id: str
    species: Species
    checkpoints: list[Region] = field(default_factory=list)
    total_distance_km: float = 0.0

    def add_checkpoint(self, region: Region) -> None:
        if region not in self.checkpoints:
            self.checkpoints.append(region)

    def set_distance(self, distance_km: float) -> None:
        self.total_distance_km = distance_km
