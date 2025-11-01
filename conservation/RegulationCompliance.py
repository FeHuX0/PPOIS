from __future__ import annotations

from dataclasses import dataclass, field

from ecology.exceptions.ComplianceBreachException import ComplianceBreachException


@dataclass
class RegulationCompliance:
    compliance_id: str
    project: ConservationProject
    regulations_checked: list[str] = field(default_factory=list)
    breaches_found: list[str] = field(default_factory=list)

    def record_check(self, regulation: str) -> None:
        self.regulations_checked.append(regulation)

    def add_breach(self, breach: str) -> None:
        if breach in self.breaches_found:
            raise ComplianceBreachException("Breach already recorded.")
        self.breaches_found.append(breach)
