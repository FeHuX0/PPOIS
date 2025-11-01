from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ClimateInitiative:
    initiative_id: str
    name: str
    lead_group: CommunityGroup
    measured_metrics: list[str] = field(default_factory=list)
    achieved_targets: list[str] = field(default_factory=list)

    def add_metric(self, metric: str) -> None:
        self.measured_metrics.append(metric)

    def record_target(self, target: str) -> None:
        self.achieved_targets.append(target)
