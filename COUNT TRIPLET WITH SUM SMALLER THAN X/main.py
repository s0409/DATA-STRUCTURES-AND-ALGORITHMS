def countTriplets(arr,n,sum):
    arr.sort()
    #intialize result
    ans=0
    #every iteration of loop counts triplets with first element as arr[i]
    for i in range(0,n-2):
        #initialize two pointers at corner elements
        j=i+1
        k=n-1
        #use meet in middle concept
        while j<k:

              if arr[i]+arr[j]+arr[k]>=sum:
                  k=k-1

        #else move left corner
              else:
            #this is important for current i and j
            #there can be total k-j third elements
                  ans+=k-j
                  j=j+1
    return ans
arr=[-2, 0, 1, 3]
n=len(arr)
sum=2
print(countTriplets(arr,n,sum))