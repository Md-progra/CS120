#Insteadd of printing the number we want to  print the index of the number:
#Understand #Input: list    #Outpuut::indices of the list
#Plan:  iterate using a for loop and print i after each iteration


#IImplementation
def print_indices(lst):
    for i in range(len(lst)):
        print (i)
list = [5,1,3,8,2]
print_indices(list)
