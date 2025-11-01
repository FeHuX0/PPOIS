from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Survey:
    survey_id: str
    conducted_by: Researcher
    target_region: Region
    observations: list[FieldObservation] = field(default_factory=list)
    volunteers: list[Volunteer] = field(default_factory=list)

    def add_observation(self, observation: FieldObservation) -> None:
        self.observations.append(observation)

    def enroll_volunteer(self, volunteer: Volunteer) -> None:
        if volunteer not in self.volunteers:
            self.volunteers.append(volunteer)
