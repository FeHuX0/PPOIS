from __future__ import annotations

from dataclasses import dataclass, field

from ecology.exceptions.PolicyConflictException import PolicyConflictException


@dataclass
class Ecosystem:
    name: str
    dominant_biome: Biome
    regions: list[Region] = field(default_factory=list)
    protected_areas: list[ProtectedArea] = field(default_factory=list)
    policies: list[EnvironmentalPolicy] = field(default_factory=list)

    def add_region(self, region: Region) -> None:
        if region not in self.regions:
            self.regions.append(region)

    def enforce_policy(self, policy: EnvironmentalPolicy) -> None:
        if policy in self.policies:
            raise PolicyConflictException("Policy already applied to ecosystem.")
        self.policies.append(policy)
