def countRev(s):
    #if length is odd we cant balance
    if len(s)%2==1:
        return -1

    #number of opening and closing braces
    open=0
    close=0
    res=0
    for i in s:
        if i=="{":
            open+=1
        else:
            close+=1
        #if close exceeds open then we balance the brackets till that point
        if close>open:
            res+=close-open
            close,open=open,close
    #finally we reverse the half of brackets that from the unbalance
    #to balance the unbalanced pairs
    res+=abs(close-open)//2
    return  res
string="{{"
print(countRev(string))