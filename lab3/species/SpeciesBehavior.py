from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class SpeciesBehavior:
    species: Species
    behaviors: list[str] = field(default_factory=list)
    mating_patterns: list[str] = field(default_factory=list)
    seasonal_variations: list[str] = field(default_factory=list)

    def add_behavior(self, behavior: str) -> None:
        self.behaviors.append(behavior)

    def record_seasonal_change(self, description: str) -> None:
        self.seasonal_variations.append(description)
