from __future__ import annotations

from dataclasses import dataclass, field

from ecology.exceptions.HabitatCapacityException import HabitatCapacityException


@dataclass
class Habitat:
    code: str
    area_hectares: float
    biome: Biome
    resident_species: list[Species] = field(default_factory=list)
    capacity: int = 0

    def register_species(self, species: Species) -> None:
        if len(self.resident_species) >= self.capacity > 0:
            raise HabitatCapacityException("Habitat capacity reached.")
        if species not in self.resident_species:
            self.resident_species.append(species)

    def available_capacity(self) -> int:
        return max(self.capacity - len(self.resident_species), 0)
