class Quadrant:
    def __init__(self, x,y):
        self.x =x
        self.y = y
    def checkquad(self):
        if self.x > 0 and self.y > 0:
            print("Points are in the first Quadrant")
        elif self.x < 0 and self.y > 0:
            print("Points are in the Second quadrant")
        elif self.x < 0 and self.y < 0:
            print("Points are in Third Quadrant")
        elif self.x > 0 and self.y < 0:
            print("Points are in Fourth Quadrant")
        elif self.x == 0 and self.y != 0:
            print("Points are on the y-axis")
        elif self.y == 0 and self.x != 0:
            print("Points are on the x-axis")
        else:
            print("Points are on the origin")
#Object of the class
check1= Quadrant(3,4)
check1.checkquad()

#Object of the class
check2= Quadrant(-3,4)
check2.checkquad()

#Object of the class
check3= Quadrant(-3,-4)
check3.checkquad()

#Object of the class
check4= Quadrant(0,5)
check4.checkquad()

#Object of the class
check5= Quadrant(0,0)
check5.checkquad()


        
