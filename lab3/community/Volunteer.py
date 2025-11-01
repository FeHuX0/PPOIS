from __future__ import annotations

from dataclasses import dataclass, field

from ecology.exceptions.VolunteerRegistrationException import VolunteerRegistrationException


@dataclass
class Volunteer:
    volunteer_id: str
    name: str
    skills: list[str] = field(default_factory=list)
    assigned_projects: list[ConservationProject] = field(default_factory=list)
    active: bool = True

    def add_skill(self, skill: str) -> None:
        if skill not in self.skills:
            self.skills.append(skill)

    def join_project(self, project: ConservationProject) -> None:
        if not self.active:
            raise VolunteerRegistrationException("Inactive volunteer cannot join projects.")
        self.assigned_projects.append(project)
