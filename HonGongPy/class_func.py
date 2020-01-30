class Student:
    # class variable
    count = 0
    students = []

    # class function
    @classmethod
    def print(cls):
        print("-----Student List-----")
        print("Name\tSum\tAverage")
        for student in cls.students:
            print(str(student))
        print("------- ------- -------")

    # instance function
    def __init__(self, name, korean, math):
        self.name = name
        self.korean = korean
        self.math = math
        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math

    def get_average(self):
        return self.get_sum() / 2

    def __str__(self):
        return "{}\t{}\t{}".format(
            self.name,
            self.get_sum(),
            self.get_average()
        )

# Student List Declare

Student("Jack", 87, 99)
Student("Sally", 32, 12)
Student("Lion", 1 ,5)
Student("Muzi", 23, 14)
Student("Con", 84, 33)

Student.print()