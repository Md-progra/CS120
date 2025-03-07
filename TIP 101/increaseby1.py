#understand: input: Receive lst Output: Increase each item by 1 and put it in a list (in-place)

#plan: iterate and add 1 to each element in list then return the list

def increment_values(lst):
    for i in range(len(lst)):
        lst[i] +=1
    return lst
lst = [3,5,8,2]
new_lst = increment_values(lst)
print(new_lst)
