class Example:
    def hello():
        "Вызывается только от класса"
        print("hello world!")

    def instance_hello(self):
        "Вызывается только от объекта класса"
        print("hello world from instance method!")

    @staticmethod
    def static_hello():
        "Вызывается от класса и от объекта класса"
        print("hellow world from static method!")

    @classmethod
    def class_hello(cls):
        "Вызывается только от класса"
        print("hello world form class method!")


obj = Example()

# work
Example.hello()
try:
    # error
    obj.hello()
except TypeError as e:
    print(e)

try:
    # error
    Example.instance_hello()
except TypeError as e:
    print(e)
# work
obj.instance_hello()

# work
Example.static_hello()
# work
obj.static_hello()

# work
Example.class_hello()
# work
obj.class_hello()
