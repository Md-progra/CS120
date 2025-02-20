class Rectangles:
    def area(self):
        pass
class Rectangle(Rectangles):
    def __init__(self,length,height):
        self.length = length
        self.height = height
    def area(self):
        return self.length * self.height
    def __gt__(self,other):
        return self.area() > other.area()
    

    # Creation of Object
rec = Rectangle(5,6)
rec.area()
rec2 = Rectangle(10,12)
rec2.area()
#Call the greater than method
print(rec < rec2)
print(rec > rec2)


