"""
A class called rectangle
Two inputs: width and length
Two methods: area and perimeter
"""
class Rectangle:
    def __init__(self, l,w):  #Assume all l and w are in centimeters
        self.l = l
        self.w = w
    def area(self):
        return self.l * self.w
    def perimeter(self):
        return (2*self.l + 2*self.w)
    
Rec1 = Rectangle(5,3)
print(Rec1.perimeter())
print(Rec1.area())
