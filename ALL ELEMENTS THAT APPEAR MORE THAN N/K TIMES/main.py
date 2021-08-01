"""def morethan(arr,n,k):
    x=n//k
    #create hashmap
    freq={}
    for i in range(n):
        if arr[i] in freq:
            freq[arr[i]]+=1
        else:
            freq[arr[i]]=1
    #traverse the map
    for i in freq:
        if freq[i]>x:"""
from collections import Counter
def morethan(arr,n,k):
    x=n//k
    freq=Counter(arr)
    for i in freq:
        if freq[i]>x:
            print(i)
arr=[1,2,3,1,1,4,5,3,3,3,3,2,1]
n=len(arr)
k=4
print(morethan(arr,n,k))
