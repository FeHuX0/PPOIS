
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Protocol, Any

class PaymentGateway(ABC):
    """Abstract interface for payment gateways.

    Implementations should be interchangeable and only depend on the abstract
    methods below. Use composition to provide a PaymentGateway to higher-level
    services (do not inherit domain classes from this interface).
    """

    @abstractmethod
    def process_payment(self, source: dict, amount: float, metadata: dict | None = None) -> bool:
        """Process a payment.

        source: abstract payment source (card data, wallet id, token, etc.)
        amount: amount to charge (in base currency)
        metadata: optional additional data

        Returns True on success, False on failure.
        """
        raise NotImplementedError
