class Vector:
    def __init__(self, *args):
        self.val = list(args)

    def __repr__(self) -> str:
        return str(self.val)

    def __getitem__(self, idx):
        if 0 <= idx < len(self.val):
            return self.val[idx]
        else:
            raise IndexError("Индекс выходит за границы колекции")

    def __setitem__(self, idx, val):
        if 0 <= idx < len(self.val):
            self.val[idx] = val
        elif idx > len(self.val):
            diff = idx - len(self.val) + 1
            self.val.extend([None]*diff)
            print(self.val)
            self.val[idx] = val
        else:
            raise IndexError("Идекс выходит за границы колекции")

    def __delitem__(self, idx):
        if 0 <= idx < len(self.val):
            del self.val[idx]
        else:
            raise IndexError("Идекс выходит за границы колекции")


v1 = Vector(1, 2, 4, 5, 6, 6, 10)
print(v1)
print(v1[0])
v1[15] = 100
print(v1)
print(v1[15])
del v1[15]
print(v1)
print(v1[15])
