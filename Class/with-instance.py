#------------------------clas with instance variable----------------

class Employee:
    num_employees = 0  # Class variable

    def __init__(self, name, salary):
        self.name = name  # Instance variable
        self.salary = salary
        Employee.num_employees += 1

    def display_info(self):
        print(f"{self.name} earns ${self.salary} per year.")

employee1 = Employee("John", 50000)
employee2 = Employee("Jane", 60000)

print(f"Total employees: {Employee.num_employees}")  # Output: Total employees: 2
employee1.display_info()  # Output: John earns $50000 per year.
employee2.display_info()  # Output: Jane earns $60000 per year.
