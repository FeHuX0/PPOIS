from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class GeneticSample:
    sample_id: str
    species: Species
    collected_at: datetime
    collector: Researcher
    storage_location: str

    def relocate(self, new_location: str) -> None:
        self.storage_location = new_location

    def age_days(self, now: datetime) -> int:
        return (now - self.collected_at).days
