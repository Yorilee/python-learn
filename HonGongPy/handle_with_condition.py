user_input_a = input("정수 입력 >")

if user_input_a.isdigit():
    number_input_a = int(user_input_a)
    print(number_input_a)
else:
    print("정수입력해주세요.")