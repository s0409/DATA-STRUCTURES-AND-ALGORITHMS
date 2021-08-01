def check(x,k,stalls):
    #greedy approach put each cow in the first place you can
    cow=1
    pos=stalls[0]
    n=len(stalls)

    #traverse through the array
    for i in range(1,n):
        if stalls[i]-pos>=x:
            cow+=1
        if cow==k:
            return True
        #assign current position of stall as the pos
        pos=stalls[i]
    return False
def aggresivecows(stalls,k):
    stalls.sort()
    low=0
    high=n-1
    pos=0
    while high>=low:
        mid=(high+low)//2
        if check(mid,k,stalls):
            low=mid+1
            pos=mid
        else:
            high=mid-1
    return pos
stalls=[1,2,4,8,9]
n=len(stalls)
k=3
print(aggresivecows(stalls,k))