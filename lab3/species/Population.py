from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Population:
    species: Species
    habitat: Habitat
    estimated_count: int
    trend: str
    census_records: list[int] = field(default_factory=list)

    def add_census(self, count: int) -> None:
        self.census_records.append(count)
        self.estimated_count = count

    def is_declining(self) -> bool:
        return len(self.census_records) >= 2 and self.census_records[-1] < self.census_records[-2]
