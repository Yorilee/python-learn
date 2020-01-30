list_number =[25,34,1,3135,234]

try:
    number_input= int(input("정수 입력> "))
    print(number_input, list_number[number_input])
    예외.발생해주세요()
except ValueError as exception:
    print("정수를 입력해주세요")
    print(type(exception),exception)
except IndexError as excepttion:
    print("리스트 인덱스를 벗어났어요")
    print(type(exception), exception)
except Exception as exception:
    print("예상치 못한 에러 발생")
    print(type(exception),exception)