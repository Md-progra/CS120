#Understand - Check if number is in a list  Input:a list and a num
#Output: a boolean

def check_num(lst,num):
    for number in lst:
        if number == num:
            return True
    return False
    
lst = [5,2,3,9,10]
print(check_num(lst,11))