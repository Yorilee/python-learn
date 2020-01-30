try:
    number_input_a = int(input("정수 입력>"))
    print(number_input_a)
except:
    print("정수를 입력해달라고 했잖아요!!")
else:
    print("정수 입력해줘서 고마워요!")
finally:
    print("프로그램이 어떻게든 끝이 났습니다!")