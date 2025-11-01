from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class FoodWeb:
    habitat: Habitat
    producers: list[Species] = field(default_factory=list)
    consumers: list[Species] = field(default_factory=list)
    apex_predators: list[Species] = field(default_factory=list)

    def add_producer(self, species: Species) -> None:
        if species not in self.producers:
            self.producers.append(species)

    def total_members(self) -> int:
        return len(self.producers) + len(self.consumers) + len(self.apex_predators)
