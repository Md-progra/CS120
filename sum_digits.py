def sum_digits():
    num = int(input("Enter number:"))
    num = str(num)
    sum = 0
    for number in num:
        sum+= int(number)
    print(sum)
    return(sum)
sum_digits()