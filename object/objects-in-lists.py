#-----------------------------using Objects in Lists---------------------------------


class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

student1 = Student("Alice", 20)
student2 = Student("Bob", 22)
student3 = Student("Charlie", 19)

student_list = [student1, student2, student3]

for student in student_list:
    print(f"Name: {student.name}, Age: {student.age}")
