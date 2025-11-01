from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class RestorationPlan:
    plan_id: str
    project: ConservationProject
    steps: list[str] = field(default_factory=list)
    targeted_species: list[Species] = field(default_factory=list)
    completion_ratio: float = 0.0

    def add_step(self, step: str) -> None:
        self.steps.append(step)

    def update_completion(self, ratio: float) -> None:
        self.completion_ratio = max(0.0, min(1.0, ratio))
