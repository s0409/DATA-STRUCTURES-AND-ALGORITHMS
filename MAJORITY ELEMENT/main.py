def majority(arr,n):
    temp={}
    for i in arr:
        if i in temp:
            temp[i]+=1
        else:
            temp[i]=1
    maxx=max(temp,key=temp.get)
    if temp[maxx]>n//2:
        return maxx
    else:
        return -1
arr=[3,1,3,3,2]
n=len(arr)
print(majority(arr,n))
