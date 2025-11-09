# class variable = shared among all instances of a class
#                  Defined outside the constructor
#                  Allow you to share data among all objects created for that class


class Student:
    class_year = 2028  # class variable
    num_student = 0

    def __init__(self, name, age) -> None:
        self.name = name  # instance variable
        self.age = age
        Student.num_student += 1


student1 = Student("Venti", 2600)
student2 = Student("Zhongli", 6000)
student3 = Student("Raiden", 2000)
student4 = Student("Nahida", 500)
student5 = Student("Furina", 500)
student6 = Student("Mavuika", 30)

print(student1.name)
print(student1.age)
print(Student.class_year)  # access class variable by class name and not instance

print(student2.name)
print(student2.age)

print(student3.name)
print(student3.age)

print(student4.name)
print(student4.age)

print(student5.name)
print(student5.age)

print(student6.name)
print(student6.age)

print(f"Number of student are: {Student.num_student}")

print(f"My graduating class of {Student.class_year} has {Student.num_student} students")
