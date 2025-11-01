from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class EcoEducator:
    educator_id: str
    name: str
    specializations: list[str] = field(default_factory=list)
    hosted_trainings: list[TrainingSession] = field(default_factory=list)
    outreach_materials: list[str] = field(default_factory=list)

    def host_training(self, session: TrainingSession) -> None:
        self.hosted_trainings.append(session)

    def add_material(self, material: str) -> None:
        self.outreach_materials.append(material)
