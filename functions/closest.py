#a program that returns a number from a list thatis closest to it but not greater than it
def closest(L,n):
    L.sort()
    for i in range(len(L)-1,-1,-1):
        if L[i] < n:
            return L[i]
    return None
print(closest([1,6,9,3,11],8))