class Student:
    def __init__(self, name):
        self.name = name

    def __iter__(self):
        self.index = 0
        return self

    def __next__(self):
        if self.index >= len(self.name):
            raise StopIteration
        letter = self.name[self.index]
        self.index += 1
        return letter


s = Student("Masha")

for i in s:
    print(i)
