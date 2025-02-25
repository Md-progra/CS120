# A program that randomly generates an integer between 1 and 10 and prints users name * randomly generated integer
# Now based on the number times that the user's name was printed
# Let's create a function that will allow the user to guess the number that was randomly generated
# Now if user's guess is equal to the randomly generated number, print Yay!, else print! Nope


import random

def guess_number():
   user_name = input("Enter your name:")
   a = random.randint(0,10)
   for number in range(a):
      print(user_name)

   print ("Can you guess the number that was generated? \n")
   guess = int(input("Enter your guess:"))
   if guess == a:
      print("Yay!")
   else:
      print("Nope")
      return 
guess_number()


