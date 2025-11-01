from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class EcoCampaign:
    campaign_id: str
    organizer: CommunityGroup
    target_audience: str
    scheduled_events: list[EnvironmentalEvent] = field(default_factory=list)
    sponsors: list[str] = field(default_factory=list)

    def add_event(self, event: EnvironmentalEvent) -> None:
        self.scheduled_events.append(event)

    def add_sponsor(self, sponsor: str) -> None:
        if sponsor not in self.sponsors:
            self.sponsors.append(sponsor)
