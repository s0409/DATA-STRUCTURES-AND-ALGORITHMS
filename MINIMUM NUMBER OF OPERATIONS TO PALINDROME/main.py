def minop(arr,n):
    ans=0
    i=0
    j=n-1
    #if corner elements are same
    while i<=j:
        if arr[i]==arr[j]:
            i+=1
            j-=1
        elif arr[i]>arr[j]:
            j-=1
            arr[j]+=arr[j+1]
            ans+=1
        else:
            i+=1
            arr[i]+=arr[i-1]
            ans+=1
    return ans
arr=[1,4,5,9,1]
n=len(arr)
print(minop(arr,n))