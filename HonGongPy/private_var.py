import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)

circle = Circle(10)

# Print circumference, area
print(circle.get_circumference())
print(circle.get_area())

## Access __radius
print(circle.__radius)