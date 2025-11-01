from __future__ import annotations

from dataclasses import dataclass

from ecology.exceptions.SpeciesNotFoundException import SpeciesNotFoundException


@dataclass
class Species:
    scientific_name: str
    common_name: str
    trophic_level: str
    conservation_status: EndangeredStatus
    typical_habitats: list[Habitat]

    def ensure_status(self) -> None:
        if not self.conservation_status:
            raise SpeciesNotFoundException("Conservation status missing.")

    def rename_common(self, new_name: str) -> None:
        self.common_name = new_name
