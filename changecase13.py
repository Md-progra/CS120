def change_case(s):
    char = ""
    for i in range(len(s)):
       if s[i].islower():
           char += s[i].upper()
       elif s[i].isupper():
            char += s[i].lower()
       else:
            char += s[i]
    return char

  # return s.swapcase()
print(change_case("disstressssS"))