def digital_root(number):
    while number > 10:
        sum = 0
        for digit in str(number):
            sum+=int(digit)
        number = sum
    print (number)
    return number
digital_root(45893)

