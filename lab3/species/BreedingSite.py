from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class BreedingSite:
    site_id: str
    habitat: Habitat
    species: Species
    nests: list[str] = field(default_factory=list)
    protection_level: str = "medium"

    def add_nest(self, nest_id: str) -> None:
        if nest_id not in self.nests:
            self.nests.append(nest_id)

    def upgrade_protection(self, level: str) -> None:
        self.protection_level = level
