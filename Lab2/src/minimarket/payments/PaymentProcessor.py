from __future__ import annotations
from src.minimarket.core.payment import PaymentGateway
from dataclasses import dataclass, field
from typing import Any

@dataclass
class PaymentProcessor:
    name: str = ''
    supported_cards: list = field(default_factory=list)
    fees_percent: float = 0.0
    gateway: 'src.minimarket.core.payment.PaymentGateway' = None

    def process(self, source: dict, amount: float) -> bool:
        if self.gateway is None:
            # fallback: try to use source object if it has charge
            if hasattr(source, 'charge'):
                return source.charge(amount)
            return False
        return self.gateway.process_payment(source, amount)

    def fee(self, amount: float) -> float:
        return amount * (self.fees_percent / 100)

    def supports_card(self, card: 'Card') -> bool:
        return True