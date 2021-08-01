def mindifference(arr,n,k):
    if n==1:
        return 0
    arr.sort()
    ans=arr[n-1]-arr[0]
    small=arr[0]+k
    big=arr[n-1]-k
    if small>big:
        small,big=big,small
    for i in range(1,n-1):
        sub=arr[i]-k
        add=arr[i]+k
        if sub>=small or add<=big:
            continue
        if big-sub>add-small:
            small=sub
        else:
            big=add
    return min(ans,big-small)

arr=[1,5,15,10]
n=len(arr)
k=3
print(mindifference(arr,n,k))