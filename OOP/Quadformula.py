class Calc_for_x:
    def __init__(self,a,b,c):
        self.a = a 
        self.b = b
        self.c =c 
        print(f"Equation is: {self.a}x^2 + {self.b}x + {self.c}")


    def calc_x(self):
        x1 = (-self.b + ((self.b**2) - 4*self.a*self.c)**0.5)/(2*self.a)
        print(f"x1 is: {x1}")
        x2 = (-self.b - ((self.b**2) - 4*self.a*self.c)**0.5)/(2*self.a)
        print(f"x2 is: {x2}")

        #conditions for solulu 
        if x1 == x2:
            print(f"Equation has one value of x: {x1}")
        elif x1 != x2:
            print(f"Equation has two values of x: {x1} and {x2}")
        else:
            print("Equation has no value of x")

#Object of class  has two roots
soln = Calc_for_x(1,5,6)
soln.calc_x()
#Object of class has one root
soln = Calc_for_x(1,2,1)
soln.calc_x()
#Object of class  too many decimal points
soln = Calc_for_x(1,1,1)
soln.calc_x()



    