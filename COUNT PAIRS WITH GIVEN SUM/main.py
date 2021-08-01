import sys
import array
def pairs(arr,n,sum):
    m=[0]*1000
    for i in range(0,n):
        m[arr[i]]+=1
    twice_count=0
    for i in range(0,n):
        twice_count+=m[sum-arr[i]]
        if sum-arr[i]==arr[i]:
            twice_count-=1
    return twice_count//2
arr=[1,1,1,1]
n=len(arr)
k=2
print(pairs(arr,n,k))