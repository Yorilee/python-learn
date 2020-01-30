def print_n_times(n, *values):
    for _ in range(n):
        for value in values:
            print(value)
        print()

print_n_times(3, "안녕하세요","즐거운","파이썬프로그래밍")