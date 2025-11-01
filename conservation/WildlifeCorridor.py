from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class WildlifeCorridor:
    corridor_id: str
    connecting_habitats: list[Habitat] = field(default_factory=list)
    length_km: float = 0.0
    monitored_species: list[Species] = field(default_factory=list)

    def add_habitat(self, habitat: Habitat) -> None:
        if habitat not in self.connecting_habitats:
            self.connecting_habitats.append(habitat)

    def add_species(self, species: Species) -> None:
        if species not in self.monitored_species:
            self.monitored_species.append(species)
