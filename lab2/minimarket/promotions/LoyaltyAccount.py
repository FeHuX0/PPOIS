from __future__ import annotations

from dataclasses import dataclass, field

from minimarket.promotions.Reward import Reward


@dataclass
class LoyaltyAccount:
    account_id: str
    points: int = 0
    tier: str = "bronze"
    transactions: list[str] = field(default_factory=list)

    def add_points(self, amount: int, reason: str) -> None:
        self.points += amount
        self.transactions.append(f"+{amount} {reason}")

    def redeem_reward(self, reward: Reward) -> None:
        if reward.cost_points > self.points:
            raise ValueError("Insufficient points for reward redemption.")
        self.points -= reward.cost_points
        self.transactions.append(f"-{reward.cost_points} {reward.name}")

    def qualify_for_tier(self, thresholds: dict[str, int]) -> None:
        for tier, min_points in sorted(thresholds.items(), key=lambda item: item[1]):
            if self.points >= min_points:
                self.tier = tier
