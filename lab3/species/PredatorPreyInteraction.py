from __future__ import annotations

from dataclasses import dataclass


@dataclass
class PredatorPreyInteraction:
    predator: Species
    prey: Species
    frequency_per_month: float
    observation_location: Region

    def adjust_frequency(self, new_value: float) -> None:
        self.frequency_per_month = new_value

    def describe(self) -> str:
        return f"{self.predator.common_name} hunts {self.prey.common_name}"
