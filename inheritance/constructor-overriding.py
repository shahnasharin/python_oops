#--------------------------constructor overriding--------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Employee(Person):
    def __init__(self, name, age, emp_id):
        super().__init__(name, age)
        self.emp_id = emp_id

    def display_info(self):
        return f"{self.name}, {self.age} years old, Employee ID: {self.emp_id}"

employee = Employee("John", 30, "E12345")
print(employee.display_info())


# Output: John, 30 years old, Employee ID: E12345
