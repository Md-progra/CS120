def add_excitement(excitement):
    n=len(excitement)
    for word in range(n):
        excitement[word]+= "!"
    print(excitement)
    return excitement
add_excitement(['wow','aye','hii'])

    
