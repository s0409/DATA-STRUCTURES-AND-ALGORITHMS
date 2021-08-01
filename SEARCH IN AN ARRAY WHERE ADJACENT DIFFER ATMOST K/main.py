def search(arr,n,k,x):
    #traverse the array from starting leftmost
    i=0
    while i<n:
        #if x is found at index i
        if arr[i]==x:
            return i
        #jump the difference between current array
        #element and x divded by k
        i=i+max(1,int(abs(arr[i]-i)/k))
    print("Number is not found")
    return -1
arr=[2,4,5,7,7,6]
x=6
k=2
n=len(arr)
print(search(arr,n,k,x))