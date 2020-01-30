numbers = [273, 103, 5, 32, 65, 9, 72, 800, 99]

# example 1
for number in numbers :
    if number % 2 == 0 :
        print("{}는 짝수 입니다.".format(number))
    else :
        print("{}는 홀수 입니다.".format(number))

# example 2
for number in numbers :
    print("{}는 {} 자리수 입니다.".format(number, len(str(number))))
