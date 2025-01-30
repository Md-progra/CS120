def is_sorted(li):
    # check if the list is sorted
    for i in range(len(li)-1):
        if li[i] > li[i+1]:
            return False
    return True

    
print(is_sorted(['q','u','l','i']))