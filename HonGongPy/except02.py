list_number=[52,273,32,72,100]

try:
    number_input = int(input("정수 입력>"))
    print(number_input, list_number[number_input])

except Exception as exception:
    print(type(exception))
    print(exception) 