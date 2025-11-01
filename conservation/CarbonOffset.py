from __future__ import annotations

from dataclasses import dataclass


@dataclass
class CarbonOffset:
    offset_id: str
    project: ConservationProject
    tons_co2e: float
    verified_by: str
    issue_year: int

    def update_verifier(self, verifier: str) -> None:
        self.verified_by = verifier

    def increment_offset(self, amount: float) -> None:
        self.tons_co2e += amount
