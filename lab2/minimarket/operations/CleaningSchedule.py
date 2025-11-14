from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class CleaningSchedule:
    area: str
    slots: list[datetime] = field(default_factory=list)
    completed: list[datetime] = field(default_factory=list)

    def add_slot(self, slot: datetime) -> None:
        if slot not in self.slots:
            self.slots.append(slot)

    def mark_completed(self, slot: datetime) -> None:
        if slot in self.slots and slot not in self.completed:
            self.completed.append(slot)
