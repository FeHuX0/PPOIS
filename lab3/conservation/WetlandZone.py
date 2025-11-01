from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class WetlandZone:
    zone_id: str
    region: Region
    water_sources: list[str] = field(default_factory=list)
    protected_species: list[Species] = field(default_factory=list)
    restoration_plans: list[RestorationPlan] = field(default_factory=list)

    def add_water_source(self, name: str) -> None:
        if name not in self.water_sources:
            self.water_sources.append(name)

    def link_restoration(self, plan: RestorationPlan) -> None:
        if plan not in self.restoration_plans:
            self.restoration_plans.append(plan)
