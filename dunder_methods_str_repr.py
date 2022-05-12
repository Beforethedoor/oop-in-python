class Lion:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        "Работает для отображения имени объекта в системе"
        return f"The object Lion - {self.name}"

    def __sts___(self):
        "Работает при вызове методов print() и str()"
        return f"Lion - {self.name}"


o = Lion(name="Valera")
print(o)
