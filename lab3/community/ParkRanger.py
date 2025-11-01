from __future__ import annotations

from dataclasses import dataclass, field

from ecology.exceptions.FundingApprovalException import FundingApprovalException


@dataclass
class ParkRanger:
    ranger_id: str
    name: str
    assigned_region: Region
    patrol_routes: list[str] = field(default_factory=list)
    incident_reports: list[IncidentReport] = field(default_factory=list)

    def add_patrol_route(self, route: str) -> None:
        self.patrol_routes.append(route)

    def submit_incident(self, incident: IncidentReport) -> None:
        if not incident.description:
            raise FundingApprovalException("Incident must include description.")
        self.incident_reports.append(incident)
