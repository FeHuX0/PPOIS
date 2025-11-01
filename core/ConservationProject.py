from __future__ import annotations

from dataclasses import dataclass, field

from ecology.exceptions.RestorationDelayException import RestorationDelayException


@dataclass
class ConservationProject:
    project_id: str
    name: str
    lead_researcher: Researcher
    habitats: list[Habitat] = field(default_factory=list)
    actions: list[ConservationAction] = field(default_factory=list)
    delayed: bool = False

    def add_action(self, action: ConservationAction) -> None:
        self.actions.append(action)

    def flag_delay(self) -> None:
        if self.delayed:
            raise RestorationDelayException("Project delay already recorded.")
        self.delayed = True
