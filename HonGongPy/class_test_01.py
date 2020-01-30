class Student:
    def __init__ (self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

students = [
    Student("S1",1,2,3,4),
    Student("S2",3,4,5,6),
    Student("S3",5,3,2,1)
]

print(students[0].name)
print(students[0].korean)
print(students[0].math)
print(students[0].english)
print(students[0].science)