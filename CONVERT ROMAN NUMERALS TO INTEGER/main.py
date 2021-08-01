def romanToInt(str):
    value={
        "M":1000,
        "D":500,
        "C":100,
        "L":50,
        "X":10,
        "V":5,
        "I":1
    }
    #initialize previous character and answer
    p=0
    ans=0
    #traverse through all characters
    n=len(str)
    for i in range(n-1,-1,-1):
        #if greater than or equal to previous
        #add to answer
        if value[str[i]]>=p:
            ans+=value[str[i]]
        #if smaller than previous
        else:
            ans-=value[str[i]]
        #update previous
        p=value[str[i]]
    return ans
print(romanToInt("MCMIV"))