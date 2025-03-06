def multiples_of_five(lst):
    multiples = []
    for num in lst:
        if num % 5 == 0:
            multiples.append(num)
    return multiples
print(multiples_of_five([1,4,5,10]))