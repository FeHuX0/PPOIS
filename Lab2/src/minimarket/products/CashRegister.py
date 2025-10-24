from __future__ import annotations
from dataclasses import dataclass, field
from typing import Any

@dataclass
class CashRegister:
    id: str = ''
    name: str = ''
    meta: dict = field(default_factory=dict)

    def scan(self, product: 'Product') -> str:
        return product.sku

    def print_receipt(self, receipt: 'Receipt') -> str:
        return f'Receipt {receipt.receipt_id}'
