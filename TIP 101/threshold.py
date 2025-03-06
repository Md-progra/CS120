def count_less_than(numbers, threshold):
    counter = 0
    for num in numbers:
        if num > threshold:
            counter += 1
    return counter
numbers = [12,8,2,4,4,10]
counters = count_less_than(numbers,5)
print(counters)