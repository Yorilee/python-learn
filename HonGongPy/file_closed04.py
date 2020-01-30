try:
    file = open("info.txt","w")
    sefsd.test()
except Exception as e:
    print(e)

file.close()

print(file.closed)