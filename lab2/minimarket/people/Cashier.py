from __future__ import annotations

from dataclasses import dataclass, field

from minimarket.exceptions.UnauthorizedDiscountException import UnauthorizedDiscountException
from minimarket.people.Employee import Employee


@dataclass
class Cashier:
    employee: Employee
    registers_handled: list[str] = field(default_factory=list)
    voided_transactions: list[str] = field(default_factory=list)

    def assign_register(self, register_id: str) -> None:
        if register_id not in self.registers_handled:
            self.registers_handled.append(register_id)

    def void_transaction(self, receipt_id: str, reason: str | None = None) -> None:
        if reason is None:
            raise UnauthorizedDiscountException("A reason is required to void a transaction.")
        self.voided_transactions.append(receipt_id)
