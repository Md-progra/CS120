def findall(string, letter):
    loc = []
    if letter not in string:
        return []
    else:
        for i in range(len(string)):
            if string[i]== letter:
                loc.append(i)
        print(loc)
        return loc
findall("disstresssss", "s")