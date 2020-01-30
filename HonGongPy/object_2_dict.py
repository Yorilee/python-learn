def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean" : korean,
        "math" : math,
        "english" : english,
        "science" : science
    }

students =[
    create_student("윤인성", 76,74,73,62),
    create_student("윤인수", 76,64,73,62),
    create_student("윤인숙", 76,54,73,62),
    create_student("윤인사", 76,17,73,62),
    create_student("윤인서", 76,24,73,62),
    create_student("윤인송", 72,74,73,62),
]

print("이름", "총점", "평균", sep="\t")

for student in students:
    score_sum = student["korean"]+student["math"]+\
        student["english"]+student["science"]
    score_average = score_sum / 4

    print(student["name"], score_sum, score_average, sep="\t")