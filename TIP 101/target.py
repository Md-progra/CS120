#Understand - Input:Take in a list and an integer as a target. #Output: Index of integer in list == targert 
#if not found in list then reuurn a -1
# Plan (iterate through list and check if number == tarrget, return target if not -1)

#Implement
def linear_search(lst,n):
    for i in range(len(lst)):
        if lst[i] == n:
            return i
    return -1
lst = [1,4,5,2,8]
position = linear_search(lst,8)
print(position)
