from __future__ import annotations

from dataclasses import dataclass

from ecology.exceptions.FundingApprovalException import FundingApprovalException


@dataclass
class FundingGrant:
    grant_id: str
    project: ConservationProject
    amount: float
    approved: bool = False
    sponsor: str = ""

    def approve(self) -> None:
        if self.approved:
            raise FundingApprovalException("Grant already approved.")
        self.approved = True

    def assign_sponsor(self, sponsor_name: str) -> None:
        self.sponsor = sponsor_name
