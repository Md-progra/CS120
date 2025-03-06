#Understand -  Input is a list Output is an average of lists content
#Plan, add all items in list together then divide by the len of the lst

#Implement:

def average(scores):
    ans = 0
    for score in scores:
        ans += score
    avg = ans/len(scores)
    return avg
scores = [84,73,92,95,88]
avg_score = average(scores)
print(avg_score)