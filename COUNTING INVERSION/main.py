def inversion(arr,n):
    temp_arr=[0]*n #storing the elements to merge function
    return merge_sort(arr,temp_arr,0,n-1)
def merge_sort(arr,temp_arr,left,right):
    inv_count=0
    if left<right:
        mid=(right+left)//2
        inv_count+=merge_sort(arr,temp_arr,left,mid) #this is for right sub array
        inv_count+=merge_sort(arr,temp_arr,mid+1,right) #this is for right subaray
        inv_count+=merge(arr,temp_arr,left,mid,right) #this will merge two sorted array
    return inv_count
def merge(arr,temp_arr,left,mid,right):
    i=left
    j=mid+1
    k=left
    inv_count=0
    while i<=mid and j<=right:
        if arr[i]<=arr[j]:
            temp_arr[k]=arr[i]
            k+=1
            i+=1
        else:
            temp_arr[k]=arr[j]
            inv_count+=(mid-i+1)
            k=+1
            j+=1
    while i<=mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1
    while j<=right:
        temp_arr[k]=arr[j]
        k+=1
        j+=1
    for var in range(left,right+1):
        arr[var]=temp_arr[var]
    return inv_count
arr=[1,20,6,4,5]
n=len(arr)
print(inversion(arr,n))
