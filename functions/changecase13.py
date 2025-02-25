def change_case(s):
    swapped = ""
    for i in range(len(s)):
       if s[i].islower():
           swapped += s[i].upper()
       elif s[i].isupper():
            swapped += s[i].lower()
       else:
            swapped += s[i]
    return swapped

  # return s.swapcase()
print(change_case("KoFi"))