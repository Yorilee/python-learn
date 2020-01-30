# Declare Parent Class
class Parent:
    def __init__(self):
        self.value ="test"
        print("Parent Class's __init__ method")
    def test(self):
        print("Parent Class's test() method")

# Declare Child Class
class Child(Parent):
    def __init__(self):
        Parent.__init__(self)
        print("Child Class's __init__ method")

child = Child()
child.test()
print(child.value)