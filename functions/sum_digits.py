def sum_digits(num):
    #This function takes a number and returns the sum of its digit
    num = str(num)
    sum = 0
    for number in num:
        sum+= int(number)
    print(sum)
    return(sum)
sum_digits(1234)