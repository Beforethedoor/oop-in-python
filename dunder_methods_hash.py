class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return isinstance(other, Point) \
            and self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x, self.y))


p1 = Point(3, 4)
p2 = Point(3, 4)

print(p1 == p2)
print(hash(p1), hash(p2))
print(hash(p1) == hash(p2))
