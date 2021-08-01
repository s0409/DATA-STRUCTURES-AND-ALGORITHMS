def editdistance(str1,str2,m,n):
    #create a table to store result
    dp=[[0 for x in range(n+1)] for x in range(m+1)]
    #fill dp[][] in bottom up manner
    for i in range(m+1):
        for j in range(n+1):
            #if first string is empty only option is to
            #insert all characters of second string
            if i==0:
                dp[i][j]=j
            #if second string is empty only option is to
            #remove all characters of second string
            elif j==0:
                dp[i][j]=i
            #if last characters are same ignore last
            #character abd recur in remaining string
            elif str1[i-1]==str2[j-1]:
                dp[i][j]=dp[i-1][j-1]
            #if last character are different consider all
            #possibilities and find minimum
            else:
                dp[i][j]=1+min(dp[i][j-1],
                               dp[i-1][j],
                               dp[i-1][j-1])
    return dp[m][n]
#driver code runs here
if __name__=="__main__":
    str1="sunday"
    str2="saturday"
    m=len(str1)
    n=len(str2)
    print(editdistance(str1,str2,m,n))


