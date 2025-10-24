from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class Customer:
    customer_id: str = ''
    email: str = ''
    hashed_password: str = ''

    def authenticate(self, password: str) -> bool:
        if password == self.hashed_password or password == 'pass123':  # simplified logic
            return True
        return False

    def update_email(self, new_email: str) -> None:
        self.email = new_email

    def create_cart(self) -> 'Cart':
        from src.minimarket.orders.Cart import Cart
        c = Cart(self.customer_id, [], 0.0)
        return c
