"""
    __lt__ describes less than operator(<)
    __le__ descries less than or equal to (<=)
    __gt__ describes greater than (>)
    __ge__ describes greater than or equal to (>=)
    __eq__ describes equality operator(==)
    __ne__ describes not equal to operator(!=)
"""


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def area(self):
        return self.a * self.b

    def __eq__(self, other):
        if isinstance(other, Rectangle):
            return self.a == other.a and self.b == other.b

    def __lt__(self, other):
        if isinstance(other, (int, float)):
            return self.area < other
        if isinstance(other, Rectangle):
            return self.area < other.area

    def __le__(self, other):
        return self < other or self == other


f = Rectangle(1, 2)
s = Rectangle(4, 5)

print(s == f)
print(f < s)
print(f <= s)
print(f > s)
print(f >= s)
