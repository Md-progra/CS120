def get_evens(lst):
    evens_lst = []
    for num in lst:
        if num % 2 == 0:
            evens_lst.append(num)
    return evens_lst
lst = [1,2,3,4]
evens_lsst = get_evens(lst)
print(evens_lsst)