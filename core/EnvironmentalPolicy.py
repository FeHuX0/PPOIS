from __future__ import annotations

from dataclasses import dataclass, field

from ecology.exceptions.ComplianceBreachException import ComplianceBreachException


@dataclass
class EnvironmentalPolicy:
    policy_id: str
    title: str
    enforced_by: CommunityGroup
    compliance_requirements: list[str] = field(default_factory=list)
    compliant_entities: list[str] = field(default_factory=list)

    def add_requirement(self, requirement: str) -> None:
        if requirement not in self.compliance_requirements:
            self.compliance_requirements.append(requirement)

    def mark_compliant(self, entity: str) -> None:
        if entity in self.compliant_entities:
            raise ComplianceBreachException("Entity already marked as compliant.")
        self.compliant_entities.append(entity)
