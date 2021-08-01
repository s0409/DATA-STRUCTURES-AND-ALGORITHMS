#this function returns LCS with a condition that
#same characters at same index are not considered
def longestrepeated(str):
    n=len(str)
    dp=[[0 for i in range (n+1)] for j in range(n+1)]
    for i in range(1,n+1):
        for j in range(1,n+1):
            if str[i-1]==str[j-1] and i!=j:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i][j-1],dp[i-1][j])
    #this part of code finds the result
    res=""
    i=n
    j=n
    while i>0 and j>0:
        #if this cell is same as diagonally adjacent cell just above
        #then same characters are present at str[i-1] and str[j-1]
        #Apppend any of them to result
        if dp[i][j]==dp[i-1][j-1]+1:
            res+=str[i-1]
            i-=1
            j-=1
        elif dp[i][j]==dp[i-1][j]:
            i-=1
        else:
            j-=1
        #since we traverse dp[][] from bottom we get result
        #in reverse order
    res=''.join(reversed(res))
    return res
str = 'AABEBCDD'
print(longestrepeated(str))
