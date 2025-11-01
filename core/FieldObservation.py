from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class FieldObservation:
    observation_id: str
    observer: CitizenScientist
    species: Species
    region: Region
    observed_at: datetime
    notes: str

    def summarize(self) -> str:
        return f"{self.species.common_name} seen in {self.region.name}"

    def update_notes(self, new_notes: str) -> None:
        self.notes = new_notes
