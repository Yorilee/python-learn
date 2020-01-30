class Student:
    def __init__(self, name, korean, math):
        self.name = name
        self.korean = korean
        self.math = math
    
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

# 학생 리스트 선언
students = [
    Student("예나", 89, 90),
    Student("혜리", 99, 43)
]

print("이름","총점","평균", sep="\t")

for student in students:
    print(str(student))

