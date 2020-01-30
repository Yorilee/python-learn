import os

print(os.name)
print(os.getcwd())
print(os.listdir())

os.mkdir("hello")
print(os.listdir())
os.rmdir("hello")
print(os.listdir())

with open("original.txt","w") as file:
    file.write("hello")

os.rename("original.txt","new.txt")

os.remove("new.txt")
os.system("dir")