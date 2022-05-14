"""
    Если в классе не определен ни метод __len__ ни метод __bool__
    питон всегда возвращает True
"""


class Point:
    """
        Когда в классе не определен метод __bool__ питон
        ссылается на метод __len__
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print("colled __len__ method")
        return abs(self.x - self.y)


p1 = Point(1, 2)
p2 = Point(1, 1)

print(bool(p1))
# len равен 0 поэтому возвращается False
print(bool(p2))


class Point:
    """
        Когда в классе не определен метод __bool__ питон
        ссылается на метод __len__
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __len__(self):
        print("colled __len__ method")
        return abs(self.x - self.y)

    def __bool__(self):
        print("colled __bool__")
        return self.x != 0 or self.y != 0


p1 = Point(1, 2)
p2 = Point(1, 1)
p3 = Point(0, 0)

print(bool(p1))
print(bool(p2))
# вернется False т.к. не выполнится условие
print(bool(p3))
