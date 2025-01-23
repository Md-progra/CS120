def first_diff(str1, str2):
    if str1 == str2:
        print(-1)
        return -1
    if len(str1) != len(str2):
        max_length = max(len(str1), len(str2))
        str1 = str1.ljust(max_length)
        str2 = str2.ljust(max_length)
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            print(i)
            return i
    print(-1)
    return -1

# Example usage
first_diff('baccs', 'bac')
first_diff('daddy','daddye')
