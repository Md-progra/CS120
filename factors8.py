def number_of_factors(n):
    if n == 0 and n < 0:
        raise ValueError("Zero has no factors")
    count = 0
    
    for i in range(1,n+1):
        if n % i == 0:
            count += 1
    return count
            

        


