from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class MarineReserve:
    reserve_id: str
    name: str
    area_sq_km: float
    protected_species: list[Species] = field(default_factory=list)
    regulations: list[str] = field(default_factory=list)

    def add_protected_species(self, species: Species) -> None:
        if species not in self.protected_species:
            self.protected_species.append(species)

    def add_regulation(self, regulation: str) -> None:
        self.regulations.append(regulation)
