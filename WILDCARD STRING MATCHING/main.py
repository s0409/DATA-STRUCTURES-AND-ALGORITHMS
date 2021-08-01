def match(first,second):
    #if we reach end of both strings
    if len(first)==0 and len(second)==0:
        return True
    #make sure that characters after * are present in second string
    if len(first)>1 and first[0]=="*" and len(second)==0:
        return False
    #if the first string contains ? or current character of both string match
    if len(first)>1 and first[0]=="?" or len(first)!=0 and len(second)!=0 and first[0]==second[0]:
        return match(first[1:],second[1:])
    #if there is * then there are two possibilities
    # a. we consider current character of second string
    # b. we ignore current character of second string
    if len(first)!=0 and first[0]=="*":
        return match(first[1:],second) or match(first,second[1:])
    return False
def test(first,second):
    if match(first,second):
        print("yes")
    else:
        print("No")
test("ge*ks","geeks")