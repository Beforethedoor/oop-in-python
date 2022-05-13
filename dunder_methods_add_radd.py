# Dunder methods __add__ __mul__ __sub__ __truediv__


class BankAccount:
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance

    def __add__(self, other):
        print("__add__ colled")
        if isinstance(other, (int, float)):
            return self.balance + other
        if isinstance(other, BankAccount):
            return self.balance + other.balance
        else:
            raise NotImplemented

    def __radd__(self, other):
        print("__radd__ colled")
        return self+other


m = BankAccount("Misha", 100)
t = BankAccount("Tanya", 100)

print(m+12)
print(12+m)
print(m+t)
