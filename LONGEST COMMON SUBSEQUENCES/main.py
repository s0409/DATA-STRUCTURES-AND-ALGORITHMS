def lcs(str1,str2):
    m=len(str1)
    n=len(str2)
    dp=[[0 for i in range(n+1)] for j in range(m+1)]
    for i in range(m+1):
        for j in range(n+1):

            if str1[i-1]==str2[j-1]:
                dp[i][j]=1+dp[i-1][j-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i][j-1])
    return dp[m][n]
str1="ABCDGH"
str2="AEDFHR"
print(lcs(str1,str2))