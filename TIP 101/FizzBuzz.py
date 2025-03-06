# Understand - input: integer output: is made up of integers and strings
#Plan (Based on the value of parameter)
#use a for loop to iterate through range of number
#if the number at a point iss a muultiple of 3 print Fizz instead of number
#if the number is a multiiple of 5 print Buzz instead of number
#else: print tnumber
#Implement
def fizzbuzz(n):
    for num in range(1,n+1):
        if num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print ("Buzz")
        else:
            print(num)
fizzbuzz(13)

