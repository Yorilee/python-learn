import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    def get_area(self):
        return math.pi * (self.__radius ** 2)
    
    # Declare getter, setter
    def get_radius(self):
        return self.__radius
    def set_radius(self, value):
        self.__radius = value

circle = Circle(10)

# Print circumference, area
print(circle.get_circumference())
print(circle.get_area())
print()

## Access __radius
print(circle.get_radius())
print()

# set radius
circle.set_radius(2)
print(circle.get_circumference())
print(circle.get_area())
print()
