def check(p,n):
    temp=p
    count=0
    f=5
    while(f<=temp):
        count+=temp/f
        f=f*5
    return count>=n
def findNum(n):
    if n==1:
        return 5
    low=0
    high=5*n
    while low<high:
        mid=(high+low)>>1
        if check(mid,n):
            high=mid
        else:
            low=mid+1
    return low
n=6
print(findNum(n))
