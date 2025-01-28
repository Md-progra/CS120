def matches(str1,str2):
    if len(str1) != len(str2):
        max_length = max(len(str1), len(str2))  # picks the longer string
        str1 = str1.ljust(max_length) #pads shorter string with spaces to match the longer string
        str2 = str2.ljust(max_length) #pads shorter string with spaces to match the longer string
        count = 0
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                count += 1
        print(count)
    else:

        count = 0
        for i in range(len(str1)):
            if str1[i] == str2[i]:
                count += 1
        print(count)


matches('bactseoooo','baccseo')