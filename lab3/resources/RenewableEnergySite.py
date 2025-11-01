from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class RenewableEnergySite:
    site_id: str
    type: str
    capacity_mw: float
    supporting_projects: list[ConservationProject] = field(default_factory=list)
    environmental_benefits: list[str] = field(default_factory=list)

    def link_project(self, project: ConservationProject) -> None:
        if project not in self.supporting_projects:
            self.supporting_projects.append(project)

    def add_benefit(self, benefit: str) -> None:
        self.environmental_benefits.append(benefit)
