class Circle:
    def __init__(self,center_y,center_x,radius):
        self.center_y=center_y
        self.center_x=center_x
        self.radius = radius
    def validation(self,x,y):
       soln = (x - self.center_x)**2 + (y - self.center_y)**2    #Formula to check if points are within,out or on circle
       if soln < self.radius ** 2 :
           print("Within")
       elif soln > self.radius ** 2 :
           print("Outside the circle")
       else:
           print("On the Circle")

validate1 = Circle(0,2,3)
validate1.validation(4,4)