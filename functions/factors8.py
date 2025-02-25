def factors(n):
    if n == 0 or n <0:
        raise ValueError(" has no factors")
    factors_of_ = []
    for i in range(1,n+1):
        if n % i == 0:
            factors_of_.append(i)
    return factors_of_
            

