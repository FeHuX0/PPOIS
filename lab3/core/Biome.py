from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Biome:
    biome_type: str
    climate: str
    average_rainfall_mm: float
    keystone_species: list[Species] = field(default_factory=list)

    def add_keystone_species(self, species: Species) -> None:
        if species not in self.keystone_species:
            self.keystone_species.append(species)

    def describe(self) -> str:
        return f"{self.biome_type} with {self.climate} climate"
