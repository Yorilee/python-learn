try:
    file = open("info.txt","w")

    file.close()

except Exception as e:
    print(e)

print(file.closed)