from collections import defaultdict
def duplicates(string):
    count=defaultdict(int)
    for i in range(len(string)):
        count[string[i]]+=1
    for var in count:
        if count[var]>1:
            print(var,"count=",count[var])
var="shivams"
duplicates(var)