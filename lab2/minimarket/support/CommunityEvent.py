from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class CommunityEvent:
    event_id: str
    topic: str
    attendees: list[str] = field(default_factory=list)

    def register(self, name: str) -> None:
        if name not in self.attendees:
            self.attendees.append(name)
