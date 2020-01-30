def print_n_times(*values, n=2):
    for _ in range(n):
        for value in values:
            print(value)
        print()

print_n_times("안녕하세요","즐거운","Python Programming!", n=3)