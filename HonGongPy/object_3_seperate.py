def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean" : korean,
        "math" : math,
        "english" : english,
        "science" : science
    }

# 학생을 처리하는 함수를 선언
def student_get_sum(student):
    return student["korean"]+student["math"]+\
        student["english"]+student["science"]

def student_get_average(student):
    return student_get_sum(student) / 4

def student_to_string(student):
    return "{}\t{}\t{}".format(
        student["name"],
        student_get_sum(student),
        student_get_average(student)
    )

print("이름", "총점", "평균", sep="\t")

students =[
    create_student("윤인성", 76,74,73,62),
    create_student("윤인수", 76,64,73,62),
    create_student("윤인숙", 76,54,73,62),
    create_student("윤인사", 76,17,73,62),
    create_student("윤인서", 76,24,73,62),
    create_student("윤인송", 72,74,73,30),
]

for student in students:
    print(student_to_string(student))