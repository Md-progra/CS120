class Circle:
    def __init__(self, radius):
        self.radius = radius
    def circumference(self):
        return 2 * 22/7* self.radius
    def area(self):
        return 22/7*(self.radius)**2
    def __str__(self):
        return f'Circle with radius: {self.radius}'


circum1 = Circle(7)
print(circum1)  # Output: Circle with radius: 7
print(f'Circumference: {circum1.circumference()}')
print(f'Area: {circum1.area()}')