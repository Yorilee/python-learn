try:
    file = open("info.txt","w")
    Except.Occur()
except Exception as e:
    print(e)
finally:
    file.close()

print(file.closed)