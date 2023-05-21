class StringDescriptor:
    def __set_name__(self, owner_class, property_name) -> None:
        self.property_name = property_name

    def __set__(self, instance, value) -> None:
        if not isinstance(value, str):
            raise ValueError(
                f"{self.property_name} must be str "
                f"but {type(value).__name__} was passed."
            )
        instance.__dict__[self.property_name] = value

    def __get__(self, instance, owner) -> str:
        if instance is None:
            return self
        return instance.__dict__.get(self.property_name, None)


class Person:
    name = StringDescriptor()
    surname = StringDescriptor()


p = Person()
print(p.name)
p.name = "asdf"
print(p.name)
# p.name = 1234  # ValueError
