
"""
This module defines an Investment class that 
calculates the future value of an investment.
"""



class Investment:
    def __init__(self,p,i,n):
        self.p = p
        self.i = i/100       #Interest rate is in percentage
        self.n = n

    def __str__(self):
        print(f"Principal: {self.p}, Interest Rate: {self.i}, Years: {self.n}")
    def value_after(self):
        print(self.p * (1 + self.i)**self.n)
    
Inv1 = Investment(100,5.12,4)  #Object  1 creation

Inv1.value_after()


Inv2 = Investment(200,10,10) #Object 2 creation
Inv2.value_after()
       