from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class VisitorCenter:
    center_id: str
    name: str
    region: Region
    exhibits: list[str] = field(default_factory=list)
    programs: list[EcoCampaign] = field(default_factory=list)

    def add_exhibit(self, exhibit: str) -> None:
        self.exhibits.append(exhibit)

    def host_program(self, campaign: EcoCampaign) -> None:
        self.programs.append(campaign)
