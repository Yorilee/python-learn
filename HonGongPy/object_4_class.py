class Student:
    def __init__ (self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science
    
    def get_sum(self):
        return self.korean + self.math +\
            self.english + self.science

    def get_average(self):
        return self.get_sum() / 4

    def to_string(self):
        return "{}\t{}\t{}".format(\
            self.name,\
            self.get_sum(),\
            self.get_average()
            )
    
students = [
    Student("S1",1,2,3,4),
    Student("S2",3,4,5,6),
    Student("S3",5,3,2,1)
]

print("이름", "총점", "평균", sep="\t")
    
for student in students:
    print(student.to_string())