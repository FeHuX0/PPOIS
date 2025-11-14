from __future__ import annotations

from dataclasses import dataclass, field
from datetime import date

from minimarket.people.Employee import Employee


@dataclass
class ShiftRoster:
    roster_date: date
    assignments: dict[str, list[Employee]] = field(default_factory=dict)

    def assign(self, area: str, employee: Employee) -> None:
        self.assignments.setdefault(area, [])
        if employee not in self.assignments[area]:
            self.assignments[area].append(employee)
