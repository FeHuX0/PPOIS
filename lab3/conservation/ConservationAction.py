from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ConservationAction:
    action_id: str
    description: str
    scheduled_for: str
    responsible_team: CommunityGroup
    target_species: list[Species] = field(default_factory=list)

    def add_target_species(self, species: Species) -> None:
        if species not in self.target_species:
            self.target_species.append(species)

    def reschedule(self, new_date: str) -> None:
        self.scheduled_for = new_date
