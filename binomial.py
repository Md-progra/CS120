def binomial(n,k):
    if k > n:
        print("undefined")
    if k == 0 or k == n:
        return ("...")
    k = min(k, n - k)  
    c = 1
    for i in range(k):
        c = c * (n - i) // (i + 1)
    print (c)
    return c
binomial(7,8)
