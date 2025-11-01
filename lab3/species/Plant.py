from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Plant:
    species: Species
    plot_location: Region
    height_cm: float
    flowering_dates: list[str] = field(default_factory=list)
    pollinators: list[Species] = field(default_factory=list)

    def record_flowering(self, date_str: str) -> None:
        self.flowering_dates.append(date_str)

    def add_pollinator(self, species: Species) -> None:
        if species not in self.pollinators:
            self.pollinators.append(species)
