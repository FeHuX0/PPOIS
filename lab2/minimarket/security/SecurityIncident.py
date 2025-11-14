from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class SecurityIncident:
    incident_id: str
    description: str
    severity: str = "low"
    resolved: bool = False
    timeline: list[str] = field(default_factory=list)

    def escalate(self, note: str) -> None:
        self.severity = "high"
        self.timeline.append(note)

    def close(self) -> None:
        self.resolved = True
