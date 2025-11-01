from __future__ import annotations

from dataclasses import dataclass, field

from ecology.exceptions.PollutionLevelException import PollutionLevelException


@dataclass
class RecyclingProgram:
    program_id: str
    community: CommunityGroup
    collected_materials_tons: float
    drop_off_sites: list[str] = field(default_factory=list)
    monthly_reports: list[str] = field(default_factory=list)

    def add_drop_off_site(self, site: str) -> None:
        if site not in self.drop_off_sites:
            self.drop_off_sites.append(site)

    def submit_report(self, report: str) -> None:
        if not report:
            raise PollutionLevelException("Report content required.")
        self.monthly_reports.append(report)
