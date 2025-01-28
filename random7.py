import random
def gen_erate(n):
    a = 10**(n-1)
    b = (10**n)-1
    generated_number = random.randint(a,b)
    print(generated_number)

gen_erate(3)






# Title: Find the Largest Element Less Than or Equal to a Given Number

# Description:

# Given a list of integers L and an integer n, 
# write a function closest that returns the largest 
# element in L that is not larger than n. If all elements in 
# L are larger than n, return None.

# The list L will have at least one element.

# The elements in L are not necessarily sorted.

# The elements in L and the integer n are all integers.