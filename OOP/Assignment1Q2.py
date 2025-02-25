"""
Question 2: 
"""
#Imported gcd to find greatest common divisor so that I can simplify and 
#display fractions
from math import gcd
# Created a class Fraction

class Fraction:
    #constructor takes in numerator and denominator
    #It also checks if the denominator is zero and raises an error
    

    def __init__ (self, numerator,denominator):
        if denominator == 0:
          raise ValueError("Denominator cannot be zero/undefined")
        #Uses gcd to simplify the fraction
        divisor = gcd(numerator, denominator)
        self.numerator = numerator//divisor
        self.denominator =  denominator//divisor
        # __str__ method returns the fraction in the form of a string
        # not in a form of a float but as numerator/denominator
    def __str__(self):
        return f"{self.numerator}/{self.denominator}"
    #As the name suggests, this method adds two fractions
    def add(self, other):
        numerator = self.numerator * other.denominator + other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)
    #This method subtracts two fractions
    def subtract(self, other):
        numerator = self.numerator * other.denominator - other.numerator * self.denominator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)
    #Multiplies
    def multiply(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)
    #divides
    def divide(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)
#Example
#Creation of self.fraction object and other.fraction object
f1 = Fraction(1, 2)
f2 = Fraction(1, 4)
print(f1.add(f2))
print(f1.subtract(f2))
print(f1.multiply(f2))








"""
Question 3: If the same method is inherited from both parents when using 
multiple inheritance what happens is that the method from the first parent is 
selected first, this is called Method Resolution Order (MRO). If the child 
overrrides the method thw child can invoke the method from the parent class
using the super() function or MRO.
""" 

"""
Question 4: A class is basically a blueprint for the creation of objects.
For example before one can create a house, one needs a blueprint of the house
in our case the blueprint is the class.
An example of a class is Car, the class Car can have different car objects.

An object is an instance of a class. For example; once you have the blueprint of a 
house, you can create as many houses as you want using the blueprint. The houses
created using the blueprint are the objects.
An example of an object is a car, the car can have attributes such as color, model, year, etc.

"""
# #Example
# class Car:  #class Car is the blueprint
#     def __init__(self, color, model, year):
#         self.color = color
#         self.model = model
#         self.year = year    
# #Objects of the class Car
# car1 = Car("red", "Toyota", 2020)


"""
Question 5: 
__init__ is called a constructor in python. It is a special method that is
 called when an object is created from a class. For example we have a blueprint, 
 we want to build a house (object), we need to call the constructor to build the house.
    The constructor initializes the object's attributes.
    """
"""
Question 6:
Class attributes are attributes that are shared by all instances of a class.
Data attributes are attributes that are specific to each instance of a class.

"""
# #Example
# class Car:
#     car_type = "SUV" #class attribute
#     def __init__(self, color, model, year):
#         self.color = color #data attribute
#         self.model = model #data attribute
#         self.year = year   #data attribute