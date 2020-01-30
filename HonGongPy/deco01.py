import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)
    
    # Declare getter, setter
    @property
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise TypeError("길이는 양의 숫자여야 합니다.")
        self.__radius = value

circle = Circle(10)

# Print circumference, area
print(circle.get_circumference())
print(circle.get_area())
print(circle.radius)
print()

## Access __radius
circle.radius = 2
print(circle.radius)
print()

# set radius
circle.radius= -10
