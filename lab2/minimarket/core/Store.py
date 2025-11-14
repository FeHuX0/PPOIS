from __future__ import annotations

from dataclasses import dataclass, field

from minimarket.core.Department import Department
from minimarket.inventory.InventoryRecord import InventoryRecord
from minimarket.people.Employee import Employee


@dataclass
class Store:
    name: str
    departments: list[Department] = field(default_factory=list)
    employees: list[Employee] = field(default_factory=list)
    inventory_records: list[InventoryRecord] = field(default_factory=list)

    def add_department(self, department: Department) -> None:
        if department not in self.departments:
            self.departments.append(department)

    def hire(self, employee: Employee) -> None:
        if employee not in self.employees:
            self.employees.append(employee)

    def add_inventory_record(self, record: InventoryRecord) -> None:
        self.inventory_records.append(record)

    def total_products(self) -> int:
        return sum(dept.count_products() for dept in self.departments)
