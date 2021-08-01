def wordBreak(line,dictionary):
    str=set(dictionary)
    length=len(line)
    dp=[False]*(length+1)
    dp[0]=True

    for i in range(1,length+1):
        for j in range(i-1,-1,-1):
            if dp[j] and line[j:i] in str:
                dp[i]=True
                break
    return dp[length]
dictionary={"i","like","man","go"}
line="ilikemango"
length=len(line)
res=wordBreak(line, dictionary)
if res:
    print("1")
else:
    print("0")