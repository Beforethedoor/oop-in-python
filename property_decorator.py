class BankAccount:

    def __init__(self, name, balance):
        self.name = name
        self.__balance = balance

    @property
    def balance(self) -> int:
        return self.__balance

    @balance.setter
    def balance(self, value: int) -> None:
        if not isinstance(value, int):
            raise ValueError("Value must be integer")
        self.__balance = value

    @balance.deleter
    def balance(self) -> None:
        del self.__balance


h = BankAccount("Mike", 100)

# Print 100
print(h.balance)

h.balance = 200
# Print 200
print(h.balance)

del h.balance
# AttributeError
print(h.balance)
