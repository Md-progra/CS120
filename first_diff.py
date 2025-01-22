def first_diff(str1,str2):
    if str1 == str2:
        print (-1)
        return -1
    for letter in range(min(len(str1), len(str2))):
        if str1[letter] != str2[letter]:
            print (letter)
            return letter
        else:
            return (min(len(str1),len(str2)))
    
first_diff("man","mantle")
       
       
    