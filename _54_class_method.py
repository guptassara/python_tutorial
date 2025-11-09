# Class methods = Allow operations related to the class itself
#                 Take (cls) as the first parameter, which represents the class itself.


class Student:
    count = 0
    total_cgpa = 0

    def __init__(self, name, cgpa) -> None:
        self.name = name
        self.cgpa = cgpa
        Student.count += 1
        Student.total_cgpa += cgpa

    # INSTANCE METHOD
    def get_info(self):
        return f"{self.name} {self.cgpa}"

    @classmethod
    def get_count(cls):
        return f"Total # of students: {cls.count}"

    @classmethod
    def get_average_cgpa(cls):
        if cls.count == 0:
            return 0
        else:
            return f"Average cgpa is: {cls.total_cgpa / cls.count: .2f}"


student1 = Student("Venti", 5.0)
student2 = Student("Zhongli", 7.0)
student3 = Student("Ei", 8.5)
student4 = Student("Nahida", 10)
student5 = Student("Furina", 6.5)
student6 = Student("Mavuika", 10)
student7 = Student("Columbina", 7.8)
student8 = Student("Tsaritsa", 8.9)

print(Student.get_count())
print(Student.get_average_cgpa())
