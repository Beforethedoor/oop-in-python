class Rectangle:
    __slots__ = ("__width", "heigth")

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, val):
        self.__width = val


class Square(Rectangle):
    """
    При наследовании __slots__ в потомке не создается,
    не смотря на то что он есть в родителе
    """
    def __init__(self, width, height):
        super().__init__(width, height)


s = Square(4, 4)
print(s.__dict__)
print(s.width)
