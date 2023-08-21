#-----------multiple objects in same classs---------------------------

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model

    def info(self):
        return f"{self.make} {self.model}"

car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Accord")

print(car1.info())  # Output: Toyota Camry
print(car2.info())  # Output: Honda Accord
