from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class MentorshipSession:
    mentor_id: str
    mentee_id: str
    topics: list[str] = field(default_factory=list)
    completed: bool = False

    def add_topic(self, topic: str) -> None:
        if topic not in self.topics:
            self.topics.append(topic)

    def complete(self) -> None:
        self.completed = True
