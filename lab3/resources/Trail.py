from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Trail:
    trail_id: str
    name: str
    difficulty: str
    length_km: float
    maintenance_tasks: list[str] = field(default_factory=list)

    def schedule_maintenance(self, task: str) -> None:
        self.maintenance_tasks.append(task)

    def update_difficulty(self, difficulty: str) -> None:
        self.difficulty = difficulty
