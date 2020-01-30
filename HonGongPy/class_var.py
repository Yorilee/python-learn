class Student:
    count = 0

    def __init__(self, name, korean, math):
        self.name = name
        self.korean = korean
        self.math = math

        # 클래스 변수 설정
        Student.count += 1
        print("{}번째 학생이 생성되었습니다.".format(Student.count))

    
# 학생 리스트 선언
students = [
    Student("예나", 89, 90),
    Student("혜리", 99, 43)
]

# 출력
print()
print("현재 생성된 총 학생 수는 {}명 입니다.".format(Student.count))
