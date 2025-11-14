from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TrainingModule:
    module_id: str
    title: str
    duration_minutes: int
    requirements: list[str] = field(default_factory=list)

    def add_requirement(self, requirement: str) -> None:
        if requirement not in self.requirements:
            self.requirements.append(requirement)
