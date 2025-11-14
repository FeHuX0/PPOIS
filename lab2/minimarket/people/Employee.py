from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class Employee:
    employee_id: str
    name: str
    role: str
    active: bool = True
    shifts: list[str] = field(default_factory=list)

    def assign_shift(self, shift_id: str) -> None:
        if shift_id not in self.shifts:
            self.shifts.append(shift_id)

    def deactivate(self) -> None:
        self.active = False
