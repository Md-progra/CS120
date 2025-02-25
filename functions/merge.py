# def merge(sortedlist_1,sortedlist_2):
#     new_list =(sortedlist_1 + sortedlist_2)
#     new_list.sort()
#     print(new_list)
# merge([4,7,2,9],[3,6,8,1])

#without sort method
def merge(sortedlist_1,sortedlist_2):
    new_list =sortedlist_1 + sortedlist_2
    for i in range(len(new_list)):
        for j in range(i+1,len(new_list)):
            if new_list[i] > new_list[j]:
                new_list[i],new_list[j] = new_list[j],new_list[i]
    print (new_list)

merge([4,7,2,9],[3,6,8,1])