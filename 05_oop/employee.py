"""Dataclasses, class methods and sorting objects."""

from dataclasses import dataclass


@dataclass
class Employee:
    name: str
    department: str
    salary: float

    @classmethod
    def from_csv_row(cls, row: str) -> "Employee":
        name, department, salary = (part.strip() for part in row.split(","))
        return cls(name, department, float(salary))

    def give_raise(self, percent: float) -> None:
        self.salary *= 1 + percent / 100


def average_salary_by_department(employees: list[Employee]) -> dict[str, float]:
    totals: dict[str, list[float]] = {}
    for employee in employees:
        totals.setdefault(employee.department, []).append(employee.salary)
    return {dept: sum(values) / len(values) for dept, values in totals.items()}


if __name__ == "__main__":
    rows = ["Ravi, DevOps, 90000", "Meera, DevOps, 110000", "John, QA, 70000"]
    staff = [Employee.from_csv_row(row) for row in rows]
    staff[2].give_raise(10)
    for employee in sorted(staff, key=lambda e: e.salary, reverse=True):
        print(employee)
    print(average_salary_by_department(staff))
