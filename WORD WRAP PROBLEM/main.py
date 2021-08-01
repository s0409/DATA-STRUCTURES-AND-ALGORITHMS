import sys
def solvewordwrap(arr,n,k):
    dp=[0]*n

    #to store index of last word
    ans=[0]*n

    #if only one word is present then only one line is
    #required cost of last line is 0 .ending point is also
    #n-1 as single word is present
    dp[n-1]=0
    ans[n-1]=n-1

    #make each word first word of line
    #by iterating each index in arr
    for i in range(n-2,-1,-1):
        currlen=-1
        dp[i]=sys.maxsize

        #keep on adding words in current line by
        #iterating from starting word upto last word in arr
        for j in range(i,n):
            #update number of characters in current line
            #arr[j] is number of characters in current word and 1
            #represent space character
            currlen+=(arr[j]+1)

            #if limit of character is violated
            #then no more words can be added to
            #current line
            if currlen>k:
                break
            #if current word aadded to line is last word of arr
            #then current line is last line cost of line line is zero
            #else cost is square of extra spaces plus cost of putting line
            if j==n-1:
                cost=0
            else:
                cost=((k-currlen)*(k-currlen)+dp[j+1])
            #check if this gives minimum cost for line
            if cost<dp[i]:
                dp[i]=cost
                ans[i]=j
    i=0
    while i<n:
        print(i+1,ans[i]+1,end=" ")
        i=ans[i]+1
arr=[3,2,2,5]
n=len(arr)
k=6
solvewordwrap(arr,n,k)






