from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class TaskSchedule:
    schedule_id: str
    responsible: ParkRanger
    tasks: list[str] = field(default_factory=list)
    due_dates: list[str] = field(default_factory=list)

    def add_task(self, task: str, due_date: str) -> None:
        self.tasks.append(task)
        self.due_dates.append(due_date)

    def clear_tasks(self) -> None:
        self.tasks.clear()
        self.due_dates.clear()
