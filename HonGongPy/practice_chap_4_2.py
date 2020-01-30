## 1
dict_a = {}

dict_a["name"]="구름"

print(dict_a)

del dict_a["name"]

print(dict_a)

## 2
pets = [
    {"name" : "구름", "age" : 5},
    {"name" : "초코", "age" : 3},
    {"name" : "아지", "age" : 1},
    {"name" : "호랑이", "age" : 1}
]

print("======================")                              

for i in range(len(pets)) :
    print("{} {}살".format(pets[i]["name"], pets[i]["age"]))       

## 3
numbers =[1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}

for number in numbers :
    if str(number) in counter :
        counter[str(number)] += 1
    else :
        counter[str(number)] = 1

print(counter)

## 4
