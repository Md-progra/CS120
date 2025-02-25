
#Divide and Conquer
"""
the function closest takes 
two arguments a list of integers L and an integer n.
Then first of all, it takes care of the edge case 
where the list is empty
"""

def closest(L,n):
    numbers = []
    for i in range (len(L)):
        if L[i] < n:
            numbers.append(L[i])
    if len(numbers) == 0:
        return None
    else:
        max_value = max(numbers)
        print(max_value)
        return max_value
        
        

closest([6,8,9,10],5)  #4