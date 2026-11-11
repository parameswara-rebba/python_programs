"""A bank account class: encapsulation, validation and custom exceptions."""


class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, owner: str, balance: float = 0.0):
        if balance < 0:
            raise ValueError("opening balance cannot be negative")
        self.owner = owner
        self._balance = balance
        self._transactions: list[tuple[str, float]] = []

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self._balance += amount
        self._transactions.append(("deposit", amount))

    def withdraw(self, amount: float) -> None:
        if amount <= 0:
            raise ValueError("withdrawal must be positive")
        if amount > self._balance:
            raise InsufficientFundsError(
                f"cannot withdraw {amount:.2f}; balance is {self._balance:.2f}"
            )
        self._balance -= amount
        self._transactions.append(("withdraw", amount))

    def statement(self) -> str:
        lines = [f"Statement for {self.owner}"]
        lines += [f"  {kind:<8} {amount:>10.2f}" for kind, amount in self._transactions]
        lines.append(f"  {'balance':<8} {self._balance:>10.2f}")
        return "\n".join(lines)

    def __repr__(self) -> str:
        return f"BankAccount(owner={self.owner!r}, balance={self._balance:.2f})"


if __name__ == "__main__":
    account = BankAccount("Asha", 100)
    account.deposit(50)
    account.withdraw(30)
    print(account.statement())
    try:
        account.withdraw(1000)
    except InsufficientFundsError as error:
        print("Error:", error)
