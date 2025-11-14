from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class IssueTicket:
    ticket_id: str
    category: str
    status: str = "open"
    messages: list[str] = field(default_factory=list)

    def add_message(self, message: str) -> None:
        self.messages.append(message)
