from __future__ import annotations

from dataclasses import dataclass


@dataclass
class AssessmentResult:
    employee_id: str
    module_id: str
    score: float
    passed: bool = False
    attempts: int = 0

    def record_attempt(self, score: float, passing_score: float) -> None:
        self.score = score
        self.attempts += 1
        self.passed = score >= passing_score
