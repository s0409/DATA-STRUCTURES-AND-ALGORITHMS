def valueequal(arr,n,x):
    l=[]
    for i in range(0,n):
        if arr[i]==i+1:
            l.append(i+1)
        return l
arr=[1,2,3,4]
n=len(arr)
print(valueequal(arr,n,x))
