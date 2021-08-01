def numberofpainters(arr,n,maxlen):
    total=0
    painters=1
    for i in arr:
        total+=i
        if total>maxlen:
            #for next count
            total=i
            painters+=1
    return painters
def partition(arr,n,k):
    low=max(arr)
    high=sum(arr)
    while low<=high:
        mid=(high+low)//2
        requiredpainters=numberofpainters(arr,n,mid)
        #find better optimum in lowerhalf
        #here mid is included because we may not get
        #anything better
        if requiredpainters<=k:
            high=mid-1
        else:
            low=mid+1
    return low
arr=[10,20,30,40]
n=len(arr)
k=2
print(partition(arr,n,k))
