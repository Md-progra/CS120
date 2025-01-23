import random
def gen_erate(n):
    a = 10**(n-1)
    b = (10**n)-1
    generated_number = random.randint(a,b)
    print(generated_number)

gen_erate(3)