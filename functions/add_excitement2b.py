def add_excitement(words):
    modified_words =[] #Created a new list 
    for item in range(len(words)):
        word = words[item] #assigned word at pointer neew name
        word += "!" #modified word
        modified_words.append(word) #appended modified word to list
    print(modified_words)
    return modified_words
add_excitement(['ayyee','peace','ziing'])
        
