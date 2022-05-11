class Square:
    def __init__(self, side):
        self.__side = side
        self.__area = None

    @property
    def side(self):
        return self.__side

    @side.setter
    def side(self, value):
        self.__side = value
        self.__area = None

    @property
    def area(self):
        if not self.__area:
            self.__area = self.__side ** 2
        return self.__area


s = Square(side=4)
print(s.side)
print(s.area)

s.side = 6
print(s.side)
print(s.area)
