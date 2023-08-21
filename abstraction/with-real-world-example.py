#----------------------------Abstraction with a Real-World Example--------------------------


from abc import ABC, abstractmethod

class Vehicle(ABC):
    def __init__(self, brand):
        self.brand = brand

    @abstractmethod
    def start_engine(self):
        pass

class Car(Vehicle):
    def start_engine(self):
        return f"{self.brand} car engine started."

class Motorcycle(Vehicle):
    def start_engine(self):
        return f"{self.brand} motorcycle engine started."

car = Car("Toyota")
motorcycle = Motorcycle("Honda")

print(car.start_engine())          # Output: Toyota car engine started.
print(motorcycle.start_engine())   # Output: Honda motorcycle engine started.
