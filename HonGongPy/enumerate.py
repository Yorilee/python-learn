example_list = ["요소A","요소B","요소B"]

print(example_list)
print()

print(enumerate(example_list))
print()

print(list(enumerate(example_list)))
print()

for i, value in enumerate(example_list):
    print("{}번째 요소는 {}입니다.".format(i, value))