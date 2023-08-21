#-----------------------------using private-------------------------------------

class Person:
    def __init__(self, name, age):
        self.__name = name  # Private variable
        self.__age = age    # Private variable

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age >= 0:
            self.__age = age
        else:
            print("Age cannot be negative.")

person = Person("Alice", 30)

# Accessing private variables through getter and setter methods.
print(person.get_name())  # Output: Alice
print(person.get_age())   # Output: 30

person.set_name("Bob")
person.set_age(-5)  # This will print "Age cannot be negative."

# Attempting to access private variables directly will raise an error.
# print(person.__name)  # This will raise an error.
