try:
    number_input_a = int(input("정수 입력 >"))

    print(number_input_a)
except Exception as exception:
    print(type(exception))
    print(exception)