number = int(input("정수 입력> :"))

if number % 2 == 0 :
    print("""\
        입력한 문자열은 {} 입니다.
        {}는 짝수 입니다.""".format(number, number))
else :
    print("""\
        입력한 문자열은 {} 입니다.
        {}는 홀수 입니다.""".format(number, number))

