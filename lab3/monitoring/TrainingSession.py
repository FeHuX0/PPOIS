from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TrainingSession:
    session_id: str
    topic: str
    instructor: EcoEducator
    attendees: list[Volunteer] = field(default_factory=list)
    scheduled_date: str = ""

    def add_attendee(self, volunteer: Volunteer) -> None:
        if volunteer not in self.attendees:
            self.attendees.append(volunteer)

    def reschedule(self, new_date: str) -> None:
        self.scheduled_date = new_date
