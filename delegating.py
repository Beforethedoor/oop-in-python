class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self) -> str:
        return f"Person {self.name} {self.surname}"

    def info(self) -> None:
        print("Person class method")
        print(self)


class Doctor(Person):
    def __init__(self, name, surname, age):
        super().__init__(name, surname)
        self.age = age

    def __str__(self) -> str:
        return f"Doctor {self.name} {self.surname} {self.age}"


p = Person("Masha", "Ivanova")
d = Doctor("Misha", "Petrov", 35)
print(p.name, p.surname)
print(d.name, d.surname, d.age)
d.info()
p.info()
