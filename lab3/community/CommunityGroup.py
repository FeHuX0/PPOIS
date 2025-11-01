from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class CommunityGroup:
    group_id: str
    name: str
    members: list[Volunteer] = field(default_factory=list)
    initiatives: list[EcoCampaign] = field(default_factory=list)
    partner_organizations: list[str] = field(default_factory=list)

    def add_member(self, volunteer: Volunteer) -> None:
        if volunteer not in self.members:
            self.members.append(volunteer)

    def launch_campaign(self, campaign: EcoCampaign) -> None:
        self.initiatives.append(campaign)
