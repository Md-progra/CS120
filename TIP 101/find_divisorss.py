def find_divisors(n):
    divisors = []
    for num in range(1,n+1):
        if (n/num).is_integer():
            divisors.append(num)
    return divisors
lst = find_divisors(15)
print(lst)