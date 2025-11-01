from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass
class IncidentReport:
    report_id: str
    description: str
    reported_by: ParkRanger
    occurred_at: datetime
    severity: str

    def escalate(self, new_severity: str) -> None:
        self.severity = new_severity

    def short_summary(self) -> str:
        return f"{self.severity}: {self.description[:40]}"
