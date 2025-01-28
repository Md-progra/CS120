def factorial(n): 
    if n < 0:
        raise ValueError('Factorial is non-existent for negative numbers')
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def coefficient(a, b):
    if b > a or b < 0:  # Ensure b is a valid value for combinations
        raise ValueError("Invalid input: b must be between 0 and a inclusive.")
    binomial_coefficient = factorial(a) / (factorial(b) * factorial(a - b))
    return binomial_coefficient


        


        # practice 8,9 and 10 