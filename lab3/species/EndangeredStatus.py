from __future__ import annotations

from dataclasses import dataclass


@dataclass
class EndangeredStatus:
    status: str
    legal_protection: str
    population_threshold: int
    review_date: str

    def requires_intervention(self) -> bool:
        return self.status.lower() in {"endangered", "critically endangered"}

    def update_status(self, new_status: str, threshold: int) -> None:
        self.status = new_status
        self.population_threshold = threshold
