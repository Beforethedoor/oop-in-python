class Builder:
    def __init__(self, rank) -> None:
        self.rank = rank


class Doctor:
    def __init__(self, degree) -> None:
        self.degree = degree


class Person(Builder, Doctor):
    def __init__(self, rank, degree) -> None:
        super().__init__(rank)
        Doctor.__init__(self, degree)

    def __str__(self) -> str:
        return f"Person {self.rank} {self.degree}"


print(Person.__mro__)
p = Person(4, "spec")
print(p)
