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

    def __eq__(self, value):
        if not isinstance(value, Student):
            raise TypeError("Student 클래스의 인스턴스만 비교할 수 있습니다.")
        return self.get_sum() == value.get_sum()
    def __ne__(self, value):
        if not isinstance(value, Student):
            raise TypeError("Student 클래스의 인스턴스만 비교할 수 있습니다.")
        return self.get_sum() != value.get_sum()
    def __gt__(self, value):
        if not isinstance(value, Student):
            raise TypeError("Student 클래스의 인스턴스만 비교할 수 있습니다.")
        return self.get_sum() > value.get_sum()
    def __ge__(self, value):
        if not isinstance(value, Student):
            raise TypeError("Student 클래스의 인스턴스만 비교할 수 있습니다.")
        return self.get_sum() >= value.get_sum()
    def __lt__(self, value):
        if not isinstance(value, Student):
            raise TypeError("Student 클래스의 인스턴스만 비교할 수 있습니다.")
        return self.get_sum() < value.get_sum()
    def __le__(self, value):
        if not isinstance(value, Student):
            raise TypeError("Student 클래스의 인스턴스만 비교할 수 있습니다.")
        return self.get_sum() <= value.get_sum()
    
# 학생 리스트 선언
students = [
    Student("예나", 89, 90),
    Student("혜리", 99, 43)
]

print("이름","총점","평균", sep="\t")

student_a = Student("예나", 89, 90)
student_b = Student("혜리", 99, 43)

print("student_a == student_b = ", student_a == student_b)
print("student_a != student_b = ", student_a != student_b)
print("student_a > student_b = ", student_a > student_b)
print("student_a >= student_b = ", student_a >= student_b)
print("student_a < student_b = ", student_a < student_b)
print("student_a <= student_b = ", student_a <= student_b)
print("test")

student_a == 10


