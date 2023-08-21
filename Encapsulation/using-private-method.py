#-------------------------using private method----------------

class MyClass:
    def __init__(self, value):
        self.__value = value

    def __private_method(self):
        print("This is a private method.")

    def public_method(self):
        print(f"This is a public method. Value: {self.__value}")
        self.__private_method()

obj = MyClass(42)
obj.public_method()

# Attempting to call a private method from outside the class will raise an error.
# obj.__private_method()  # This will raise an error.
