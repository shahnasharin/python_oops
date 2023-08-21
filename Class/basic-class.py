#---------------------basic class ----------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, I'm {self.name} and I'm {self.age} years old.")

person = Person("Alice", 30)
person.introduce()  # Output: Hi, I'm Alice and I'm 30 years old.
