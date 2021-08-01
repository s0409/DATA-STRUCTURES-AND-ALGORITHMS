def countPS(str):
    N=len(str)

    #create a 2D array to store the count of palindromic subsequence
    dp=[[0 for i in range(N+2)]for j in range(N+2)]

    #palindromic subsequence of length 1
    for i in range(N):

        dp[i][i]=1
    #check subsequence of length L is palindromic is not
    for L in range(2,N+1):
        for i in range(N):
            k=L+i-1
            if k<N:
               if str[i]==str[k]:
                   dp[i][k]=(dp[i][k-1]+dp[i+1][k]+1)
               else:
                   dp[i][k]=(dp[i][k-1]+dp[i+1][k]-dp[i+1][k-1])
    ss=dp[0][N-1]
    temp = ss % (10 ** 9 + 7)
    return temp

str="abcd"
print(countPS(str))
