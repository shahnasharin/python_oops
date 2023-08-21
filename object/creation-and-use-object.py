#-------------creating and usinng of an object----------------


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

# Creating objects (instances) of the Person class.
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Using objects' methods and properties.
person1.introduce()  # Output: Hi, I'm Alice and I'm 30 years old.
person2.introduce()  # Output: Hi, I'm Bob and I'm 25 years old.
