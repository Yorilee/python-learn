try:
    file = open("info.txt","w")
    예외.발생한다()
    file.close()

except Exception as e:
    print(e)

print(file.closed)