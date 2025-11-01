from __future__ import annotations

from dataclasses import dataclass


@dataclass
class BiodiversityIndex:
    region: Region
    richness_score: float
    evenness_score: float
    threatened_species_count: int

    def update_scores(self, richness: float, evenness: float) -> None:
        self.richness_score = richness
        self.evenness_score = evenness

    def is_declining(self, threshold: float = 0.1) -> bool:
        return self.richness_score < threshold
