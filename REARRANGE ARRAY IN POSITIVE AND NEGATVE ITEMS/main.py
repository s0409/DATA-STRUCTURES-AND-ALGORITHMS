def rearrange(arr,n):
    i=0
    j=n-1

    #shift all negative elements to the end
    while i<j:
        while(i<=n-1 and arr[i]>0):
            i+=1
        while(j>=0 and arr[j]<0):
            j-=1
        if i<j:
            temp=arr[i]
            arr[i]=arr[j]
            arr[j]=temp
        #i has index of leftmost negative element
    if i==0 and i==n:
        return 0
        #start with first positive element at index 0
        #Rearrrange array in alternating positive and negative items
    k=0
    while(k<n and i<n):
        temp=arr[k]
        arr[k]=arr[i]
        arr[i]=temp
        i=i+1
        k=k+2
        #utility function
def printArray(arr,n):
    for i in range(n):
        print(arr[i],end=" ")
    print("\n")
arr=[2,3,-4,-1,6,-9]
n=len(arr)
print("given array:")
printArray(arr,n)
rearrange(arr,n)
print(printArray(arr,n))

