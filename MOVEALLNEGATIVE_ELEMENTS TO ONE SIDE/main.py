import array
def reverselist(arr,n):
    j=0
    for i in range(0,n):
        if (arr[i]<0):
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
            j+=1
    return arr
arr=[-1,4,5,-6,8]
n=len(arr)
print(reverselist(arr,n)) 

