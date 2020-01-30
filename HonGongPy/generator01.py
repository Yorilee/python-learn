def test():
    print("Region A Pass")
    yield 1
    print("Region B Pass")
    yield 2
    print("Region C Pass")

output = test()

print("Region D Pass")
a = next(output)
print(a)

print("Region E Pass")
b = next(output)
print(b)
 
print("Region F Pass")
c = next(output)
print(c)

next(output)

