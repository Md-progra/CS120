#Understand - I have to check through a list of numbers
# then return the number that is not in the list
#Output: lst of nums Input: returns missing num
# Plan -  Sort the list. then create a new list
# New list contains the elements in the for loop, (append use)
#Now compare the two lists and if ele in new_list and not in
#Original list of numbers, return that number

def find_missing(nums):
    nums.sort()
    #New list
    new_list = []
    #length of nums
    n = len(nums)
    for i in range(0,n+1):
        new_list.append(i)
        for i in new_list:
            if i not in  nums:
                return i
            
nums = [2,4,1,0,5]
print(find_missing(nums))


