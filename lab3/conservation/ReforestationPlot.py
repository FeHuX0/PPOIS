from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ReforestationPlot:
    plot_id: str
    habitat: Habitat
    planted_species: list[Plant] = field(default_factory=list)
    survival_rate: float = 0.0
    monitoring_notes: list[str] = field(default_factory=list)

    def add_plant(self, plant: Plant) -> None:
        self.planted_species.append(plant)

    def update_survival_rate(self, rate: float) -> None:
        self.survival_rate = rate
