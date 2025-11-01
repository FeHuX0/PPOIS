from __future__ import annotations

from dataclasses import dataclass, field


@dataclass
class ImpactAssessment:
    assessment_id: str
    project: ConservationProject
    indicators: list[str] = field(default_factory=list)
    scores: list[float] = field(default_factory=list)
    evaluator: Researcher | None = None

    def add_indicator(self, indicator: str, score: float) -> None:
        self.indicators.append(indicator)
        self.scores.append(score)

    def average_score(self) -> float:
        if not self.scores:
            return 0.0
        return sum(self.scores) / len(self.scores)
