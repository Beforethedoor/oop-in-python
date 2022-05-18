from timeit import timeit


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


class PointSlot:
    __slots__ = ("x", "y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


# Класс без определения __slots__ занимает больше памяти
p = Point(1, 2)
print(p.__sizeof__(), p.__dict__.__sizeof__())
# Класс с __slots__ не содержит __dict__
s = PointSlot(1, 2)
print(p.__sizeof__())


def make_c1():
    c = Point(1, 2)
    c.x = 100
    c.x
    del c.x


def make_c2():
    c = PointSlot(1, 2)
    c.x = 100
    c.x
    del c.x


# Класс с определенным __slots__ работает быстрее
print(f"Время работы объекта класса Point {timeit(make_c1)}")
print(f"Время работы объекта класса PointSlot {timeit(make_c2)}")


# В объект с определенным __slots__ нельзя добавлять новые поля
p.z = 100
s.z = 100
